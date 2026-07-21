## Lab - EDA Univariate Analysis: Diving into Amazon UK Product Insights

**Objective**: Explore the product listing dynamics on Amazon UK to extract actionable business insights. By understanding the distribution, central tendencies, and relationships of various product attributes, businesses can make more informed decisions on product positioning, pricing strategies, and inventory management.

**Dataset**: This lab utilizes the [Amazon UK product dataset](https://www.kaggle.com/datasets/asaniczka/uk-optimal-product-price-prediction/)
which provides information on product categories, brands, prices, ratings, and more from from Amazon UK. You'll need to download it to start working with it.


---

### Part 1: Understanding Product Categories

**Business Question**: What are the most popular product categories on Amazon UK, and how do they compare in terms of listing frequency?
Sports & Outdoors alone accounts for over a third (34.2%) of every listing in the dataset — more than 40x the size of the next-largest category. Everything after it (Beauty, Handmade goods, Bath & Body, etc.) sits in a tight, thin band around 0.7–0.8% each. So the real picture is: one category is massively over-represented, and the remaining 295 categories form the long tail.

1. **Frequency Tables**:
    - Generate a frequency table for the product `category`.
    Frequency table — top 15 categories

Category	Listings	% of all listings
Sports & Outdoors	836,265	34.22%
Beauty	19,312	0.79%
Handmade Clothing, Shoes & Accessories	19,229	0.79%
Bath & Body	19,092	0.78%
Birthday Gifts	18,978	0.78%
Manicure & Pedicure Products	18,940	0.78%
Skin Care	18,769	0.77%
Make-up	18,756	0.77%
Hair Care	18,735	0.77%
Fragrances	18,564	0.76%

    - Which are the top 5 most listed product categories?
    Top 5 most listed categories: Sports & Outdoors, Beauty, Handmade Clothing/Shoes & Accessories, Bath & Body, Birthday Gifts.

2. **Visualizations**:
    - Display the distribution of products across different categories using a bar chart. *If you face problems understanding the chart, do it for a subset of top categories.*
    Bar chart: Sports & Outdoors (red) dwarfs every other category — its bar is roughly 43x longer than the next one down (Beauty, at ~19K listings).

    - For a subset of top categories, visualize their proportions using a pie chart. Does any category dominate the listings?
    Pie chart: Sports & Outdoors takes over a third of the entire pie by itself, while the other 295 categories combined (the grey "Other" slice plus the thin colored slivers) fill the rest.

---

### Part 2: Delving into Product Pricing

**Business Question**: How are products priced on Amazon UK, and are there specific price points or ranges that are more common?

1. **Measures of Centrality**:
    - Calculate the mean, median, and mode for the `price` of products.
    Statistic	Value
Mean	£89.24
Median	£19.09
Mode	£9.99 (appears 48,922 times)

    - What's the average price point of products listed? How does this compare with the most common price point (mode)?
    Average vs. most common price: these tell very different stories. The average price (£89.24) is dragged way up by a relatively small number of expensive products, while the median (£19.09) and mode (£9.99) reflect what a "typical" listing actually costs. The mean is roughly 4.7x the median and 9x the mode — a strong signal of right skew, not a normal, bell-shaped price distribution.

2. **Measures of Dispersion**:
    - Determine the variance, standard deviation, range, and interquartile range for product `price`.
    Variance	119,445.49
Std deviation	£345.61
Min / Max	£0.00 / £100,000.00
Range	£100,000.00
Q1 / Q3	£9.99 / £45.99
IQR	£36.00
    - How varied are the product prices? Are there any indicators of a significant spread in prices?
    How varied are prices? Very — but unevenly so. The standard deviation (£345.61) is nearly 4x the mean itself, which is a strong red flag for extreme outliers rather than genuine broad-based spread. The full range (£0–£100,000) is dominated entirely by a tiny number of extreme listings. The IQR is a much more trustworthy picture: the middle 50% of products fall in a narrow £9.99–£45.99 band. Using the standard 1.5×IQR rule, 327,688 products (13.4%) are flagged as statistical outliers (priced above £99.99) — that's a large chunk of the catalogue sitting in the "expensive" tier, not just a handful of anomalies.

3. **Visualizations**:
    - Is there a specific price range where most products fall? Plot a histogram to visualize the distribution of product prices. *If its hard to read these diagrams, think why this is, and explain how it could be solved.*.
    Very — but unevenly so. The standard deviation (£345.61) is nearly 4x the mean itself, which is a strong red flag for extreme outliers rather than genuine broad-based spread. The full range (£0–£100,000) is dominated entirely by a tiny number of extreme listings. The IQR is a much more trustworthy picture: the middle 50% of products fall in a narrow £9.99–£45.99 band. Using the standard 1.5×IQR rule, 327,688 products (13.4%) are flagged as statistical outliers (priced above £99.99) — that's a large chunk of the catalogue sitting in the "expensive" tier, not just a handful of anomalies.
    - Are there products that are priced significantly higher than the rest? Use a box plot to showcase the spread and potential outliers in product pricing. 
    Unambiguously yes. In the full-range box plot (left), the box itself is squashed into a barely visible line near £0 — that's how extreme the highest-priced listings are relative to everything else; a sea of red outlier dots stretches all the way up toward £100,000. Zooming in to £0–£250 (right) reveals the actual box (Q1–Q3, £9.99–£45.99), the median line, and whiskers clearly, with dense outlier clustering starting just above £100.

---

### Part 3: Unpacking Product Ratings

**Business Question**: How do customers rate products on Amazon UK, and are there any patterns or tendencies in the ratings?
Quick note before the numbers: 50.2% of listings (1,225,641 of 2,443,651) have stars = 0 with zero reviews — these are unrated products, not products rated "0 stars." Including them would make it look like customers rate Amazon UK products terribly, which is false — it just means half the catalogue has no reviews yet. All stats below use the 1,218,010 actually-rated products, with the raw all-listings numbers shown for contrast.

1. **Measures of Centrality**:
    - Calculate the mean, median, and mode for the `rating` of products.
    Mean	4.319	2.153
Median	4.400	0.000
Mode	4.5 (151,577 listings)	0.0
    - How do customers generally rate products? Is there a common trend?
    Common trend: among products people have actually reviewed, customers rate generously and consistently — mean, median, and mode all sit tightly in the 4.3–4.5 range. The "all listings" column is a good illustration of why that filter mattered: taken at face value it implies a median rating of 0, which would be a completely wrong read on customer sentiment.

2. **Measures of Dispersion**:
    - Determine the variance, standard deviation, and interquartile range for product `rating`.
    Variance	0.308
Std deviation	0.555
Q1 / Q3	4.1 / 4.6
IQR	0.5
    - Are the ratings consistent, or is there a wide variation in customer feedback?
    Consistency: ratings are quite consistent. A standard deviation of ~0.55 stars and an IQR of just 0.5 (4.1–4.6) means the middle half of all rated products sit within half a star of each other — there isn't a lot of disagreement in the aggregate, though individual products can obviously vary.

3. **Shape of the Distribution**:
    - Calculate the skewness and kurtosis for the `rating` column. 
    Skewness	-2.38
Excess kurtosis	9.78
    - Are the ratings normally distributed, or do they lean towards higher or lower values?
    Skewness (-2.38) is strongly negative: a long tail stretches down toward 1 star while the bulk of ratings pile up near the top (4–5 stars). Ratings lean heavily toward higher values.
Excess kurtosis (9.78) is far above 0 (normal), meaning the distribution is sharply peaked around its center with heavier tails than a bell curve — ratings cluster tightly around ~4.5 stars, with a thin but present spread of lower outliers pulling the tail down.

4. **Visualizations**:
    - Plot a histogram to visualize the distribution of product ratings. Is there a specific rating that is more common?
    Yes — 4.5 stars is the single most common exact value (151,577 listings), closely followed by 4.6, 4.4, and a straight 5.0. The left panel (rated only) shows a clear peak in the 4.3–4.7 range with a sharp left skew — very few products land below 3 stars. The right panel (all listings) shows exactly why the unrated group had to be excluded: that enormous red spike at 0 would otherwise swamp the chart and make "0 stars" look like the dominant rating, when it's really "not yet reviewed."

---

**Submission**: Submit a Jupyter Notebook which contains code and a business-centric report summarizing your findings. 

