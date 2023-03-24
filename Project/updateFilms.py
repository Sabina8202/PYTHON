from connect import *
from readFilms import *


def update():
    readData = read()
    if readData == 0:
        print("Database is empty")
    else:
        id = int(input("Enter Film ID: "))
        title = input("Enter the name of the film: ")
        year = int(input(" Enter the year released: "))
        rating = input("Enter the rating: ")
        duration = int(input("Enter the duration: "))
        genre = input("Enter the genre: ")

        sqlCode = f"""
        update tblfilms
        SET title = "{title}", yearReleased = "{year}", rating = "{rating}", duration ="{duration}", genre = "{genre}"
        WHERE filmID = {id}



        """

        cursor.execute(sqlCode)
        conn.commit()

        print(f"Film has been updated successfully")
        read()


if __name__ == "__main__":
    update()
