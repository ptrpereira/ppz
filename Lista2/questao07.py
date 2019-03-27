tamanho = float(input('Qual tamanho em metros quadrados: '))
if tamanho % 54 == 0:
  latas = tamahho / 54
else:
  latas = int(tamanho / 54) + 1
preco = latas * 80.00
print('Latas: %.1f' %latas)
print('Preço: %.2f' %preco)

