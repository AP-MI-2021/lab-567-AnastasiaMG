from Domain.cheltuiala import getNrAp, getSuma, getData, getTip, getId
from Logic.CRUD import adaugaCheltuiala, getById, stergereCheltuialaById, stergereCheltuialaByNrAp, getByNrAp


def testAdaugaCheltuiala():
    lista = []
    undoList = []
    redoList = []
    lista = adaugaCheltuiala("1", 12, 120000, "28.07.2021", "blabla", lista, undoList, redoList)

    assert len(lista) == 1
    assert getId(getById("1", lista)) == "1"
    assert getNrAp(getById("1", lista)) == 12
    assert getSuma(getById("1", lista)) == 120000
    assert getData(getById("1", lista)) == "28.07.2021"
    assert getTip(getById("1", lista)) == "blabla"

def testStergeCheltuialaById():
    lista = []
    undoList = []
    redoList = []
    lista = adaugaCheltuiala("1", 2, 240000, "28.0.,2021", "blabla", lista, undoList, redoList)
    lista = adaugaCheltuiala("2", 3, 650000, "28.07.2021", "blabla", lista, undoList, redoList)

    lista = stergereCheltuialaById("1", lista, undoList, redoList)

    assert len(lista) == 1
    assert getById("1", lista) is None
    assert getById("2", lista) is not None

    try:
        lista = stergereCheltuialaById("3", lista, undoList, redoList)
        assert False
    except ValueError:
        assert len(lista) == 1
        assert getById("2", lista) is not None
    except Exception:
        assert False

def testStergeCheltuialaByNrAp():
    lista = []
    undoList = []
    redoList = []
    lista = adaugaCheltuiala("1", 2, 240000, "28.07.2021", "blabla", lista, undoList, redoList)
    lista = adaugaCheltuiala("2", 3, 650000, "28.07.2021", "blabla", lista, undoList, redoList)
    lista = adaugaCheltuiala("3", 2, 720000, "28.07.2021", "blabla", lista, undoList, redoList)

    lista = stergereCheltuialaByNrAp(2, lista, undoList, redoList)

    assert len(lista) == 1
    assert getByNrAp(2, lista) is None
    assert getByNrAp(3, lista) is not None

    try:
        lista = stergereCheltuialaByNrAp(1, lista, undoList, redoList)
        assert False
    except ValueError:
        assert len(lista) == 1
        assert getByNrAp(3, lista) is not None
    except Exception:
        assert False