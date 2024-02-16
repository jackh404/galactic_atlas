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


        







    
def stars_menu():
    while True:
        system('clear')
        scan_print(
            """> Stars | Please select an option:
    _________________________________________________
    0. Back to main menu
    1. List Stars
    3. Find Stars by Type
    4. Create Star""",0.01
        )
        choice = input("> ")
        if choice == "0":
            return
        elif choice == "1":
            list_options(Star,"Star")
        elif choice == "2":
            find_star_by_id()
        elif choice == "3":
            find_star_by_type()
        elif choice == "4":
            create_star()
        elif choice == "5":
            update_star()
        elif choice == "6":
            delete_star()
            
def planet_menu():
    while True:
        system('clear')
        scan_print(
            """> Planets | Please select an option:
    _________________________________________________
    0. Back to main menu
    1. List Planets
    2. Find Planet by ID
    3. Find Planet by Type
    4. Create Planet
    5. Update Planet
    6. Delete Planet""",0.01
        )
        choice = input("> ")
        if choice == "0":
            return
        elif choice == "1":
            list_planets()
        elif choice == "2":
            find_planet_by_id()
        elif choice == "3":
            find_planet_by_type()
        elif choice == "4":
            create_planet()
        elif choice == "5":
            update_planet()
        elif choice == "6":
            delete_planet()
            
def species_menu():
    while True:
        system('clear')
        scan_print(
            """> Species | Please select an option:
    _________________________________________________
    0. Back to main menu
    1. List Species
    2. Find Species by ID
    3. Find Species by Type
    4. Create Species
    5. Update Species
    6. Delete Species""",0.01
        )
        choice = input("> ")
        if choice == "0":
            return
        elif choice == "1":
            list_species()
        elif choice == "2":
            find_species_by_id()
        elif choice == "3":
            find_species_by_type()
        elif choice == "4":
            create_species()
        elif choice == "5":
            update_species()
        elif choice == "6":
            delete_species()
            
def civilization_menu():
    while True:
        system('clear')
        scan_print(
            """> Civilizations | Please select an option:
    _________________________________________________
    0. Back to main menu
    1. List Civilizations
    2. Find Civilization by ID
    3. Find Civilization by Type
    4. Create Civilization
    5. Update Civilization
    6. Delete Civilization""",0.01
        )
        choice = input("> ")
        if choice == "0":
            return
        elif choice == "1":
            list_civilizations()
        elif choice == "2":
            find_civilization_by_id()
        elif choice == "3":
            find_civilization_by_type()
        elif choice == "4":
            create_civilization()
        elif choice == "5":
            update_civilization()
        elif choice == "6":
            delete_civilization()
          


if __name__ == "__main__":
    main()
