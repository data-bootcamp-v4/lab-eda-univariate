# 📊 Amazon UK Product Analysis – Univariate EDA

**By:** Paulina Mamiaga  

---

## 📌 Objective

The objective of this analysis is to explore and understand the structure and distribution of product listings on Amazon UK through univariate exploratory data analysis (EDA).

This study focuses on key product attributes such as **category, price, and customer ratings** in order to:

- Identify the most represented product categories and assess market concentration  
- Analyze pricing patterns, including central tendencies and variability  
- Understand customer rating behavior and detect potential biases or trends  

From a business perspective, this analysis aims to generate insights that support **product positioning, pricing strategies, and inventory decisions** in a competitive e-commerce environment.

---

## 📂 Data Source

Dataset used:  
👉 https://www.kaggle.com/datasets/asaniczka/uk-optimal-product-price-prediction/

---

# 🧠 Part 1: Understanding Product Categories

## 🔍 Key Findings

- The dataset shows **extreme concentration in a single category: _Sports & Outdoors_**
- This category dominates the dataset, representing the vast majority of listings
- Other categories (Beauty, Bath & Body, etc.) contribute only marginal shares (~2% each)

## 💡 Business Insights

👉 **Market Concentration Risk**
- The dataset is highly skewed → global insights may be misleading  
- Results are heavily driven by one dominant category  

👉 **Competitive Dynamics**
- High concentration → high competition  
- Smaller categories → potential niche opportunities  

👉 **Recommendation**
- Always segment analysis by category  
- Identify underrepresented categories for strategic positioning  

---

# 💰 Part 2: Product Pricing Analysis

## 📊 Central Tendency

- Mean price: **£89.24**
- Median price: **£19.09**
- Mode price: **£9.99**

## 📊 Dispersion

- Standard deviation: **345.61**
- Range: **£0 – £100,000**
- IQR: **£36**

## 🔍 Key Findings

- Strong gap between mean and median → **right-skewed distribution**
- Majority of products are low-priced
- Presence of extreme high-value outliers

## 💡 Business Insights

👉 **Skewed Pricing Structure**
- Marketplace operates in a **low-price, high-volume model**

👉 **Mean is Misleading**
- Average price is inflated by outliers  
- Median better represents typical product pricing  

👉 **Outliers**
- Extreme values distort analysis  
- Likely luxury or incorrectly priced products  

👉 **Recommendation**
- Use median & IQR for pricing strategy  
- Segment pricing by category  
- Consider removing or capping outliers  

---

# ⭐ Part 3: Product Ratings Analysis

## 📊 Centrality

- Mean rating: **2.15**
- Median rating: **0.0**
- Mode rating: **0.0**

## 📊 Dispersion

- Standard deviation: **2.19**
- IQR: **4.4**

## 🔍 Key Findings

- 50% of products have rating = 0  
- Sharp jump from 0 → 4.4 (75th percentile)  
- Ratings are not normally distributed  

## 💡 Business Insights

👉 **Critical Interpretation**
- Rating = 0 likely means **no reviews**, not poor quality  

👉 **Hidden Structure**
Two groups exist:
1. Products without ratings  
2. Products with high ratings (4–5 stars)  

👉 **Misleading Average**
- Mean rating underestimates real customer satisfaction  

👉 **Business Opportunity**
- Many products lack reviews → opportunity to influence perception early  

👉 **Recommendation**
- Separate analysis:
  - Rated products (stars > 0)
  - Unrated products (stars = 0)  

---

# 🚀 Overall Business Insights

The Amazon UK marketplace shows strong structural imbalances:

### 1. Category Concentration
- One category dominates the dataset  
- Risk of biased insights  

### 2. Price Skewness
- Most products are low-priced  
- Few outliers distort averages  

### 3. Rating Bias
- Many products have no ratings  
- Customer satisfaction is higher than it appears  

---

## 🎯 Final Takeaways

- Always segment before analyzing  
- Median > Mean for pricing decisions  
- Ratings must be interpreted carefully  
- Unrated products = growth opportunity  

---

## 🛠️ Tech Stack

- Python (Pandas, NumPy)
- Matplotlib / Seaborn
- Jupyter Notebook  

---

## 📎 Notes

- No missing values detected  
- Duplicate products exist at ASIN level  
- Large dataset (~2.4M rows) ensures robustness  

------

## 🌐 Data Source

[https://www.kaggle.com/datasets/asaniczka/uk-optimal-product-price-prediction/]