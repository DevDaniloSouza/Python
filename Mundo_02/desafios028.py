print('Gerador de tabuada')
print('Digite um número negativo para parar o programa.')

while True:
    num = int(input('Digite um número para ver sua tabuada: '))
    if num < 0:
        break
    for c in range(1, 11):
        print(f'{num} x {c} = {num * c}')

print('Programa encerrado. Volte sempre!')
