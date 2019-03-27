salarioHora = float(input('Salário por hora: '))
horasTrabalhadas = int(input('Horas trabalhadas: '))
salarioBruto = salarioHora * horasTrabalhadas
ir = 11 * salarioBruto / 100
inss = 8 * salarioBruto / 100
sindicato = 5 * salarioBruto / 100
salarioLiq = salarioBruto - ir - inss - sindicato
print('Salário Bruto: R$ %.2f' %salarioBruto)
print('Importo de Renda: R$ %.2f' %ir)
print('INSS: R$ %.2f' %inss)
print('Sindicato: R$ %.2f' %sindicato)
print('Salário Líquido: R$ %.2f' %salarioLiq)