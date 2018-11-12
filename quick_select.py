import random


def inputnumber(message):
    while True:
        try:
            userInput = int(input(message))

        except ValueError:
            print("Not an integer, enter int value")
            continue

        else:
            return userInput


def partition(arr, low, high):
    wall = low - 1
    pivot = arr[high]

    for j in range(low, high):
        if arr[j] <= pivot:
            wall += 1
            arr[j], arr[wall] = arr[wall], arr[j]
    arr[wall + 1], arr[high] = arr[high], arr[wall + 1]
    return wall + 1


def quick_select(arr, low, high, k):
    if low < high:
        pivot_idx = random.randint(low, high)
        arr[high], arr[pivot_idx] = arr[pivot_idx], arr[high]

        pi = partition(arr, low, high)

        if k < pi:
            return quick_select(arr, low, pi - 1, k)
        elif k > pi:
            return quick_select(arr, pi + 1, high, k)
        else:
            return arr[pi]






n = inputnumber("enter number of elements in array:")
k = inputnumber("enter the element position required")
arr = []

for i in range(n):
    a = inputnumber("enter element of array")
    arr.append(a)

len_arr = len(arr)

result = quick_select(arr, 0 , len_arr -1,k)
print("The element at {}th position is {}".format(k, result))


