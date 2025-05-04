# бинарный поиск

import random

n = 40
arr = list()
for i in range(n):
    number = random.randint(1, 100)
    arr.append(number)

to_sourch = random.randint(1, 100)
answer = -1
########################################################################################################
arr.sort()

first = 0
last = n - 1 

while first <= last and answer == -1:
    mid_index = (first + last) // 2
    
    if arr[mid_index] == to_sourch:
        answer = mid_index
    else:
        if arr[mid_index] > to_sourch:
            last = mid_index - 1
        else:
            first = mid_index + 1

########################################################################################################


print(to_sourch)
print(arr)

if answer != -1:
    print(f"Элемент в списке есть, его индекс: {answer}")
else:
    print("такого элемента нет в списке")