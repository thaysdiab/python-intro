
class Receita():

    def __init__(self, ingredientes, preparo, duracao):
        self.ingredientes=ingredientes
        self.preparo=preparo
        self.duracao=duracao

    def get_ingredientes(self):
        return self.ingredientes

    def get_preparo(self):
        return self.preparo

    def get_duracao(self):
        return self.duracao    

receita=Receita(["leite", "ovos"], "misture todos os ingredientes e está pronto", "20min")

print(receita.duracao)


