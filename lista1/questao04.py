salario = float(input('Valor do salário: R$ '))
porcentagem = float(input('Porcentagem do aumento: '))
aumento = salario * porcentagem / 100
novoSalario = salario + aumento
print('Aumento: R$ %.2f' % aumento)
print('Novo salário: R$ %.2f' % novoSalario)
