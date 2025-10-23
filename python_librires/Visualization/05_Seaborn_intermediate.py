import seaborn as sns
import matplotlib.pyplot as plt

sns.set_style('darkgrid')   # options: darkgrid, whitegrid, dark, white, ticks

df = sns.load_dataset('tips')

sns.scatterplot(x='total_bill', y='tip', data=df.head())
plt.title('Seaborn Theme Example - darkgrid')
plt.show()

# Context Settings (set_context)
sns.set_context('notebook')  # options: paper, notebook, talk, poster

sns.barplot(x='day', y='total_bill', data=df, palette='magma')
plt.title('Barplot with talk context')
plt.show()

# Color Palettes (advanced use)
colors = sns.color_palette('coolwarm', 5)
sns.palplot(colors)  # shows palette strip

# Subplots with Seaborn + Matplotlib
fig, axes = plt.subplots(1, 2, figsize=(12,5))

sns.boxplot(x='day', y='total_bill', data=df, ax=axes[0], palette='Set2')
axes[0].set_title('Boxplot - Total Bill by Day')

sns.violinplot(x='day', y='tip', data=df, ax=axes[1], palette='viridis')
axes[1].set_title('Violinplot - Tips by Day')

plt.tight_layout()
plt.show()

# Figure-Level Plots (FacetGrid)
g = sns.FacetGrid(df, col='sex')
g.map_dataframe(sns.scatterplot, x='total_bill', y='tip')
plt.show()

# Custom Titles, Labels & Legends
sns.set_style('whitegrid')
sns.scatterplot(x='total_bill', y='tip', hue='day', data=df, palette='Set1')

plt.title('Total Bill vs Tip by Day')
plt.xlabel('Total Bill (in $)')
plt.ylabel('Tip Amount (in $)')
plt.legend(title='Day of Week')
plt.show()
print(df.head())