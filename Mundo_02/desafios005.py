import datetime

anoNasc = int(input('Digite seu ano de nascimento: '))
anoAtual = datetime.datetime.now().year
idade = anoAtual - anoNasc

if idade <= 9:
    print('Você tem {} anos. Categoria: MIRIM.'.format(idade))
elif idade <= 14:
    print('Você tem {} anos. Categoria: INFANTIL.'.format(idade))
elif idade <= 19:
    print('Você tem {} anos. Categoria: JÚNIOR.'.format(idade))
elif idade <= 20:
    print('Você tem {} anos. Categoria: SÊNIOR.'.format(idade))
else:
    print('Você tem {} anos. Categoria: MASTER.'.format(idade))