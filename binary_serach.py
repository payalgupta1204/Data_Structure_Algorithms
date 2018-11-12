import numpy as np


def inputnumber(message):
    while True:
        try:
            userInput = int(input(message))

        except ValueError:
            print("Not an integer, enter int value")
            continue

        else:
            return userInput

n = inputnumber("enter number of elements in array:")
elem = inputnumber("enter element to search in array")
arr = []

for i in range(n):
    a = inputnumber("enter element of array")
    arr.append(a)

arr = np.sort(arr)
print("input array is {}".format(arr))
len_arr = len(arr)
left = 0
right = len_arr
while True:
    mid_idx = int((right - left)/2)
    if elem > arr[mid_idx]:
        left = mid_idx
    elif elem < arr[mid_idx]:
        right = mid_idx
    elif elem == arr[mid_idx]:
        print("index of the element is {}".format(mid_idx))
        break
    else:
        print("element not in array")
        break












