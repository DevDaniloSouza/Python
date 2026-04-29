lista = [[], []]
num = 0

for c in range(0, 7):
    num = (int(input(f'Digite o {c + 1}º valor: ')))

    if num % 2 == 0:
        lista[0].append(num)
    else:
        lista[1].append(num)

lista[0].sort()
lista[1].sort()

print(f'Os valores pares digitados foram: {lista[0]}')
print(f'Os valores ímpares digitados foram: {lista[1]}')