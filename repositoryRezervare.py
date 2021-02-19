from domain.rezervare import Rezervare
fileName = "rezervare.txt"
import datetime


class RepositoryRezervare():
    def __init__(self, fileName):
        self.__fileName = fileName
        self.__rezList = []
        self.__readFile()

    def addRezervare(self, rez):
        """
        Adauga o rezervare
        :param rez: Rezervare
        :return:
        """
        for r in self.__rezList:
            if r.getId() == rez.getId():
                raise ValueError("Id existent")
        self.__rezList.append(rez)
        self.__writeToFile()

    def removeRezervare(self, rezId):
        """
        Sterge o rezervare
        :param rezId: int
        :return:
        """
        for i in range(len(self.__rezList)):
            rez = self.__rezList[i]
            if rez.getId() == rezId:
                del self.__rezList[i]
                # rez.setDeleteRezervare("True")
                break
        self.__writeToFile()

    def updateRezervare(self, id, newId, newIdFilm, newIdCard, newDate, newHour):
        """
        Modifica o rezervare
        :param id: int
        :param newId: int
        :param newIdFilm: int
        :param newIdCard: int
        :param newDate: datetime.date (yyyy.mm.dd)
        :param newHour: datetime.time (hh:mm:ss)
        :return:
        """
        for rez in self.__rezList:
            idl = rez.getId()
            if idl == int(id):
                if newId == "":
                    rez.setId(id)
                else:
                    rez.setId(newId)
                if newIdFilm == "":
                    rez.setIdFilm(rez.getIdFilm())
                else:
                    rez.setIdFilm(newIdFilm)
                if newIdCard == "":
                    rez.setIdCard(rez.getIdCard())
                else:
                    rez.setIdCard(newIdCard)
                if newDate == "":
                    rez.setDate(rez.getDate())
                else:
                    rez.setDate(newDate)
                if newHour == "":
                    rez.setHour(rez.getHour())
                else:
                    rez.setHour(newHour)
        self.__writeToFile()

    def getAll(self, id=None):
        """
        :return: lista de rezervari
        """
        if id is None:
            return self.__rezList[:]
        else:
            for i in range(len(self.__rezList)):
                rez = self.__rezList[i]
                if id == rez.getId():
                    return rez

    def eraseFile(self):
        f = open(self.__fileName, 'w').close()

    def __writeToFile(self):
        """
        Scrie o rezervare intr-un fisier.
        :return:
        """
        content = ""
        for rez in self.__rezList:
            rezString = "/".join([str(rez.getId()), str(rez.getIdFilm()), str(rez.getIdCard()), str(rez.getDate()), str(rez.getHour())])
            content = content + rezString + "\n"
        f = open(self.__fileName, 'w')
        f.write(content)
        f.close()

    def __readFile(self):
        """
        Citeste o lista de rezervari dintr-un fisier.
        :return: lista de rezervari
        """
        f = open(self.__fileName, 'r')
        try:
            lines = f.readlines()
            for line in lines:
                str = line[:-1]
                comp = str.split("/")
                id = int(comp[0])
                idFilm = int(comp[1])
                idCard = int(comp[2])
                date = comp[3]
                dateStr = date.split("-")
                an = int(dateStr[0])
                luna = int(dateStr[1])
                zi = int(dateStr[2])
                date = datetime.date(an, luna, zi)
                hour = comp[4]
                hourStr = hour.split(":")
                ora = int(hourStr[0])
                min = int(hourStr[1])
                hour = datetime.time(ora, min)
                r = Rezervare(id, idFilm, idCard, date, hour)
                self.__rezList.append(r)
        except Exception as e:
            print("fisierul este gol")
        f.close()
