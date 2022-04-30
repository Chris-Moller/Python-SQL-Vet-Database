import sqlite3
from os import path
from animal_data import animals

class Animal1:
    def __init__(self, animal, owner, age, vaccine):
        self.first = animal
        self.owner = owner
        self.age = age
        self.vaccine = vaccine
    def __repr__(self):
        return "Animal('{}','{}','{}')".format(self.first, self.owner, self.age, self.vaccine)

conn = sqlite3.connect('animal_data2.db')   

c = conn.cursor()

def showDB():
    c.execute("SELECT * FROM Animal_Data")
    result = c.fetchall()
    for row in result:
        print(row)
def add_data(db):
    with conn:
        c.executemany("INSERT INTO Animal_Data VALUES (?, ?, ?, ?)", db)

def insert_animal(animal):
    with conn:
        c.execute("INSERT INTO Animal_Data VALUES (:Animal, :Owner, :age, :vaccine)", {'Animal': animal.first, 'Owner': animal.owner, 'age': animal.age, 'vaccine': animal.vaccine})

def call_insert_animal():
    print("Animal Name: ")
    animal = input()
    print("Owner Name: ")
    owner = input()
    print("Age: ")
    age = input()
    print("Vaccine status(0=True/1=False): ")
    vaccine = input()
    finalentry = Animal1(animal, owner, age, vaccine)
    insert_animal(finalentry)
    showDB()

def get_animal_by_name(aName):
    c.execute("SELECT * FROM Animal_Data WHERE Animal = :Animal", {'Animal': aName})
    return c.fetchall()

def call_animal_by_name():
    print( "Animal name: ")
    queryA = input()
    queryA = get_animal_by_name(queryA)
    print(queryA)

def get_animal_by_owner(oName):
    c.execute("SELECT * FROM Animal_Data WHERE Owner=:Owner", {'Owner': oName})
    return c.fetchall()

def call_animal_by_owner():
    print( "Owner name: ")
    queryA = input()
    queryA = get_animal_by_owner(queryA)
    print(queryA)

def update_age(animal0, age):
    with conn:
        c.execute("""UPDATE Animal_Data SET age = :age
                    WHERE Animal = :Animal""",
                    {'Animal': animal0.first, 'age': age})

def call_update_age():
    print("Name of animal to update:")
    animal = input()
    print("updated age: ")
    age = input()
    final_entry = Animal1(animal, animal, age, 0)
    update_age(final_entry, age)
    showDB()

def update_vaccine(animal0, vaccine):
    with conn:
        c.execute("""UPDATE Animal_Data SET vaccine = :vaccine
                    WHERE Animal = :Animal""",
                    {'Animal': animal0.first, 'vaccine': vaccine})

def call_update_vaccine():
    print("Name of animal to update:")
    animal = input()
    print("Vaccine Status(0=True/1=False): ")
    vaccine = input()
    final_entry = Animal1(animal, animal, 1, vaccine)
    update_vaccine(final_entry, vaccine)
    showDB()

def remove_animal(animal0):
    with conn:
        c.execute("DELETE from Animal_Data WHERE Animal = :Animal AND Owner = :Owner",
        {'Animal': animal0.first, 'Owner': animal0.owner})

def call_remove_animal():
    print( "Animal Name: ")
    animal = input()
    print("Owner Name: ")
    owner = input()
    final_entry = Animal1(animal, owner, 10, True)
    remove_animal(final_entry)
    showDB()

def checkdb():
    if not path.exists("animal_data2.py"):
        try:
            c.execute('''CREATE TABLE Animal_Data(
                    Animal text,
                    Owner text,
                    age integer,
                    vaccine integer)''')
            conn.commit()
            add_data(animals)
        except:
            pass
    else:
        pass

def main():
    checkdb()
    print( "Enter SQL Vet Database?(y/n): ")
    answer2 = input()
    answer2 = toUpper( answer2 )
    if answer2 == "Y":
        print( "Welcome to the Awesome SQL Vet Database" )
        print( "Type one of the following letters to select a feature" )
        print( "A: Show the list of all animals" )
        print( "B: Search by animal name" )
        print( "C: Search by owner name" )
        print( "D: Add new animal" )
        print( "E: Remove animal" )
        print( "F: Update animal age" )
        print( "G: Update vaccine status" )
        print( "H: Do nothing" )

        feature_letter = input()
        feature_letter = toUpper( feature_letter )
        if feature_letter == "A":
            showDB()
        elif feature_letter == "B":
            call_animal_by_name()
        elif feature_letter == "C":
            call_animal_by_owner()
        elif feature_letter == "D":
            call_insert_animal()
        elif feature_letter == "E":
            call_remove_animal()
        elif feature_letter == "F":
            call_update_age()
        elif feature_letter == "G":
            call_update_vaccine()
        elif feature_letter == "H":
            print( "Have a nice day" )
        else:
            print( "Sorry, I don't understand: %s" % feature_letter )
    elif answer2 == "N":
        print( "Have a nice day!")

def toUpper( s ):
    return s.upper()

if __name__ == "__main__":
    main()

conn.close()
