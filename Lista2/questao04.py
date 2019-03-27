n1 = int(input('Primeiro número: '))
n2 = int(input('Segundo número: '))
n3 = int(input('Terceiro número: '))
if n1 > n2 and n1 > n3:
  maior = n1
elif n2 > n1 and n2 > n3:
  maior = n2
elif n3 > n1 and n3 > n2:
  maior = n3
print('O maior é %d' %maior)