def leiaInt(msg):
    while True:    
        try:
            num = int(input(msg))
        except (ValueError, TypeError):
            print('\033[31mErro! Digite um número inteiro válido: \033[m')
            continue
        except KeyboardInterrupt:
            print('\033[31mEntrada de dados interrompida pelo usuário.\033[m')
            return 0
        else:
            return num

def leiaFloat(msg):
    while True:    
        try:
            num = float(input(msg))
        except (ValueError, TypeError):
            print('\033[31mErro! Digite um número Real válido: \033[m')
            continue
        except KeyboardInterrupt:
            print('\033[31mEntrada de dados interrompida pelo usuário.\033[m')
            return 0.0
        else:
            return num

n1 = leiaInt('Digite um número inteiro: ')
n2 = leiaFloat('Digite um número Real: ')

print(f'O valor inteiro digitado foi {n1}')
print(f'O valor real digitado foi {n2}')