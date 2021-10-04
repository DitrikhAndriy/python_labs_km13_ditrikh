salary_list = [6.4, 9.35, 11.4, 14, 23.8, 28.15, 34.7]

salary_list_up = [round((i * 1.3), 2) for i in salary_list]
salary_list_index = [round((salary_list_up[i] - salary_list[i]), 2) for i in range(len(salary_list))]

print("Salary table:"), print()
for i in range(len(salary_list)):
    print(salary_list[i], salary_list_up[i], salary_list_index[i])
    print()