from Domain.cheltuiala import creeazaCheltuiala, getNrAp, getSuma, getData, getTip, getId


def testCheltuiala():
    cheltuiala = creeazaCheltuiala(1, 12, 120000, "28.07,2021", "blabla")

    assert getId(cheltuiala) == 1
    assert getNrAp(cheltuiala) == 12
    assert getSuma(cheltuiala) == 120000
    assert getData(cheltuiala) == "28.07,2021"
    assert getTip(cheltuiala) == "blabla"
