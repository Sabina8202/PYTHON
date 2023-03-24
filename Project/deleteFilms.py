from connect import *
from readFilms import *


def delete():
    readData = read()
    if readData == 0:
        print("No data in FilmFlix database")
    else:
        Film = input("Enter a film Title to delete: ")

        sqlCode = f"""
                        delete from tblfilms
                        where title = "{Film}"




                        """

        cursor.execute(sqlCode)
        conn.commit()

        print(f"Film Title: {Film} has been deleted from database!")

        sleep(2)
        read()


if __name__ == "__main__":
    delete()
