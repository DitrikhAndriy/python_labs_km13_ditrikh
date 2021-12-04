dict_M = {}
dict_F = {}

files = []
for i in range(1880, 2020):
    files.append(f"yob{str(i)}.txt")

for i in files:
    file = open(i, "r")
    name_M = []
    name_F = []
    max_M = 0
    max_F = 0
    for words1 in file:
        words1 = words1.split(",")
        if words1[1] == "M":
            max_M = max(max_M, int(words1[2]))
            name_M.append(words1[0])

        if words1[1] == "F":
            max_F = max(max_F, int(words1[2]))
            name_F.append(words1[0])
    file.close()

    file = open(i, "r")
    for words2 in file: 
        words2 = words2.split(",")
        if words2[1] == "M" and int(words2[2]) == max_M:
            dict_M[words2[0]] = dict_M.get(words2[0], 0) + 1

        if words2[1] == "F" and int(words2[2]) == max_F:
            dict_F[words2[0]] = dict_F.get(words2[0], 0) + 1
    file.close()

dict_M = sorted(dict_M.items(), key=lambda h: h[1], reverse=True)
dict_F = sorted(dict_F.items(), key=lambda h: h[1], reverse=True)

print("Найпопулярніші чоловічі імена: ")
for i in dict_M:
    print(f"{i[0]} – {i[1]}")
    
print("Найпопулярніші жіночі імена: ")
for i in dict_F:
    print(f"{i[0]} – {i[1]}")