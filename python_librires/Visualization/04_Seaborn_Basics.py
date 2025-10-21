import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# Load a sample dataset
tips = sns.load_dataset('tips')   # Restaurant bills dataset
print(tips.head())

# Show average tip by gender
sns.barplot(x='sex', y='tip', data=tips, palette='viridis')

plt.title("Average Tip by Gender")
plt.xlabel("Gender")
plt.ylabel("Average Tip ($)")
plt.show()

# Line plot of total_bill vs tip
sns.lineplot(x='total_bill', y='tip', data=tips, color='orange')

plt.title("Tip Trend vs Total Bill")
plt.xlabel("Total Bill ($)")
plt.ylabel("Tip ($)")
plt.show()

# Scatter plot with gender color coding
sns.scatterplot(x='total_bill', y='tip', hue='sex', data=tips.head(10), style='time')

plt.title("Bill vs Tip by Gender")
plt.xlabel("Total Bill ($)")
plt.ylabel("Tip ($)")
plt.show()


# Count of customers by day
sns.countplot(x='day', data=tips, palette='magma')

plt.title("Customer Count per Day")
plt.xlabel("Day of Week")
plt.ylabel("Count")
plt.show()
