from Filme import Filme


class SeletorFilme:
    def __init__(self):
        self.filmes = []
        self.filme_assistidos = []

    def carrega_filmes(self):
        with open("filmes.txt","r",encoding="utf-8") as file:
            todos_filmes = [linha.replace("\n", "") for linha in file]  # captura todos os jogadores disponiveis
            for linha in todos_filmes:
                filme = linha.split(";")
                novo_filme = Filme(filme[0],filme[1],filme[2],filme[3])
                self.filmes.append(novo_filme)


    def informa_filme_assistido(self):
        pass

    def escolhe_filme_por_ator(self, nome_ator):
        pass

    def escolhe_filme_por_genero(self, genero_filme):
        pass