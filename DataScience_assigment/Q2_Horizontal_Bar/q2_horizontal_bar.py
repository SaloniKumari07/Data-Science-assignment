# Q2: Horizontal Bar Plot - Students vs Marks
# Requirements: pip install matplotlib

import matplotlib.pyplot as plt

nos   = [2, 9, 20, 25, 30, 39]
marks = [12, 24, 25, 27, 29, 30]

plt.figure(figsize=(8, 5))
plt.barh(marks, nos, color='steelblue')
plt.xlabel('Number of Students')
plt.ylabel('Marks Obtained')
plt.title('Number of Students vs Marks Obtained')
plt.tight_layout()
plt.savefig('q2_horizontal_bar.png')
plt.show()
print("Q2 done.")
