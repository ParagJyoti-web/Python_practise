n = int(input("Enter a number of elements: "))
arr = []
for i in range(n):
    num = int(input("Enter a number :"))
    arr.append(num)

print("The array is:", arr)

key = int(input("Enter a number to search: "))
for i in range(len(arr)):
    if arr[i] == key:
        print("Element found at index:", i)
        break
else:
    print("Element not found")