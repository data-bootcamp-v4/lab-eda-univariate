import os
import math
import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats

DATA_PATH = "amz_uk_price_prediction_dataset.csv"
PLOTS_DIR = "plots"


# We'll sample for charts where appropriate.
PLOT_SAMPLE_SIZE = 200_000  


def ensure_plots_dir():
    os.makedirs(PLOTS_DIR, exist_ok=True)


def safe_mode(series: pd.Series):
    """Return a single mode value if exists, otherwise None."""
    m = series.mode(dropna=True)
    if len(m) == 0:
        return None
    return m.iloc[0]


def describe_numeric(series: pd.Series) -> dict:
    """Compute centrality/dispersion metrics required in the lab."""
    s = series.dropna()

    mean = s.mean()
    median = s.median()
    mode = safe_mode(s)

    var = s.var(ddof=1)
    std = s.std(ddof=1)
    data_range = s.max() - s.min()
    q1 = s.quantile(0.25)
    q3 = s.quantile(0.75)
    iqr = q3 - q1

    return {
        "count": int(s.shape[0]),
        "mean": float(mean),
        "median": float(median),
        "mode": None if mode is None else float(mode),
        "variance": float(var),
        "std_dev": float(std),
        "min": float(s.min()),
        "max": float(s.max()),
        "range": float(data_range),
        "q1": float(q1),
        "q3": float(q3),
        "iqr": float(iqr),
    }


def average_duration_hours_minutes(length_minutes_avg: float):
    """Convert average minutes to (hours, minutes) without decimals."""
    hours = int(math.floor(length_minutes_avg / 60))
    minutes = int(round(length_minutes_avg - (hours * 60)))
    return hours, minutes


def plot_category_bar(category_counts: pd.Series, top_n: int = 20):
    top = category_counts.head(top_n)

    plt.figure()
    top.sort_values(ascending=True).plot(kind="barh")
    plt.title(f"Top {top_n} categories by listing frequency")
    plt.xlabel("Number of products")
    plt.ylabel("Category")
    plt.tight_layout()
    out = os.path.join(PLOTS_DIR, "category_top20_bar.png")
    plt.savefig(out, dpi=200)
    plt.close()
    return out


def plot_category_pie(category_counts: pd.Series, top_n: int = 10):
    top = category_counts.head(top_n)
    other = category_counts.iloc[top_n:].sum()
    pie = top.copy()
    pie.loc["Other"] = other

    plt.figure()
    plt.pie(pie.values, labels=pie.index, autopct="%1.1f%%", startangle=90)
    plt.title(f"Category share (Top {top_n} + Other)")
    plt.tight_layout()
    out = os.path.join(PLOTS_DIR, "category_top10_pie.png")
    plt.savefig(out, dpi=200)
    plt.close()
    return out


def plot_price_hist(price_series: pd.Series):
    s = price_series.dropna()

    # Sampling for speed and readability.
    if len(s) > PLOT_SAMPLE_SIZE:
        s_plot = s.sample(PLOT_SAMPLE_SIZE, random_state=42)
        sampled = True
    else:
        s_plot = s
        sampled = False

    plt.figure()
    plt.hist(s_plot, bins=60)
    plt.title("Price distribution (histogram)")
    plt.xlabel("Price")
    plt.ylabel("Count")
    plt.tight_layout()
    out = os.path.join(PLOTS_DIR, "price_hist.png")
    plt.savefig(out, dpi=200)
    plt.close()

    return out, sampled


def plot_price_box(price_series: pd.Series):
    s = price_series.dropna()

    # Sampling for speed and readability.
    if len(s) > PLOT_SAMPLE_SIZE:
        s_plot = s.sample(PLOT_SAMPLE_SIZE, random_state=42)
        sampled = True
    else:
        s_plot = s
        sampled = False

    plt.figure()
    plt.boxplot(s_plot, vert=False)
    plt.title("Price spread (box plot)")
    plt.xlabel("Price")
    plt.tight_layout()
    out = os.path.join(PLOTS_DIR, "price_boxplot.png")
    plt.savefig(out, dpi=200)
    plt.close()

    return out, sampled


