from Tests.testCRUD import testAdaugaCheltuiala, testStergeCheltuialaById, testStergeCheltuialaByNrAp
from Tests.testDomain import testCheltuiala
from Tests.testFunctionalitati import testAddValToCheltuialaByDate, testSumMaxByTip, testOrdonareDupaSuma, \
    testSumeLunarePerApartament
from Tests.testUndoRedo import testUndoRedo


def runAllTests():
    testCheltuiala()
    testAdaugaCheltuiala()
    testStergeCheltuialaById()
    testStergeCheltuialaByNrAp()
    testAddValToCheltuialaByDate()
    testSumMaxByTip()
    testOrdonareDupaSuma()
    testSumeLunarePerApartament()
    testUndoRedo()