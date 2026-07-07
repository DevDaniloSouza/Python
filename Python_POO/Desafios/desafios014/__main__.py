from classes import *

def main():
    d = Diario("DaniloPDS")

    d.escrever("Mensagem especial!")
    d.escrever("Segredo número dois!")
    d.escrever("Eu amo minha mulher!")
    d.escrever("Ana Paula, linda e perfeita!")

    d.ler("DaniloPS")

if __name__ == "__main__":
    main()
