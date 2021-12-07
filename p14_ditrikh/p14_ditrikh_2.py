import json

print("Відкриття файлу \"/image_info_test-dev2017.json\"...\n")
with open("image_info_test-dev2017.json") as file:
    dictionary = json.load(file)
    print("Кількість фотографій:", len(dictionary["images"]))
    print("Кількість категорій:", len(dictionary["categories"]))

    print("\nІнформація фотографії \"000000000001.jpg\":")
    for image in dictionary["images"]:
        if image["file_name"] == "000000000001.jpg":
            print("Посилання –", image["coco_url"])
            print("Висота –", image["height"])
            print("Довжина –", image["width"])
            print("Ідентифікатор –", image["id"])
    
    max_id = max([image["id"] for image in dictionary["images"]])
    for image in dictionary["images"]:
        if image["id"] == max_id:
            print("\nНазва фотографії з найбільшим номером –", image["file_name"])