import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
df = sns.load_dataset('healthexp')

# Define countries
countries = ['Germany', 'USA']
colors = ["#509C95", '#81C784']

plt.figure(figsize=(12, 6))
for i, country in enumerate(countries, 1):
    df_country = df[df['Country'] == country].tail(10)
    plt.subplot(1, 2, i)
    
    bars = plt.bar(df_country['Year'], df_country['Life_Expectancy'],
                   color=colors[i-1], edgecolor='black', alpha=0.8)
    
    # Titles & labels
    plt.title(f"📊 Life Expectancy in {country} (Last 10 Years)", fontsize=13, fontweight='bold')
    plt.ylabel('Life Expectancy')
    plt.xlabel('Years')
    plt.xticks(rotation=90, ha='center')
    plt.grid(axis='y', linestyle='--', alpha=0.4)
    
    # Annotate bars
    for bar in bars.patches:
        value = bar.get_height()
        plt.text(bar.get_x() + bar.get_width()/2, value + 0.3,
                 f"{value:.1f}", ha='center', fontsize=10,
                 color='black', fontweight='semibold')
plt.suptitle('Comparison of Life Expectancy between Germany and USA', fontsize=15, fontweight='bold', color='darkred')
plt.tight_layout(rect=[0, 0, 1, 0.97])
plt.show()
