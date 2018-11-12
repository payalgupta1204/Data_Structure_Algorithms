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
arr = []

for i in range(n):
    a = inputnumber("enter element of array")
    arr.append(a)

len_arr = len(arr)

while True:
    flag = 0
    for i in range(len_arr):
        if i == len_arr - 1:
            break
        else:
            if arr[i] > arr[i + 1]:
                temp = arr[i]
                arr[i] = arr[i + 1]
                arr[i + 1] = temp
                flag = 1

    if flag == 0:
        break
print("The sorted array is {}".format(arr))







