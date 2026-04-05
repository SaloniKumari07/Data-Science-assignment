# Q10: Histogram - Monthly Profit Ranges
# Requirements: pip install matplotlib

import matplotlib.pyplot as plt

profit = [180000, 210000, 220000, 215000, 205000,
          225000, 275000, 290000, 215000, 310000,
          340000, 210000]

plt.figure(figsize=(9, 5))
plt.hist(profit, bins=7, label='Profit data', color='steelblue', edgecolor='white')
plt.title('Profit data')
plt.xlabel('profit range in dollar')
plt.ylabel('Actual Profit in dollar')
plt.legend()
plt.tight_layout()
plt.savefig('q10_profit_histogram.png')
plt.show()
print("Q10 done.")
