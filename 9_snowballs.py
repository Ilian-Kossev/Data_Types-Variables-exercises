number_of_snowball = int(input())
max_value = 0
previous_value = 0
for number in range(number_of_snowball):
    snow = int(input())
    time = int(input())
    quality = int(input())
    value = (snow / time) ** quality
    if value > previous_value and value > max_value:
        max_value = value
    previous_value = value
   # print(f"{snow} : {time} = {value} ({quality})")
print(max_value)

