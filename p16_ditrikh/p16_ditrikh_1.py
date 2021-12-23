from functools import reduce

while 1:
    try:
        pages = int(input("Введіть число сторінок: "))
        if pages<16 or pages>1280:
            print("Ви ввели число менше 16, або більше 1280. Спробуйте ще раз")
            continue
        elif pages%16 != 0:
            print("Ви ввели число не кратне 16. Спробуйте ще раз")
            continue
        print()
        break
    except:
        print("Ви ввели не число. Спробуйте ще раз")
        continue

def work(active=False):    
    def wrap(func):
        def wrapper(arg):
            result = [*func(arg)]
            if active == False:
                print("Список без додаткової функції:")
                print(result)
                print(f"Кількість зошитів в книжці – {len(result)}")
            elif active == True:
                new_result = []
                for i in result:
                    skip = []
                    for k in range(4, len(i)+1, 4):
                        skip.append((i[k-4], i[k-3], i[k-2], i[k-1]))
                    new_result.append(skip)
                print("Список з додатковою функцією:")
                print(new_result)
                print(f"Кількість зошитів в книжці – {len(result)}")
        return wrapper
    return wrap

@work(active=False)
def book_list(pages):
    book = []
    for page in range(16, pages+1, 16):
        copybook = []
        for i in range(4):
            copybook += (page - 2*i, page + 2*i - 15, page + 2*i - 14, page - 2*i - 1)
        book.append(copybook)
    return book

@work(active=True)
def book_list_yield(pages):
    for page in range(16, pages+1, 16):
        yield reduce(lambda res, lst: res + lst, [[page-i, (i+1)+(page-16), (i+2)+(page-16), page-i-1] for i in range(0, 8, 2)])

book_list(pages)
print("-"*50)
book_list_yield(pages)