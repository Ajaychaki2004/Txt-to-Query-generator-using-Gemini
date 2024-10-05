import sqlite3

connection = sqlite3.connect("student.db")

cursor = connection.cursor()

table_info ="""
Create table STUDENT(NAME VACHAR(25),CLASS VARCHAR(20), SECTION VARCHAR(25),
MARKS INT);

"""


cursor.execute(table_info)

cursor.execute('''Insert into STUDENT values ('Rahul', 'Datascience', 'A', 90)''')
cursor.execute('''Insert into STUDENT values ('Harlee', 'Datascience', 'B', 95)''')
cursor.execute('''Insert into STUDENT values ('Ajay', 'Datascience', 'C', 76)''')
cursor.execute('''Insert into STUDENT values ('Hari', 'Computerscience', 'A', 54)''')
cursor.execute('''Insert into STUDENT values ('Priya', 'Artificialintelligence', 'C', 99)''')

print("The inserted data are")

data = cursor.execute('''Select * From STUDENT''')

for row in data:
    print(row)

connection.commit()
connection.close()