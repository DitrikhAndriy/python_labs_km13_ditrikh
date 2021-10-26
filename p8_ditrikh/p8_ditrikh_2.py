import math

print("Програма підрахунку коренів квадратного рівняння без попередніх перевірок\nКвадратне рівння алгебраїчного виду: ax²+bx+c=...")
print("-"*73)

def finish():
    answer = input("\n""Щоб спробувати ще раз напишіть 1. Щоб вийти напишіть будь-яке інше значення: ")
    if answer == "1":
        print()
        work()
    else:
        print("-"*73)
        print("Роботу завершено")

def work():
    while 1:
        try:
            a = float(input('Введіть число замість змінної "a": '))
            b = float(input('Введіть число замість змінної "b": '))
            c = float(input('Введіть число замість змінної "c": '))
        except ValueError:
            print("Помилка! Значення не є числом")
            continue
    
        try:
            D = b**2 - 4*a*c
            if D < 0:
                raise ValueError
            sqrt_D = math.sqrt(D)
        except ValueError:
            print("Помилка! Рівняння не має розв'язків (D<0)")
            continue


        try:
            x1 = (-b + sqrt_D)/(2*a)
            x2 = (-b - sqrt_D)/(2*a)
            if x1 == x2:
                print("\nx1 = x2 = {}".format(x1))
            else:
                print("\nx1 = {}\nx2 = {}".format(x1, x2))
        except ZeroDivisionError:
            if b != 0:
                x = -c/b
                print("\nx = {}".format(x))
            else:
                print("Помилка! Ділення на 0 (a=0)")
        finally:
            break
    finish()
work()