from domain.card import Card


class CardService():
    """
    Manages card logic
    """
    def __init__(self, repo):
        """
        Creates a card service.
        """
        self.__repo = repo
        self.__undo_operations = []
        self.__redo_operations = []

    def add_card(self, idCard, name, fisrtName, CNP, dateB, dateR, puncte):
        """
        Creates and add a card in the cards list.
        :param idCard: -int
        :param name: -str
        :param fisrtName: -str
        :param CNP: -int,unic
        :param dateB: -datetime.date(yyyy.mm.dd)
        :param dateR: -str
        :param puncte:int
        :return:
        """
        errors = []
        if idCard in self.__repo.getAll():
            errors.append('Exista deja un card cu id-ul []'.format(idCard))
        if CNP in self.__repo.getAll():
            errors.append("CNP-ul trebuie sa fie unic! Exista deja o persoana inregistrata cu acest CNP.")
        if errors != []:
           raise ValueError(errors)
        card = Card(idCard, name, fisrtName, CNP, dateB, dateR, puncte)
        self.__repo.addCard(card)
        self.__undo_operations.append(lambda: self.__repo.removeCard(idCard))
        self.__redo_operations.append(lambda: self.__repo.addCard(card))

    def getAll(self):
        """
        :return: a list of all the cards.
        """
        return self.__repo.getAll()

    def remove_card(self, cardId):
        """
        Sterge un card
        :param cardId: int
        :return:
        """
        card1 = self.__repo.getAll(cardId)
        self.__repo.removeCard(cardId)
        self.__undo_operations.append(lambda: self.__repo.addCard(card1))
        self.__redo_operations.append(lambda: self.__repo.removeCard(cardId))

    def update_card(self, id, newId, newName, newFirstName, newCNP, newDateB, newDateR, newPuncte):
        """
        Modifica un card
        :param id:int
        :param newId:int
        :param newName:int
        :param newFirstName:string
        :param newCNP:string
        :param newDateB:datetime.date(yyyy.mm.dd)
        :param newDateR:string
        :param newPuncte:int
        :return:
        """
        # oldCard = self.__repo.getAll(id)
        oldCard = self.__repo.getAll(1)
        for card in self.getAll():
            if card.getCardId() == id:
                oldCard = card

        self.__repo.updateCard(id, newId, newName, newFirstName, newCNP, newDateB, newDateR, newPuncte)
        self.__undo_operations.append(lambda: self.update_card(oldCard.getCardId(), oldCard.getCardId(), oldCard.getName(), oldCard.getFirstName(), oldCard.getCNP(), oldCard.getDateB(), oldCard.getDateR(), oldCard.getPuncte()))

    def search_card_by_nume(self, nume):
        """
        Cauta un card dupa numele clientului
        :param nume: string
        :return: lista de carduri cu numele dat
        """
        cardList = []
        for card in self.getAll():
            if nume in card.getName():
                cardList.append(card)
        return cardList

    def search_card_by_prenume(self, prenume):
        """
        Cauta un card dupa prenumele clientului
        :param prenume: string
        :return: lista de carduri cu prenumele dat
        """
        cardList = []
        for card in self.getAll():
            if prenume in card.getFirstName():
                cardList.append(card)
        return cardList

    def search_card_by_cnp(self, cnp):
        """
        Cauta un card dupa cnp-ul clientului
        :param cnp: string
        :return: lista de carduri cu cnp-ul dat
        """
        cardList = []
        for card in self.getAll():
            if cnp in card.getCNP():
                cardList.append(card)
        return cardList

    def search_card_by_dataN(self, data):
        """
        Cauta un card dupa data nasterii clientului
        :param data: datetime.date(yyyy.mm.dd)
        :return: lista de carduri cu data nasterii data
        """
        cardList = []
        for card in self.getAll():
            if data == card.getDateB():
                cardList.append(card)
        return cardList

    def search_card_by_dataI(self, data):
        """
        Cauta un card dupa data inregistrarii clientului
        :param data: string
        :return: lista de carduri cu data inregistrarii data
        """
        cardList = []
        for card in self.getAll():
            if data in card.getDateR():
                cardList.append(card)
        return cardList

    def mySort(self, list, key=None, reverse=True):
        list = self.getAll()
        newList = list[:]
        for i in range(len(newList)):
            for j in range(i, len(newList)):
                e1 = newList[i]
                e2 = newList[j]
                if key != None:
                    e1 = key(e1)
                    e2 = key(e2)
                cond = e1 > e2
                if reverse:
                    cond = not cond
                if cond:
                    aux = newList[i]
                    newList[i] = newList[j]
                    newList[j] = aux
        return newList

    def orderedByPoints(self):
        """
        Ordoneaza lista de carduri descrescator dupa nr de puncte
        :return: lista de carduri ordonata descrescator dupa nr de puncte
        """
        #return sorted(self.__repo.getAll(), key=lambda card: card.getPuncte(), reverse=True)
        s = self.mySort(self.getAll(), key=lambda card: card.getPuncte())
        return s

    def incrementare(self, valoare, data_start, data_final):
        """
        Incrementeaza cu o valoare data punctele de pe cardurile clientilor a caror zi de nastere se afla intr-un
        interval dat
        :param valoare: int
        :param data_start: datetime.date(yyyy.mm.dd)
        :param data_final: datetime.date(yyyy.mm.dd)
        :return: lista de carduri cu valorile potrivite incrementate
        """
        '''
        for card in self.getAll():
            if (data_start < card.getDateB()) and (data_final > card.getDateB()):
                card.setPuncte(card.getPuncte()+valoare)
        return self.getAll()
        '''
        l = self.getAll()
        list = map(lambda x: (x.getPuncte() + valoare) if (data_start < x.getDateB()) and (data_final > x.getDateB())
        else x.getPuncte(), l)
        return list

    def undo(self):
        if len(self.__undo_operations) > 0:
            undo_op = self.__undo_operations.pop()
            undo_op()

    def redo(self):
        if len(self.__redo_operations) > 0:
            redo_op = self.__redo_operations.pop()
            redo_op()



