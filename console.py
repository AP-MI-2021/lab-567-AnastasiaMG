from Domain.cheltuiala import toString, getId, getNrAp, getData, getTip, getSuma
from Logic.CRUD import adaugaCheltuiala, modificaCheltuiala, stergereCheltuialaById, stergereCheltuialaByNrAp
from Logic.functionalitate import addValToCheltuialaByDate, sumMaxByTip, ordonareDupaSuma, sumeLunarePerApartament


def printMenu():
    print("1. Adaugare cheltuiala")
    print("2. Stergere cheltuiala dupa Id")
    print("3. Modificare cheltuiala")
    print("4. Stergere cheltuiala dupa numarul apartamentului")
    print("5. Adauga o suma la o cheltuiala dupa data")
    print("6. Cea mai mare suma dupa tipul cheltuielii")
    print("7. Ordoneaza lista descrescator dupa suma")
    print("8. Afiseaza sumele lunare pentru fiecare apartament")
    print("u. Undo")
    print("r. Redo")
    print("a. Afisare cheltuiala")
    print("x. Iesire")


def uiAdaugaCheltuiala(lista, undoList, redoList):
    try:
        id = input("Dati ID: ")
        nrAp = int(input("Dati numarul apartamentului: "))
        suma = float(input("Dati suma: "))
        data = input("Dati data in format (dd.mm.yyyy): ")
        tip = input("Dati tipul cheltuielii (intretinere/canal/alte cheltuieli): ")

        if len(data) != 10 or (data[2] != "." or data[5] != "."):
             data = input("Ati gresit format data! Reincercati in format (dd.mm.yyyy): ")
        elif int(data[0] + data[1]) > 31 or int(data[3] + data[4]) > 12:
             data = input("Data imposibila! Introduceti o data valida in format (dd.mm.yyyy): ")
        if tip != "intretinere":
            if tip != "canal":
                if tip != "alte cheltuieli":
                    tip = input("Reincercati tip de ap!: ")
        if suma < 0:
            suma = float(input("Dati o suma mai mare ca 0: "))
        if nrAp <= 0:
            nrAp = int(input("Dati un nr de apartament valid: "))

        rezultat = adaugaCheltuiala(id, nrAp, suma, data, tip, lista, undoList, redoList)
        undoList.append(lista)
        redoList.clear()
        return rezultat
    except ValueError as ve:
        print("Eroare!: {}".format(ve))
        return lista

def uiStergeCheltuialaById(lista, undoList, redoList):
    try:
        id = input("Dati ID-ul cheltuielii de sters: ")
        rezultat = stergereCheltuialaById(id, lista)
        undoList.append(lista)
        redoList.clear()
        return rezultat
    except ValueError as ve:
        print("Eroare!: {}".format(ve))
        return lista

def uiStergeCheltuialaByNrAp(lista, undoList, redoList):
    try:
        nrAp = int(input("Dati numarul apartamentului al cheltuielii de sters: "))
        if nrAp <= 0:
            nrAp = int(input("Dati un nr de apartament valid: "))
        rezultat = stergereCheltuialaByNrAp(nrAp, lista, undoList, redoList)
        undoList.append(lista)
        redoList.clear()
        return rezultat
    except ValueError as ve:
        print("Eroare!: {}".format(ve))
        return lista


