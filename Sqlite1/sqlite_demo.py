import sqlite3
from Employee import Employee

conn = sqlite3.connect(':memory:')
c = conn.cursor()
c.execute("""CREATE TABLE employees(
            first text,
            last text,
            pay integer
            )""")


def insert_emp(emp):
    with conn:
        c.execute("INSERT INTO employees VALUES(?, ?, ?)", (emp.first, emp.last, emp.pay))

def get_emps_by_name(lastname):
    c.execute("SELECT * FROM employees WHERE last=?", (lastname,))
    return c.fetchall()

def update_pay(emp, pay):
    with conn:
        c.execute("""UPDATE employees SET pay = ? WHERE first=? AND last=?""", (emp.first, emp.last,pay))

def remove_emp(emp):
    with conn:
        c.execute("""DELETE FROM employees WHERE first = ? AND last = ? """, (emp.first, emp.last))

        
emp_1 = Employee('John', 'Doe', 80000)
emp_2 = Employee('Jane', 'Doe', 9000)
emp_3 = Employee('Marco', 'Narca', 2000)

insert_emp(emp_1)
insert_emp(emp_2)

emps = get_emps_by_name('Doe')
print(emps)

update_pay(emp_2, 9200)
remove_emp(emp_1)

emps = get_emps_by_name('Doe')
print(emps)
#c.execute("INSERT INTO employees VALUES(?, ?, ?)", (emp_1.first, emp_1.last, emp_1.pay))
#conn.commit()

#c.execute("INSERT INTO employees VALUES(:first, :last, :pay)", {'first':emp_2.first, 'last':emp_2.last, 'pay': #emp_2.pay})
#conn.commit()

#c.execute("INSERT INTO employees VALUES(?, ?, ?)", (emp_3.first, emp_3.last, emp_3.pay))
#conn.commit()

#c.execute("SELECT * FROM employees WHERE last='Narca'")
#print(c.fetchall())

#c.execute("SELECT * FROM employees WHERE last=?", ('Doe',))
#print(c.fetchall())
#conn.commit()
conn.close()


#c.fetchone()
#c.fetchmany(5)