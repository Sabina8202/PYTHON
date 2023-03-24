import sqlite3 as sql  # import sql libraries
# connect to database
conn = sql.connect(
    r"C:\Users\sabin\OneDrive\Documents\PYTHON\WEEK-2\DB\bootcamp.db")

# cursor() func will let us perform SQL on a given connection.
cursor = conn.cursor()
"""
# execute() function will let us execute SQL code
cursor.execute("SELECT * FROM table")


# connection must be committed as we execute statement
conn.commit()

"""
"""
create table
insert songs
read songs
update songs
delete songs

"""
