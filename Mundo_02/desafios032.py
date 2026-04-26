print('-' * 30)
print('- Caixa Eletrônico 24h -')
print('-' * 30)

valor = int(input('Digite o valor a ser sacado: R$ '))
total = valor
restDiv = 0
totalNotas = 0

while True:
    if valor >= 50:
        restDiv = total % 50
        totalNotas = total // 50
        print(f'Total de {totalNotas} cédulas de R$ 50')
        total = restDiv
    if valor >= 20:
        restDiv = total % 20
        totalNotas = total // 20
        print(f'Total de {totalNotas} cédulas de R$ 20')
        total = restDiv
    if valor >= 10:
        restDiv = total % 10
        totalNotas = total // 10
        print(f'Total de {totalNotas} cédulas de R$ 10')
        total = restDiv
    if valor >= 1:
        restDiv = total % 1
        totalNotas = total // 1
        print(f'Total de {totalNotas} cédulas de R$ 1')
        total = restDiv
    break

print('-' * 30)
print('Volte sempre ao Caixa Eletrônico 24h. Tenha um bom dia!')