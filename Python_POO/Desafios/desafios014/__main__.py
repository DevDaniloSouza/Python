from classes import *
from rich import print, inspect

def main():
    d = Diario()

    d.escrever("Mensagem especial!")
    d.escrever("Segredo número dois!")
    d.escrever("Eu amo minha mulher!")
    d.escrever("Ana Paula, linda e perfeita!")

    try:
        d.ler("704")
    except Exception as e:
        print(f'[red]ERRO: {e}[/]')

    inspect(d, private=True)

if __name__ == "__main__":
    main()
