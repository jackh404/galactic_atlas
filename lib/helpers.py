# lib/helpers.py 
from models.planet import Planet
from models.star import Star
from models.species import Species
from models.civilization import Civilization
from seed_db import Seeder
from time import sleep
from sys import stdout, exit
from os import system

title_string = """
   ____         _               _    _            _    _    _             
  / ___|  __ _ | |  __ _   ___ | |_ (_)  ___     / \  | |_ | |  __ _  ___ 
 | |  _  / _` || | / _` | / __|| __|| | / __|   / _ \ | __|| | / _` |/ __|
 | |_| || (_| || || (_| || (__ | |_ | || (__   / ___ \| |_ | || (_| |\__ \
  \____| \__,_||_| \__,_| \___| \__||_| \___| /_/   \_\\\__||_| \__,_||___/
                                                                          
"""
title_array = ["   ____         _               _    _            _    _    _              ",
               "  / ___|  __ _ | |  __ _   ___ | |_ (_)  ___     / \  | |_ | |  __ _  ___  ",
               " | |  _  / _` || | / _` | / __|| __|| | / __|   / _ \ | __|| | / _` |/ __| ",
               " | |_| || (_| || || (_| || (__ | |_ | || (__   / ___ \| |_ | || (_| |\__ \ ",
               "  \____| \__,_||_| \__,_| \___| \__||_| \___| /_/   \_\\\__||_| \__,_||___/ "]

def check_database():
    try:
        Star.get_all()
        Planet.get_all()
        Species.get_all()
        Civilization.get_all()
    except:
        Seeder.main()

def intro():
    system('clear')
    scan_print("Greetings Starfinder, and welcome to the",0.05)
    for line in title_array:
        scan_print(line,0.002)
    print()
    scan_print("Press Enter to continue")
    input()
    system('clear')


def exit_program():
    system('clear')
    scan_print("Until next time, Starfinder.")
    exit()

def scan_print(s,t=0.01):
    for c in s:
        stdout.write(c)
        stdout.flush()
        sleep(t)
    print()
    
def list_options(cat,name,option=None):
    """Takes a category (either a list or a Class), the (singular) name of the category as a string, and an optional filter for use with entity types. It then asks the user to choose from items printed by list_items"""
    system('clear')
    scan_print(f"Please select a {name}{f' of Type {option}' if option else ''}:")
    print("_________________________________________________")
    scan_print("0: Back to Previous Menu")
    list_items(cat,option)

def list_items(items, option=None):
    """Takes a list of items (either a list or a Class) and an optional filter for use with entity types. It then produces a list of options"""
    if type(items) is list:
        i = 1
        for item in items:
            scan_print(f'{i}: {item}')
            i += 1
    elif type(items) is type:
        if option:
            things = items.find_by_type(option)
            for thing in things:
                scan_print(f'{thing.id}: {thing.name}')
        else:
            things = items.get_all()
            for thing in things:
                scan_print(f'{thing.id}: {thing.name}')
                
def pick_item(name,option=None):
    """Takes the name of a class and an optional filter parameter, calls the list_options function to display a list of options for the user to choose from, then calls item_menu to display the interaction options for the selected item"""
    system('clear')
    list_options(name,name.__name__,option)
    choice = input("=> ")
    if choice != "0":
        item_menu(name.find_by_id(int(choice)))
    
def item_menu(item):
    while True:
        system('clear')
        scan_print(f"""
<>  <>  {item.name} | Please select an option:
        _________________________________________________
        0. Back to {type(item).__name__} menu
        1. View Details
        2. Update {item.name}
        3. Delete {item.name}""",0.01)
        choice = input("> ")
        if choice == "0":
            return
        elif choice == "1":
            print()
            scan_print(item.__str__())
            input("Press Enter to continue")
        elif choice == "2":
            update_item(item)
        elif choice == "3":
            delete_item(item)
            
def delete_item(item):
    scan_print(f"Delete {item.name}? (y/n): ")
    if 'y' in input("=> ").lower():
        try:
            item.delete()
        except:
            scan_print("Something went wrong")
            input("Press Enter to continue")
            
