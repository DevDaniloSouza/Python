n1 = input('Digite um número: ')
n2 = input('Digite outro número: ')
s = n1 + n2

print('A soma entre {} e {} é {}'.format(n1, n2, s))

""" O código acima tem um erro, pois o input retorna uma string e a soma de duas strings é a concatenação delas.
Para corrigir isso, precisamos converter as entradas para números inteiros usando a função int()."""

n1 = int(input('Digite um número: '))
n2 = int(input('Digite outro número: '))
s = n1 + n2

print('A soma entre {} e {} é {}'.format(n1, n2, s))