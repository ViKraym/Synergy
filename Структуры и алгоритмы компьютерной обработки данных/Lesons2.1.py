# Алгоритм шела

import random

n = 15
arr = list()
for i in range(n):
    number = random.randint(1, 100)
    arr.append(number)

print("Not sorted:")
print(arr)
print("------")


# step = len(arr) // 2
# while step > 0:
#     for i in range(step, n, 1):
#         val = arr[i]
#         cur = i 
#         check_index = cur - step
#         while (cur > 0) and (arr[check_index] > val):
#             arr[cur] = arr[check_index]
#             cur -= step
#             check_index -= step
#         arr[cur] = val
#     step = step // 2


step = len(arr) // 2
while step > 0:
    for i in range(step, n, 1):
        cur = i 
        check_index = cur - step
        while (cur > 0) and (arr[check_index] > arr[cur]):
            
            temp = arr[cur]
            arr[cur] = arr[check_index]
            arr[check_index] = temp

            cur -= step
            check_index -= step
    step = step // 2



print("Sorted:")
print(arr)
print("------")
