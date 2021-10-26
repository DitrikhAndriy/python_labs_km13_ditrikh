import re

pose_estimation = input("Введіть рядок: ")
points = list()
scores = list()

pattern = re.compile(r"0.[0-9][0-9], 0.[0-9][0-9]|0.[0-9][0-9]")
list = re.findall(pattern, pose_estimation)

for i in list:
    if len(i) > 4:
        j = [float(j) for j in i.split(", ")]
        [points.append(k) for k in j]
    else:
        scores.append(float(i))

print("\npoints =", points)
print("scores =", scores)