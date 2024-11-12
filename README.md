# EDA Univariate Analysis: Insights into Amazon UK Product Listings

## Objective:
The purpose of this analysis is to explore the distribution and characteristics of product listings on Amazon UK. By analyzing various attributes, such as product categories, pricing, and ratings, we aim to extract actionable business insights that can inform product positioning, pricing strategies, and inventory management.

## Dataset:
This analysis utilizes the **Amazon UK product dataset**, which contains information on product categories, brands, prices, ratings, and more. The dataset provides a comprehensive view of product listings on Amazon UK and is available for download on [Kaggle](https://www.kaggle.com/datasets/asaniczka/uk-optimal-product-price-prediction/). **Note:** The dataset is not included in the repository due to its large size (over 400MB).

---

## Part 1: Understanding Product Categories
### Business Question: 
What are the most popular product categories on Amazon UK, and how do they compare in terms of listing frequency?

The product listings on Amazon UK are heavily dominated by the **"Sports & Outdoors"** category, which accounts for a staggering 836,000 listings, more than 40 times the number of any other category. The remaining categories—**Beauty**, **Handmade Clothes**, **Bath & Body**, and **Birthday Gifts**—each contribute around 20,000 listings. This shows a much smaller but relatively equal distribution among them.

**Key Insight:** 
Approximately **9 out of 10 products** listed on Amazon UK belong to the **Sports & Outdoors** category.

---

## Part 2: Delving into Product Pricing
### Business Question: 
How are products priced on Amazon UK, and are there specific price points or ranges that are more common?

- The **average price** of products listed on Amazon UK is **£89.24**, which is much higher than the **most common price** of **£9.99**. 
- The **most frequent price** of £9.99 indicates that many products are priced lower, but the high average price suggests that a few high-priced items are significantly raising the overall mean.
- The **median price** is £19.09, meaning that half of the products are priced at or below this point.

**Key Insights:**
- The **prices range from £0.0 to £100,000.0**, with some products having prices that might be errors or inconsistencies, possibly involving multiple currencies. 
- There are **products priced significantly higher** than the majority, as illustrated by the **log price** distribution, where the majority of products fall within a price range of **£7 to £54** (log values 2 to 4).

**Visualizations:**
- The **box plot** showcases the spread of product prices, highlighting outliers on both ends of the price spectrum.

---

## Part 3: Unpacking Product Ratings
### Business Question: 
How do customers rate products on Amazon UK, and are there any patterns or tendencies in the ratings?

- To ensure accuracy, I filtered out products with no reviews, as these were skewed by ratings of **0 stars**.
- The **average rating** for products is **4.3 out of 5** stars, with the **most common rating** being **4.5 stars**.

**Key Insights:**
- The majority of ratings fall between **4.1 and 4.6**, indicating that most customers are satisfied with their purchases.
- **Skewness**: The ratings distribution has a **negative skew** (-1.77), meaning that most ratings are concentrated at the higher end of the scale.
- **Kurtosis**: The **kurtosis** value of **6.18** suggests that the distribution is **highly leptokurtic**, meaning there is a sharp peak around the most frequent ratings, with relatively few lower ratings.

**Overall Customer Sentiment:**
- There is a general trend of **high customer satisfaction**, with most ratings clustering near the maximum of **5 stars**.
- The **low variance** and **standard deviation** further support this, indicating minimal variation in the ratings.

---

## In Conclusion...
The product ratings in this dataset reveal a strong trend of **high customer satisfaction**, with an average rating of **4.3 stars** and the most frequent rating being **4.5 stars**. The distribution of ratings is **skewed to the right**, indicating that customers are generally very satisfied, with relatively few low ratings. The **high kurtosis** suggests that the ratings are concentrated around the higher end of the scale, showing that customers typically give products positive reviews. Overall, businesses can infer that the products in this dataset enjoy broad approval, with only occasional dissatisfaction.
