valores = []

for c in range(0, 5):    
    num = int(input('Digite um número: '))
    for i, v in enumerate(valores):
        if num <= v:
            valores.insert(i, num)
            print(f'Adicionado na posição {i} da lista...')
            break
    else:
        valores.append(num)
        print('Adicionado ao final da lista...')

print(f'Os valores digitados em ordem crescente são: {valores}')