meses = {
    '01': 'janeiro',
    '02': 'fevereiro',
    '03': 'março',
    '04': 'abril',
    '05': 'maio',
    '06': 'junho',
    '07':  'julho',
    '08': 'agosto',
    '09': 'setembro',
    '10': 'outrobro',
    '11': 'novembro',
    '12': 'dezembro'
}
data = input('Insira a data (dd/mm/aaaa): ')
sdata = data.split('/')
sdata[1] = meses[sdata[1]]
jdata = ' de '.join(sdata)
print(jdata)
