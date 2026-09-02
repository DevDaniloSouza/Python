from classes import *

def main():
    c1 = Carteira(100)
    c2 = Carteira(100)
    print(c1.__eq__(c2))
    c1 += 50

    print(c1)

if __name__ == "__main__":
    main()
