A = float(input('Lado A: '))
B = float(input('Lado B: '))
C = float(input('Lado C: '))
if A + B > C and A + C > B and B + C > A:
    if A == B and A == C and B == C:
        print('Trinângulo Equilátero!')
    elif A != B and A != C and B != C:
        print('Triângulo Escaleno!')
    else:
        print('Triângulo Isósceles')
else:
    print('Não é triângulo!')
    