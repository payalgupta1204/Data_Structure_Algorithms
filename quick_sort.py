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


def quick_sort(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)

        quick_sort(arr, low, pi - 1)
        quick_sort(arr, pi + 1, high)


n = inputnumber("enter number of elements in array:")
arr = []

for i in range(n):
    a = inputnumber("enter element of array")
    arr.append(a)

len_arr = len(arr)

quick_sort(arr, 0 , len_arr -1)
print("The sorted array is {}".format(arr))


