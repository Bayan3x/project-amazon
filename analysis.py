import pandas as pd
df = pd.read_csv("amazon_cleaned.csv")
# just for check on cleaning
#print(cleaned_df.shape)
#print(cleaned_df.dtypes)
#print(cleaned_df.isnull().sum())

# Q1 how much products we have for every main category
print('///Q1///')
category_counts = (
    df["category"]
    .str.split("|")
    .str[0]
    .value_counts()
)

print(category_counts)

# Q2 the mean for actual price and discounted price
print('///Q2///')
print(df[["actual_price", "discounted_price"]].mean())

#ََQ3 the mean for discount percentage
print('///Q3///')
print(df["discount_percentage"].mean())
# Q4 How are product ratings distributed?
print('///Q4///')
print(df["rating"].value_counts().sort_index())
#The ratings are mainly concentrated between 3.8 and 4.4, with 4.1 being the most common rating. Very low and very high ratings are relatively rare.

# Q5 is there correlation between rating and rating count
print('///Q5///')
print(df[["rating", "rating_count"]].corr())
# the result is 0.102 the relation is to weak

# Q6 which catogry had high prices and less
print('///Q6///')
category_price = (
    df.assign(
        main_category=df["category"].str.split("|").str[0]
    )
    .groupby("main_category")[
        ["actual_price", "discounted_price"]
    ]
    .mean()
    .sort_values("actual_price", ascending=False)
)

print(category_price)
#Electronics has the highest average prices, while Toys&Games has the lowest average prices.

# Q7 Which categories have the highest discounts?
print('///Q7///')

category_discount = (
    df.assign(
        main_category=df["category"].str.split("|").str[0]
    )
    .groupby("main_category")["discount_percentage"]
    .mean()
    .sort_values(ascending=False)
)

print(category_discount)
# HomeImprovement had the highest average discount percentage at 57.5%, while Toys&Games had the lowest at 0%.

# Q8 Which products have the highest number of reviews?
print('///Q8///')
top_products = (
    df.groupby("product_id")
      .agg({
          "product_name": "first",
          "rating_count": "max"
      })
      .sort_values("rating_count", ascending=False)
      .head(10)
)

print(top_products)


#َQ9 Which products have the highest ratings, with a sufficient number of reviews?
print('///Q9///')
top_rated_products = (
    df.groupby("product_id")
      .agg({
          "product_name": "first",
          "rating": "max",
          "rating_count": "max"
      })
      .sort_values("rating", ascending=False)
      .head(10)
)

print(top_rated_products)
