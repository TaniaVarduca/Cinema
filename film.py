fileName = "film.txt"


class Film():
    """
        Car business object.
    """
    def __init__(self, idFilm, titlu, an, pret, program, deleteFilm=None):
        """
        Creates a movie
        :param idFilm: int
        :param titlu: string
        :param an: int
        :param pret: float
        :param program: string
        """
        self.__idFilm = idFilm
        self.__titlu = titlu
        if an > 0:
            self.__an = an
        else:
            raise ValueError("The year should be a strictly positive number!")
        if pret >= 0:
            self.__pret = pret
        else:
            raise ValueError("Pret should be a positive number!")
        self.__program = program
        self.__deleteFilm = deleteFilm

    def getFilmId(self):
        return self.__idFilm

    def setId(self, newId):
        self.__idFilm = int(newId)

    def getTitlu(self):
        return self.__titlu

    def setTitlu(self, newTitlu):
        self.__titlu = str(newTitlu)

    def getAn(self):
        return self.__an

    def setAn(self, newAn):
        if int(newAn) < 0:
            raise ValueError("Year cannot be negative!")
        self.__an = int(newAn)

    def getPret(self):
        return self.__pret

    def setPret(self, newPret):
        if float(newPret) < 0:
            raise ValueError("Price cannot be negative!")
        self.__pret = float(newPret)

    def getProgram(self):
        return self.__program

    def setProgram(self, newProgram):
        if newProgram not in ["da", "nu"]:
            raise ValueError("In program should be 'da' or 'nu'")
        self.__program = newProgram

    def getDeleteFilm(self):
        return self.__deleteFilm

    def setDeleteFilm(self, newDeleteFilm):
        self.__deleteFilm = newDeleteFilm

    def __str__(self) -> str:
        return "Film Id: {0}; Titlu: {1}; An: {2}; Pret: {3};In program: {4}; e_sters: {5}".format(self.getFilmId(),
                                                                                                   self.getTitlu(),
                                                                                                   self.getAn(),
                                                                                                   self.getPret(),
                                                                                                   self.getProgram(),
                                                                                                   self.getDeleteFilm())

    def __eq__(self, other):
        if not isinstance(other, Film):
            return False
        return self.getFilmId() == other.getFilmId() and \
               self.getTitlu() == other.getTitlu() and \
               self.getAn() == other.getAn() and \
               self.getPret() == other.getPret() and \
               self.getProgram() == other.getProgram()

    def __ne__(self, other):
        return not (self == other)
