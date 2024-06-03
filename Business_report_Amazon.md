### Business report on Amazon dataset

# Product listings
- The Top 5 product categories are: Sports & Outdoors; Beauty; Handmade Clothing, Shoes & Accessories; Bath & Body; Birthday Gifts.

- The category Sports & Outdoors clearly dominates the product listings, with over 400 times as many listings as the following categories.

# Product pricing
- **Comment on centrality**: The average price point for products listed is around USD 89, far above the mode price point which is  USD 9.99. While there are a large number of products priced at USD 9.99 and the distribution is centred on the median at USD 19.09, there is a significant skew of the mean value - likely due to a significant number of high value products.

- **Comment on dispersion**: The relatively low IQR value suggests that there ought not to be too wide a spread in prices. However, the significant size of the std/var values suggest that a large number of high value items are present which skew the distribution and dispersion variables.

- **Comment on plots**: These plots are hard to read because there are some outlying values that result in the axes covering significantly larger range of values than is required for the vast majority of products. This could be rectified by excluding the outlying values.

# Product ratings
- **Comment on centrality**: The prevailing trend appears to be that customers either do **not** rate products or rate them as '0'. Given the likelihood of a significant number of zero values, it also seems that there are a relatively high number of high values, in order to achieve the mean value of 2.15. This would suggest a hollow distribution, with values concentrated at either end of the scale.

- **Comment on dispersion**: There is a medium variation in customer feedback, with a standard deviation of just over 2.19. This 'variation' may also be a result of a high number of zero values. The high value for the interquartile range suggests that there is a reasonable degree of variation, but this may also be due to a high proportion of polarised values.

- **Comment on skew and kurtosis**: The positive skew value suggests that the distribution leans slightly towards lower values (long tail). The kurtosis value of -1 suggests that the ratings values are relatively heavy-tailed and have a shallow peak.

- **Comment on histogram of ratings**: There are indeed a high value of 0 values, as well as a high proportion of values over 4, which explains the wide IQR value and relatively central mean value.



Data: Amazon product listings
Source: Kaggle
URL: https://www.kaggle.com/datasets/asaniczka/uk-optimal-product-price-prediction/
DA: mhga94