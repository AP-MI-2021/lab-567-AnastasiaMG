from Logic.CRUD import adaugaCheltuiala, getById
from UI.console import undo, redo


def testUndoRedo():

# 1. lista initiala goala
    lista = []
    undoList = []
    redoList = []

#2. adaugam un obiect
    lista = adaugaCheltuiala("1", 12, 1200, "28.07.2021", "canal", lista, undoList, redoList)

#3. adaugam inca un obiect
    lista = adaugaCheltuiala("2", 15, 4500, "15.08.2020", "intretinere", lista, undoList, redoList)

#4. adaugam inca un obiect
    lista = adaugaCheltuiala("3", 12, 3200, "28.07.2021", "canal", lista, undoList, redoList)

#5. undo scoate ultimul obiect adaugat
    if len(undoList) > 0:
        lista = undo(lista, undoList, redoList)
    assert len(lista) == 2
    assert getById("1", lista) is not None
    assert getById("2", lista) is not None
    assert getById("3", lista) is None

#6. inca un undo scoate penultimul obiect adaugat
    if len(undoList) > 0:
        lista = undo(lista, undoList, redoList)
    assert len(lista) == 1
    assert getById("1", lista) is not None
    assert getById("2", lista) is None
    assert getById("3", lista) is None

#7. inca un undo scoate si primul element adaugat
    if len(undoList) > 0:
        lista = undo(lista, undoList, redoList)
    assert len(lista) == 0
    assert getById("1", lista) is None
    assert getById("2", lista) is None
    assert getById("3", lista) is None

#8. inca un undo nu face nimic
    if len(undoList) > 0:
        lista = undo(lista, undoList, redoList)
    assert len(lista) == 0
    assert getById("1", lista) is None
    assert getById("2", lista) is None
    assert getById("3", lista) is None

#9. adaugam trei obiecte
    lista = adaugaCheltuiala("1", 65, 8900, "15.08.2020", "intretinere", lista, undoList, redoList)
    lista = adaugaCheltuiala("2", 12, 2500, "28.07.2021", "canal", lista, undoList, redoList)
    lista = adaugaCheltuiala("3", 12, 9000, "15.08.2020", "intretinere", lista, undoList, redoList)

#10. redo nu face nimic
    if len(redoList) > 0:
        lista = redo(lista, undoList, redoList)
    assert len(lista) == 3
    assert getById("1", lista) is not None
    assert getById("2", lista) is not None
    assert getById("3", lista) is not None

#11. doua undo-uri scot ultimele 2 obiecte
    if len(undoList) > 0:
        lista = undo(lista, undoList, redoList)
    if len(undoList) > 0:
        lista = undo(lista, undoList, redoList)
    assert len(lista) == 1
    assert getById("1", lista) is not None
    assert getById("2", lista) is None
    assert getById("3", lista) is None

#12. redo anuleaza ultimul undo, daca ultima operatie e undo
    if len(redoList) > 0:
        lista = redo(lista, undoList, redoList)
    assert len(lista) == 2
    assert getById("1", lista) is not None
    assert getById("2", lista) is not None
    assert getById("3", lista) is None

#13. redo anuleaza si primul undo
    if len(redoList) > 0:
        lista = redo(lista, undoList, redoList)
    assert len(lista) == 3
    assert getById("1", lista) is not None
    assert getById("2", lista) is not None
    assert getById("3", lista) is not None
#14. doua undo-uri scot ultimele 2 obiecte
    if len(undoList) > 0:
        lista = undo(lista, undoList, redoList)
    if len(undoList) > 0:
        lista = undo(lista, undoList, redoList)
    assert len(lista) == 1
    assert getById("1", lista) is not None
    assert getById("2", lista) is None
    assert getById("3", lista) is None

#15. adaugam un obiect
    lista = adaugaCheltuiala("4", 29, 1000, "28.07.2021", "canal", lista, undoList, redoList)

#16. redo nu face nimic, deoarece ultima operatie nu este un undo
    if len(redoList) > 0:
        lista = redo(lista, undoList, redoList)
    assert len(lista) == 2
    assert getById("1", lista) is not None
    assert getById("4", lista) is not None

#17. undo anuleaza adaugarea lui o4
    if len(undoList) > 0:
        lista = undo(lista, undoList, redoList)
    assert len(lista) == 1
    assert getById("1", lista) is not None
    assert getById("4", lista) is None

#18. undo anuleaza adaugarea lui o1 - practic se continua sirul de undo de la pct 14
    if len(undoList) > 0:
        lista = undo(lista, undoList, redoList)
    assert len(lista) == 0
    assert getById("1", lista) is None

#19. se anuleaza ultimele 2 undo-uri
    if len(redoList) > 0:
        lista = redo(lista, undoList, redoList)
    if len(redoList) > 0:
        lista = redo(lista, undoList, redoList)
    assert len(lista) == 2
    assert getById("1", lista) is not None
    assert getById("4", lista) is not None

#20. redo nu face nimic
    if len(redoList) > 0:
        lista = redo(lista, undoList, redoList)
    assert len(lista) == 2
    assert getById("1", lista) is not None
    assert getById("4", lista) is not None
