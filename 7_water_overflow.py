n = int(input())
total_volume = 0

for number in range(n):
    litres = int(input())
    total_volume += litres
    if total_volume > 255:
        total_volume -= litres
        print("Insufficient capacity!")
        continue
print(total_volume)

