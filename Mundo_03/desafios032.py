def leiaInt(texto):
    while True:
        try:
            n = int(input(texto))
        except (ValueError, TypeError):
            print('\033[0;31mERRO: Digite um número inteiro válido.\033[m')
            continue
        except KeyboardInterrupt:
            print('\n\033[0;31mEntrada de dados interrompida pelo usuário.\033[m')
            return 0
        else:
            return n
    
n = leiaInt('Digite um número inteiro: ')
print(f'Você digitou o número {n}')