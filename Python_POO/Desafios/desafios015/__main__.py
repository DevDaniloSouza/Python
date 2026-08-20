from classes import *

def main():
    c = Credencial()
    c.senha = "DaniloPDS"
    print(c.senha)

    c.validar("DaniloPS")

if __name__ == "__main__":
    main()
