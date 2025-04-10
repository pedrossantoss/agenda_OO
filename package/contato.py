class contato():
    def __init__(self, nome: str, telefone: str):
        self.nome = nome
        self.telefone = telefone

    def __str__(self):
        return f"{self.nome} - {self.telefone}"
    