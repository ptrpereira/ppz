word = input('Digite a palavra: ')
inverse = word[::-1]
if word == inverse:
  print ('É palíndrome! Parabéns!')
else:
  print('Uai! Não é palíndrome.')