def uiModificaCheltuiala(lista, undoList, redoList):
    try:
        id = input("Dati ID-ul cheltuielii de modificat: ")
        nrAp = int(input("Introduceti noul numar de apartament: "))
        suma = float(input("Dati noua suma: "))
        data = input("Dati noua data in format (dd.mm.yyyy): ")
        tip = input("Dati tipul nou: ")
        if len(data) != 10 or (data[2] != "." or data[5] != "."):
             data = input("Ati gresit format data! Reincercati in format (dd.mm.yyyy): ")
        elif int(data[0] + data[1]) > 31 or int(data[3] + data[4]) > 12:
             data = input("Data imposibila! Introduceti o data valida in format (dd.mm.yyyy): ")
        if tip != "intretinere":
            if tip != "canal":
                if tip != "alte cheltuieli":
                    tip = input("Reincercati tip de ap!: ")
        if suma < 0:
            suma = float(input("Dati o suma mai mare ca 0: "))
        if nrAp <= 0:
            nrAp = int(input("Dati un nr de apartament valid: "))
        rezultat = modificaCheltuiala(id, nrAp, suma, data, tip, lista)
        undoList.append(lista)
        redoList.clear()
        return rezultat
    except ValueError as ve:
        print("Eroare!: {}".format(ve))
        return lista

def uiAddValToCheltuialaByDate(lista):
    try:
        dataNoua = input("Dati data la care doriti sa adaugati o suma in format (dd.mm.yyyy): ")
        addSum = float(input("Dati suma pe care doriti sa o adaugati: "))
        if len(dataNoua) != 10 or (dataNoua[2] != "." or dataNoua[5] != "."):
            dataNoua = input("Ati gresit format data! Reincercati in format (dd.mm.yyyy): ")
        elif int(dataNoua[0] + dataNoua[1]) > 31 or int(dataNoua[3] + dataNoua[4]) > 12:
            dataNoua = input("Data imposibila! Introduceti o data valida in format (dd.mm.yyyy): ")
        if addSum < 0:
            addSum = float(input("Dati o suma mai mare ca 0: "))
        return addValToCheltuialaByDate(dataNoua, addSum, lista)
    except ValueError as ve:
        print("Eroare!: {}".format(ve))
        return lista

def showAll(lista):
    for cheltuiala in lista:
        print(toString(cheltuiala))


def uiSumMaxByTip(lista):
    rezultat = sumMaxByTip(lista)
    for tip in rezultat:
        print("Tipul {} are suma maxima: {}".format(tip, rezultat[tip]))


def uiOrdonareDupaSuma(lista):
    showAll(ordonareDupaSuma(lista))


def uiSumeLunarePerApartament(lista):
    rezultat = sumeLunarePerApartament(lista)
    for nrAp in rezultat:
        print("Apartamentul {} in luna {} are suma de {}".format(nrAp, rezultat[nrAp]['luna'], rezultat[nrAp]['suma']))


def undo(lista, undoList, redoList):
    if len(undoList) > 0:
        redoList.append(lista)
        lista = undoList.pop()
    else:
        print("Nu se poate face undo.")
    return lista

def redo(lista, undoList, redoList):
    if len(redoList) > 0:
        undoList.append(lista)
        lista = redoList.pop()
    else:
        print("Nu se poate face redo.")
    return lista

def runMenu(lista):
    undoList = []
    redoList = []
    lista = []
    while True:
        printMenu()
        optiune = input("Dati optiune: ")

        if optiune == "1":
            lista = uiAdaugaCheltuiala(lista, undoList, redoList)
        elif optiune == "2":
            lista = uiStergeCheltuialaById(lista, undoList, redoList)
        elif optiune == "3":
            lista = uiModificaCheltuiala(lista, undoList, redoList)
        elif optiune == "4":
            lista = uiStergeCheltuialaByNrAp(lista, undoList, redoList)
        elif optiune == "5":
            lista = uiAddValToCheltuialaByDate(lista)
        elif optiune == "6":
            lista = uiSumMaxByTip(lista)
        elif optiune == "7":
            lista = uiOrdonareDupaSuma(lista)
        elif optiune == "8":
            lista = uiSumeLunarePerApartament(lista)
        elif optiune == "u":
            lista = undo(lista, undoList, redoList)
        elif optiune == "r":
            lista = redo(lista, undoList, redoList)
        elif optiune == "a":
            showAll(lista)
        elif optiune == "x":
            break
        else:
            print("Optiune gresita.")