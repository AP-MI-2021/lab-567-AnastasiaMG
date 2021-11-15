from Domain.cheltuiala import getSuma, getId
from Logic.CRUD import adaugaCheltuiala, getById
from Logic.functionalitate import addValToCheltuialaByDate, sumMaxByTip, ordonareDupaSuma


def testAddValToCheltuialaByDate():
    lista = []
    lista = adaugaCheltuiala("1", 12, 1200, "28.07.2021", "canal", lista)
    lista = adaugaCheltuiala("2", 15, 4500, "15.08.2020", "canal", lista)
    lista = adaugaCheltuiala("3", 20, 3200, "28.07.2021", "canal", lista)

    rezultat = addValToCheltuialaByDate("28.07.2002", 1000, lista)

    assert len(rezultat) == 3
    assert getSuma(getById("1", lista)) == 1200
    assert getSuma(getById("2", lista)) == 4500
    assert getSuma(getById("3", lista)) == 3200

def testSumMaxByTip():
    lista = []
    lista = adaugaCheltuiala("1", 12, 1200, "28.07.2021", "canal", lista)
    lista = adaugaCheltuiala("2", 15, 4500, "15.08.2020", "intretinere", lista)
    lista = adaugaCheltuiala("3", 20, 3200, "28.07.2021", "canal", lista)

    rezultat = sumMaxByTip(lista)

    assert len(rezultat) == 2
    assert rezultat["canal"] == 3200
    assert rezultat["intretinere"] == 4500

def testOrdonareDupaSuma():
    lista = []
    lista = adaugaCheltuiala("1", 12, 1200, "28.07.2021", "canal", lista)
    lista = adaugaCheltuiala("2", 15, 4500, "15.08.2020", "intretinere", lista)
    lista = adaugaCheltuiala("3", 20, 3200, "28.07.2021", "canal", lista)
    lista = adaugaCheltuiala("4", 65, 8900, "15.08.2020", "intretinere", lista)
    lista = adaugaCheltuiala("5", 29, 2500, "28.07.2021", "canal", lista)

    rezultat = ordonareDupaSuma(lista)

    assert getId(rezultat[0]) == "1"
    assert getId(rezultat[1]) == "5"
    assert getId(rezultat[2]) == "3"
    assert getId(rezultat[3]) == "2"
    assert getId(rezultat[4]) == "4"

