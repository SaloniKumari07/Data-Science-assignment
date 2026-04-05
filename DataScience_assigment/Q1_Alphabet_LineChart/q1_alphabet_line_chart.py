# Q1: Line chart of Alphabet Inc. financial data
# Requirements: pip install matplotlib pandas numpy

import matplotlib.pyplot as plt
import pandas as pd

data = {
    'Date':  ['10-03-16', '10-04-16', '10-05-16', '10-06-16', '10-07-16'],
    'Open':  [774.25,     776.030029, 779.309998, 779.0,      779.659973],
    'High':  [776.065002, 778.710022, 782.070007, 780.47998,  779.659973],
    'Low':   [769.5,      772.890015, 775.650024, 775.539978, 770.75],
    'Close': [772.559998, 776.429993, 776.469971, 776.859985, 775.080017],
}
df = pd.DataFrame(data)

plt.figure(figsize=(10, 5))
plt.plot(df['Date'], df['Open'],  marker='o', label='Open')
plt.plot(df['Date'], df['High'],  marker='o', label='High')
plt.plot(df['Date'], df['Low'],   marker='o', label='Low')
plt.plot(df['Date'], df['Close'], marker='o', label='Close')

plt.title('Alphabet Inc. Stock Data (Oct 3-7, 2016)')
plt.xlabel('Date')
plt.ylabel('Price (USD)')
plt.legend()
plt.tight_layout()
plt.savefig('q1_alphabet_line_chart.png')
plt.show()
print("Q1 done.")
