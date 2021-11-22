from Tests.testAll import runAllTests
from UI.console import runMenu
from UI.newConsole import runNewMenu


def menu():
    print("1. Meniu vechi")
    print("2. Meniu nou")
    print("x. Exit")

def main():
    runAllTests()
    while True:
        menu()
        optiune = input("Dati optiune meniu: ")

        if optiune == "1":
            runMenu([])
        elif optiune == "2":
            runNewMenu([])
        elif optiune == "x":
            break
        else:
            print("Ati gresit optiunea!")
main()