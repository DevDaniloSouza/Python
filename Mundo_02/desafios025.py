print('Gerador de PA')
num = int(input('Primeiro termo: '))
razao = int(input('Razão da PA: '))
c = 0
total = 0
mais = 10

while mais != 0:
    total += mais
    while c <= total:
        print(num, end=' → ')
        num += razao
        c += 1
    mais = int(input('Quantos termos a mais você quer mostrar? [0 para encerrar]: '))

print('Progressão finalizada com {} termos mostrados.'.format(total))
print('FIM')
