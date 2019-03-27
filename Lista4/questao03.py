import random
arr = []
arrA = []
arrB = []
for i in range(10):
    arrA.append(random.randint(1, 100))
for i in range(10):
    arrB.append(random.randint(1, 100))
for i in range(10):
    arr.append(arrA[i])
    arr.append(arrB[i])
print('Array A: ', arrA)
print('Array B: ', arrB)
print('Array A + B: ', arr)
