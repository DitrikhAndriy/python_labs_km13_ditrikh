print("RGB color codes to Hex Color Codes")
print("-"*34)

hex_color_code = "#{}{}{}"

def finish():
    answer = int(input("\n""Write 1 to try again, and anything else to quit: "))
    if answer == 1:
        print("")
        work()
    else:
        print("\n""Work completed!")
        print("-"*34)

def check(color):
    tf = True
    try:
        color = int(color)
        if color < 0 or color > 255:
            tf = False
    except:
        tf = False
    return color, tf

def convert(color):
    dict = {10:"A", 11:"B", 12:"C", 13:"D", 14:"E", 15:"F"}
    color_first = color//16
    if color_first in dict:
        color_first = dict[color_first]
    color_second = color%16
    if color_second in dict:
        color_second = dict[color_second]
    color = "{}{}".format(color_first, color_second)
    return color

def work():
    while 1:
        red, m = check(input("Enter the value of red color: "))
        if m == False:
            print("Enter an integer from 0 to 255 inclusive!")
            continue
        red = convert(red)
        break
    while 1:
        green, m = check(input("Enter the value of green color: "))
        if m == False:
            print("Enter an integer from 0 to 255 inclusive!")
            continue
        green = convert(green)
        break
    while 1:
        blue, m = check(input("Enter the value of blue color: "))
        if m == False:
            print("Enter an integer from 0 to 255 inclusive!")
            continue
        blue = convert(blue)
        break
    print("Your Hex Color Code:", hex_color_code.format(red, green, blue))
    finish()

work()