# import sql libraries
import sqlite3 as sql
from time import sleep
# connecting to the database
conn = sql.connect(
    r"C:\Users\sabin\OneDrive\Documents\PYTHON\Project\filmflix.db")
# r says python to treat blackslash \ as a literal or raw character.
# cursor() lets user to perform SQL on a given connection
cursor = conn.cursor()
