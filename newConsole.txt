from Domain.cheltuiala import toString
from Logic.CRUD import adaugaCheltuiala, stergereCheltuialaById, stergereCheltuialaByNrAp, modificaCheltuiala


def help():
    print("INSTRUCTIUNI:")
    print("Pentru a creea o cheltuiala tb sa adaugati id, nr apartament(nrAp), suma, data si tip")
    print("Id-ul, nrAp, suma, data si tip-ul vor fi separate prin ' , ' ")
    print("Comenzile/Operatiile vor fi separate prin ' ; ' ")
    print("add -> adauga o cheltuiala noua la lista")
    print("showall -> afiseaza toate cheltuielile din lista")
    print("delete -> sterge o cheltuiala din lista")
    print("exit -> iesire din meniu")


def add(id, nrAp, suma, data, tip, lista, undoList, redoList):
    try:
        lista = adaugaCheltuiala(id, nrAp, suma, data, tip, lista, undoList, redoList)
    except ValueError as ve:
        print("Eroare!: ", ve)
    return lista


def showall(lista):
    for cheltuiala in lista:
        print(toString(cheltuiala))


def delete(id, lista, undoList, redoList):
    try:
        lista = stergereCheltuialaById(id, lista, undoList, redoList)
    except ValueError as ve:
        print("Eroare!: ", ve)
    return lista


def deleteByNrAp(nrAp, lista, undoList, redoList):
    try:
        lista = stergereCheltuialaByNrAp(nrAp, lista, undoList, redoList)
    except ValueError as ve:
        print("Eroare!: ", ve)
    return lista


def modify(id, nrAp, suma, data, tip, lista, undoList, redoList):
    try:
        lista = modificaCheltuiala(id, nrAp, suma, data, tip, lista, undoList, redoList)
    except ValueError as ve:
        print("Eroare: ", ve)
    return lista


def runNewMenu(lista):
    undoList = []
    redoList = []
    instructiuni = input("Pentru instructiuni, tastati 'help': ")
    while True:
        if instructiuni == "help":
            help()
        comanda = input("Dati comenzile: ")
        optiuni = comanda.split(';')
        for comenzi in optiuni:
            optiune = comenzi.split(',')
            if optiune[0] == "add":
                id = optiune[1]
                nrAp = int(optiune[2])
                suma = float(optiune[3])
                data = optiune[4]
                tip = optiune[5]
                lista = add(id, nrAp, suma, data, tip, lista, undoList, redoList)
            elif optiune[0] == "showall":
                showall(lista)
            elif optiune[0] == "delete":
                id = optiune[1]
                lista = delete(id, lista, undoList, redoList)
            elif optiune[0] == "deleteByNrAp":
                nrAp = int(optiune[1])
                lista = deleteByNrAp(nrAp, lista, undoList, redoList)
            elif optiune[0] == 'modify':
                id = optiune[1]
                nrAp = int(optiune[2])
                suma = float(optiune[3])
                data = optiune[4]
                tip = optiune[5]
                lista = modify(id, nrAp, suma, data, tip, lista, undoList, redoList)
            elif optiune[0] == "exit":
                break
            else:
                print("Ati gresit!")
