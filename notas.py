notas = []
i = 1
j = 0
soma = 0
while i <= 4:
  n = float(input('Digite a nota %d: ' %i))
  notas.append(n)
  i += 1
while j < 4:
  print('Nota %d: %1.1f' %((j+1), notas[j]))
  soma += notas[j]
  j += 1
print('Média: %1.1f' %(soma / i))
