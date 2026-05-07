c = ('\033[m',        # 0 - sem cor
     '\033[0;30;41m', # 1 - vermelho
     '\033[0;30;42m', # 2 - verde
     '\033[0;30;43m', # 3 - amarelo
     '\033[0;30;44m', # 4 - azul
     '\033[0;30;45m', # 5 - roxo
     '\033[7;30m'     # 6 - branco
    )

def titulo(msg, cor=0):
    print(c[cor], end='')
    print(f'~' * (len(msg) + 4))
    print(f'  {msg}  ' )
    print(f'~' * (len(msg) + 4))
    print(c[0])

def ajuda(comando):
    titulo(f'Acessando o manual do comando "{comando}"', 4)
    print(c[6], end='')
    help(comando)
    print(c[0], end='')

while True:
    titulo('SISTEMA DE AJUDA PyHELP', 2)
    comando = str(input('Função ou Biblioteca > ')).strip()
    if comando.upper() == 'FIM':
        titulo('ATÉ LOGO!', 1)
        break
    else:
        ajuda(comando)
