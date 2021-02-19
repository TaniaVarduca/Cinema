from domain.rezervare import Rezervare
import copy


class RezervareService():
    """
    Manages booking logic
    """
    def __init__(self, repo_rez, repo_film, repo_card):
        """
        Creates a booking service.
        """
        self.__repo_rez = repo_rez
        self.repo_film = repo_film
        self.repo_card = repo_card

        self.__undo_operations = []
        self.__redo_operations = []

    def add_rezervare(self, id, idFilm, idCard, date, hour):
        """
        Creates and add a booking in the list.
        :param id: -int
        :param idFilm: -int
        :param idCard: -int
        :param date: datetime.date(yyyy.mm.dd)
        :param hour: datetime.time(hh:mm:ss)
        :return:
        """
        errors = []
        if id in self.__repo_rez.getAll():
            errors.append('Exista deja o rezervare cu id-ul []'.format(id))
        if errors != []:
            raise ValueError(errors)
        rez = Rezervare(id, idFilm, idCard, date, hour)
        self.__repo_rez.addRezervare(rez)
        self.__redo_operations.append(lambda: self.__repo_rez.addRezervare(rez))
        self.__undo_operations.append(lambda: self.__repo_rez.removeRezervare(id))

    def getAll(self):
        """
        :return: a list of all the bookings.
        """
        return self.__repo_rez.getAll()

    def remove_rezervare(self, id):
        """
        Sterge o rezervare
        :param id: int
        :return:
        """
        rez1 = self.__repo_rez.getAll(id)
        self.__repo_rez.removeRezervare(id)
        self.__redo_operations.append(lambda: self.__repo_rez.removeRezervare(id))
        self.__undo_operations.append(lambda: self.__repo_rez.addRezervare(rez1))



    def update_rezervare(self, id, newId, newIdFilm, newIdCard, newDate, newHour):
        """
        Modifica o rezervare
        :param id:int
        :param newId:int
        :param newIdFilm:int
        :param newIdCard:int
        :param newDate:datetime.date(yyyy.mm.dd)
        :param newHour:datetime.time(hh:mm:ss)
        :return:
        """
        self.__repo_rez.updateRezervare(id, newId, newIdFilm, newIdCard, newDate, newHour)

    def show_rezervari_between_hours(self, ora_start, ora_final):
        """
        Afiseaza rezervarile care sunt intr-un interval de ore dat
        :param ora_start: datetime.time(hh:mm:ss)
        :param ora_final: datetime.time(hh:mm:ss)
        :return: lista de rezervari care sunt intr-un interval de ore dat
        """
        '''
        rezList = []
        for rezervare in self.getAll():
            if (ora_start < rezervare.getHour()) and (ora_final > rezervare.getHour()):
                rezList.append(rezervare)
        return rezList
        '''
        results = []
        rezList = self.getAll()

        def inner(rez_curenta):
            if len(rez_curenta):
                results.append(rez_curenta)
                return
            for rez in rezList:
                if (ora_start < rez.getHour()) and (ora_final > rez.getHour()):
                    inner(rez_curenta + [rez])
        inner([])
        return results

    def delete_rezervari_between_dates(self, data_start, data_final):
        """
        Sterge rezevarile care sunt intr-un anumit interval de zile dat
        :param data_start: datetime.date(yyyy.mm.dd)
        :param data_final: datetime.date(yyyy.mm.dd)
        :return: lista de rezervari fara rezervarile care sunt intr-un anumit interval de zile dat
        """
        rezList = self.getAll()
        '''
        i = 0
        n = len(rezList)
        while i <= n:
            rezervare = rezList[i]
            if (data_start < rezervare.getDate()) and (data_final > rezervare.getDate()):
                self.__repo.removeRezervare(rezervare.getId())
                del rezervare
                n = n-1
            i = i + 1
        '''
        for rezervare in rezList:
            if (data_start < rezervare.getDate()) and (data_final > rezervare.getDate()):
                rez1 = self.__repo_rez.getAll(rezervare.getId())
                self.__repo_rez.removeRezervare(rezervare.getId())
                self.__undo_operations.append(lambda: self.__repo_rez.addRezervare(rez1))
                self.__redo_operations.append(lambda: self.__repo_rez.removeRezervare(rez1.getId()))
        return self.getAll()

    def undo(self):
        if len(self.__undo_operations) > 0:
            undo_op = self.__undo_operations.pop()
            undo_op()

    def redo(self):
        if len(self.__redo_operations) > 0:
            redo_op = self.__redo_operations.pop()
            redo_op()