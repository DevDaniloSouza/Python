valores = []

while True:
    num = int(input('Digite um número: '))
    valores.append(num)
    resp = input('Quer continuar? [S/N] ')
    if resp in 'Nn':
        break

print(f'Foram digitados {len(valores)} números.')
print(f'Lista ordenada de forma decrescente: {sorted(valores, reverse=True)}')
print(f'O valor 5 está na lista.' if 5 in valores else 'O valor 5 não está na lista.')