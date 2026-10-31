import pandas as pd

df = pd.read_csv("amazon.csv")


#print(" <<the begining>>")
#print(df.shape)
# print(df.info())
# print ('this is how much we have missing value')
# print(df.isnull().sum())
# print ('this is about duplicated ')
# print(df.duplicated().sum())
# print('//////sample //////')
# print(df[[
    #"discounted_price",
 #   "actual_price",
  #  "discount_percentage",
   # "rating",
  #  "rating_count"
#]].head(10))
#print(df["discount_percentage"].head(10))
#print(df["rating"].head(10))
# there is problem in the five columns , and I need to transform them to num
# I need to know the missing value in rating_count
#print(df[df["rating_count"].isnull()]["rating_count"])
# the missing values in rows 324, 282
#print(df.loc[[282, 324], [
    #"product_name",
    #"rating",
  #  "rating_count",
   # "actual_price",
  #  "discounted_price"
#]])
# the upper code just to know what it was the product

#//////////cleaning and fixed columns

#1 rating col
# her from the easier one ratint column from str into float
#print(df[df["rating"] == "|"])
# I found the row 
df["rating"] = pd.to_numeric(df["rating"], errors="coerce")
#print(df["rating"].dtype)



#2 discount_percentage col
# this is for discount_percentage I'm gonna remove % and transform into float
df["discount_percentage"] = df["discount_percentage"].str.replace("%", "")

# still str now we will transform

df["discount_percentage"] = pd.to_numeric(
    df["discount_percentage"],
    errors="coerce"
)
#print(df["discount_percentage"].dtype)



#3 actual_price col
# 3.1 I will clean the num form ₹
df["actual_price"] = df["actual_price"].str.replace("₹", "")

# 3.2 I will clean the num form ,

df["actual_price"] = df["actual_price"].str.replace(",", "")

# 3.3 transform from str into float
df["actual_price"] = pd.to_numeric(
    df["actual_price"],
    errors="coerce"
)


#4 discounted_price col
# 4.1 I will clean the num form ₹
df["discounted_price"] = df["discounted_price"].str.replace("₹", "")
# 4.2 I will clean the num form ,
df["discounted_price"] = df["discounted_price"].str.replace(",", "")
# 4.3 transform from str into float
df["discounted_price"] = pd.to_numeric(
    df["discounted_price"],
    errors="coerce"
)


#5  rating_count col
#5.1 I will clean the num form ,
df["rating_count"] = df["rating_count"].str.replace(",", "")
# 5.2 transform from str into float
df["rating_count"] = pd.to_numeric(
    df["rating_count"],
    errors="coerce"
)

#print(df["rating_count"].head(10))
#print(df["rating_count"].dtype)
#print(df["rating_count"].isnull().sum())


#//////////////After cleaning//////////////////////


# print('////check about datatypes')
# print(df.dtypes)
# print('////check about missing values')
# print(df.isnull().sum())
# print('////check about duplicate')
# print(df.duplicated().sum())


# to be ensure form logical num in rating
#print(df["rating"].min())
#print(df["rating"].max())

#print(df["rating"].value_counts().sort_index())
#print(df["category"].head(10))

#to check how much we have category
#print(df["category"].nunique())
# to know how many we have main category
##print(df["category"].str.split("|").str[0].value_counts())

#print(df["category"].str.split("|").str.len().value_counts().sort_index())
#print(df["category"].isnull().sum())
#print(df["category"].head(10).tolist())
# at the end of category I realized there is no misssing value and | is for subcategory

#print(df["product_id"].duplicated().sum()) # =114

#print(df[df["product_id"].duplicated()]["product_id"].value_counts().head(10))
#print(df[df["product_id"] == "B07JW9H4J1"])

#print(df.loc[[0, 369, 614], [
    #"product_id",
   # "product_name",
    #"category",
    #"discounted_price",
   # "actual_price",
  #  "discount_percentage",
   # "rating",
    #"rating_count"
#]].to_string()) # the rows deiffer in rating_count col


#print(df["product_id"].nunique()) # the result is 1351


# I am goona to see if there is missing value on product_name
#print(df["product_name"].isnull().sum()) # the result is 0
#print(df["product_name"].duplicated().sum()) # the result is 128
#print(df["product_name"].value_counts().head(10))
# there is no missing values 

#print(df["about_product"].isnull().sum()) # about_product col = 0
#print(df["user_id"].isnull().sum()) # user_id col = 0
#print(df["user_name"].isnull().sum())# user_name col = 0
#print(df["review_id"].isnull().sum()) # review_id col =0
#print(df["review_title"].isnull().sum()) # eview_title col = 0
#print(df["review_content"].isnull().sum())# review_content col = 0
#print(df["img_link"].isnull().sum())# img_link col = 0
#print(df["product_link"].isnull().sum())# product_link col = 0
df.to_csv("amazon_cleaned.csv", index=False)