from Domain.cheltuiala import getNrAp, getSuma, getData, getTip, getId
from Logic.CRUD import adaugaCheltuiala, getById, stergereCheltuialaById, stergereCheltuialaByNrAp, getByNrAp


def testAdaugaCheltuiala():
    lista = []
    lista = adaugaCheltuiala("1", 12, 120000, "28.07.2021", "blabla", lista)

    assert len(lista) == 1
    assert getId(getById("1", lista)) == "1"
    assert getNrAp(getById("1", lista)) == 12
    assert getSuma(getById("1", lista)) == 120000
    assert getData(getById("1", lista)) == "28.07.2021"
    assert getTip(getById("1", lista)) == "blabla"

def testStergeCheltuialaById():
    lista = []
    lista = adaugaCheltuiala("1", 2, 240000, "28.0.,2021", "blabla", lista)
    lista = adaugaCheltuiala("2", 3, 650000, "28.07.2021", "blabla", lista)

    lista = stergereCheltuialaById("1", lista)

    assert len(lista) == 1
    assert getById("1", lista) is None
    assert getById("2", lista) is not None

    lista = stergereCheltuialaById("3", lista)

    assert len(lista) == 1
    assert getById("2", lista) is not None

def testStergeCheltuialaByNrAp():
    lista = []
    lista = adaugaCheltuiala("1", 2, 240000, "28.07.2021", "blabla", lista)
    lista = adaugaCheltuiala("2", 3, 650000, "28.07.2021", "blabla", lista)
    lista = adaugaCheltuiala("3", 2, 720000, "28.07.2021", "blabla", lista)

    lista = stergereCheltuialaByNrAp(2, lista)

    assert len(lista) == 1
    assert getByNrAp(2, lista) is None
    assert getByNrAp(3, lista) is not None

    lista = stergereCheltuialaByNrAp(1, lista)

    assert len(lista) == 1
    assert getByNrAp(3, lista) is not None