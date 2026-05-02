import datetime

pessoa = {}
dataHoje = datetime.date.today().year
dataNasc = 0

pessoa['nome'] = str(input('Nome: '))
dataNasc = int(input('Data de nascimento: '))
pessoa['idade'] = dataHoje - dataNasc
pessoa['ctps'] = int(input('Carteira de trabalho (0 não tem): '))

if pessoa['ctps'] != 0:
    pessoa['contratação'] = int(input('Ano de contratação: '))
    pessoa['salário'] = float(input('Salário: R$ '))
    pessoa['aposentadoria'] = pessoa['idade'] + ((pessoa['contratação'] + 35) - dataHoje)

print('-=' * 30)
for k, v in pessoa.items():
    print(f' - {k.capitalize()}: {v}')
print('-=' * 30)
