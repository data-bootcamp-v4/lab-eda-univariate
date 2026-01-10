# Amazon UK Product Dataset — Univariate EDA Report
## Part 1: Product Categories
### Top 5 categories by listing frequency
- **Sports & Outdoors**: 836,265 listings
- **Beauty**: 19,312 listings
- **Handmade Clothing, Shoes & Accessories**: 19,229 listings
- **Bath & Body**: 19,092 listings
- **Birthday Gifts**: 18,978 listings

Top category share: **34.22%**. A single category dominates the listings.

Charts saved:
- `plots/category_top20_bar.png`
- `plots/category_top10_pie.png`

## Part 2: Product Pricing
### Centrality
- Mean price: **89.24**
- Median price: **19.09**
- Mode price: **9.99**

### Dispersion
- Std dev: **345.61**
- Range: **100000.00** (min 0.00, max 100000.00)
- IQR: **36.00** (Q1 9.99, Q3 45.99)

### Visualization notes
Price distributions often have a long right tail (a small number of very expensive products). This stretches the x-axis and compresses the bulk of products into a narrow area. Common fixes are: using a log-scaled x-axis, limiting to a percentile range (e.g., <= 95th percentile), or plotting separate histograms for different price bands.

Charts saved:
- `plots/price_hist.png` (sampled=True)
- `plots/price_boxplot.png` (sampled=True)

## Part 3: Product Ratings (Stars)
### Centrality
- Mean rating: **2.15**
- Median rating: **0.00**
- Mode rating: **0.00**

### Dispersion & distribution shape
- Std dev: **2.1949**
- IQR: **4.4000**
- Skewness: **0.0812** (positive means more low ratings with a tail to higher values; negative means the opposite)
- Kurtosis: **-1.9260** (Fisher; >0 heavier tails than normal, <0 lighter tails)

Chart saved:
- `plots/stars_hist.png` (sampled=True)
