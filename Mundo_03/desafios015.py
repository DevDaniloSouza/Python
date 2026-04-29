matriz = [[], [], []]
somaPares = 0
somaCol = 0

for l in range(0, 3):
    for c in range(0, 3):
        matriz[l].append(int(input(f'Digite um valor para [{l}, {c}]: ')))
        if matriz[l][c] % 2 == 0:
            somaPares += matriz[l][c]

for c in range(0, 3):
    somaCol += matriz[c][2]

print('-=' * 20)

for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz[l][c]:^5}]', end='')
    print()

print('-=' * 20)

print(f'O maior valor da segunda linha é {max(matriz[1])}')
print(f'A soma dos valores pares é {somaPares}')
print(f'A soma dos valores da terceira coluna é {somaCol}')