numExt = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')
ind = int(input('Digite um número entre 0 e 20 para ver seu extenso: '))

while True:
    if ind < 0 or ind > 20:
        ind = int(input('Número inválido. Digite um número entre 0 e 20: '))
    else:
        print(f'Você digitou o número {numExt[ind]}.')
        break
    