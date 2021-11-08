import numpy as np

def finish():
    answer = input("\nВведіть 1 якщо хочете спробувати ще раз, або що-небудь інше якщо ні: ")
    if answer == "1":
        work()
    else:
        print("-"*55)
        print("Роботу завершено")

def work():
    print("-"*55)
    years = np.arange(1900, 2020+1, 1)

    while 1:
        try:
            year = int(input("Введіть рік: "))
            if year<1900 or year>2020:
                raise TypeError
            break
        except ValueError:
            print("Ви ввели не число. Спробуйте ще раз.")
        except TypeError:
            print("Ви ввели не натуральне число в діапазоні — [1900, 2020]. Спробуйте ще раз.")

    while 1:
        try:
            month = int(input("Введіть місяць: "))
            if month<1 or month>12:
                raise TypeError
            break
        except ValueError:
            print("Ви ввели не число. Спробуйте ще раз.")
        except TypeError:
            print("Ви ввели не натуральне число в діапазоні — [1, 12]. Спробуйте ще раз.")

    days = [31,   31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

    def leap_year(years):
        return list(filter(lambda i: i%400 == 0 or i%100 != 0 and i%4 == 0, years))

    def day_in_month(month, year, function):
        if year in function(years):
            days.insert(1, 29)
        else:
            days.insert(1, 28)
        print("\nВ {} місяці {} року {} день(днів)".format(month, year, days[month-1]))

    day_in_month(month, year, leap_year)
    finish()
work()