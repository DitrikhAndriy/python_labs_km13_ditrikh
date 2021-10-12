while 1:
    word1 = input("Enter the first phrase: ")
    set1 = set(list(word1.replace(",", "").replace(" ", "").replace(".", "").replace("!", "").replace("?", "").lower()))
    word2 = input("Enter the second phrase: ")
    set2 = set(list(word2.replace(",", "").replace(" ", "").replace(".", "").replace("!", "").replace("?", "").lower()))
    if set1 & set2 == set2:
        print("From the letters of the first phrase, you can make a second phrase")
        print()
    else:
        print("From the letters of the first phrase, you can't make a second phrase")
        print()
    print("First phrase:", word1)
    print("Second phrase:", word2)
    
    answer = int(input("Write 1 to try again, and anything else to quit: "))
    if answer == 1:
        continue
    else:
        print("Work completed")
        break