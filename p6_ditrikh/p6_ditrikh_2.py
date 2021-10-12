button = {
    1: (".",",","?","!",":"),
    2: ("A","B","C"),
    3: ("D","E","F"),
    4: ("G","H","I"),
    5: ("J","K","L"),
    6: ("M","N","O"),
    7: ("P","Q","R","S"),
    8: ("T","U","V"),
    9: ("W","X","Y","Z"),
    0: (" ")
}
def get(value):
    for k, val in button.items():
        for j in val:
            if j == value:
                return k, val.index(j)
    return None, None

def finish():
    answer = int(input("Write 1 to try again, and anything else to quit: "))
    if answer == 1:
        work()
    else:
        print("Work completed")
def work():
    numbers = list()
    string = list(str(input("Enter the string: ")).upper())
    for i in range(len(string)):
        key, time = get(string[i])
        if key is not None:
            numbers.append(str(key)*(time+1))

    print("Your string in the form of telephone buttons: ", end="")
    if len(numbers) == 0:
        print("Empty")
    else:
        for i in numbers:
            print(i, end="")
    print()
    finish()
work()