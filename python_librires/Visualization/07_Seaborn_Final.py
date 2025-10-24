# Custom Figure Size and Style
import seaborn as sns
import matplotlib.pyplot as plt

sns.set_style('whitegrid')
plt.figure(figsize=(8,5))  # width=8, height=5 inches

df = sns.load_dataset('tips')

sns.barplot(x='day', y='total_bill', data=df, palette='magma')
plt.title('Average Total Bill per Day', fontsize=14, weight='bold')
plt.xlabel('Day of Week', fontsize=12)
plt.ylabel('Average Bill ($)', fontsize=12)
plt.show()

# Add Annotations (values on bars)
plt.figure(figsize=(8,5))
graph = sns.barplot(x='day', y='total_bill', data=df, palette='crest')

for p in graph.patches:
    graph.annotate(format(p.get_height(), '.1f'),
                   (p.get_x() + p.get_width() / 2., p.get_height()),
                   ha='center', va='center',
                   xytext=(0, 9),
                   textcoords='offset points')

plt.title('Annotated Barplot - Average Total Bill')
plt.show()

# Saving Your Plot
plt.figure(figsize=(8,5))
sns.boxplot(x='day', y='tip', data=df, palette='viridis')
plt.title('Tips Distribution per Day')
plt.savefig('tips_boxplot.png', dpi=300, bbox_inches='tight')
plt.show()


# Combine Multiple Plots in One Figure (Grid)
fig, axes = plt.subplots(2, 2, figsize=(12,10))

sns.histplot(df['total_bill'], bins=20, kde=True, ax=axes[0,0], color='purple')
sns.boxplot(x='day', y='total_bill', data=df, ax=axes[0,1], palette='magma')
sns.scatterplot(x='total_bill', y='tip', hue='day', data=df, ax=axes[1,0])
sns.heatmap(df.corr(numeric_only=True), annot=True, cmap='coolwarm', ax=axes[1,1])

plt.suptitle('Tips Dataset - Multi Visualization Summary', fontsize=16, weight='bold')
plt.tight_layout()
plt.show()

# Custom Themes + Backgrounds
sns.set_style('darkgrid')
sns.set_palette('Set2')
sns.set_context('talk')

sns.scatterplot(x='total_bill', y='tip', hue='day', data=df)
plt.title('Custom Theme Scatter Plot')
plt.show()
