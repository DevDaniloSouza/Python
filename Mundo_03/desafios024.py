larg = float(input('Largura: '))
comp = float(input('Comprimento: '))

def area(l, c):
    a = l * c
    print(f'A área de um terreno {l} x {c} é de {a}m².')

area(larg, comp)