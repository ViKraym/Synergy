import random

# fresh sort

n = 10
arr = list()
for i in range(n):
    number = random.randint(1, 100)
    arr.append(number)

print("Not sorted:")
print(arr)
print("------")


for i in range(n):
    val = arr[i]
    j = i - 1
    while val > arr[j] and j >= 0:
        arr[j+1] = arr[j]
        j -= 1
    arr[j+1] = val

print("Sorted:")
print(arr)
print("------")