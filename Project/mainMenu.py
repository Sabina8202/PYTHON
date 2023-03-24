from connect import *
from addFilms import *
from readFilms import *
from deleteFilms import *
from updateFilms import *
from report import *


def MainMenu():
    menu1 = """
            WELCOME TO FILMFLIX DATABASE:

            Choose any following options:
            1. Display List of movies
            2. Add movie to the Filmflix Database
            3. Update an existing movie
            4. Delete movie from the Filmflix Database
            5. Display the report of FilmFlix Database
    """

    print(menu1)
    sleep(1)
    options = ["1", "2", "3", "4", "5"]
    choice = input("Enter any option: ")

    while choice not in options:
        print("sorry, not valid!")
        choice = input("Enter a valid option: ")

    return choice


if __name__ == "__main__":
    menuLoop = True

    while menuLoop == True:
        userChoice = MainMenu()
        if userChoice == "1":
            read()
        elif userChoice == "2":
            add()
        elif userChoice == "3":
            update()
        elif userChoice == "4":
            delete()
        elif userChoice == "5":
            report()

print("End Program")
