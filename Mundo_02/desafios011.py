soma = 0

for c in range (1, 501):
    if c % 2 == 1 and c % 3 == 0:
        soma += c
        print(c, end=' ')
        
print(f'\nA soma dos valores é: {soma}')