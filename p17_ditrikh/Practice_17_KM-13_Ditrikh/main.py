from exp_root.exponentiation import exp2, exp3
from exp_root.root import root2, root3
from factorial.factorial import fact
from logarithm.logarithm import log, ln, lg

def main():
    while 1:
        try:
            choice = int(input("1 – Логарифмічна (log, ln, lg)\n"
                               "2 – Факторіал\n"
                               "3 – Піднесення до степеня\n"
                               "4 – Корінь\n"
                               "Оберіть функцію якою бажаєте скористуватися: "))
            if choice not in range(1,5):
                print("Ви ввели число поза межами дозволених. Спробуйте ще раз")
                continue
            break
        except:
            print("Ви не ввели відповідне число. Спробуйте ще раз")
            continue
    print()
    if choice == 1:
        while 1:
            try:
                pick = int(input("1 – Логарифм (log)\n"
                                 "2 – Натуральний логарифм (ln)\n"
                                 "3 – Десятковий логарифм (lg)\n"
                                 "Уточніть яке саме рівняння вам потрібно: "))
                if pick not in range(1,4):
                    print("Ви ввели число поза межами дозволених. Спробуйте ще раз")
                    continue
                break
            except:
                print("Ви не ввели відповідне число. Спробуйте ще раз")
                continue
        if pick == 1:
            while 1:
                try:
                    a = float(input("Задайте основу логарифму: "))
                    if a < 0:
                        print("Основа не може бути меньше 0. Спробуйте ще раз")
                        continue
                    elif a == 1:
                        print("Основа не моде дорівнювати 1. Спробуйте ще раз")
                        continue
                    break
                except:
                    print("Ви ввели не число. Спробуйте ще раз")
                    continue
            while 1:
                try:
                    b = float(input("Введіть значення логарифму: "))
                    if b < 0:
                        print("Значення не може бути меньше 0. Спробуйте ще раз")
                        continue
                    break
                except:
                    print("Ви ввели не число. Спробуйте ще раз")
                    continue
            print(f"log({a}, {b}) = {log(a, b)}")
        else:
            while 1:
                try:
                    b = float(input("Введіть значення логарифму: "))
                    if b < 0:
                        print("Значення не може бути меньше 0. Спробуйте ще раз")
                        continue
                    break
                except:
                    print("Ви ввели не число. Спробуйте ще раз")
                    continue
            if pick == 2:
                print(f"ln({b}) = {ln(b)}")
            else:
                print(f"lg({b}) = {lg(b)}")

    elif choice == 2:
        while 1:
            try:
                n = int(input("Введіть число, факторіал якого буде знайдено: "))
                if n <= 0:
                    print("Ви ввели не натуральне число. Спробуйте ще раз")
                    continue
                break
            except:
                print("Ви ввели не число. Спробуйте ще раз")
                continue
        print(f"{n}! = {fact(n)}")

    elif choice == 3:
        while 1:
            try:
                pick = int(input("1 – До квадрату\n"
                                 "2 – До кубу\n"
                                 "Уточніть до якого степеня потрібно піднести число: "))
                if pick not in range(1, 3):
                    print("Ви ввели число поза межами дозволених. Спробуйте ще раз")
                    continue
                break
            except:
                print("Ви не ввели відповідне число. Спробуйте ще раз")
                continue
        while 1:
            try:
                n = float(input("Введіть число, яке хочете піднести до степеня: "))
                break
            except:
                print("Ви ввели не число. Спробуйте ще раз")
                continue
        if pick == 1:
            print(f"n**2 = {exp2(n)}")
        else:
            print(f"n**3 = {exp3(n)}")

    else:
        while 1:
            try:
                pick = int(input("1 – Квадратичним (2)\n"
                                 "2 – Кубічним (3)\n"
                                 "Уточніть яким саме корнем ви хочете скористуватись: "))
                if pick not in range(1, 3):
                    print("Ви ввели число поза межами дозволених. Спробуйте ще раз")
                    continue
                break
            except:
                print("Ви не ввели відповідне число. Спробуйте ще раз")
                continue
        while 1:
            try:
                n = float(input("Введіть число, корінь якого буде знайдено: "))
                if pick == 1 and n < 0:
                    print("Значення не може бути від'ємним. Спробуйте ще раз")
                    continue
                break
            except:
                print("Ви ввели не число. Спробуйте ще раз")
                continue
        if pick == 1:
            print(f"n^2 = {root2(n)}")
        else:
            print(f"n^3 = {root3(n)}")

if __name__ == '__main__':
    main()