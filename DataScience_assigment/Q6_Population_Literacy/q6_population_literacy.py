# Q6: Scatter Plot + Bar Chart - Population vs Literacy Rate
# Requirements: pip install matplotlib pandas numpy

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

data = {
    'State':        ['Maharashtra', 'Gujarat', 'Rajasthan', 'UP',
                     'WestBengal', 'Odisha', 'Bihar', 'Assam',
                     'TamilNadu', 'Kerala', 'Karnataka', 'AndhraPradesh'],
    'Population':   [112374333, 60383628, 68548437, 199812341,
                     91276115,  41974218, 104099452, 31205576,
                     72147030,  33406061, 61095297,  84580777],
    'LiteracyRate': [82.9, 78.0, 66.1, 67.7,
                     76.3, 72.9, 61.8, 72.2,
                     80.1, 93.9, 75.6, 67.0],
    'Region':       ['West', 'West', 'West', 'North',
                     'East', 'East', 'East', 'East',
                     'South', 'South', 'South', 'South'],
}
df = pd.DataFrame(data)

regions = df['Region'].unique()
colors  = {'East': 'blue', 'West': 'green', 'North': 'orange', 'South': 'red'}

fig, axes = plt.subplots(1, 2, figsize=(14, 5))

ax1 = axes[0]
for region in regions:
    subset = df[df['Region'] == region]
    sizes  = np.sqrt(subset['LiteracyRate']) * 20
    ax1.scatter(subset['Population'], subset['LiteracyRate'],
                marker='D', s=sizes, label=region,
                color=colors[region], alpha=0.8)
ax1.set_title('Population vs Literacy Rate by Region')
ax1.set_xlabel('Population')
ax1.set_ylabel('Literacy Rate (%)')
ax1.legend()

avg_literacy = df.groupby('Region')['LiteracyRate'].mean()
ax2 = axes[1]
ax2.bar(avg_literacy.index, avg_literacy.values,
        color=[colors[r] for r in avg_literacy.index])
ax2.set_title('Average Literacy Rate by Region')
ax2.set_xlabel('Region')
ax2.set_ylabel('Average Literacy Rate (%)')

plt.tight_layout()
plt.savefig('q6_population_literacy.png')
plt.show()
print("Q6 done.")
