from Domain.cheltuiala import creeazaCheltuiala, getId, getNrAp, getData


def adaugaCheltuiala(id, nrAp, suma, data, tip, lista):
    '''
    Adauga o cheltuiala intr o lista
    :param id: string
    :param nrAp: int
    :param suma: float
    :param data: string
    :param tip: string
    :param lista: lista de cheltuieli
    :return: o lista continand elem vechi si noua cheltuiala
    '''
    cheltuiala = creeazaCheltuiala(id, nrAp, suma, data, tip)
    return lista + [cheltuiala]

def getById(id, lista):
    '''
    Da cheltuiala cu id-ul dat dintr o lista
    :param id: string
    :param lista: lista de cheltuieli
    :return: cheltuiala cu ID-UL dat din lista sau None, daca nu exista
    '''
    for cheltuiala in lista:
        if getId(cheltuiala) == id:
            return cheltuiala
    return None

def stergereCheltuialaById(id, lista):
    '''
    Sterge o cheltuiala dupa id
    :param id: string
    :param lista: lista de cheltuieli
    :return:
    '''
    return [cheltuiala for cheltuiala in lista if getId(cheltuiala) != id]

def getByNrAp(nrAp, lista):
    '''
    Da cheltuiala cu nr apartamentului dintr o lista
    :param nrAp: int
    :param lista: lista de cheltuieli
    :return: cheltuiala cu nr apartamentului(nrAp) dat din lista sau None, daca nu exista
    '''
    for cheltuiala in lista:
        if getNrAp(cheltuiala) == nrAp:
            return cheltuiala
    return None

def stergereCheltuialaByNrAp(nrAp, lista):
    '''
    Sterge o cheltuiala dupa numarul apartamentului(nrAp)
    :param nrAp: int
    :param lista: lista de cheltuieli
    :return:
    '''
    return [cheltuiala for cheltuiala in lista if getNrAp(cheltuiala) != nrAp]


def modificaCheltuiala(id, nrAp, suma, data, tip, lista):
    '''
    Modifica cheltuiala dupa id
    :param id: string
    :param nrAp: int
    :param suma: float
    :param data: string
    :param tip: string
    :param lista: lista de cheltuieli
    :return: modifica o lista identificata dupa id
    '''
    listaNoua = []
    for cheltuiala in lista:
        if getId(cheltuiala) == id:
            cheltuialaNoua = creeazaCheltuiala(id, nrAp, suma, data, tip)
            listaNoua.append(cheltuialaNoua)
        else:
            listaNoua.append(cheltuiala)
    return listaNoua