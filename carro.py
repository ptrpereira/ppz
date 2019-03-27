v = int(input('Velocidade do carro: '))
if v > 110:
  multa = (v - 110) * 5
  print('Multa: %d' %multa)