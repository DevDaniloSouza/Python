print('Sequencia de Fibonacci')

num = int(input('Quantos termos você quer mostrar? '))
t1 = 0
t2 = 1
c = 3

print('{} -> {}'.format(t1, t2), end='')

while c <= num:
    t3 = t1 + t2
    print(' -> {}'.format(t3), end='')
    t1 = t2
    t2 = t3
    c += 1

print(' -> FIM')