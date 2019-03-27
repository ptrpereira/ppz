arquivo = open('números.txt', 'r')
for linha in arquivo.readlines():
    print(linha.rstrip())
arquivo.close()


with open ('números.txt') as f:
    print(f.read())
