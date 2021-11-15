from Domain.cheltuiala import toString, getId, getNrAp, getData, getTip, getSuma
from Logic.CRUD import adaugaCheltuiala, modificaCheltuiala, stergereCheltuialaById, stergereCheltuialaByNrAp
from Logic.functionalitate import addValToCheltuialaByDate, sumMaxByTip, ordonareDupaSuma


def printMenu():
    print("1. Adaugare cheltuiala")
    print("2. Stergere cheltuiala dupa Id")
    print("3. Modificare cheltuiala")
    print("4. Stergere cheltuiala dupa numarul apartamentului")
    print("5. Adauga o suma la o cheltuiala dupa data")
    print("6. Cea mai mare suma dupa tipul cheltuielii")
    print("7. Ordoneaza lista descrescator dupa suma")
    print("a. Afisare cheltuiala")
    print("x. Iesire")


def uiAdaugaCheltuiala(lista):
    id = input("Dati ID: ")
    nrAp = int(input("Dati numarul apartamentului: "))
    suma = float(input("Dati suma: "))
    data = input("Dati data in format (dd.mm.yyyy): ")

    if len(data) != 10 or (data[2] != "." or data[5] != "."):
        data = input("Ati gresit format data! Reincercati in format (dd.mm.yyyy): ")
    elif int(data[0] + data[1]) > 31 or int(data[3] + data[4]) > 12:
        data = input("Data imposibila! Introduceti o data valida in format (dd.mm.yyyy): ")

    tip = input("Dati tipul cheltuielii (intretinere/canal/alte cheltuieli): ")

    if tip != "intretinere":
        if tip != "canal":
            if tip != "alte cheltuieli":
                tip = input("Reincercati tip de ap!: ")


    return adaugaCheltuiala(id, nrAp, suma, data, tip, lista)


def uiStergeCheltuialaById(lista):
    id = input("Dati ID-ul cheltuielii de sters: ")

    return stergereCheltuialaById(id, lista)

def uiStergeCheltuialaByNrAp(lista):
    nrAp = int(input("Dati numarul apartamentului al cheltuielii de sters: "))

    return stergereCheltuialaByNrAp(nrAp, lista)


def uiModificaCheltuiala(lista):
    id = input("Dati ID-ul cheltuielii de modificat: ")
    nrAp = int(input("Introduceti noul numar de apartament: "))
    suma = float(input("Dati noua suma: "))
    data = input("Dati noua data in format (dd.mm.yyyy): ")
    tip = input("Dati tipul nou: ")

    return modificaCheltuiala(id, nrAp, suma, data, tip, lista)

def uiAddValToCheltuialaByDate(lista):
    dataNoua = input("Dati data la care doriti sa adaugati o suma in format (dd.mm.yyyy): ")
    addSum = float(input("Dati suma pe care doriti sa o adaugati: "))

    return addValToCheltuialaByDate(dataNoua, addSum, lista)

def showAll(lista):
    for cheltuiala in lista:
        print(toString(cheltuiala))


def uiSumMaxByTip(lista):
    rezultat = sumMaxByTip(lista)
    for tip in rezultat:
        print("Tipul {} are suma maxima: {}".format(tip, rezultat[tip]))


def uiOrdonareDupaSuma(lista):
    return ordonareDupaSuma


def runMenu(lista):
    while True:
        printMenu()
        optiune = input("Dati optiune: ")

        if optiune == "1":
            lista = uiAdaugaCheltuiala(lista)
        elif optiune == "2":
            lista = uiStergeCheltuialaById(lista)
        elif optiune == "3":
            lista = uiModificaCheltuiala(lista)
        elif optiune == "4":
            lista = uiStergeCheltuialaByNrAp(lista)
        elif optiune == "5":
            lista = uiAddValToCheltuialaByDate(lista)
        elif optiune == "6":
            lista = uiSumMaxByTip(lista)
        elif optiune == "7":
            lista = uiOrdonareDupaSuma(lista)
        elif optiune == "a":
            showAll(lista)
        elif optiune == "x":
            break
        else:
            print("Optiune gresita.")