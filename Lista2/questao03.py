excesso = 0
multa = 0
peso = float(input('Peso: '))
if peso > 50:
    excesso = peso - 50
    multa = excesso * 4
print('Excesso: %.1f' % excesso)
print('Multa: R$ %.2f' % multa)
