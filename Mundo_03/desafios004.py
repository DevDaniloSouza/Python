num1 = int(input('Digite um número: '))
num2 = int(input('Digite um número: '))
num3 = int(input('Digite um número: '))
num4 = int(input('Digite um número: '))

tupla = (num1, num2, num3, num4)
pares = []
nines = 0

for c in tupla:
    if c % 2 == 0:
        pares.append(c)

print(f'O número 9 apareceu {tupla.count(9)} vezes.')
print(f'O número 3 apareceu na {tupla.index(3)+1}ª posição.' if 3 in tupla else 'O número 3 não foi digitado.') 
print(f'Os números pares digitados foram: {pares}', end='' if pares else 'Nenhum número par foi digitado.')