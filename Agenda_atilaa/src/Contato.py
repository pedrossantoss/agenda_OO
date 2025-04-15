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
        delete_id = self.idContact
        for i in self.arrayContacts:
            if(delete_id == self.saveID["id"]):
                self.arrayContacts.remove(self.saveID)
    
                
    

instanciarNome = Contacts("", 0,"")
instanciarNome.createContact()
instanciarNome.readContacts()
instanciarNome.logicDeleteContacts()