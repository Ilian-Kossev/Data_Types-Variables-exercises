n = int(input())
sum_numbers = 0
for number in range(n):
    letter = input()
    letter_to_number = ord(letter)
    sum_numbers += letter_to_number
print(f'The sum equals: {sum_numbers}')