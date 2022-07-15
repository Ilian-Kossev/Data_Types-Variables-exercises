party_size = int(input())
days = int(input())
sum_earned = 0
sum_spent = 0
for day in range(1, days + 1):
    sum_earned += 50
    if day % 10 == 0:
        party_size -= 2
    if day % 15 == 0:
        party_size += 5
    sum_spent += 2 * party_size
    if day % 3 == 0:
        sum_spent += 3 * party_size
    if day % 5 == 0:
        sum_earned += 20 * party_size
        if day % 3 == 0:
            sum_spent += 2 * party_size
money_per_person = (sum_earned - sum_spent) / party_size
print(f"{party_size} companions received {int(money_per_person)} coins each.")



