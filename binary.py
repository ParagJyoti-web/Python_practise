def binary_search(arr, new):
    low = 0
    high = len(arr) - 1
    while low <= high:
        mid = (low + high) // 2
        if arr[mid] == new:
            return mid
        elif arr[mid] < new:
            low = mid + 1
        else:
            high = mid - 1
    return -1
arr= [89,45,67,23,9,12,78,34]
key = 12

arr.sort()
new = int(input("Enter the number to search for: "))
result = binary_search(arr, new)
if result != -1:
    print("Element found at index: ", result)
else:
    print("Element not found")