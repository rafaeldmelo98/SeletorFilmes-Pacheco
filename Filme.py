


class Filme:
    def __init__(self, filme, ator, genero, ano):
        self.filme = filme
        self.ator = ator
        self.genero = genero
        self.ano = ano

    def __str__(self):
        return "{} - {} - {} - {}".format(self.filme, self.ator,self.genero,self.ano)