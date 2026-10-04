def two_sum(arr, target):
    num_sum = {}
    for i, num in enumerate(arr):
        need = target - num
        if need in num_sum:
            return (num_sum[need], i)
        num_sum[num] = i
    return "Not found"

n = int(input("Enter a number of elements: "))
arr = []
for i in range(n):
    num = int(input("Enter a number: "))
    arr.append(num)
key= int(input("Enter the target sum: "))
result = two_sum(arr, key)
if result != "Not found":
    print("Pair found  :", result)
else:
    print("Pair not found")