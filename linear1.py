def linear_search(arr, key):
    for i in range(len(arr)):
        if arr[i] == key:
            return i
    return -1

arr = []
n = int(input("Enter a number of elements: "))
for i in range(n):
    num = int(input("Enter a number: "))
    arr.append(num)

key = int(input("Enter a number to search: "))
Found= False
result = linear_search(arr, key)
if result != -1:
    print("Element found at index:", result)
else:
    print("Element not found")