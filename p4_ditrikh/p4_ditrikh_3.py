while 1:
    duration = int(input("Enter the duration of your conversations with other mobile carriers (in minutes): "))
    if duration<=0:
        print("Oh, how did you do it?")
    elif duration>0 and duration<=50:
        print("You need to pay 100 hryvnias")
    elif duration>50 and duration<=100:
        print("You need to pay 150 hryvnias")
    else:
        value = 150 + (duration-100)*2
        print("You need to pay", value, "hryvnias")
    
    answer = 0
    answer = int(input("Write 1 to try again, or anything else to quit: "))
    if answer == 1:
        continue
    else:
        print("Work completed")
        break
