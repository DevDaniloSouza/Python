class Avaliacao():
    def __init__(self, nome, disciplina, nota):
        self.nome = nome
        self.disciplina = disciplina
        self._nota = nota

    # Atributos validáveis:

    @property
    def nota(self): #getter
        return self._nota
    
    @nota.setter
    def nota(self, valor): #setter
        if 0 <= valor <= 10:
            self._nota = valor
        else:
            print('Nota inválida!')        
 