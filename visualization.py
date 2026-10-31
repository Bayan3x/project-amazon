import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv("amazon_cleaned.csv")

#1 Products by Category
category_counts = (
    df["category"]
    .str.split("|")
    .str[0]
    .value_counts()
)

sns.barplot(
    x=category_counts.index,
    y=category_counts.values
)

plt.xticks(rotation=45)
plt.title("Number of Products by Category")
plt.xlabel("Category")
plt.ylabel("Number of Products")

#plt.show()

#2 Rating distribution
sns.countplot(
    x="rating",
    data=df
)

plt.title("Rating Distribution")
plt.xlabel("Rating")
plt.ylabel("Number of Products")

#plt.show()

#3 Average Price by category
category_price = (
    df.assign(
        main_category=df["category"].str.split("|").str[0]
    )
    .groupby("main_category")[
        ["actual_price", "discounted_price"]
    ]
    .mean()
)

price_comparison = category_price.reset_index().melt(
    id_vars="main_category",
    value_vars=["actual_price", "discounted_price"],
    var_name="price_type",
    value_name="price"
)
sns.barplot(
    data=price_comparison,
    x="main_category",
    y="price",
    hue="price_type"
)

plt.xticks(rotation=45)
plt.title("Average Original vs Discounted Price by Category")
plt.xlabel("Category")
plt.ylabel("Average Price")

#plt.show()

#4 Average Discount by category
category_discount = (
    df.assign(
        main_category=df["category"].str.split("|").str[0]
    )
    .groupby("main_category")["discount_percentage"]
    .mean()
    .sort_values(ascending=False)
)
sns.barplot(
    x=category_discount.index,
    y=category_discount.values
)

plt.xticks(rotation=45)
plt.title("Average Discount by Category")
plt.xlabel("Category")
plt.ylabel("Average Discount (%)")

#plt.show()



#5 Rating vs Rating Count
plt.figure()

sns.scatterplot(
    data=df,
    x="rating_count",
    y="rating"
)

plt.title("Rating vs Rating Count")
plt.xlabel("Rating Count")
plt.ylabel("Rating")

plt.show()