'''
Sorteie 10 inteiros entre 1 e 100 para uma listae descubrao maior e o menor valor, sem usar as funções max e min
'''

import random
lista = []
maior, menor = 0, 0
for i in range(10):
    lista.append(random.randint(1, 100))
lista.sort()
print('Lista:', lista)
print('Menor: %d' % lista[0])
print('Maior: %d' % lista[9])    