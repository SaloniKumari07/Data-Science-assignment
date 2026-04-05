# Q7: Boxplot - Student Marks in 5 Subjects
# Requirements: pip install matplotlib pandas

import matplotlib.pyplot as plt
import pandas as pd

marks_data = {
    'English':        [95, 95, 78, 88],
    'Maths':          [95, 76, 81, 63],
    'Hindi':          [90, 79, 75, 67],
    'Science':        [94, 77, 76, 77],
    'Social_Studies': [95, 89, 88, 80],
}
df = pd.DataFrame(marks_data)

plt.figure(figsize=(9, 5))
df.boxplot(column=list(marks_data.keys()), grid=False)
plt.title('Subject-wise Performance Analysis (Boxplot)')
plt.xlabel('Subject')
plt.ylabel('Marks')
plt.tight_layout()
plt.savefig('q7_marks_boxplot.png')
plt.show()
print("Q7 done.")
