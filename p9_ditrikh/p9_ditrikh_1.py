import numpy as np
import itertools
from functools import reduce

def random_matrix(dimension):
    matrix = np.random.randint(10, size = (dimension, dimension))
    return matrix

def permutation(dimension):
    permutations = list(itertools.permutations(''.join(str(i) for i in range(1, dimension+1)), dimension))
    return permutations

def multiplication(permutations):
    perm = [[matrix[int(j)][int(i[j])-1] for j in range(dimension)] for i in permutations]
    sign = [len([1 for j in range(len(i)-1) for k in range(j+1,len(i)) if int(i[j])>int(i[k])]) for i in permutations]
    multiplication = [(-1)**sign[i]*reduce(lambda x,y: x*y,perm[i],1) for i in range(len(perm))]
    return multiplication

def add(list):
    return sum(list)

print("Программа підрахунку визначника матриці методом перестановки")
print("-"*60)
while 1:
    while 1:
        dimension = int(input("Введіть розмірність матриці: "))
        if dimension <= 0:
            print("Розмір матриці повинен бути натуральним числом")
            continue
        break

    matrix = random_matrix(dimension)

    det = add(multiplication(permutation(dimension)))

    print("Визначник матриці:", det)
    print("Визначник матриці (перевірочний):", round(np.linalg.det(matrix), 1))

    question = input("\nЯкщо бажаєте побачити дану матрицю напишіть 1, і будь-що інше щоб продовжити: ")
    if question == "1":
        print("")
        for i in matrix:
            print(i)

    answer = input("\nЩоб спробувати ще раз напишіть 1, і будь-що інше щоб вийти: ")
    if answer == "1":
        print("-"*60)
        continue
    else:
        print("\nРоботу завершено")
        print("-"*60)
        break