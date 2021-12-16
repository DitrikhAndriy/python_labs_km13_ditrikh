from math import factorial as fac

def binomial(n):
    C = lambda n, k: round(fac(n) / (fac(k) * fac(n-k)))
    for i in range(n+1):
        answer = [str(C(i, j)) for j in range(i + 1)]
        yield answer

while 1:
    try:
        n = int(input("Введіть степінь многочлена: "))
        if n<0:
            print("Ви ввели не невід'ємне ціле число. Спробуйте ще раз")
            continue
        break
    except:
        print("Ви ввели не число. Спробуйте ще раз")
        continue
    
for i in binomial(n):
    print(*i, sep=" ")