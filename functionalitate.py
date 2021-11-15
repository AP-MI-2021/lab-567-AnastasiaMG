from Domain.cheltuiala import creeazaCheltuiala, getId, getNrAp, getSuma, getData, getTip


def addValToCheltuialaByDate(dataNoua, addSum, lista):
    '''
    Adauga o valoare la o cheltuiala
    :param data: string
    :param addSum: float
    :param lista: lista de cheltuieli
    :return: lista cu suma modificata
    '''
    listaNoua = []
    for cheltuiala in lista:
        if getData(cheltuiala) == dataNoua:
            cheltuialaNoua = creeazaCheltuiala(
                getId(cheltuiala),
                getNrAp(cheltuiala),
                getSuma(cheltuiala) + addSum,
                getData(cheltuiala),
                getTip(cheltuiala)
            )
            listaNoua.append(cheltuialaNoua)
        else:
            listaNoua.append(cheltuiala)
    return listaNoua

def sumMaxByTip(lista):
    '''
    Determina cea mai mare suma pentru fiecare tip de cheltuiala
    :param lista: lista de cheltuieli
    :return: cea mai mare suma in functie de tipul de cheltuiala
    '''
    rezultat = {}
    for cheltuiala in lista:
        tip = getTip(cheltuiala)
        suma = getSuma(cheltuiala)
        if tip in rezultat:
            if suma > rezultat[tip]:
                rezultat[tip] = suma
        else:
            rezultat[tip] = suma
    return rezultat

def ordonareDupaSuma(lista):
    '''
    Ordoneaza lista descrescator dupa suma
    :param lista: lista de cheltuieli
    :return: lista ordonata descrescator
    '''
    sorted(lista, key=getSuma)
