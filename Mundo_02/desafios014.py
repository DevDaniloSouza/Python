num = int(input('Digite um número inteiro: '))
total = 0

for c in range(1, num + 1):
    if num % c == 0:
        total += 1

if total == 2:
    print('O número {} é primo.'.format(num))
else:
    print('O número {} não é primo.'.format(num))
