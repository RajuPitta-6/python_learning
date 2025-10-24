# Heatmap – Correlation between numerical columns
import seaborn as sns
import matplotlib.pyplot as plt

df = sns.load_dataset('tips')

corr = df.corr(numeric_only=True)

sns.heatmap(corr, annot=True, cmap='magma', linewidths=0.5)
plt.title('Correlation Heatmap')
plt.show()

# Jointplot – Relation between two variables (scatter + hist)
sns.jointplot(x='total_bill', y='tip', data=df, kind='scatter', color='purple')
plt.show()

# Pairplot – Pairwise relationships for all numerical columns
sns.pairplot(df, hue='sex', palette='coolwarm')
plt.show()

# Regression Plot (regplot / lmplot)
sns.regplot(x='total_bill', y='tip', data=df, color='green')
plt.title('Regression Plot - Total Bill vs Tip')
plt.show()

# KDE Plot – Data distribution smoothly
sns.kdeplot(x='total_bill', data=df, shade=True, color='orange')
plt.title('KDE Plot - Total Bill Distribution')
plt.show()

# Violin Plot – Distribution + Boxplot combined
sns.violinplot(x='day', y='total_bill', data=df, palette='viridis')
plt.title('Violin Plot - Total Bill Distribution per Day')
plt.show()
