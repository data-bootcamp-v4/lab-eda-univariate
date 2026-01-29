import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Load dataset
df = pd.read_csv("amazon_uk.csv")

# Preview data
df.head()

# PART 1: Understanding Product Categories
# Frequency Table
category_freq = df['category'].value_counts()
category_freq

# Top 5 Most Listed Categories
top_5_categories = category_freq.head(5)
top_5_categories

# Bar Chart – Top Categories
top_5_categories.plot(kind='bar')
plt.title("Top 5 Product Categories on Amazon UK")
plt.xlabel("Category")
plt.ylabel("Number of Listings")
plt.xticks(rotation=45)
plt.show()

# Pie Chart – Category Proportions
top_5_categories.plot(kind='pie', autopct='%1.1f%%')
plt.title("Proportion of Listings by Top Categories")
plt.ylabel("")
plt.show()

# PART 2: Delving into Product Pricing
mean_price = df['price'].mean()
median_price = df['price'].median()
mode_price = df['price'].mode()[0]

mean_price, median_price, mode_price

# Measures of Dispersion
plt.hist(df['price'], bins=50)
plt.title("Distribution of Product Prices")
plt.xlabel("Price (£)")
plt.ylabel("Frequency")
plt.show()

# Alternative (to improve readability)
df[df['price'] < 200]['price'].hist(bins=40)
plt.title("Price Distribution (Prices under £200)")
plt.xlabel("Price (£)")
plt.ylabel("Frequency")
plt.show()

# Box Plot – Price Outliers
plt.boxplot(df['price'], vert=False)
plt.title("Box Plot of Product Prices")
plt.xlabel("Price (£)")
plt.show()

# PART 3: Unpacking Product Ratings
# Measures of Centrality
mean_rating = df['rating'].mean()
median_rating = df['rating'].median()
mode_rating = df['rating'].mode()[0]

mean_rating, median_rating, mode_rating

# Measures of Dispersion
rating_variance = df['rating'].var()
rating_std = df['rating'].std()
rating_iqr = df['rating'].quantile(0.75) - df['rating'].quantile(0.25)

rating_variance, rating_std, rating_iqr

# Shape of Distribution (Skewness & Kurtosis)
rating_skewness = df['rating'].skew()
rating_kurtosis = df['rating'].kurtosis()

rating_skewness, rating_kurtosis

# Histogram – Ratings
plt.hist(df['rating'], bins=20)
plt.title("Distribution of Product Ratings")
plt.xlabel("Rating")
plt.ylabel("Frequency")
plt.show()

# Optional: Clean Data (if needed)
df = df.dropna(subset=['category', 'price', 'rating'])



