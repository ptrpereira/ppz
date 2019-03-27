preco = float(input('Preço mercadoria: '))
porcentagem = float(input('Desconto: '))
desconto = porcentagem * preco / 100
pagar = preco - desconto
print('Desconto: R$ %.2f' % desconto)
print('Pagar: R$ %.2f' % pagar)
