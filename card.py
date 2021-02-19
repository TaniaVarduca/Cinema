class Card():
    """
        Card business object.
    """

    def __init__(self, id, name, firstName, CNP, dateB, dateR, puncte, deleteCard=None):
        """
        Creates a card.
        :param id: card id-int
        :param name: name -str
        :param firstName: -str
        :param CNP: -str
        :param dateB: datetime.date (yyyy.mm.dd)
        :param dateR: str
        :param puncte: int
        """
        self.__id = id
        self.__name = name
        self.__firstName = firstName
        self.__CNP = CNP
        self.__dateB = dateB
        self.__dateR = dateR
        self.__puncte = puncte
        self.__deleteCard = deleteCard

    def getCardId(self):
        return self.__id

    def setId(self, newId):
        self.__id = int(newId)

    def getName(self):
        return self.__name

    def setName(self, newName):
        self.__name = newName

    def getFirstName(self):
        return self.__firstName

    def setFirstName(self, newFirstName):
        self.__firstName = newFirstName

    def getCNP(self):
        return self.__CNP

    def setCNP(self, newCNP):
        self.__CNP = newCNP

    def getDateB(self):
        return self.__dateB

    def setDateB(self, newDateB):
        self.__dateB = newDateB

    def getDateR(self):
        return self.__dateR

    def setDateR(self, newDateR):
        self.__dateR = newDateR

    def getPuncte(self):
        return self.__puncte

    def setPuncte(self, newPuncte):
        self.__puncte = int(newPuncte)

    def getDeleteCard(self):
        return self.__deleteCard

    def setDeleteCard(self, newDeleteCard):
        self.__deleteCard = newDeleteCard

    def __str__(self) -> str:
        return "Card Id: {0}, Name: {1}, First Name: {2}, CNP: {3}, Date of birth: {4}, Date of registration: {5}, Puncte: {6}, e_sters: {7}".format(
            self.getCardId(),
            self.getName(),
            self.getFirstName(),
            self.getCNP(),
            self.getDateB(),
            self.getDateR(),
            self.getPuncte(),
            self.getDeleteCard()
        )

    def __eq__(self, other):
        if not isinstance(other, Card):
            return False
        return self.getCardId() == other.getCardId() and \
               self.getName() == other.getName() and \
               self.getFirstName() == other.getFirstName() and \
               self.getCNP() == other.getCNP() and \
               self.getDateB() == other.getDateB() and \
               self.getDateR() == other.getDateR() and \
               self.getPuncte() == other.getPuncte()

    def __ne__(self, other):
        return not (self == other)
