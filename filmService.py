from domain.film import Film
fileName = "film.txt"


class FilmService():
    """
    Manages film logic
    """

    def __init__(self, repo, rezervareService):
        """
        Creates a film service.
        """

        self.__repo = repo
        self.__rezervareService = rezervareService

        self.__undo_operations = []
        self.__redo_operations = []

    def add_film(self, idFilm, titlu, an, pret, program):
        """
        :param idFilm: int
        :param titlu: string
        :param an: int
        :param pret: float
        :param program: string
        :return:
        """
        errors = []
        if idFilm in self.__repo.getAll():
            errors.append('Exista deja o masina cu id-ul []'.format(idFilm))
        if an <= 0:
            errors.append('Anul trebuie sa fie strict pozitiv!')
        if pret <= 0:
            errors.append('Pretul trebuie sa fie strict poztiv!')
        if program not in ["da", "nu"]:
            errors.append("In program trebuie sa fie una dintre:da,nu.")
        if errors != []:
            raise ValueError(errors)
        film = Film(idFilm, titlu, an, pret, program)
        self.__repo.addFilm(film)
        self.__undo_operations.append(lambda: self.__repo.removeFilm(idFilm))
        self.__redo_operations.append(lambda: self.__repo.addFilm(film))

    def get_all(self):
        """
        :return: a list of all the movies.
        """
        return self.__repo.getAll()

    def remove_film(self, filmId):
        """
        Sterge un film
        :param filmId: int
        :return:
        """
        '''
        if filmId not in self.__repo.getAll():
            raise ValueError("Nu exista acest ID film")
        '''
        film1 = self.__repo.getAll(filmId)
        self.__repo.removeFilm(filmId)
        self.__undo_operations.append(lambda: self.__repo.addFilm(film1))
        self.__redo_operations.append(lambda: self.__repo.removeFilm(filmId))

    def update_film(self, id, newId, newTitlu, newAn, newPret, newProgram):
        """
        Modifica un film
        :param id:int
        :param newId:int
        :param newTitlu:string
        :param newAn:int
        :param newPret:float
        :param newProgram:string
        :return:
        """
        errors = []
        if newProgram not in ["da", "nu"]:
            errors.append("In program trebuie sa fie una dintre:da,nu.")
        if errors != []:
            raise ValueError(errors)
        self.__undo_operations.append(lambda : self.__repo.getAll())
        self.__repo.updateFilm(id, newId, newTitlu, newAn, newPret, newProgram)
        self.__redo_operations.append(lambda : self.__repo.getAll())

    def search_film_by_title(self, titlu):
        """
        Cauta un film dupa titlu
        :param titlu:
        :return: lista de filme cu titlul dat
        """
        filmList = []
        for film in self.get_all():
            if titlu in film.getTitlu():
                filmList.append(film)
        return filmList

    def search_film_by_year(self, an):
        """
        Cauta un film dupa an
        :param an:
        :return: lista de filme cu anul dat
        """
        '''
        filmList = []
        for film in self.get_all():
            if an == film.getAn():
                filmList.append(film)
        return filmList
        '''
        filmList = filter(lambda x: x.getAn() == an, self.get_all())
        return filmList

    def binary_search(self, film, list):
        """
        searches for needle in haystack
        """

        list = sorted(self.get_all(), key=lambda film: film.getPret(), reverse=False)
        st = 0
        dr = len(list) - 1

        while st <= dr:
            m = (st + dr) // 2  # st + (dr - st) // 2
            # TODO: get rid of the first if
            # hint: modificat un pic conditia din while
            if list[m] == film:
                return True
            if list[m] < film:
                st = m + 1
            else:
                dr = m - 1
        return False

    def search_film_by_price(self, pret):
        """
        Cauta un film dupa pret
        :param pret:
        :return: lista de filme cu pretul dat
        """
        filmList = []
        for film in self.get_all():
            if pret == film.getPret():
                filmList.append(film)
        return filmList

    def search_film_by_program(self, program):
        """
        Cauta un film dupa program
        :param program:
        :return: lista de filme cu programul dat
        """
        filmList = []
        for film in self.get_all():
            if program in film.getProgram():
                filmList.append(film)
        return filmList

    def order_filme_desc(self):
        """
        Ordoneaza descrescator filmele dupa numarul de rezervari
        :return: lista filmelor ordonate descrescator dupa nr de rezervari
        """
        filmList = self.get_all()
        rezList = self.__rezervareService.getAll()
        idFilmList = []
        for i in range(len(filmList)):
            idFilmList.append([0, 0])
        idFilmList.append([0, 0])
        for film in filmList:
            idFilm = film.getFilmId()
            for rez in rezList:
                if rez.getIdFilm() == idFilm:
                    idFilmList[film.getFilmId()][0] = film.getFilmId()
                    idFilmList[film.getFilmId()][1] +=1
        idFilmList = sorted(idFilmList, key=lambda x: x[1], reverse=True)
        newFilmList = []
        for i in range(len(idFilmList)):
            _idFilm = idFilmList[i][0]
            for film in filmList:
                if film.getFilmId() == _idFilm:
                    newFilmList.append(film)
        return newFilmList

    def undo(self):
        if len(self.__undo_operations) > 0:
            undo_op = self.__undo_operations.pop()
            undo_op()

    def redo(self):
        if len(self.__redo_operations) > 0:
            redo_op = self.__redo_operations.pop()
            redo_op()

    def permutari(self):
        results = []
        filmList = self.get_all()
        n = len(filmList)

        def inner(permutare_curenta):
            if len(permutare_curenta) == n:
                results.append(permutare_curenta)
                return
            for film in filmList:
                if film not in permutare_curenta:
                    inner(permutare_curenta + [film])
        inner([])
        return results