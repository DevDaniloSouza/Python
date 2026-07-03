from classes import *

def main():
    d = Diario("DaniloPDS")

    d.escrever("Mensagem especial repetida!")
    d.escrever("Mensagem especial repetida!")
    d.escrever("Mensagem especial repetida!")
    d.escrever("Mensagem especial repetida!")

    d.ler("DaniloPDS")

if __name__ == "__main__":
    main()
