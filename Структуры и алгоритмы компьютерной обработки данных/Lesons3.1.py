# Линейный поиск

import random

n = 40
arr = list()
for i in range(n):
    number = random.randint(1, 100)
    arr.append(number)

to_sourch = random.randint(1, 100)
answer = -1
########################################################################################################

for i in range(n):
    if arr[i] == to_sourch:
        answer = i
        break


########################################################################################################


print(to_sourch)
print(arr)

if answer != -1:
    print(f"Элемент в списке есть, его индекс: {answer}")
else:
    print("такого элемента нет в списке")