from classes import *

def main():
    g = Gerente("Thiago", 12_000)
    dev = Desenvolvedor("Danilo", 3_500)
    dsg = Desingner("Andrey", 2_800)

    g.calcular_bonus()
    dev.calcular_bonus()
    dsg.calcular_bonus()

    #g.salario = 9_000

    print(g)
    print(dev)
    print(dsg)


if __name__ == "__main__":
    main()
