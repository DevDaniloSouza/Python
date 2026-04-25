sexo = str(input('Digite o seu sexo [M/F]: ')).strip().upper()
while sexo not in 'MF':
    print('Opção inválida. Digite novamente.')
    sexo = str(input('Digite o seu sexo [M/F]: ')).strip().upper()

if sexo == 'M':
    print('Sexo masculino registrado.')
elif sexo == 'F':
    print('Sexo feminino registrado.')