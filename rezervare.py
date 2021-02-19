class Rezervare():
    """
        Booking business object.
    """

    def __init__(self, id, idFilm, idCard, date, hour, deleteRez=None):
        """
        Creates a booking.
        :param id: int
        :param idFilm: int
        :param idCard: int
        :param date: datetime.date (yyyy.mm.dd)
        :param hour: datetime.time (hh.mm.ss)
        """
        self.__id = id
        self.__idFilm = idFilm
        self.__idCard = idCard
        self.__date = date
        self.__hour = hour
        self.__deleteRez = deleteRez

    def getId(self):
        return self.__id

    def setId(self, newId):
        self.__id = int(newId)

    def getIdFilm(self):
        return self.__idFilm

    def setIdFilm(self, newIdFilm):
        self.__idFilm = int(newIdFilm)

    def getIdCard(self):
        return self.__idCard

    def setIdCard(self, newIdCard):
        self.__idCard = int(newIdCard)

    def getDate(self):
        return self.__date

    def setDate(self, newDate):
        self.__date = newDate

    def getHour(self):
        return self.__hour

    def setHour(self, newHour):
        self.__hour = newHour

    def getDeleteRezervare(self):
        return self.__deleteRez

    def setDeleteRezervare(self, newDeleteRez):
        self.__deleteRez = newDeleteRez

    def __str__(self) -> str:
        return "Rezervare Id: {0}, Film Id: {1}, Card Id: {2}, Date:{3},Hour: {4}, e_sters: {5}".format(
            self.getId(),
            self.getIdFilm(),
            self.getIdCard(),
            self.getDate(),
            self.getHour(),
            self.getDeleteRezervare()
        )

    def __eq__(self, other):
        if not isinstance(other, Rezervare):
            return False
        return self.getId() == other.getId() and \
               self.getIdFilm() == other.getIdFilm() and \
               self.getIdCard() == other.getIdCard() and \
               self.getDate() == other.getDate() and \
               self.getHour() == other.getHour()

    def __ne__(self, other):
        return not (self == other)
