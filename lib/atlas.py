#!/usr/bin/env python3
#lib/atlas.py
from helpers import *
from os import system
    
def main():
    check_database()
    intro()
    while True:
        top_menu()
        choice = input("=> ")
        if choice == "0":
            exit_program()
        elif choice == "1":
            browse(Star)
        elif choice == "2":
            browse(Planet)
        elif choice == "3":
            browse(Species)
        elif choice == "4":
            browse(Civilization)
        else:
            print("Incorrect choice, please try again.")


def top_menu():
    system('clear')
    scan_print(
        """
Please select an option:
_________________________________________________
0. Exit the Atlas
1. Browse Stars
2. Browse Planets
3. Browse Species
4. Browse Civilizations""",0.01
    )

def browse(name):
    """Primary sub-menu for browsing entities individually or by type"""
    while True:
        system('clear')
        scan_print(f"""
<>  {name.__name__} | Please select an option:
    _________________________________________________
    0. Back to main menu
    1. List {name.__name__}s
    2. Find {name.__name__}s by Type
    3. Create {name.__name__}""",0.01)
        choice = input("> ")
        if choice == "0":
            return
        elif choice == "1":
            pick_item(name)
        elif choice == "2":
            list_options(name.types,f'{name.__name__} Type')
            choice = input("=> ")
            if choice != "0":
                pick_item(name,name.types[int(choice)-1])
        elif choice == "3":
            system('clear')
            scan_print(f"""Creating a new {name.__name__}
                       _________________________________________________
                       """)
            if name == Star:
                create_star()
            elif name == Planet:
                create_planet()
            elif name == Species:
                create_species()
            elif name == Civilization:
                create_civilization()
            else:
                print("Something went wrong.")
                return


if __name__ == "__main__":
    main()
