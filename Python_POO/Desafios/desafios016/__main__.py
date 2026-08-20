from classes import *

def main():
    r = Retangulo()
    try:
        r.base = 12
        r.altura = 15
    except Exception as e:
        print(f"Ocorreu um erro do tipo {type(e).__name__}: {e}")

    print(r.medidas)

if __name__ == "__main__":
    main()