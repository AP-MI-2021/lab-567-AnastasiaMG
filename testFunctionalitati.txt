from Domain.cheltuiala import getSuma, getId
from Logic.CRUD import adaugaCheltuiala, getById
from Logic.functionalitate import addValToCheltuialaByDate, sumMaxByTip, ordonareDupaSuma, sumeLunarePerApartament


def testAddValToCheltuialaByDate():
    lista = []
    undoList = []
    redoList = []
    lista = adaugaCheltuiala("1", 12, 1200, "28.07.2021", "canal", lista, undoList, redoList)
    lista = adaugaCheltuiala("2", 15, 4500, "15.08.2020", "canal", lista, undoList, redoList)
    lista = adaugaCheltuiala("3", 20, 3200, "28.07.2021", "canal", lista, undoList, redoList)

    rezultat = addValToCheltuialaByDate("28.07.2002", 1000, lista)

    assert len(rezultat) == 3
    assert getSuma(getById("1", lista)) == 1200
    assert getSuma(getById("2", lista)) == 4500
    assert getSuma(getById("3", lista)) == 3200

def testSumMaxByTip():
    lista = []
    undoList = []
    redoList = []
    lista = adaugaCheltuiala("1", 12, 1200, "28.07.2021", "canal", lista, undoList, redoList)
    lista = adaugaCheltuiala("2", 15, 4500, "15.08.2020", "intretinere", lista, undoList, redoList)
    lista = adaugaCheltuiala("3", 20, 3200, "28.07.2021", "canal", lista, undoList, redoList)

    rezultat = sumMaxByTip(lista)

    assert len(rezultat) == 2
    assert rezultat["canal"] == 3200
    assert rezultat["intretinere"] == 4500

def testOrdonareDupaSuma():
    lista = []
    undoList = []
    redoList = []
    lista = adaugaCheltuiala("1", 12, 1200, "28.07.2021", "canal", lista, undoList, redoList)
    lista = adaugaCheltuiala("2", 15, 4500, "15.08.2020", "intretinere", lista, undoList, redoList)
    lista = adaugaCheltuiala("3", 20, 3200, "28.07.2021", "canal", lista, undoList, redoList)
    lista = adaugaCheltuiala("4", 65, 8900, "15.08.2020", "intretinere", lista, undoList, redoList)
    lista = adaugaCheltuiala("5", 29, 2500, "28.07.2021", "canal", lista, undoList, redoList)

    rezultat = ordonareDupaSuma(lista)

    assert getId(rezultat[0]) == "4"
    assert getId(rezultat[1]) == "2"
    assert getId(rezultat[2]) == "3"
    assert getId(rezultat[3]) == "5"
    assert getId(rezultat[4]) == "1"

def testSumeLunarePerApartament():
    lista = []
    undoList = []
    redoList = []
    lista = adaugaCheltuiala("1", 12, 1200, "28.07.2021", "canal", lista, undoList, redoList)
    lista = adaugaCheltuiala("2", 15, 4500, "15.08.2020", "intretinere", lista, undoList, redoList)
    lista = adaugaCheltuiala("3", 12, 3200, "28.07.2021", "canal", lista, undoList, redoList)

    rezultat = sumeLunarePerApartament(lista)

    assert len(rezultat) == 2

