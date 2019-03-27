ano = int(input('Qual ano: '))
if ano % 4 == 0:
    if ano % 100 == 0:
        print('Não é bissexto')
    else:
        print('Bissexto')
elif ano % 400 == 0:
    print('Bissexto')
else:
    print('Não é bissexto')
