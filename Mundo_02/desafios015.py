from datetime import date

adultos = 0
menores = 0

for c in range(1, 9):
    ano = int(input('Digite o ano de nascimento da {}ª pessoa: '.format(c)))
    ano_atual = date.today().year
    idade = ano_atual - ano
    if idade >= 18:
        adultos += 1
    else:
        menores += 1

print(f'Quantidade de pessoas maiores de idade: {adultos}')
print(f'Quantidade de pessoas menores de idade: {menores}')