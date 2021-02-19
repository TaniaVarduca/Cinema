from domain.film import Film
fileName = "film.txt"


class DuplicateIdException(Exception):
    pass


class RepositoryFilm():

    def __init__(self, fileName):
        self.__fileName = fileName
        self.__filmList = []
        self.__readFile()

    def addFilm(self, film):
        """
        Adauga un film
        :param film: Film
        :return: -
        """
        for f in self.__filmList:
            if f.getFilmId() == film.getFilmId():
                raise ValueError("Id existent")
        self.__filmList.append(film)
        self.__writeToFile()

    def removeFilm(self, filmId):
        """
        Sterge un film
        :param filmId: int
        :return: -
        """
        for i in range(len(self.__filmList)):
            film = self.__filmList[i]
            if film.getFilmId() == filmId:
                del self.__filmList[i]
                #film.setDeleteFilm("True")
                break
        self.__writeToFile()

    def eraseFile(self):
        f = open(self.__fileName, 'w').close()


    def updateFilm(self, id, newId, newTitlu, newAn, newPret, newProgram):
        """
        Modifica un film
        :param id: int
        :param newId: int
        :param newTitlu: string
        :param newAn: int
        :param newPret: float
        :param newProgram: string
        :return:
        """
        for film in self.__filmList:
            idl = film.getFilmId()
            if idl == int(id):
                if newId == "":
                    film.setId(id)
                else:
                    film.setId(newId)
                if newTitlu == "":
                    film.setTitlu(film.getTitlu())
                else:
                    film.setTitlu(newTitlu)
                if newAn == "":
                    film.setAn(film.getAn())
                else:
                    film.setAn(newAn)
                if newPret == "":
                    film.setPret(film.getPret())
                else:
                    film.setPret(newPret)
                if newProgram == "":
                    film.setProgram(film.getProgram())
                else:
                    film.setProgram(newProgram)
        self.__writeToFile()

    def getAll(self, id=None):
        """
        :return: lista de filme
        """
        if id is None:
            return self.__filmList[:]
        else:
            for i in range(len(self.__filmList)):
                film = self.__filmList[i]
                if id == film.getFilmId():
                    return film

    def __writeToFile(self):
        """
        Scrie un film in fisier.
        :return:
        """
        content = ""
        for film in self.__filmList:
            filmString = "/".join([str(film.getFilmId()), film.getTitlu(), str(film.getAn()), str(film.getPret()), film.getProgram()])
            content = content+filmString+"\n"
        f = open(self.__fileName, 'w')
        f.write(content)
        f.close()

    def __readFile(self):
        """
        Citeste o lista de filme dintr-un fisier.
        :return: lista de filme
        """
        f = open(self.__fileName, 'r')
        try:
            lines = f.readlines()
            for line in lines:
                str = line[:-1]
                comp = str.split("/")
                id = int(comp[0])
                titlu = comp[1]
                an = int(comp[2])
                pret = float(comp[3])
                program = comp[4]
                film = Film(id, titlu, an, pret, program)
                self.__filmList.append(film)
        except Exception as e:
            print("fisierul este gol")
        f.close()
