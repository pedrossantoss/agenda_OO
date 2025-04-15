from Contato import Contacts

instanciarContato = Contacts("",0,"","")

class Agenda():
    
    def __init__(self):
        pass

    def menu_nav(self):
        print("Bem vindo!\n Selecione o que gostaria de fazer abaixo:\n")
    
        print("Criar contato - (C)\n")
        print("Listar contatos - (L)\n")
        print("Editar contato - (E)\n")
        print("Deletar contato - (D)\n")
        
        user_answer = input("").upper()

        if(user_answer == "C"):
            instanciarContato.createContact()
        elif(user_answer == "L"):
            instanciarContato.readContacts()
        elif(user_answer == "E"):
            instanciarContato.editContact()
        elif(user_answer == "D"):
            instanciarContato.deleteContacts()
    


instanciaAgenda = Agenda()
instanciaAgenda.menu_nav()