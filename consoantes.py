i = 1
soma = 0
arr = []
while i <= 10:
  ltr = input('%d Letra: ' %i)
  arr.append(ltr)
  if ltr != 'a' and ltr != 'e' and ltr != 'i' and ltr != 'o' and ltr != 'u':
    soma += 1 
  i += 1
print('Consoantes digitadas: %d' %soma)
