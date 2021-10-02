while 1:
    name = input("Enter your name: ")
    surname = input ("Enter your surname: ")
    phone_number = input("Enter your phone number: ")
    street = input("Enter the name of your street: ")
    street_number = input("Enter your street number: ")
    apartment_number = input("Enter your apartment number: ")
    city = input("Enter the name of your city: ")
    zip = input ("Enter your zip code: ")
    country = input("Enter the name of your country: ")

    all = "{0} {1}\n{2}\nStr. {3} {4}, ap. {5}, {6}\n{7}\n{8}".format(name, surname, phone_number, street, street_number, apartment_number, city, zip, country)
    print(all)

    answer = 0
    answer = int(input("Write 1 to try again, or anything else to quit: "))
    if answer == 1:
        continue
    else:
        print("Work completed")