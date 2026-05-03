def contador(i, f, p):
    print(f'Contagem de {i} até {f} de {p} em {p}')
    for c in range(i, f + 1, p):
        print(c, end=' ')
    print('FIM!')

contador(1, 10, 1)
contador(10, 0, 2)
contador(int(input('Início: ')), int(input('Fim: ')), int(input('Passo: ')))