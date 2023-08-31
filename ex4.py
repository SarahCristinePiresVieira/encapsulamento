class livros:
    def __init__(self, titulo, autor,ano, precoDeProducao):
        self.titulo= titulo
        self.autor= autor
        self.ano = ano
        self.__precoDeProducao = precoDeProducao
    def atualizarano(self,atual):
        self.ano=atual

p1 = livros("Os Segredos da Mente Milionária","T. Harv Eker", 2020, 38.00)
print(p1.ano)