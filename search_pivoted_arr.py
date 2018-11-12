def inputnumber(message):
    while True:
        try:
            userInput = int(input(message))

        except ValueError:
            print("Not an integer, enter int value")
            continue

        else:
            return userInput

def search(arr, left, right, key):
    mid = (left + right)//2

    if left > right:
        return -1

    if key == arr[mid]:
        return mid
    if arr[left] <= arr[mid] :
        if key >= arr[left] and key <= arr[mid]:
            return search(arr, left, mid - 1, key)
        return search(arr, mid + 1, right, key)

    if key >= arr[mid] and key <= arr[right]:
        return search(arr, mid + 1, right, key)
    return search(arr, left, mid -1, key)


n = inputnumber("enter number of elements in array:")
elem = inputnumber("enter element to search in array")
arr = []

for i in range(n):
    a = inputnumber("enter element of array")
    arr.append(a)

print("input array is {}".format(arr))
len_arr = len(arr)

key_idx = search(arr, 0, len_arr -1, elem)
print("elem is present at {}".format(key_idx))

