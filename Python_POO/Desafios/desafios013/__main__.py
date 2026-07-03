from rich import inspect
from classes import *

def main():
    t = Termostato()
    t.temperatura = 22
    inspect(t)
    print(f'A temperatura está em {t.ftemperatura}')

if __name__ == "__main__":
    main()
