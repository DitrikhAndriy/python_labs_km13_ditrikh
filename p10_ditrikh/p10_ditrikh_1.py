salary_list = [6.4, 9.35, 11.4, 14, 23.8, 28.15, 34.7]

salary_list_up = list(map(lambda i: i * 1.3, salary_list))
salary_list_index = list(map(lambda i, j: i - j, salary_list_up, salary_list))

print("Salary table:")
for i in range(len(salary_list)):
    print()
    print(round(salary_list[i], 2), round(salary_list_up[i], 2), round(salary_list_index[i], 2))