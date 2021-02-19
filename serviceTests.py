from repository.repositoryFilm import RepositoryFilm
from repository.repositoryCard import RepositoryCard
from repository.repositoryRezervare import RepositoryRezervare
from domain.film import Film
from domain.card import Card
from domain.rezervare import Rezervare
from service.filmService import FilmService
from service.cardService import CardService
from service.rezervareService import RezervareService


def add_film_test():
    repoFilm = RepositoryFilm("filmTests.txt")
    film_service = FilmService(repoFilm, "")
    assert len(repoFilm.getAll()) == 1
    film = Film(2, "film2", 2019, 15, "da")
    film_service.add_film(film.getFilmId(), film.getTitlu(), film.getAn(), film.getPret(), film.getProgram())
    assert len(repoFilm.getAll()) == 2
    repoFilm.eraseFile()
add_film_test()


def remove_film_test():
    repoFilm = RepositoryFilm("filmTests.txt")
    film_service = FilmService(repoFilm, "")
    repoFilm.eraseFile()
    film = Film(1, "film1", 2019, 5, "da")
    film_service.add_film(film.getFilmId(),
                          film.getTitlu(),
                          film.getAn(),
                          film.getPret(),
                          film.getProgram())
    assert len(repoFilm.getAll()) == 1
    film2 = Film(2, "film2", 2008, 78, "da")
    film_service.add_film(film2.getFilmId(),
                          film2.getTitlu(),
                          film2.getAn(),
                          film2.getPret(),
                          film2.getProgram())
    assert len(repoFilm.getAll()) == 2
    film_service.remove_film(2)
    assert len(repoFilm.getAll()) == 1
    repoFilm.eraseFile()
remove_film_test()


def update_film_test():
    repoFilm = RepositoryFilm("filmTests.txt")
    film_service = FilmService(repoFilm, "")
    repoFilm.eraseFile()
    film = Film(1, "film1", 2019, 20, "da")
    film_service.add_film(film.getFilmId(),
                          film.getTitlu(),
                          film.getAn(),
                          film.getPret(),
                          film.getProgram())
    assert film.getTitlu() == "film1"
    film_service.update_film(1, 1, "film2", 2019, 20, "da")
    assert film.getTitlu() == "film2"
    repoFilm.eraseFile()
update_film_test()


def add_card_test():
    repoCard = RepositoryCard("cardTests.txt")
    card_service = CardService(repoCard)
    assert len(repoCard.getAll()) == 0
    card = Card(1, "Tanasa", "Monica", 6000923271718, "2019.12.11", "12.12.2018", 10)
    card_service.add_card(card.getCardId(),
                          card.getName(),
                          card.getFirstName(),
                          card.getCNP(),
                          card.getDateB(),
                          card.getDateR(),
                          card.getPuncte())
    assert len(repoCard.getAll()) == 1
    repoCard.eraseFile()
add_card_test()


def remove_card_test():
    repoCard = RepositoryCard("cardTests.txt")
    card_service = CardService(repoCard)
    repoCard.eraseFile()
    card = Card(1, "Tanasa", "Monica", 6000923271718, "2010.12.12", "12.12.2018", 100)
    card_service.add_card(card.getCardId(),
                          card.getName(),
                          card.getFirstName(),
                          card.getCNP(),
                          card.getDateB(),
                          card.getDateR(),
                          card.getPuncte())
    assert len(repoCard.getAll()) == 1
    card2 = Card(2, "Tanasa", "Sorina", 6000923271719, "2000.10.10", "13.12.2018", 50)
    card_service.add_card(card2.getCardId(),
                          card2.getName(),
                          card2.getFirstName(),
                          card2.getCNP(),
                          card2.getDateB(),
                          card2.getDateR(),
                          card.getPuncte())
    assert len(repoCard.getAll()) == 2
    card_service.remove_card(card.getCardId())
    assert len(repoCard.getAll()) == 1
    repoCard.eraseFile()
remove_card_test()


def update_card_test():
    repoCard = RepositoryCard("cardTests.txt")
    card_service = CardService(repoCard)
    card = Card(1, "Tanasa", "Monica", 6000923271718, "2000.10.10", "12.12.2018", 60)
    card_service.add_card(card.getCardId(),
                          card.getName(),
                          card.getFirstName(),
                          card.getCNP(),
                          card.getDateB(),
                          card.getDateR(),
                          card.getPuncte())
    assert len(repoCard.getAll()) == 1
    card_service.update_card(1, "", "", "Andreea", "", "", "", "")
    assert card.getFirstName() == "Andreea"
    repoCard.eraseFile()
update_card_test()


def add_rezervare_test():
    repoRez = RepositoryRezervare("rezervareTests.txt")
    repoFilm = RepositoryFilm("filmTests.txt")
    film_service = FilmService(repoFilm, "")
    rez_service = RezervareService(repoRez, film_service)
    assert len(repoRez.getAll()) == 0
    rez = Rezervare(1, 1, 1, "2019.10.10", "13:30")
    rez_service.add_rezervare(rez.getId(),
                              rez.getIdFilm(),
                              rez.getIdCard(),
                              rez.getDate(),
                              rez.getHour())
    assert len(repoRez.getAll()) == 1
    repoRez.eraseFile()
add_rezervare_test()


def remove_rezervare_test():
    repoRez = RepositoryRezervare("rezervareTests.txt")
    repoFilm = RepositoryFilm("filmTests.txt")
    film_service = FilmService(repoFilm, "")
    rez_service = RezervareService(repoRez, film_service)
    repoRez.eraseFile()
    assert len(repoRez.getAll()) == 0
    rez = Rezervare(1, 1, 1, "2019.10.10", "10:00")
    rez_service.add_rezervare(rez.getId(),
                              rez.getIdFilm(),
                              rez.getIdCard(),
                              rez.getDate(),
                              rez.getHour())
    assert len(repoRez.getAll()) == 1
    rez2 = Rezervare(2, 2, 2, "2019.10.11", "14:00")
    rez_service.add_rezervare(rez2.getId(),
                              rez2.getIdFilm(),
                              rez2.getIdCard(),
                              rez2.getDate(),
                              rez2.getHour())
    assert len(repoRez.getAll()) == 2
    rez_service.remove_rezervare(rez.getId())
    assert len(repoRez.getAll()) == 1
    repoRez.eraseFile()
remove_rezervare_test()

def update_rezervare_test():
    repoRez = RepositoryRezervare("rezervareTests.txt")
    repoFilm = RepositoryFilm("filmTests.txt")
    film_service = FilmService(repoFilm, "")
    rez_service = RezervareService(repoRez, film_service)
    assert len(repoRez.getAll()) == 0
    rez = Rezervare(1, 1, 1, "2010.10.10", "13:00")
    rez_service.add_rezervare(rez.getId(),
                              rez.getIdFilm(),
                              rez.getIdCard(),
                              rez.getDate(),
                              rez.getHour())
    assert len(repoRez.getAll()) == 1
    rez_service.update_rezervare(1, 1, 2, 1, "2010.10.10", "12:00")
    assert rez.getIdFilm() == 2
    repoRez.eraseFile()
update_rezervare_test()