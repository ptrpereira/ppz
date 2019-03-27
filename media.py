i = 0
notas = [10, 3, 8, 7, 9]
soma = 0
while i <= 4:
  soma = soma + notas[i]
  i = i + 1
media = soma / len(notas)
print('Média: %.1f' %media)  