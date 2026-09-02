from classes import *

def main():
    d = DOC("Trabalho", 250_000)
    p = PDF("Currículo", 2_450_000)

    d.abrir_arquivo()
    p.abrir_arquivo()

if __name__ == "__main__":
    main()