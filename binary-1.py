def binary_search(arr, new):
    low = 0
    high = len(arr) - 1
    while low <=high:
        mid = (low + high) // 2
        if arr[mid] == new:
            return mid
        elif arr[mid] < new:
            low = mid + 1
        else:
            high = mid - 1
    return -1
n = int(input("Enter a number of elements: "))
arr = []
for i in range(n):
    num = int(input("Enter a number: "))
    arr.append(num)
new = int(input("Enter the element to search: "))
result = binary_search(arr, new)
if result != -1:
    print("Element found at index: ", result)
else:
    print("Element not found")