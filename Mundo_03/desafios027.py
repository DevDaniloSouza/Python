lista = []

def maior(*num):
    print('Analisando os valores passados...')
    lista.append(num)

    print(f'Foram informados {len(num)} valores ao todo.')
    print(f'O maior valor informado foi {max(num)}.')

maior(2, 9, 4, 5, 7, 1)
