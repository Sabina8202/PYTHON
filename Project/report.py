from connect import *
from readFilms import *


def report():

    print("REPORT: ")
    print("------------------------------------------------------------------- ")
    print("\n")
    sqlCode = """
                select filmID, title from tblfilms
                


                """

    cursor.execute(sqlCode)
    print("LIST OF MOVIES: ")
    data = cursor.fetchall()
    for row in data:
        print(row)

    # --------------------------------------------------------------------------------

    sqlCode1 = """
                    select filmID, title from tblfilms
                    where yearReleased = 2018


                    """

    cursor.execute(sqlCode1)
    print("\n")
    print("LIST OF MOVIES RELEASED IN 2018: ")
    data = cursor.fetchall()
    for row in data:
        print(row)

    # --------------------------------------------------------------------------------

    sqlCode2 = """

                    select filmID, title, Genre from tblfilms
                    where genre LIKE "%Horror%"


                    """
    cursor.execute(sqlCode2)
    print("\n")
    print("HORROR MOVIES: ")
    data = cursor.fetchall()
    for row in data:
        print(row)

    # --------------------------------------------------------------------------------

    sqlCode3 = """

                    select filmID, title, Genre from tblfilms
                    where genre LIKE "%Animation%"


                    """
    cursor.execute(sqlCode3)
    print("\n")
    print("ANIMATED MOVIES: ")
    data = cursor.fetchall()
    for row in data:
        print(row)

    # --------------------------------------------------------------------------------

    sqlCode4 = """

                    select title, yearReleased from tblfilms
                    where yearReleased > 2015 AND yearReleased < 2019



                    """
    cursor.execute(sqlCode4)
    print("\n")
    print("MOVIES RELEASED BETWEEN YEAR 2015 AND YEAR 2019 ")
    data = cursor.fetchall()
    for row in data:
        print(row)

    # ------------------------------------------------------------------------

    sqlCode5 = """

                    select title, yearReleased, rating from tblfilms
                    where rating > 8.0

                    """

    cursor.execute(sqlCode5)
    print("\n")
    print("MOVIES WHOSE RATING IS ABOVE EIGHT: ")
    data = cursor.fetchall()
    for row in data:
        print(row)

    # ------------------------------------------------------------------------

    sqlCode6 = """

                    select title, MAX(yearReleased) from tblfilms


                    """
    cursor.execute(sqlCode6)
    print("\n")
    print("LATEST MOVIE FROM FILMFLIX DATABASE: ")
    data = cursor.fetchall()
    for row in data:
        print(row)
