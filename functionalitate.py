from Domain.cheltuiala import creeazaCheltuiala, getId, getNrAp, getSuma, getData, getTip


def addValToCheltuialaByDate(dataNoua, addSum, lista):
    '''
    Adauga o valoare la o cheltuiala
    :param data: string
    :param addSum: float
    :param lista: lista de cheltuieli
    :return: lista cu suma modificata
    '''
    if addSum <= 0:
        raise ValueError("Suma ce tb adaugata nu trebuie sa fie nula sau negativa")

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

def suma(cheltuiala):
    return getSuma(cheltuiala)

def ordonareDupaSuma(lista):
    '''
    Ordoneaza lista descrescator dupa suma
    :param lista: lista de cheltuieli
    :return: lista ordonata descrescator
    '''

    return sorted(lista, key=suma, reverse = True)

def sumeLunarePerApartament(lista):
    '''

    :param lista:
    :return:
    '''
    rezultat = {}
    for cheltuiala in lista:
        nrAp = getNrAp(cheltuiala)
        suma = getSuma(cheltuiala)
        data = getData(cheltuiala)
        luna = data[3] + data[4]
        if nrAp in rezultat:
            if luna in rezultat[nrAp]['luna']:
                rezultat[nrAp]['suma'] = rezultat[nrAp]['suma'] + suma
            else:
                rezultat[nrAp]['luna'] = luna
                rezultat[nrAp]['suma'] = suma
        else:
            rezultat[nrAp] = {}
            rezultat[nrAp]['luna'] = luna
            rezultat[nrAp]['suma'] = suma
    return rezultat


