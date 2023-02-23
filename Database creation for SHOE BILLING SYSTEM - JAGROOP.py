import mysql.connector as sql
conn = sql.connect(
    host="localhost",
    user="root",
    password="100821"
)

if conn.is_connected():
    print("Connection Successfull")


conn.cursor().execute("CREATE DATABASE shoe_billing_system")
print("Database Created")
conn.cursor().execute("USE shoe_billing_system")
conn.cursor().execute('create table staff(emp_id int, emp_name varchar(75), password varchar(15))')
print("Staff table created")
conn.cursor().execute("CREATE TABLE invoices (bill_no INT AUTO_INCREMENT PRIMARY KEY, cust_name VARCHAR(50), item_name VARCHAR(255), qnt int, price int, pur_date DATE, t_price int, phone bigint)")
print("Invoices table created")
conn.cursor().execute("insert into staff values(2111,'Gurpreet Kaur','10082021')")
conn.commit()
print("Account Created")


