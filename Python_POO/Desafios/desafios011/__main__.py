from classes import *

def main():
    f1 = Horista("Gabriel", 24, 200)
    f1.calc_salario()
    f1.analizar_salario()

    f2 = Mensalista("Ana Paula", 2_468)
    f2.calc_salario()
    f2.analizar_salario()

if __name__ == "__main__":
    main()