def update_item(item):
    system('clear')
    scan_print(f"""Updating {item.name}
               _______________________________________________
               {item.__str__()}
               """)
    if type(item) is Star:
        update_star(item)
    elif type(item) is Planet:
        update_planet(item)
    elif type(item) is Species:
        update_species(item)
    elif type(item) is Civilization:
        update_civilization(item)
    
    
def create_star():
    star = None
    sname = None
    stype = None
    sdescription = None
    sdiameter = None
    smass = None
    while(not star):
        if not sname: sname = input("Enter the name of the new star: ")
        print()
        scan_print("Available star types: ")
        list_items(Star.types)
        print()
        if not stype: stype = input("Enter the type number of the new star: ")
        stype = Star.types[int(stype)-1]
        if not sdescription: sdescription = input("Enter the description of the new star: ")
        if not sdiameter: sdiameter = input("Enter the diameter of the new star in kilometers: ")
        if not smass: smass = input("Enter the mass of the new planet in trillions of kilograms: ")
        try:
            star = Star.create(sname,stype,sdescription,sdiameter,smass)
            scan_print(f"Star {star.name} created successfully!\n{star}")
        except Exception as e:
            scan_print(f"Error: {e}")
            if input("Try again? (y/n): ") =="n": 
                break
            else:
                if "Name" in e._str_(): sname = None
                elif "Type" in e._str_():stype = None
                elif "Description" in e._str_(): sdescription = None
                elif "Diameter" in e._str_(): sdiameter = None
                elif "Smass" in e._str_(): smass = None
                star = None
    print()
    input("Press Enter to return to menu")
                

def update_star(star):
    try:
        ans = input("Change the star's name? (y/n): ")
        if "y" in ans.lower():
            name = input("Enter the star's new name: ")
            star.name = name 
        ans = input("Change the star type? (y/n): ")
        if "y" in ans.lower():
            print()
            scan_print("Please select a star type:")
            list_items(Star.types)
            print()
            typ = input("=> ")
            type = Star.types[int(typ)-1]
            star.type = type
        ans = input("Change the star's description? (y/n): ")
        if "y" in ans.lower():
            description = input("Enter the star's new description: ")
            star.description = description
        ans = input("Change the star's diameter? (y/n): ")
        if "y" in ans.lower(): 
            diameter = input("Enter the new diameter in kilometers: ")
            star.diameter = diameter
        ans = input("Change the star's mass? (y/n): ")
        if "y" in ans.lower(): 
            mass = input("Enter the new mass in trillions of kilograms: ")
            star.mass = mass
        star.update()
        scan_print("Star parameters successfully adjusted.")
        input("Press Enter to return to menu")
    except Exception as e: 
        scan_print(f"Error updating Star: {e}")
        print()
        input("Press Enter to return to menu")

def create_planet():
    planet = None
    name = None
    type = None
    description = None
    diameter = None
    mass = None
    day = None
    year = None
    star = None
    while(not planet):
        if not name: name = input("Enter the name of the new planet: ")
        print()
        scan_print("Available planet types:")
        list_items(Planet.types)
        print()
        if not type: ptype = input("Enter the type number of the new planet: ")
        type = Planet.types[int(ptype)-1]
        if not description: description = input("Enter the description of the new planet: ")
        if not diameter: diameter = input("Enter the diameter of the new planet in kilometers: ")
        if not mass: mass = input("Enter the mass of the new planet in trillions of kilograms: ")
        if not day: day = input("Enter the day length of the new planet in Earth days: ")
        if not year: year = input("Enter the year length of the new planet in Earth years: ")
        print()
        # scan_print("Available stars:")
        list_options(Star, "Star")
        print()
        star = input("Enter the star ID of the new planet: ")
        try:
            planet = Planet.create(name, type, description, diameter, mass, day, year, int(star))
            scan_print(f"Planet {name} created successfully!\n{planet}")
        except Exception as e:
            scan_print(f"Error: {e}")
            if input("Try again? (y/n): ") == "n":
                break
            else:
                if "Name" in e.__str__(): name = None
                if "Type" in e.__str__(): type = None
                if "Description" in e.__str__(): description = None
                if "Diameter" in e.__str__(): diameter = None
                if "Mass" in e.__str__(): mass = None
                if "Day" in e.__str__(): day = None
                if "Year" in e.__str__(): year = None
                if "Star" in e.__str__(): star = None
                planet = None
    print()
    input("Press Enter to return to menu")
    print()
    
