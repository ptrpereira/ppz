import random
arr = []
arrEven = []  # par
arrOdd = []  # impar
for i in range(20):
    arr.append(random.randint(1, 100))
for i in range(20):
    if arr[i] % 2 == 0:
        arrEven.append(arr[i])
    else:
        arrOdd.append(arr[i])
print('List: ', arr)
print('Even list: ', arrEven)
print('Odd list: ', arrOdd)
