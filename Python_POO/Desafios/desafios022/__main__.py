from rich.panel import Panel
from rich import print
from classes import *

def main():
    Mensagem("Olá mundo! Essa é minha mensagem.").mostrar()
    Erro("Deu merda! Corrija o erro.").mostrar()
    Alerta("Tome cuidado! Isso é um aviso.").mostrar()

if __name__ == "__main__":
    main()