def create_species():
    species = None
    name = None
    type = None
    description = None
    home_world_id = None
    while(not species):
        if not name: name = input("Enter the name of the new species: ")
        print()
        scan_print("Available species types:")
        list_items(Species.types)
        print()
        if not type: type = input("Enter the type number of the new species: ")
        type = Species.types[int(type)-1]
        if not description: description = input("Enter the description of the new species: ")
        print()
        if not home_world_id: 
            scan_print("Please select a home world for the new species:")
            list_items(Planet)
            print()
            home_world_id = input("=> ")
        try:
            species = Species.create(name, type, description, int(home_world_id))
            scan_print(f"Species {name} created successfully!\n{species}")
        except Exception as e:
            scan_print(f"Error: {e}")
            if input("Try again? (y/n): ") == "n":
                break
            else:
                if "Name" in e.__str__(): name = None
                if "Type" in e.__str__(): type = None
                if "Description" in e.__str__(): description = None
                if "Home World" in e.__str__(): home_world_id = None
                species = None
    print()
    input("Press Enter to return to menu")
    print()

def create_civilization():
    civ = None
    name = None
    type = None
    description = None
    religions = None
    languages = None
    species_ids = []
    planet_ids = []
    while(not civ):
        if not name: name = input("Enter the name of the new civilization: ")
        print()
        if not type: 
            scan_print("Please choose the type of the new civilization:")
            list_items(Civilization.types)
            print()
            type = input("=> ")
            type = Civilization.types[int(type)-1]
        if not description: description = input("Enter the description of the new civilization: ")
        if not religions: religions = input("Enter the major religions of the new civilization separated by commas: ")
        if not languages: languages = input("Enter the major languages of the new civilization separated by commas: ")
        if not species_ids: 
            while True:
                print()
                scan_print("Select species from the list one at a time to be a part of the new civilization:")
                scan_print("0: Done adding species")
                list_items(Species)
                print()
                id_ = input("=> ")
                if id_:
                    id_ = int(id_)
                    if id_ not in species_ids:
                        species_ids.append(id_)
                else:
                    break
        if not planet_ids: 
            while True:
                print()
                scan_print("Select planets from the list one at a time to be a part of the new civilization:")
                scan_print("0: Done adding planets")
                list_items(Planet)
                print()
                id_ = input("=> ")
                if id_:
                    id_ = int(id_)
                    if id_ not in planet_ids:
                        planet_ids.append(id_)
                else:
                    break
        try:
            civ = Civilization.create(name, type, description, religions, languages, species_ids, planet_ids)
            scan_print(f"Civilization {name} created successfully!\n{civ}")
        except Exception as e:
            scan_print(f"Error: {e}")
            if input("Try again? (y/n): ") == "n":
                break
            else:
                if "Name" in e.__str__(): name = None
                if "Type" in e.__str__(): type = None
                if "Description" in e.__str__(): description = None
                if "Religions" in e.__str__(): religions = None
                if "Languages" in e.__str__(): languages = None
                if "Species" in e.__str__(): species_ids = []
                if "Planets" in e.__str__(): planet_ids = []
                civ = None
                
    print()
    input("Press Enter to return to menu")
    print()
    
