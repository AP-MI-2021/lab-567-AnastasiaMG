from Tests.testCRUD import testAdaugaCheltuiala, testStergeCheltuialaById, testStergeCheltuialaByNrAp
from Tests.testDomain import testCheltuiala
from Tests.testFunctionalitati import testAddValToCheltuialaByDate, testSumMaxByTip, testOrdonareDupaSuma


def runAllTests():
    testCheltuiala()
    testAdaugaCheltuiala()
    testStergeCheltuialaById()
    testStergeCheltuialaByNrAp()
    testAddValToCheltuialaByDate()
    testSumMaxByTip()
    #testOrdonareDupaSuma()