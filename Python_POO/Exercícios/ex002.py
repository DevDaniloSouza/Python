class Gafanhoto:
    def __init__(self, nome="vazio", idade=0):
        self.nome = nome
        self.idade = idade

    def aniversario(self):
        self.idade += 1

    def __str__(self):
        return f"Olá, meu nome é {self.nome} e tenho {self.idade} anos."
    
    def __getstate__(self):
        return f"Estado: Nome = {self.nome} | Idade = {self.idade}"


g1 = Gafanhoto('João', 25)
g1.aniversario()
print(g1.__dict__)
print(g1.__getstate__())
print(g1.__class__)

g2 = Gafanhoto('Maria', 30)
g2.aniversario()
print(g2)

g3 = Gafanhoto()
print(g3)
