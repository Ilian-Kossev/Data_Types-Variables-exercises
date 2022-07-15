number = int(input())
for number1 in range(97, 97 + number):
    for number2 in range(97, 97 + number):
        for number3 in range(97, 97 + number):
            letter1 = chr(number1)
            letter2 = chr(number2)
            letter3 = chr(number3)
            print(f"{letter1}{letter2}{letter3}")


