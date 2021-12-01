files = []
for i in range(1880, 2020):
    files.append(f"yob{str(i)}.txt")

dict_M = {}
dict_F = {}
for i in files:
    file = open(i, "r")
    lines = file.readlines()
    for line in lines:
        name_M = ""
        name_F = ""
        line = line.split(",")
        if line[1] == "M":
            name_M = name_M + line[0]
        else:
            name_F = name_F + line[0]

        if name_M not in dict_M.keys():
            dict_M[name_M] = 0
        dict_M[name_M] += 1

        if name_F not in dict_F.keys():
            dict_F[name_F] = 0
        dict_F[name_F] += 1
    file.close()

dict_M = sorted(dict_M.items(), key = lambda x: -x[1])
dict_F = sorted(dict_F.items(), key = lambda x: -x[1])

print("Найпопулярніші чоловічі імена: ")
for i in dict_M:
    print(i[0], i[1])
    
print("Найпопулярніші жіночі імена: ")
for i in dict_F:
    print(i[0], i[1])