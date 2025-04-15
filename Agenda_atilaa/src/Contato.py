class Contacts():
    # arrayContcts = []

    def __init__(self,name, id, saveID, editFunction):
        self.name = name
        self.idContact = id
        self.saveID = saveID
        self.arrayContacts = []
        self.edit = editFunction

    def createContact(self):
        self.idContact += 1
        userInput = input("Digite o nome do contato:\n")
        self.name = userInput
        contact_data = { "Nome" : self.name, "id": self.idContact}
        self.saveID = contact_data
        self.arrayContacts.append(self.saveID)

    def readContacts(self):
        print("-- Lista de Contatos --")
        for contact in self.arrayContacts:
            print(contact)

    def deleteContacts(self):
        status = False
        input_delete = int(input("Digite o ID do contato que deseja deletar:\n"))
        for contact_ID in self.arrayContacts:
            if(input_delete == contact_ID["id"]):
                self.arrayContacts.remove(contact_ID)
                status = True
                if(status == True):
                    print("Contato excluído com sucesso!")
            
        if(status == False):
                print("ID não identificado, tente novamente.")
        
    
    def editContact(self):
        saveEdit = int(input("Digite o ID de quem deseja editar:\n"))
        status = False
        for edit_ID in self.arrayContacts:
            if(saveEdit == edit_ID["id"]):
                newName = input("Insira o novo nome:\n")
                edit_ID["Nome"] = newName
                self.edit = edit_ID
                status = True
                if(status == True):
                    print("Usuário editado com sucesso!")
                break
        if(status == False):
            print("Erro ao editar o usuário") 



instanciarNome = Contacts("", 0,"","")
# instanciarNome.createContact()
# instanciarNome.readContacts()
# instanciarNome.editContact()
# instanciarNome.readContacts()
# instanciarNome.deleteContacts()
# instanciarNome.readContacts()
