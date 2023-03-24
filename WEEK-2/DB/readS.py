# Read Songs
from connect import *
sqlCode = "SELECT * FROM songs"
cursor.execute(sqlCode)
# fetchall() will retrieve the data from the latest query
data = cursor.fetchall()
print("\nSongs List:")
for i in data:
    print(i)
