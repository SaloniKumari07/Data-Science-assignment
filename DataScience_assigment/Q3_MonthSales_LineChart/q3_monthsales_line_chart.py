# Q3: Line chart from monthsales.csv (Year-Wise Sales)
# Requirements: pip install matplotlib

import matplotlib.pyplot as plt

months = [1, 2, 3, 4, 5, 6]
sales = {
    2018: [2500, 2200, 3000, 2800, 2750, 3500],
    2019: [2600, 1800, 2500, 3000, 3200, 2000],
    2020: [2450, 2000, 3000, 3100, 1950, 3550],
    2021: [3250, 3200, 3800, 2800, 2900, 2300],
}

plt.figure(figsize=(10, 5))
for year, values in sales.items():
    plt.plot(months, values, marker='o', label=str(year))

plt.title('Year-Wise Sales')
plt.xlabel('Months')
plt.ylabel('Sales')
plt.legend()
plt.tight_layout()
plt.savefig('q3_monthsales_line_chart.png')
plt.show()
print("Q3 done.")
