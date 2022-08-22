# SQL stands for "Structured Query Langugage"

import sqlite3

with sqlite3.connect("company.db") as db:
    cursor=db.cursor()

cursor.execute("""CREATE TABLE IF NOT EXISTS employees(id integer PRIMARY KEY, name text NOT NULL, dept text NOT NULL, salary integer);""")

# Inserts data into the employees table. The db.commit() line saves the changes.
cursor.execute("""INSERT INTO employees(id,name,dept,salary) VALUES("4", "Bob", "Sales", "25000")""")
db.commit()

# Allows a user to enter new data which is then inserted into the table.
newID = input("Enter ID number: ")
newName = input("Enter name: ")
newDept = input("Enter department: ")
newSalary = input("Enter Salary: ")
cursor.execute("""INSERT INTO employees(id, name, dept, salary) VALUES(?, ?, ?, ?)""", (newID, newName, newDept, newSalary))
db.commit()

cursor.execute("SELECT * FROM employees")
print(cursor.fetchall())
db.close()

cursor.execute("SELECT * FROM employees")
for x in cursor.fetchall():
    print(x)

cursor.execute("SELECT * FROM employees WHERE salary>20000")
# Selects all the data from the employees table where the salary is over 20000

cursor.execute("""SELECT employees.id, employees.name, dept.manager FROM employees, dept WHERE employees.dept = dept.dept AND employees.salary > 20000""")

# I Think, SQL cannot learn by writing top-down tracing the comment like this. So, I don't go deep about it at all.