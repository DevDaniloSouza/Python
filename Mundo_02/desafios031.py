print('-' * 30)
print('Carrinho de Compras')
print('-' * 30)

prod_caros = prod_barato = total_gasto = 0

while True:
    produto = input('Nome do produto: ')
    preco = float(input('Preço: R$ '))
    total_gasto += preco

    if prod_barato is 0 or preco < prod_barato:
        prod_barato = produto

    if preco > 1000:
        prod_caros += 1

    continuar = input('Deseja adicionar outro produto? [S/N] ').strip().upper()
    if continuar == 'N':
        break

print('-' * 30)
print(f'Total gasto: R$ {total_gasto:.2f}')
print(f'Produtos que custam mais de R$ 1000: {prod_caros}')
print(f'Nome do produto mais barato: {prod_barato}')