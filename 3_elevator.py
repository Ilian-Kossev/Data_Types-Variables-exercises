n = int(input())
p = int(input())
number_courses = n // p
remaining_people = n % p
if n <= p:
    number_courses = 1
elif n > p:
    remaining_people = n % p
    if remaining_people == 0:
        number_courses = n // p
    else:
        number_courses = n // p + 1
print(number_courses)