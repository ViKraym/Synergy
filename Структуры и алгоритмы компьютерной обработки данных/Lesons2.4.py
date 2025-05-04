import random

n = 5
arr = list()
for i in range(n):
    number = random.randint(1, 100)
    arr.append(number)

print("Not sorted:")
print(arr)
print("------")

def qick_sort(arr):
    if len(arr) <= 1:
        return arr
    
    index = random.randint(0, len(arr)-1)
    
    strong_elem = arr[index]
    low = list()
    mid = list()
    high = list()

    for elem in arr:
        if elem == strong_elem:
            mid.append(elem)
        elif elem < strong_elem:
            low.append(elem)
        else: 
            high.append(elem)

    low = qick_sort(low)
    high = qick_sort(high)
    result = low + mid + high
    return result

arr = qick_sort(arr)
print("Sorted:")
print(arr)
