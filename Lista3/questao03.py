A = 80000
B = 200000
anos = 0
while A <= B:
    A = A + A * 3 / 100
    B = B + B * 1.5 / 100
    anos += 1
print('%d anos' % anos)
