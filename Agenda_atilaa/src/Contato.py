class Contacts():
    # arrayContcts = []

    def __init__(self,name, id, saveID):
        self.name = name
        self.idContact = id
        self.saveID = saveID
        self.arrayContacts = []

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

    def logicDeleteContacts(self):
        find_ID = False
        input_delete = int(input("Digite o ID do contato que deseja deletar:\n"))
        for contact_ID in self.arrayContacts:
            if(input_delete == contact_ID["id"]):
                self.arrayContacts.remove(contact_ID)
                find_ID = True
                if(find_ID == True):
                    print("Contato excluído com sucesso!")
            
        if(find_ID == False):
                print("ID não identificado, tente novamente.")
        
    
    
    
                
    

instanciarNome = Contacts("", 0,"")
instanciarNome.createContact()
instanciarNome.readContacts()
instanciarNome.logicDeleteContacts()