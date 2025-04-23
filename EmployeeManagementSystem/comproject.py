import mysql.connector
connect = mysql.connector.connect(host='localhost',user='root',passwd='@dmin123',database='Employee_Management')
cur=connect.cursor(buffered = True)
connect.autocommit=True
def menu():
    print('       Employee Mangement System        ')
    c=input('Do you want to continue or not - Yes or No')
    while(c=='yes' or c=='Yes'):

        print('Press 1 for Employee Registration')
        print('Press 2 for Employee details')
        print('Press 3 to perform any Updation')
        print('Press 4 for Employee List')
        print('Press 5 to enter your work experience')
        print('Press 6 to know about your performance')
        print('Press 7 to exit')
        choice = int(input('Enter your choice:'))

        if choice == 1:
            register()
        elif choice == 2:
            details()
        elif choice == 3:
            update()
        elif choice == 4:
            emplist()
        elif choice == 5:
            experience()
        elif choice == 6:
            expdata()
        else:
            print('Thank you')
            quit()
    else:
        print('Thank you \nProgram Terminated' )
def register():
    E_id = int(input('Enter your employee Id:'))
    E_name=input('Enter your name:')
    E_dept=input('Enter department:')
    E_salary=int(input('Enter your salary:'))
    E_age=int(input('Ente your age:'))
    cur.execute('insert into Employee_Docs values("'+str(E_id)+'","'+E_name+'","'+E_dept+'","'+str(E_salary)+'","'+str(E_age)+'")')
    print('You have registered successfully')

def details():
    cur.execute('select * from Employee_Docs')
    deta=cur.fetchall()
    print('number of employees:',len(deta))
    for i in range(len(deta)):
        print(deta[i])

def update():
    print('Updations available in - \n1.Name \n2.Department \n3.Salary \n4.Age')
    ch = int(input('What do you want to update Name/Department/Salary/Age'))
    if ch == 1:
        stuc=int(input('Enter the Employee Id of the employee whose name you want to change'))
        newname=input('Enter the new name')
        cur.execute('update Employee_Docs set Employee_Name = "'+newname+'" where Employee_Id = "'+str(stuc)+'"')
        print('Record updated')
    if ch == 2:
        stuc=int(input('Enter the EmployeenId of the employee whose department you want to change'))
        newsti=input('Enter name of the new department')
        cur.execute('update Employee_Docs set Employee_Department = "'+newsti+'" where Employee_Id ="'+str(stuc)+'"')
        print('Record Updated')
    if ch == 3:
        stuc=int(input('Enter the Employee Id of the employee whose salary you want to change '))
        newsub=input('Enter new salary')
        cur.execute('update Employee_Docs set Employee_Salary = "'+newsub+'" where Employee_Id ="'+str(stuc)+'"')
        print('Record Updated')
    if ch == 4:
        stuc=int(input('Enter the Employee Id of the employee whose age you want to change '))
        avg=input('Enter age ')
        cur.execute('update Employee_Docs  set Employee_Age = "'+str(avg)+'" where Employee_Id="'+str(stuc)+'"')
        connect.commit()
        print('Record Updated')

    
def emplist():
    cur.execute('select Employee_Name from Employee_Docs order by Employee_Name asc')
    for l in cur:
        print(l)

def experience():
    connectt = mysql.connector.connect(host='localhost',user='root',passwd='@dmin123',database='Employee_Management')
    cure=connectt.cursor(buffered=True)
    connectt.autocommit=True
    eeid=int(input('Enter your Employee Id:'))
    eena=input('Enter your name:')
    edep=input('Enter your department:')
    eeper=input('Enter you performance(in grades):')
    eework=input('Enter your work experience in years(in words)')
    cure.execute('insert into Employee_Stats values("'+str(eeid)+'","'+eena+'","'+edep+'","'+eeper+'","'+eework+'")')
    print('Performance added')

def expdata():
    connectt = mysql.connector.connect(host='localhost',user='root',passwd='@dmin123',database='Employee_Management')
    cure=connectt.cursor(buffered=True)
    connectt.autocommit=True
    eeidd=int(input('Enter your Employee Id:'))
    cure.execute('select * from Employee_Stats where Employee_Id = "'+str(eeidd)+'"')
    ceta = cure.fetchone()
    print(ceta)
menu()
