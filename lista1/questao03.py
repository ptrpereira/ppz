dias = int(input('Dias: '))
horas = int(input('Horas: '))
minutos = int(input('Minutos: '))
segundos = int(input('Segundos: '))
total = segundos + minutos * 60 + horas * 60 * 60 + dias * 60 * 60 * 24
print('%d segundos' % total)
