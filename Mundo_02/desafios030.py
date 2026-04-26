homens = adultos = mulheres20 = 0

while True:
    print('-' * 30)
    print('Cadastre um Pessoa')
    print('-' * 30)

    idade = int(input('Idade: '))
    sexo = input('Sexo [M/F]: ').strip().upper()

    if sexo == 'M':
        homens += 1
    elif sexo == 'F':
        if idade < 20:
            mulheres20 += 1

    if idade >= 18:
        adultos += 1

    continuar = input('Deseja continuar? [S/N] ').strip().upper()
    if continuar == 'N':
        break

print('-' * 30)
print(f'Total de mulheres com menos de 20 anos: {mulheres20}')
print(f'Total de homens: {homens}')
print(f'Total de adultos: {adultos}')
