num = int(input('Digite um número e veja seu Fatorial: '))
res = num
mult = num -1

while mult != 0:
    print(f'{num}! =', end=' ')
    print(f'{num}', end=' ')
    print(f'x {mult}')
    res *= mult
    mult -= 1
print(f'{res}')