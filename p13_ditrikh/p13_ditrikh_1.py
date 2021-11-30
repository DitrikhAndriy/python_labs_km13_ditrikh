file = open("gadsby.txt", "r")
alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]
lines = [line.lower() for line in file]

all_letter = 0
dict = {}
for i in alphabet:
    letter = 0
    for line in lines:
        letter += line.count(i)
    dict[i] = letter
    all_letter += letter

for i in alphabet:
    dict[i] = round(dict[i]/all_letter*100, 3)

dict = [(i, dict[i]) for i in sorted(dict, key=dict.get, reverse=True)]

print("Alphabet: ", end="")
for i in alphabet:
    print(f"{i}", end= "")
print()
for k, v in dict:
    if (k, v) in dict[5:(len(dict)-5)]:
        continue
    print(f"{k} – {v} %")

file.close()