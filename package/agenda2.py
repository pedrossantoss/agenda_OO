from contato import contato

class Agenda:
    def __init__(self):
        self.contatos = []

    def criar(self):
        nome = input()
        telefone = input
        self.contatos.append(Contato(nome, telefone))
        print("contato adicionado com sucesso\n")
    
    def listar(self):
        if not self.contatos:
            print("Nenhum contato adicionado\n")
        for i, contato in enumerate(self.contatos):
            print(f"{i+1}. ",  end = "")
            contato.mostrar()
        
    def editar(self):
        self.listar()
        index = int(input("Digite o número que deseja editar: ")) - 1
        if 0 <= index < len(self.contatos):
            nome = input("Novo nome")
            telefone = input("Novo telefone")
            self.contatos[index].nome = nome
            self.contatos[index].telefone = telefone
            print("Contato atualizado!\n")
        else:
            print("Contato inválido!\n")

    def remover(self):
        self.listar