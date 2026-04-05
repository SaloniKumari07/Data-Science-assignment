# Q8: Grouped Bar Chart - Scores by Group and Gender
# Requirements: pip install matplotlib numpy

import matplotlib.pyplot as plt
import numpy as np

means_men   = (22, 30, 35, 35, 26)
means_women = (25, 32, 30, 35, 29)
groups      = ('G1', 'G2', 'G3', 'G4', 'G5')

x     = np.arange(len(groups))
width = 0.35

fig, ax = plt.subplots(figsize=(9, 5))
ax.bar(x - width/2, means_men,   width, label='Men',   color='green')
ax.bar(x + width/2, means_women, width, label='Women', color='red')

ax.set_title('Scores by person')
ax.set_xlabel('Person')
ax.set_ylabel('Scores')
ax.set_xticks(x)
ax.set_xticklabels(groups)
ax.legend()
plt.tight_layout()
plt.savefig('q8_grouped_bar_gender.png')
plt.show()
print("Q8 done.")
