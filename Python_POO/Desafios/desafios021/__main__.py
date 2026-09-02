from classes import *

def main():
    finalizar_compra(Boleto(), 2_500)
    finalizar_compra(PIX(), 3_300)
    finalizar_compra(Credito(), 750)

if __name__ == "__main__":
    main()
