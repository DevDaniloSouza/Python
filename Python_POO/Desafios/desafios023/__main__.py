from classes import *
from rich import inspect

def main():
    p1 = Produto("Mouse", 250)
    p2 = Produto("Teclado", 349)
    p3 = Produto("MousePad", 49)
    p4 = Produto("Placa de Vídeo", 3_499)
    p5 = Produto("Cadeira Gamer", 1_249)

    c1 = Carrinho()
    c2 = Carrinho()

    c1 = c1 + p1 + p2 + p3
    c2 = c1 + p4 + p5

    #c1 = c1 + c2

    print(c1)
    print(c2)

if __name__ == "__main__":
    main()

