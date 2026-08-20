from classes import *

def main():
    p = Pessoa("Danilo", 2004)
    print(p.__dict__)

    a = Aluno("Danilo", 2004, "ADM")
    a.add_curso("LOG")
    print(a.cursos_oficiais)
    
if __name__ == "__main__":
    main()
