num = int(input('Digite o número: '))
a, b = 1, 1
count = 1
while count <= num-2:
    a, b = b, a + b
    count += 1
print('O número Fibonacci de %d é %d.' % (num, b))
