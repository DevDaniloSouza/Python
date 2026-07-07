class Diario():
    def __init__(self, senha = "7404"):
        self.__segredos = []
        self.__senha = senha

    def escrever(self, msg):
        self.__segredos.append(msg)

    def ler(self, senha):
        if senha == self.__senha:
            print("Diário Liberado!")
            for item in self.__segredos:
                print(f'- {item}')
        else:
            print('Senha informada inválida!')
