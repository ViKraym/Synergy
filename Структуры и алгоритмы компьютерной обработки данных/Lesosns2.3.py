import random

n = 50
arr = list()
for i in range(n):
    number = random.randint(1, 100)
    arr.append(number)

print("Not sorted:")
print(arr)
print("------")


def merge(arrl, arrr):
    sorted_arr = list()
    cur_left = 0
    cur_right = 0

    lenl = len(arrl)
    lenr = len(arrr)
    for i in range(lenl + lenr):
        if cur_left < lenl and cur_right < lenr:
            if arrl[cur_left] > arrr[cur_right]:
                sorted_arr.append(arrl[cur_left])
                cur_left += 1
            else:
                sorted_arr.append(arrr[cur_right])
                cur_right += 1
        else:
            if cur_left == lenl:
                for j in range(cur_right, lenr):
                    sorted_arr.append(arrr[j])
            else:
                for j in range(cur_left, lenl):
                    sorted_arr.append(arrl[j])
            break
    return sorted_arr

def merge_sort(arr):
    if len(arr) <= 1:
        return arr

    mid = len(arr)//2
    left_side = list()
    right_side = list()

        
    for i in range(0, mid):
        val = arr[i]
        left_side.append(val)

    for i in range(mid, len(arr)):
        val = arr[i]
        right_side.append(val)

    left_side = merge_sort(left_side)
    right_side = merge_sort(right_side)

    result = merge(left_side, right_side)
    return result

arr = merge_sort(arr)
print("Sorted:")
print(arr)

