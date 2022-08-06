import os

class MainUI():
    def __init__(self):
        self.PrintMainUI()

    def PrintMainUI(self):
        os.system('clear')
        print("Mats")
        print(20*"=")
        print()
        print("1. Schrauben")
        print("2. Platten")
        print("3. Holz")
        print("4. Chemie")
        print("5. Eisenzeug")
        print("0. Beenden")
        input("Auswahl")
        


def main():
    MainUI()

main()
