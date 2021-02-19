import datetime
from domain.card import Card
fileName = "card.txt"


class RepositoryCard():
    def __init__(self, fileName):
        self.__fileName = fileName
        self.__cardsList = []
        self.__readFile()

    def addCard(self, card):
        """
        Adauga un card
        :param card: Card
        :return:
        """
        for c in self.__cardsList:
            if c.getCardId() == card.getCardId():
                raise ValueError("Id existent")
        self.__cardsList.append(card)
        self.__writeToFile()

    def removeCard(self, cardId):
        """
        Sterge un card
        :param cardId: int
        :return:
        """
        for i in range(len(self.__cardsList)):
            card = self.__cardsList[i]
            if card.getCardId() == cardId:
                del self.__cardsList[i]
                #card.setDeleteCard("True")
                break
        self.__writeToFile()

    def updateCard(self, id, newId, newName, newFirstName, newCNP, newDateB, newDateR, newPuncte):
        """
        Modifica un card
        :param id: int
        :param newId: int
        :param newName: string
        :param newFirstName: string
        :param newCNP: string
        :param newDateB: datetime.date (yyyy.mm.dd)
        :param newDateR: string
        :param newPuncte: int
        :return:
        """

        # oldCard = 0
        # for card in self.getAll():
        #     if card.getCardId() == id:
        #         oldCard = card
        #
        # self.__undo_operations.append(lambda: self.update_card(oldCard.getCardId(), oldCard.getCardId(), oldCard.getName(), oldCard.getFirstName(), oldCard.getCNP(), oldCard.getDateB(), oldCard.getDateR(), oldCard.getPuncte()))

        for card in self.__cardsList:
            idl = card.getCardId()
            if idl == int(id):
                if newId == "":
                    card.setId(id)
                else:
                    card.setId(newId)
                if newName == "":
                    card.setName(card.getName())
                else:
                    card.setName(newName)
                if newFirstName == "":
                    card.setFirstName(card.getFirstName())
                else:
                    card.setFirstName(newFirstName)
                if newCNP == "":
                    card.setCNP(card.getCNP())
                else:
                    card.setCNP(newCNP)
                if newDateB == "":
                    card.setDateB(card.getDateB())
                else:
                    card.setDateB(newDateB)
                if newDateR == "":
                    card.setDateR(card.getDateR())
                else:
                    card.setDateR(newDateR)
                if newPuncte == "":
                    card.setPuncte(card.getPuncte())
                else:
                    card.setPuncte(newPuncte)
        self.__writeToFile()

    def getAll(self, id=None):
        """
        :return: lista de carduri
        """
        if id is None:
            return self.__cardsList[:]
        else:
            for i in range(len(self.__cardsList)):
                card = self.__cardsList[i]
                if id == card.getCardId():
                    return card

    def eraseFile(self):
        f = open(self.__fileName, 'w').close()

    def __writeToFile(self):
        """
        Scrie un card  intr-un  fisier.
        :return:
        """
        content = ""
        for card in self.__cardsList:
            cardString="/".join([str(card.getCardId()), card.getName(), card.getFirstName(), str(card.getCNP()), str(card.getDateB()), card.getDateR(), str(card.getPuncte())])
            content = content+cardString+"\n"
        f = open(self.__fileName, 'w')
        f.write(content)
        f.close()

    def __readFile(self):
        """
        Citeste o lista de carduri dintr-un fisier.
        :return: lista de carduri
        """
        f = open(self.__fileName, 'r')
        try:
            lines = f.readlines()
            for line in lines:
                str = line[:-1]
                comp = str.split("/")
                id = int(comp[0])
                name = comp[1]
                firstName = comp[2]
                CNP = comp[3]
                dateB = comp[4]
                dateStr1 = dateB.split("-")
                year1 = int(dateStr1[0])
                month1 = int(dateStr1[1])
                day1 = int(dateStr1[2])
                dateB = datetime.date(year1, month1, day1)
                dateR = comp[5]
                puncte = int(comp[6])
                c = Card(id, name, firstName, CNP, dateB, dateR, puncte)
                self.__cardsList.append(c)
        except Exception as e:
            print("fisierul este gol")
        f.close()
