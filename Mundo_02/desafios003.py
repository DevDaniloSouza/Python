idade = int(input('Informe sua idade: '))

if idade < 18:
    print('Você ainda não precisa se alistar. Faltam {} anos para o alistamento.'.format(18 - idade))
elif idade == 18:
    print('Está na hora de se alistar no exército!')
else:
    print('Você já deveria ter se alistado há {} anos.'.format(idade - 18))