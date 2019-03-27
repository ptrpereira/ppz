import random
lista = []
while len(lista) < 15:
    n = random.randint(10, 100)
    if n not in lista:
      lista.append(n)
lista.sort()
print(lista)