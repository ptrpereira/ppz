user = input('Usuário: ')
password = input('Senha: ')
while user == password:
    print('Erro. Senha precisa ser diferente de usuário.')
    user = input('Usuário: ')
    password = input('Senha: ')
print('Sucesso!')
