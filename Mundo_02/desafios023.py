print('Digite os números para calcular a média...')
res = int(input("Deseja digitar um número? [1 - Sim / 2 - Não]: "))

numeros = 0
media = 0
menor = 0
maior = 0
num = 0

while res == 1:
    num = float(input("Digite um número: "))
    res = int(input("Deseja digitar outro número? [1 - Sim / 2 - Não]: "))
    media += num
    numeros += 1

    if menor == 0 and maior == 0:
        menor = num
        maior = num
    else:
        if num < menor:
            menor = num
        if num > maior:
            maior = num

    if res != 1 and res != 2:
        print("Opção inválida. Digite 1 para Sim ou 2 para Não.")
        res = int(input("Deseja digitar outro número? [1 - Sim / 2 - Não]: "))

media = media / numeros
print(f"A média de todos os números é: {media}")
print(f"O menor número digitado foi: {menor}")
print(f"O maior número digitado foi: {maior}")
