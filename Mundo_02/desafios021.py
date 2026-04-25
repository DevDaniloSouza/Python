num1 = int(input('Digite um número inteiro: '))
num2 = int(input('Digite outro número inteiro: '))
opcao = 0

while opcao != 5:
    print('''O que você deseja fazer?
[1] Somar
[2] Multiplicar
[3] Maior
[4] novos números
[5] Sair''')
    opcao = int(input('Digite a sua opção: '))

    if opcao == 1:
        print(f'{num1} + {num2} = {num1 + num2}')
    elif opcao == 2:
        print(f'{num1} * {num2} = {num1 * num2}')
    elif opcao == 3:
        if num1 > num2:
            print(f'O maior número é {num1}')
        else:
            print(f'O maior número é {num2}')
    elif opcao == 4:
        num1 = int(input('Digite um novo número inteiro: '))
        num2 = int(input('Digite outro novo número inteiro: '))
    elif opcao == 5:
        print('Saindo do programa...')
    else:
        print('Opção inválida. Tente novamente.')