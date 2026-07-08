# ==========================================
# CAPSTONE PROJECT - SUPERSTORE SALES ANALYSIS
# ==========================================

import pandas as pd
import matplotlib.pyplot as plt

# ==========================
# LOAD DATASET
# ==========================

df = pd.read_csv("Sample - Superstore1.csv", encoding="latin1")

print("First 5 Rows")
print(df.head())

print("\nDataset Shape:")
print(df.shape)

print("\nColumns:")
print(df.columns)

print("\nDataset Info:")
print(df.info())

print("\nMissing Values:")
print(df.isnull().sum())

print("\nStatistical Summary:")
print(df.describe())

# ==========================
# DATA CLEANING
# ==========================

df.drop_duplicates(inplace=True)

df["Order Date"] = pd.to_datetime(df["Order Date"])
df["Ship Date"] = pd.to_datetime(df["Ship Date"])

print("\nDuplicates Removed")
print(df.shape)

# ==========================
# TOTAL SALES & PROFIT
# ==========================

print("\nTotal Sales:", df["Sales"].sum())
print("Total Profit:", df["Profit"].sum())

# ==========================
# SALES BY CATEGORY
# ==========================

category_sales = df.groupby("Category")["Sales"].sum()

plt.figure(figsize=(8,5))
category_sales.plot(kind="bar")
plt.title("Sales by Category")
plt.xlabel("Category")
plt.ylabel("Sales")
plt.show()

# ==========================
# PROFIT BY CATEGORY
# ==========================

category_profit = df.groupby("Category")["Profit"].sum()

plt.figure(figsize=(8,5))
category_profit.plot(kind="bar")
plt.title("Profit by Category")
plt.xlabel("Category")
plt.ylabel("Profit")
plt.show()

# ==========================
# SALES BY REGION
# ==========================

region_sales = df.groupby("Region")["Sales"].sum()

plt.figure(figsize=(8,5))
region_sales.plot(kind="pie", autopct="%1.1f%%")
plt.title("Region-wise Sales")
plt.ylabel("")
plt.show()

# ==========================
# TOP 10 STATES BY SALES
# ==========================

top_states = df.groupby("State")["Sales"].sum().sort_values(ascending=False).head(10)

plt.figure(figsize=(10,5))
top_states.plot(kind="bar")
plt.title("Top 10 States by Sales")
plt.xlabel("State")
plt.ylabel("Sales")
plt.show()

# ==========================
# TOP 10 CUSTOMERS
# ==========================

top_customers = df.groupby("Customer Name")["Sales"].sum().sort_values(ascending=False).head(10)

plt.figure(figsize=(10,5))
top_customers.plot(kind="bar")
plt.title("Top 10 Customers")
plt.xlabel("Customer")
plt.ylabel("Sales")
plt.show()

# ==========================
# SALES DISTRIBUTION
# ==========================

plt.figure(figsize=(8,5))
plt.hist(df["Sales"], bins=30)
plt.title("Sales Distribution")
plt.xlabel("Sales")
plt.ylabel("Frequency")
plt.show()

# ==========================
# PROFIT DISTRIBUTION
# ==========================

plt.figure(figsize=(8,5))
plt.hist(df["Profit"], bins=30)
plt.title("Profit Distribution")
plt.xlabel("Profit")
plt.ylabel("Frequency")
plt.show()

# ==========================
# DISCOUNT VS PROFIT
# ==========================

plt.figure(figsize=(8,5))
plt.scatter(df["Discount"], df["Profit"])
plt.title("Discount vs Profit")
plt.xlabel("Discount")
plt.ylabel("Profit")
plt.show()

# ==========================
# MONTHLY SALES TREND
# ==========================

df["Month"] = df["Order Date"].dt.to_period("M")

monthly_sales = df.groupby("Month")["Sales"].sum()

plt.figure(figsize=(12,5))
monthly_sales.plot()
plt.title("Monthly Sales Trend")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.show()

# ==========================
# SUB-CATEGORY SALES
# ==========================

subcategory_sales = df.groupby("Sub-Category")["Sales"].sum().sort_values()

plt.figure(figsize=(10,8))
subcategory_sales.plot(kind="barh")
plt.title("Sales by Sub-Category")
plt.xlabel("Sales")
plt.show()

# ==========================
# CORRELATION ANALYSIS
# ==========================

correlation = df[["Sales","Quantity","Discount","Profit"]].corr()

print("\nCorrelation Matrix")
print(correlation)

# ==========================
# TOP 10 PRODUCTS BY SALES
# ==========================

top_products = df.groupby("Product Name")["Sales"].sum().sort_values(ascending=False).head(10)

plt.figure(figsize=(10,5))
top_products.plot(kind="bar")
plt.title("Top 10 Products by Sales")
plt.xlabel("Product")
plt.ylabel("Sales")
plt.show()

# ==========================
# BUSINESS INSIGHTS
# ==========================

print("\nBusiness Insights:")
print("1. Technology category generally generates high sales.")
print("2. High discounts often reduce profit.")
print("3. Some states contribute significantly to overall sales.")
print("4. Top customers generate a large share of revenue.")
print("5. Monthly trends help identify peak sales periods.")

print("\nAnalysis Completed Successfully!")