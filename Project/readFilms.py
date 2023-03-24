from connect import *


def read():
    sqlCode = "select * from tblfilms"
    cursor.execute(sqlCode)
    data = cursor.fetchall()

    if data == []:
        print("sorry, database table is empty")
        return 0
    else:
        print("Lists of Movies:")
        for i in data:
            print(i)
        sleep(2)
        return 1


if __name__ == "__main__":
    read()
