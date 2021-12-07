import csv

with open("Bring Me the Horizon.csv", "w", newline="") as file:
    fieldnames = ["Song", "Year"]
    writer = csv.DictWriter(file, fieldnames=fieldnames)
    writer.writeheader()
    writer.writerow({"Song": "Throne",
                     "Year": 2015})
    writer.writerow({"Song": "Kingslayer",
                     "Year": 2020})
    writer.writerow({"Song": "Shadow Moses",
                     "Year": 2013})
    writer.writerow({"Song": "Parasite Eve",
                     "Year": 2020})
    writer.writerow({"Song": "Can you Feel My Heart",
                     "Year": 2013})

with open("Bring Me the Horizon.csv", newline="") as file:
    reader = csv.DictReader(file)
    for heading in reader.fieldnames:
        print(heading, end=" ")
    print("\n")
    for row in reader:
        print(row["Song"], row["Year"])