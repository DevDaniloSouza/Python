num = int(input('Primeiro termo: '))
razao = int(input('Razão da PA: '))
c = 0

while c < 10:
    print(num, end=' → ')
    num += razao
    c += 1

print('FIM')
