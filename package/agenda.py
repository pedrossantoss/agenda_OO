from Pessoa import Pessoa

class Agenda():
    def __init__(self,contatos):
        self.contatos = []
        
        
    def criarPessoas(self):
        inputPessoas = input("Insira seu nome :")
        nomePessoa = Pessoa(inputPessoas)
        self.contatos.append(nomePessoa)
        print(nomePessoa.nome)
        
            
    def listarPessoas(self):       
        for i in self.contatos:
            print("")

            
            
        

agendaTeste = Agenda()

agendaTeste.criarPessoas()
agendaTeste.listarPessoas()
# print(agendaTeste.contatos)

