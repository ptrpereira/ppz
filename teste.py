import random


def generate():
    num = random.randint(0, 10)
    return num


def test(usernum, num):
    print('Número sorteado: %d' % num)
    if usernum == num:
        print('Acertou!')
    else:
        print('Tente outra vez!')      


def main():
    usernum = int(input('Digite um número de 0 a 10: '))
    while usernum < 0 or usernum > 10:
        print('Apenas números entre 0 e 10. Tente outra vez!')
        usernum = int(input('Digite um número de 0 a 10: '))
    num = generate()
    test(usernum, num)


exit = ''
while exit != 'no':
    main()
    exit = input('Jogar novamente? yes/no: ')