def update_civilization(civ):
    try:
        ans = input("Change the civilization's name? (y/n): ")
        if "y" in ans.lower():
            name = input("Enter the civilizations's new name: ")
            civ.name = name
        ans = input("Change the civilizations's type? (y/n): ")
        if "y" in ans.lower():
            print()
            scan_print("Please choose the type of the new civilization:")
            list_items(Civilization.types)
            print()
            input("=> ")
            type = Civilization.types[int(type)-1]
            civ.type = type
        ans = input("Change the civilizations's description? (y/n): ")
        if "y" in ans.lower():
            description = input("Enter the new description: ")
            civ.description = description
        ans = input("Change the civilizations's major religions? (y/n): ")
        if "y" in ans.lower():
            religions = input("Enter the new major religions separated by commas: ")
            civ.religions = religions
        ans = input("Change the civilizations's major languages? (y/n): ")
        if "y" in ans.lower():
            languages = input("Enter the new major languages separated by commas: ")
            civ.languages = languages
        ans = input("Change the civilizations's species? You will need to enter the ID of each species again. (y/n): ")
        if "y" in ans.lower():
            civ.species_ids = []
            while True:
                print()
                scan_print("Choose species from the list one at a time to be a part of the civilization:")
                scan_print("0: Done adding species")
                list_items(Species)
                print()
                id_ = input("=> ")
                if id_:
                    id_ = int(id_)
                    if id_ not in civ.species_ids:
                        civ.species_ids.append(id_)
                else:
                    break
        ans = input("Change the civilizations's planets? You will need to enter the ID of each planet again. (y/n): ")
        if "y" in ans.lower():
            civ.species_ids = []
            while True:
                print()
                scan_print("Choose planets from the list one at a time to be a part of the civilization:")
                scan_print("0: Done adding planets")
                list_items(Planet)
                print()
                id_ = input("Enter the ID of a planet in the civilization or press Enter to continue: ")
                if id_:
                    id_ = int(id_)
                    if id_ not in civ.planet_ids:
                        civ.planet_ids.append(id_)
                else:
                    break
        civ.update()
        scan_print("Deploying memetic rewrite")
        scan_print("...\n",0.5)
        scan_print(f"Civilization {civ.name} updated successfully!\n{civ}")
    except Exception as exc:
        print("Error updating: ", exc)
    print()
    input("Press Enter to return to menu")
    print()
    
def update_planet(planet):
    try:
        ans = input("Change the planet's name? (y/n): ")
        if "y" in ans.lower():
            name = input("Enter the new name: ")
            planet.name = name
        ans = input("Change the planet's type? (y/n): ")
        if "y" in ans.lower():
            print()
            scan_print("Select the new type for the planet:")
            list_items(Planet.types)
            print()
            input("=> ")
            type = Planet.types[int(type)-1]
            planet.type = type
        ans = input("Change the planet's description? (y/n): ")
        if "y" in ans.lower():
            description = input("Enter the new description: ")
            planet.description = description
        ans = input("Change the planet's diameter? (y/n):")
        if "y" in ans.lower():
            diameter = input("Enter the new diameter in kilometers: ")
            planet.diameter = diameter
        ans = input("Change the planet's mass? (y/n): ")
        if "y" in ans.lower():
            mass = input("Enter the new mass in trillions of kilograms: ")
            planet.mass = mass
        ans = input("Change the planet's day length? (y/n): ")
        if "y" in ans.lower():
            day = input("Enter the new day length in Earth days: ")
            planet.day = day
        ans = input("Change the planet's year length? (y/n): ")
        if "y" in ans.lower():
            year = input("Enter the new year length in Earth years: ")
            planet.year = year
        planet.update()
        scan_print("Deploying terraforming platforms")
        scan_print("...\n",0.5)
        scan_print(f"Planet {name} updated successfully!\n{planet}")
    except Exception as e:
        scan_print(f"Error: {e}")  
    print()
    input("Press Enter to return to menu")
    print()
    
def update_species(species):
    try:
        ans = input("Change the species's name? (y/n): ")
        if "y" in ans.lower():
            name = input("Enter the new name: ")
            species.name = name
        ans = input("Change the species's type? (y/n): ")
        if "y" in ans.lower():
            print()
            scan_print("Select the new type for the species:")
            list_items(Species.types)
            print()
            type = input("=> ")
            type = Species.types[int(type)-1]
            species.type = type
        ans = input("Change the species's description? (y/n): ")
        if "y" in ans.lower():
            description = input("Enter the new description: ")
            species.description = description
        ans = input("Change the species's home world? (y/n): ")
        if "y" in ans.lower():
            print()
            scan_print("Select the new home world for the species:")
            list_items(Planet)
            print()
            home_world_id = input("=> ")
            species.home_world_id = home_world_id
        species.update()
        scan_print("Deploying CRISPR viruses")
        scan_print("...\n",0.5)
        scan_print(f"Species {name} updated successfully!\n{species}")
    except Exception as e:
        scan_print(f"Error: {e}")  
    print()
    input("Press Enter to return to menu")
    print()