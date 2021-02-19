fileName = "film.txt"
import datetime


class Console:

    def __init__(self, filmService, cardService, rezervareService):
        self.filmService = filmService
        self.cardService = cardService
        self.rezervareService = rezervareService

    def show_menu(self):
        print('1. Filme')
        print('2. Carduri')
        print('3. Rezervari')
        print('x. Exit')

    def run_console(self):
        while True:
            self.show_menu()
            op = input('Optiune: ')
            if op == '1':
                self.show_filme()
            elif op == '2':
                self.show_carduri()
            elif op == '3':
                self.show_rezervari()
            elif op == 'x':
                break
            else:
                print('Comanda invalida!')

    def show_filme(self):
        while True:
            self.show_menu_filme()
            op = input('Optiune: ')
            if op == '1':
                self.__handle_filme_add()
                print(self.__handle_filme_show())
            elif op == '2':
                self.__handle_filme_remove()
                print(self.__handle_filme_show())
            elif op == '3':
                self.__handle_filme_update()
                print(self.__handle_filme_show())
            elif op == '4':
                self.__handle_search_film()
            elif op == '5':
                self.__handle_order_filme_desc()
            elif op == '6':
                self.__handle_filme_undo()
            elif op == '7':
                self.__handle_film_redo()
            elif  op == '8':
                self.__handle_perm()
            elif op == 'a':
                self.__handle_filme_show()
            elif op == 'b':
                break
            else:
                print('Comanda invalida!')

    def show_carduri(self):
        while True:
            self.show_menu_carduri()
            op = input('Optiune: ')
            if op == '1':
                self.__handle_carduri_add()
                print(self.__handle_carduri_show())
            elif op == '2':
                self.__handle_carduri_remove()
                print(self.__handle_carduri_show())
            elif op == '3':
                self.__handle_carduri_update()
                print(self.__handle_carduri_show())
            elif op == '4':
                self.__handle_search_client()
            elif op == '5':
                self.__handle_carduri_ordonare()
            elif op == '6':
                self.__handle_incrementare()
            elif op == '7':
                self.__handle_card_undo()
            elif op == '8':
                self.__handle_card_redo()
            elif op == 'a':
                self.__handle_carduri_show()
            elif op == 'b':
                break
            else:
                print('Comanda invalida!')

    def show_rezervari(self):
        while True:
            self.show_menu_rezervari()
            op = input('Optiune: ')
            if op == '1':
                self.__handle_rezervari_add()
                print(self.__handle_rezervari_show())
            elif op == '2':
                self.__handle_rezervari_remove()
                print(self.__handle_rezervari_show())
            elif op == '3':
                self.__handle_rezervari_update()
                print(self.__handle_rezervari_show())
            elif op == '4':
                self.__handle_show_rezervari_between_hours()
            elif op == '5':
                self.__handle_delete_rezervari_between_dates()
            elif op == '6':
                self.__handle_rez_undo()
            elif op == '7':
                self.__handle_rez_redo()
            elif op == 'a':
                self.__handle_rezervari_show()
            elif op == 'b':
                break
            else:
                print('Comanda invalida!')

    def show_menu_filme(self):
        print('--- FILME')
        print('1. Adauga')
        print('2. Sterge')
        print('3. Update')
        print('4. Cautare film dupa o caracteristica')
        print('5. Afișare filme ordonate descrescător după numărul de rezervări')
        print('6. Undo')
        print('7. Redo')
        print('8. Permutari')
        print('a. Afisare')
        print('b. Back')

    def show_menu_carduri(self):
        print('--- CARDURI')
        print('1. Adauga')
        print('2. Sterge')
        print('3. Update')
        print('4. Cautare client dupa o caracteristica')
        print('5. Afișarea cardurilor client ordonate descrescător după numărul de puncte de pe card.')
        print('6. Incrementarea cu o valoare dată a punctelor de pe toate cardurile a căror zi de naștere '
              'se află într-un interval dat.')
        print('7. Undo')
        print('8. Redo')
        print('a. Afisare')
        print('b. Back')

    def show_menu_rezervari(self):
        print('--- REZERVARI')
        print('1. Adauga')
        print('2. Sterge')
        print('3. Update')
        print('4. Afișare rezervari dintr-un interval de ore dat')
        print('5. Ștergere rezervări dintr-un anumit interval de zile')
        print('6. Undo')
        print('7. Redo')
        print('a. Afisare')
        print('b. Back')

    def __handle_filme_add(self):
        try:
            id_film = int(input('ID: '))
            titlu = str(input("Titlu: "))
            an = int(input("Anul: "))
            pret = int(input("Pret: "))
            program = str(input("In program: "))
            self.filmService.add_film(
                id_film,
                titlu,
                an,
                pret,
                program,
            )
            print('Filmul a fost adaugat!')
        except ValueError as ve:
            print('Erori:')
            for error in ve.args[0]:
                print(error)

    def __handle_carduri_add(self):
        try:
            id_card = int(input('ID: '))
            name = str(input("Name: "))
            firstName = str(input("First Name: "))
            CNP = int(input("CNP: "))
            dateB = str(input("Date of birth (yyyy.mm.dd): "))
            dateStr1 = dateB.split(".")
            year1 = int(dateStr1[0])
            month1 = int(dateStr1[1])
            day1 = int(dateStr1[2])
            dateB = datetime.date(year1, month1, day1)
            dateR = str(input("Date of registration: "))
            puncte = int(input("Puncte: "))
            self.cardService.add_card(
                id_card,
                name,
                firstName,
                CNP,
                dateB,
                dateR,
                puncte
            )
            print('Cardul clientului a fost adaugat!')
        except ValueError as ve:
            print('Erori:')
            for error in ve.args[0]:
                print(error)

    def __handle_rezervari_add(self):
        try:
            id = int(input('ID: '))
            idFilm = int(input("Id film: "))
            idCard = int(input("Id Card: "))
            date = str(input("Date (yyyy.mm.dd): "))
            dateStr = date.split(".")
            an = int(dateStr[0])
            luna = int(dateStr[1])
            zi = int(dateStr[2])
            date = datetime.date(an, luna, zi)
            hour = input("Hour (hh:mm): ")
            hourStr = hour.split(":")
            ora = int(hourStr[0])
            min = int(hourStr[1])
            hour = datetime.time(ora, min)
            self.rezervareService.add_rezervare(
                id,
                idFilm,
                idCard,
                date,
                hour)
            print(' Rezervarea a fost adaugata!')
        except ValueError as ve:
            print('Erori:')
            for error in ve.args[0]:
                print(error)

    def __handle_filme_show(self):
        for film in self.filmService.get_all():
            print(film)

    def __handle_filme_remove(self):
        idFilm = int(input("Dati id-ul filmului pe care doriti sa il stergeti: "))
        self.filmService.remove_film(idFilm)

    def __handle_filme_update(self):
        id = input("Dati id-ul filmului pe  care doriti sa il modificati: ")
        newid = input("Dati noul id: ")
        newTitlu = input("Dati noul titlu: ")
        newYear = input("Dati noul an: ")
        newPret = input("Dati noul pret: ")
        newProgram = input("In program?: ")
        self.filmService.update_film(id, newid, newTitlu, newYear, newPret, newProgram)

    def __handle_carduri_show(self):
        for card in self.cardService.getAll():
            print(card)

    def __handle_carduri_remove(self):
        idCard = int(input("Dati id-ul cardului pe care doriti sa il stergeti: "))
        self.cardService.remove_card(idCard)

    def __handle_carduri_update(self):
        id = input("Dati id-ul cardului pe  care doriti sa il modificati: ")
        newid = input("Dati noul id: ")
        newName = input("Dati numele: ")
        newFirstName = input("Dati prenumele: ")
        newCNP = input("Dati CNP-ul: ")
        newDateB = str(input("Date of birth (yyyy.mm.dd): "))
        dateStr1 = newDateB.split(".")
        year1 = int(dateStr1[0])
        month1 = int(dateStr1[1])
        day1 = int(dateStr1[2])
        newDateB = datetime.date(year1, month1, day1)
        newDateR = input("Dati data inregistrarii: ")
        newPuncte = int(input("Dati nr de puncte:"))
        self.cardService.update_card(id, newid, newName, newFirstName, newCNP, newDateB, newDateR, newPuncte)

    def __handle_rezervari_show(self):
        for rez in self.rezervareService.getAll():
            print(rez)

    def __handle_rezervari_remove(self):
        id = int(input("Dati id-ul rezervarii pe care doriti sa o stergeti: "))
        self.rezervareService.remove_rezervare(id)

    def __handle_rezervari_update(self):
        id = input("Dati id-ul rezervarii pe  care doriti sa o modificati: ")
        newid = input("Dati noul id: ")
        newIdFilm = input("Dati id-ul filmului: ")
        newIdCard = input("Dati ig-ul cardului: ")
        newDate = str(input("Date of birth (yyyy.mm.dd): "))
        dateStr1 = newDate.split(".")
        year1 = int(dateStr1[0])
        month1 = int(dateStr1[1])
        day1 = int(dateStr1[2])
        newDate = datetime.date(year1, month1, day1)
        newHour = input("Dati ora: ")
        hourStr = newHour.split(":")
        ora = int(hourStr[0])
        min = int(hourStr[1])
        newHour = datetime.time(ora, min)
        self.rezervareService.update_rezervare(id, newid, newIdFilm, newIdCard, newDate, newHour)

    def __handle_carduri_ordonare(self):
        for card in self.cardService.orderedByPoints():
            print(card)

    def __handle_search_film(self):
        caract = input("Dati caracteristica dupa care doriti sa cautati filmul (titlu, an, pret, in program): ")
        if caract == "titlu":
            titlu = input("Dati titlul: ")
            for film in self.filmService.search_film_by_title(titlu):
                print(film)
        if caract == "an":
            an = int(input("Dati anul: "))
            for film in self.filmService.search_film_by_year(an):
                print(film)
        if caract == "pret":
            pret = float(input("Dati pretul: "))
            for film in self.filmService.search_film_by_price(pret):
                print(film)
        if caract == "in program":
            program = input("In program (da/nu): ")
            for film in self.filmService.search_film_by_program(program):
                print(film)

    def __handle_search_client(self):
        caract = input("Dati caracteristica dupa care doriti sa cautati clientul (nume, "
                       "prenume, CNP, data nastere, data inregistrare): ")
        if caract == "nume":
            nume = input("Dati numele: ")
            for card in self.cardService.search_card_by_nume(nume):
                print(card)
        if caract == "prenume":
            prenume = input("Dati prenumele: ")
            for card in self.cardService.search_card_by_prenume(prenume):
                print(card)
        if caract in ["CNP", "cnp"]:
            cnp = input("Dati cnp: ")
            for card in self.cardService.search_card_by_cnp(cnp):
                print(card)
        if caract in ["data nasterii", "data nastere"]:
            data = input("Dati data nasterii: ")
            dateStr1 = data.split(".")
            year1 = int(dateStr1[0])
            month1 = int(dateStr1[1])
            day1 = int(dateStr1[2])
            data = datetime.date(year1, month1, day1)
            for card in self.cardService.search_card_by_dataN(data):
                print(card)
        if caract in ["data inregistrarii", "data inregistrare"]:
            data = input("Dati data inregistrarii: ")
            for card in self.cardService.search_card_by_dataI(data):
                print(card)

    def __handle_show_rezervari_between_hours(self):
        ora_start = input("Dati prima ora din interval (hh:mm): ")
        ora_final = input("Dati a doua ora din interval (hh:mm): ")
        hourStr1 = ora_start.split(":")
        ora1 = int(hourStr1[0])
        min1 = int(hourStr1[1])
        ora_start = datetime.time(ora1, min1)
        hourStr2 = ora_final.split(":")
        ora2 = int(hourStr2[0])
        min2 = int(hourStr2[1])
        ora_final = datetime.time(ora2, min2)
        for rezervare in self.rezervareService.show_rezervari_between_hours(ora_start, ora_final):
            for i in rezervare:
                print(i)

    def __handle_delete_rezervari_between_dates(self):
        data_start = input("Dati prima data din interval (yyyy.mm.dd): ")
        data_final = input("Dati a doua data din interval (yyyy.mm.dd): ")
        dateStr1 = data_start.split(".")
        year1 = int(dateStr1[0])
        month1 = int(dateStr1[1])
        day1 = int(dateStr1[2])
        data_start = datetime.date(year1, month1, day1)
        dateStr2 = data_final.split(".")
        year2 = int(dateStr2[0])
        month2 = int(dateStr2[1])
        day2 = int(dateStr2[2])
        data_final = datetime.date(year2, month2, day2)
        for rezervare in self.rezervareService.delete_rezervari_between_dates(data_start, data_final):
            print(rezervare)

    def __handle_incrementare(self):
        valoare = int(input("Dati valoarea: "))
        data_start = input("Dati prima data din interval (yyyy.mm.dd): ")
        data_final = input("Dati a doua data din interval (yyyy.mm.dd): ")
        dateStr1 = data_start.split(".")
        year1 = int(dateStr1[0])
        month1 = int(dateStr1[1])
        day1 = int(dateStr1[2])
        data_start = datetime.date(year1, month1, day1)
        dateStr2 = data_final.split(".")
        year2 = int(dateStr2[0])
        month2 = int(dateStr2[1])
        day2 = int(dateStr2[2])
        data_finala = datetime.date(year2, month2, day2)
        for card in self.cardService.incrementare(valoare, data_start, data_finala):
            print(card)

    def __handle_order_filme_desc(self):
        for film in self.filmService.order_filme_desc():
            print(film)

    def __handle_filme_undo(self):
        self.filmService.undo()
        for film in self.filmService.get_all():
            print(film)

    def __handle_card_undo(self):
        self.cardService.undo()
        for card in self.cardService.getAll():
            print(card)

    def __handle_rez_undo(self):
        self.rezervareService.undo()
        for rez in self.rezervareService.getAll():
            print(rez)

    def __handle_film_redo(self):
        self.filmService.redo()
        for film in self.filmService.get_all():
            print(film)

    def __handle_card_redo(self):
        self.cardService.redo()
        for card in self.cardService.getAll():
            print(card)

    def __handle_rez_redo(self):
        self.rezervareService.redo()
        for rez in self.rezervareService.getAll():
            print(rez)

    def __handle_perm(self):
        for perm in self.filmService.permutari():
            for film in perm:
                print(film)
            print("-----------------------------------------------------------------------------")

