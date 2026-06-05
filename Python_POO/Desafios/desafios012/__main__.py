from classes import *

def main():
    p1 = Guerreiro("Kratos", 3000)
    p2 = Mago("Merlim", 2000)

    p1.atacar(p2, 1000)
    p2.atacar(p1, 1500)

    p1.curar()
    p2.curar()
    
    p1.atacar(p2, 1000)
    p2.atacar(p1, 1500)

if __name__ == "__main__":
    main()
