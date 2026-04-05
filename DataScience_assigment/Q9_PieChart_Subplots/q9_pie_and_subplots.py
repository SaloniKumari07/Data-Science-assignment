# Q9a: Pie Chart - Total Sales per Product
# Q9b: Subplots - Bathing Soap & Face Wash Sales
# Requirements: pip install matplotlib

import matplotlib.pyplot as plt

# ── Q9a: Pie Chart ──────────────────────────────────────────────
products = ['Bathing Soap', 'Face Wash', 'Shampoo', 'Toothpaste', 'Moisturizer']
units    = [120000, 45000, 60000, 80000, 35000]

plt.figure(figsize=(8, 6))
plt.pie(units, labels=products, autopct='%1.1f%%', startangle=140)
plt.title('Total Units Sold per Product (Last Year)')
plt.tight_layout()
plt.savefig('q9a_pie_chart.png')
plt.show()
print("Q9a done.")

# ── Q9b: Subplots ────────────────────────────────────────────────
months       = list(range(1, 13))
bathing_soap = [9000, 6500, 9500, 8800, 7500, 7400, 9000, 9800, 7800, 10500, 12000, 13500]
face_wash    = [1500, 1200, 1350, 1200, 1750, 1550, 1250, 1450, 1800, 1900,  2100,  1750]

fig, (ax1, ax2) = plt.subplots(2, 1, figsize=(10, 8), sharex=True)

ax1.plot(months, bathing_soap, color='black', marker='o')
ax1.set_title('Sales data of a Bathingsoap')
ax1.set_ylabel('Sales units in number')

ax2.plot(months, face_wash, color='red', marker='o')
ax2.set_title('Sales data of a facewash')
ax2.set_ylabel('Sales units in number')
ax2.set_xlabel('Month Number')

plt.tight_layout()
plt.savefig('q9b_subplot_sales.png')
plt.show()
print("Q9b done.")
