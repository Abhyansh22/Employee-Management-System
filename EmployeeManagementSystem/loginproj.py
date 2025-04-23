import mysql.connector
conn=mysql.connector.connect(host='localhost',user='root',passwd='@dmin123')
curso=conn.cursor(buffered = True)
conn.autocommit = True
curso.execute('create database if not exists Employee_Management')
curso.execute('use Employee_Management')
curso.execute('create table if not exists login(Username varchar(255),Password varchar(100) primary key)')
curso.execute('create table if not exists Employee_Docs(Employee_Id bigint primary key,Employee_Name varchar(255),Employee_Department varchar(255),Employee_Salary int,Employee_Age int)')
curso.execute('create table if not exists Employee_Stats(Employee_Id bigint primary key,Employee_Name varchar(255),Employee_Department varchar(255),Employee_Performance varchar(255),em_Work varchar(255))')
conn=mysql.connector.connect(host='localhost',user='root',passwd='@dmin123',database='Employee_Management')
curso=conn.cursor(buffered = True)
print('            Welcome To Employee Management System Program              ')
print('Register or Login to start......')
print('Press 1 to Register')
print('Press 2 to Login')
print()
ch=int(input('Enter your choice...'))
if ch== 1:
    name=input('Enter your username:')
    print()
    passw=int(input('Enter a four digit pin '))
    curso.execute('insert into login values("'+name+'","'+str(passw)+'")')
    conn.commit()
    print('User created successfully')
    print('If you want to proceed further then you have to login')
    cce=input('Do you want to continue Yes or No')
    if cce == 'yes' or cce == 'Yes':
         name=input('Enter your Username=')
         print()
         passw=int(input('Enter your four digit pin'))
         curso.execute("select * from login where Password= '"+str(passw)+"'")
         pri=curso.fetchone()
         if pri is  None:
             print()
             print('Invalid username or password')
         else:
             print()
             import comproject
    else:
        print('Thank You \nProgram Terminated')
if ch==2:
     name=input('Enter your Username=')
     print()
     passw=int(input('Enter your four digit pin'))
     curso.execute("select * from login where Password='"+str(passw)+"'")
     pri = curso.fetchone()
     if pri is  None:
          print()
          print('Invalid username or password')
     else:
          print()
          import comproject





