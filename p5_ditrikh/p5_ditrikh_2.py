while 1:
    print("Enter a name for the item, or write \"Stop\" if you want to finish:")
    list1 = list()
    while 1:
        element = input()
        if element.lower() == "stop":
            break
        list1.append(element)

    length = len(list1)
    i = 0
    while i < length:
        if i+2 < length:
            print(list1[i], end=', ')
        elif i+1 < length:
            print(list1[i], end=' ')
        else:
            print("and", list1[i])
        i+=1

    answer = int(input("Write 1 to try again, and anything else to quit: "))
    if answer == 1:
        continue
    else:
        print("Work completed")
