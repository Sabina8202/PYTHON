from connect import *
from readFilms import *


def add():
    id = int(input("Enter Film ID: "))
    title = input("Enter the name of the film: ")
    year = int(input(" Enter the year released: "))
    rating = input("Enter the rating: ")
    duration = int(input("Enter the duration: "))
    genre = input("Enter the genre: ")
    sqlCode = f"""
                insert into tblfilms values (
                "{id}", "{title}", "{year}", "{rating}", "{duration}", "{genre}"


                )

            """

    cursor.execute(sqlCode)
    conn.commit()
    print(f"{title} was added to the database successfully!")
    read()


if __name__ == "__main__":
    add()
