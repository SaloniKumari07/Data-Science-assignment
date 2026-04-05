# Q5: Bar Chart - Compu-Tech Department vs No. of Employees
# Requirements: pip install matplotlib

import matplotlib.pyplot as plt

departments = ['HR', 'Sales', 'Finance', 'Marketing', 'IT']
no_of_emp   = [40, 30, 35, 32, 45]

plt.figure(figsize=(8, 5))
plt.bar(departments, no_of_emp, color='red')
plt.title('Compu-Tech Employee Data')
plt.xlabel('Departments')
plt.ylabel('Number of Employees')
plt.tight_layout()
plt.savefig('q5_department_bar.png')
plt.show()
print("Q5 done.")
