import mysql.connector as sql
conn=sql.connect(host="localhost", user="root", passwd="100821", database="shoe_billing_system")
mycursor=conn.cursor()
if conn.is_connected():
    print("Conection With Database Establised Successfully")
else:
    print("Conection With Database Failed")

print("Welcome to GURPREET'S SHOE BILLING SYSTEM")

c1=conn.cursor()
choice = 0
while choice != 2:
    print("1. EMPLOYEE LOGIN")
    print("2. EXIT")
    choice=int(input("ENTER YOUR CHOICE:"))
    if choice==1:
     print('')
     print('Enter your Credentials')
     emp_name=input('Enter your name: ')
     print('')
     emp_id=int(input('Enter your employee Identity Number:'))
     print(' ')
     password=input('Enter your Password: ')
     print(' ')
     c1=conn.cursor()
     c1.execute('select * from staff')
     data=c1.fetchall()
     count=c1.rowcount
     for row in data:
        if (emp_name in row) and (emp_id in row) and (password in row):
            print(' ')
            print(' ')
            print("WELCOME TO GURPREET'S SHOE BILLING SYSTEM")
            print(' ')
            print(' ')
            print('NEW INVOICE,press                                     :1')
            print(' ')
            print('SHOW ALL INVOICES,press                               :2')
            print(' ')
            print('SHOW INVOICE BY CUSTOMER NAME,press                   :3')
            print(' ')
            print('SHOW ALL INVOICES BY INVOICE NUMBER,press             :4')
            print(' ')
            print('EXIT,press                                            :5')
            print(' ')
            c2=int(input('enter your choice : '))

            if(c2==1):
                 bill_no=int(input("Enter Invoice number :"))
                 cust_name=input("Enter the Customer name : ")
                 item_name=input("Enter Item Name: ")
                 qnt=int(input("Enter the Quantity of item :"))
                 price=int(input("Enter Cost of item :"))
                 pur_date=input("Enter Date of purchase :")
                 t_price=price*qnt
                 phone=int(input("Enter Customer phone number : "))
                 SQL_insert="insert into invoices values("+"'"+str(bill_no)+"'"+","+"'"+cust_name+"'"+","+"'"+item_name+"'"+","+"'"+str(qnt)+"'"+","+"'"+str(price)+"'"+","+"'"+pur_date+"'"+","+str(t_price)+","+str(phone)+")"
                 c1.execute(SQL_insert)
                 conn.commit()
                 print("Invoice generated")

            elif (c2==2):
                c1=conn.cursor()
                c1.execute('select * from invoices')
                data=c1.fetchall()
                count=c1.rowcount
                print('Details of all invoices is',count)
                for row in data:
                    print(row)

            elif(c2==3):
                print('')
                name = input("Enter customer name : ")
                cust_name=[name]
                sqlFormula = "select*from invoices WHERE cust_name = %s"
                c1.execute(sqlFormula,cust_name)
                data=c1.fetchall()
                count=c1.rowcount
                print('Details of all invoices is',count)
                for row in data:
                    print(row)

            elif(c2==4):
                print('')
                inv_no = int(input("Enter bill number : "))
                bill_no=[inv_no]
                sqlFormula = "select*from invoices WHERE bill_no = %s"
                c1.execute(sqlFormula,bill_no)
                data=c1.fetchall()
                count=c1.rowcount
                print('Details of all invoices is',count)
                for row in data:
                    print(row)      

            elif (c2==5):
                print('THANK YOU FOR VISITING')
           
            else:
                print("Oops, something went wrong, try again...........")

        
     if choice==3:
      print("THANK YOU FOR VISITING")
      c1.close

     else :
       print("")
               
                 
            
