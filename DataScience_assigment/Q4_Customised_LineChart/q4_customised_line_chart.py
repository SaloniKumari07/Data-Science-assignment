# Q4: Customised Line Chart - Month Names on X-axis
# Requirements: pip install matplotlib

import matplotlib.pyplot as plt

month_names = ['January', 'February', 'March', 'April', 'May', 'June']
sales = {
    2018: [2500, 2200, 3000, 2800, 2750, 3500],
    2019: [2600, 1800, 2500, 3000, 3200, 2000],
    2020: [2450, 2000, 3000, 3100, 1950, 3550],
    2021: [3250, 3200, 3800, 2800, 2900, 2300],
}

plt.figure(figsize=(11, 5))
for year, values in sales.items():
    plt.plot(month_names, values,
             marker='*',
             markersize=10,
             linestyle='--',
             linewidth=3,
             label=str(year))

plt.title('Year-Wise Sales (Customised)')
plt.xlabel('Months')
plt.ylabel('Sales')
plt.legend()
plt.tight_layout()
plt.savefig('q4_customised_line_chart.png')
plt.show()
print("Q4 done.")
