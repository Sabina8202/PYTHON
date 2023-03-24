from connect import *

sqlCode = """
            CREATE TABLE tblfilms (
            filmID INT,
            title TEXT,
            yearReleased INT,
            rating TEXT,
            duration INT,
            genre TEXT
            );

        """

cursor.execute(sqlCode)