def plot_stars_hist(stars_series: pd.Series):
    s = stars_series.dropna()

    if len(s) > PLOT_SAMPLE_SIZE:
        s_plot = s.sample(PLOT_SAMPLE_SIZE, random_state=42)
        sampled = True
    else:
        s_plot = s
        sampled = False

    plt.figure()
    plt.hist(s_plot, bins=40)
    plt.title("Stars rating distribution (histogram)")
    plt.xlabel("Stars")
    plt.ylabel("Count")
    plt.tight_layout()
    out = os.path.join(PLOTS_DIR, "stars_hist.png")
    plt.savefig(out, dpi=200)
    plt.close()

    return out, sampled


def main():
    ensure_plots_dir()

    if not os.path.exists(DATA_PATH):
        raise FileNotFoundError(
            f"Could not find '{DATA_PATH}' in the current folder. "
            "Place the dataset file in the repo folder and keep the name the same."
        )

    print(f"Loading dataset: {DATA_PATH}")
    df = pd.read_csv(DATA_PATH)
    print(f"Rows: {len(df):,} | Columns: {len(df.columns)}")
    print("Columns:", list(df.columns))

    
    # Part 1: Product Categories
   
    print("\nPART 1 — Product Categories")

    category_counts = df["category"].fillna("Unknown").value_counts()
    top5_categories = category_counts.head(5)

    print("\nTop 5 most listed categories:")
    for cat, cnt in top5_categories.items():
        print(f"  {cat}: {cnt:,}")

    bar_path = plot_category_bar(category_counts, top_n=20)
    pie_path = plot_category_pie(category_counts, top_n=10)

    # Business note: dominance check
    top1_share = (category_counts.iloc[0] / category_counts.sum()) * 100
    dominance_comment = (
        "A single category dominates the listings."
        if top1_share >= 25
        else "No single category dominates; listings are distributed across categories."
    )

    
    # Part 2: Product Pricing
    
    print("\nPART 2 — Product Pricing")

    price_stats = describe_numeric(df["price"])
    print("\nPrice centrality:")
    print(f"  Mean:   {price_stats['mean']:.2f}")
    print(f"  Median: {price_stats['median']:.2f}")
    if price_stats["mode"] is None:
        print("  Mode:   (no mode found)")
    else:
        print(f"  Mode:   {price_stats['mode']:.2f}")

    print("\nPrice dispersion:")
    print(f"  Variance: {price_stats['variance']:.2f}")
    print(f"  Std Dev:  {price_stats['std_dev']:.2f}")
    print(f"  Min:      {price_stats['min']:.2f}")
    print(f"  Max:      {price_stats['max']:.2f}")
    print(f"  Range:    {price_stats['range']:.2f}")
    print(f"  IQR:      {price_stats['iqr']:.2f} (Q1={price_stats['q1']:.2f}, Q3={price_stats['q3']:.2f})")

    price_hist_path, price_hist_sampled = plot_price_hist(df["price"])
    price_box_path, price_box_sampled = plot_price_box(df["price"])

    # Explanation for "hard to read histogram" (often long right tail / outliers)
    histogram_readability_explanation = (
        "Price distributions often have a long right tail (a small number of very expensive products). "
        "This stretches the x-axis and compresses the bulk of products into a narrow area. "
        "Common fixes are: using a log-scaled x-axis, limiting to a percentile range (e.g., <= 95th percentile), "
        "or plotting separate histograms for different price bands."
    )

    
    # Part 3: Product Ratings (stars)
    
    print("\nPART 3 — Product Ratings (stars)")

    stars_stats = describe_numeric(df["stars"])
    print("\nStars centrality:")
    print(f"  Mean:   {stars_stats['mean']:.2f}")
    print(f"  Median: {stars_stats['median']:.2f}")
    if stars_stats["mode"] is None:
        print("  Mode:   (no mode found)")
    else:
        print(f"  Mode:   {stars_stats['mode']:.2f}")

    print("\nStars dispersion:")
    print(f"  Variance: {stars_stats['variance']:.4f}")
    print(f"  Std Dev:  {stars_stats['std_dev']:.4f}")
    print(f"  IQR:      {stars_stats['iqr']:.4f}")

    # Skewness and kurtosis (using scipy, dropna)
    stars_clean = df["stars"].dropna()
    stars_skew = float(stats.skew(stars_clean, bias=False))
    stars_kurt = float(stats.kurtosis(stars_clean, fisher=True, bias=False))  # fisher=True => normal == 0

    print("\nStars shape:")
    print(f"  Skewness:  {stars_skew:.4f}")
    print(f"  Kurtosis:  {stars_kurt:.4f} (Fisher; normal distribution = 0)")

    stars_hist_path, stars_hist_sampled = plot_stars_hist(df["stars"])

    
    # Business-centric summary (report.md)
    
    report_lines = []
    report_lines.append("# Amazon UK Product Dataset — Univariate EDA Report\n")

    report_lines.append("## Part 1: Product Categories\n")
    report_lines.append("### Top 5 categories by listing frequency\n")
    for cat, cnt in top5_categories.items():
        report_lines.append(f"- **{cat}**: {cnt:,} listings\n")
    report_lines.append(f"\nTop category share: **{top1_share:.2f}%**. {dominance_comment}\n")
    report_lines.append(f"\nCharts saved:\n- `{bar_path}`\n- `{pie_path}`\n")

    report_lines.append("\n## Part 2: Product Pricing\n")
    report_lines.append("### Centrality\n")
    report_lines.append(f"- Mean price: **{price_stats['mean']:.2f}**\n")
    report_lines.append(f"- Median price: **{price_stats['median']:.2f}**\n")
    report_lines.append(f"- Mode price: **{price_stats['mode']:.2f}**\n" if price_stats["mode"] is not None else "- Mode price: **Not available**\n")
    report_lines.append("\n### Dispersion\n")
    report_lines.append(f"- Std dev: **{price_stats['std_dev']:.2f}**\n")
    report_lines.append(f"- Range: **{price_stats['range']:.2f}** (min {price_stats['min']:.2f}, max {price_stats['max']:.2f})\n")
    report_lines.append(f"- IQR: **{price_stats['iqr']:.2f}** (Q1 {price_stats['q1']:.2f}, Q3 {price_stats['q3']:.2f})\n")
    report_lines.append("\n### Visualization notes\n")
    report_lines.append(f"{histogram_readability_explanation}\n")
    report_lines.append(f"\nCharts saved:\n- `{price_hist_path}` (sampled={price_hist_sampled})\n- `{price_box_path}` (sampled={price_box_sampled})\n")

    report_lines.append("\n## Part 3: Product Ratings (Stars)\n")
    report_lines.append("### Centrality\n")
    report_lines.append(f"- Mean rating: **{stars_stats['mean']:.2f}**\n")
    report_lines.append(f"- Median rating: **{stars_stats['median']:.2f}**\n")
    report_lines.append(f"- Mode rating: **{stars_stats['mode']:.2f}**\n" if stars_stats["mode"] is not None else "- Mode rating: **Not available**\n")
    report_lines.append("\n### Dispersion & distribution shape\n")
    report_lines.append(f"- Std dev: **{stars_stats['std_dev']:.4f}**\n")
    report_lines.append(f"- IQR: **{stars_stats['iqr']:.4f}**\n")
    report_lines.append(f"- Skewness: **{stars_skew:.4f}** (positive means more low ratings with a tail to higher values; negative means the opposite)\n")
    report_lines.append(f"- Kurtosis: **{stars_kurt:.4f}** (Fisher; >0 heavier tails than normal, <0 lighter tails)\n")
    report_lines.append(f"\nChart saved:\n- `{stars_hist_path}` (sampled={stars_hist_sampled})\n")

    report_path = "report.md"
    with open(report_path, "w", encoding="utf-8") as f:
        f.writelines(report_lines)

    print("\nDone.")
    print(f"Saved business report to: {report_path}")
    print(f"Saved plots to folder: {PLOTS_DIR}/")


if __name__ == "__main__":
    main()
