def resumo(num, taxa_aum, taxa_dim):
    print('-' * 40)
    print('RESUMO DO VALOR'.center(40))
    print('-' * 40)
    print(f'Preço analisado: \t{moeda(num)}')
    print(f'Dobro do preço: \t{moeda(dobro(num))}')
    print(f'Metade do preço: \t{moeda(metade(num))}')
    print(f'{taxa_aum}% de aumento: \t{moeda(aumentar(num, taxa_aum))}')
    print(f'{taxa_dim}% de redução: \t{moeda(diminuir(num, taxa_dim))}')

def dobro(num):
    return num * 2

def metade(num):
    return num / 2

def aumentar(num, taxa):
    return num + (num * taxa / 100)

def diminuir(num, taxa):
    return num - (num * taxa / 100)

def moeda(num): 
    return f'R$ {num:.2f}'