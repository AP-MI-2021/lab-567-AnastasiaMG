def creeazaCheltuiala(id, nrAp, suma, data, tip):
    '''
    Creeaza un dictionar ce reprezinta o cheltuiala
    :param id: string
    :param nrAp: int
    :param suma: float
    :param data: string
    :param tip: string
    :return: un dictionar ce contine o cheltuiala
    '''
    return{
        "id": id,
        "nrAp": nrAp,
        "suma": suma,
        "data": data,
        "tip": tip
    }

def getId(cheltuiala):
    '''
    Da id-ul unei cheltuieli
    :param cheltuiala: dictionar ce contine o cheltuiala
    :return: id-ul cheltuielii
    '''
    return cheltuiala["id"]

def getNrAp(cheltuiala):
    '''
    Da numarul de apartament unei cheltuieli
    :param cheltuiala: dictionar ce contine o cheltuiala
    :return: nr de ap al cheltuielii
    '''
    return cheltuiala["nrAp"]

def getSuma(cheltuiala):
    '''
    Da suma unei cheltuieli
    :param cheltuiala: dictionar ce contine o cheltuiala
    :return: suma cheltuielii
    '''
    return cheltuiala["suma"]

def getData(cheltuiala):
    '''
    Da data unei cheltuieli
    :param cheltuiala: dictionar ce contine o cheltuiala
    :return: data cheltuielii
    '''
    return cheltuiala["data"]

def getTip(cheltuiala):
    '''
    Da tipul unei cheltuieli
    :param cheltuiala: dictionar ce contine o cheltuiala
    :return: tipul cheltuielii
    '''
    return cheltuiala["tip"]

def toString(cheltuiala):
    return "id: {}, nrAp: {}, suma: {}, data: {}, tip: {}".format(
        getId(cheltuiala),
        getNrAp(cheltuiala),
        getSuma(cheltuiala),
        getData(cheltuiala),
        getTip(cheltuiala)
    )