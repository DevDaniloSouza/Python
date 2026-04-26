num = soma = c = 0

while num != 999:
    num = int(input('Digite um número [999 para parar]: '))
    if num == 999:
        break
    soma += num
    c += 1

print('Programa finalizado! Foram digitados {} números.'.format(c))
print('A soma entre eles é {}.'.format(soma))
