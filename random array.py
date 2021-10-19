import random

array = []
choosen_number = []

n = random.randint(2, 10)

for i in range(n):
    new_number = random.randint(0, 300)
    if new_number not in choosen_number:
        array.append(new_number)
        choosen_number.append(new_number)

print("ARRAY: ", array)