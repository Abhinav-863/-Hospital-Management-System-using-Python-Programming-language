import mysql.connector as sql
con=sql.connect(host='Localhost',user='root',passwd='abhinav',database='mysql')

if con.is_connected():
    print("Successfully connected")

c1=con.cursor()
print('-------------------------------------------------------------------')
print("                     HOSPITAL MANAGEMENT SYSTEM")
print('-------------------------------------------------------------------')
print('1.  About the project')
print('2.  Create table doctor_details')
print('3.  Register Doctor Details')
print('4.  All the doctor details')
print('5.  Create Table patient_details')
print('6.  Register patients details')
print('7.  All the patients details')
print('8.  Create Table worker_details')
print('9.  Register worker details')
print('10. All the workers details')
print('11. Search doctor details')
print('12. Search patients details')
print('13. Search worker details')
print('14. Update patient details')
print('15. Update doctor details')
print('16. Update worker details')
print('17. Delete doctor details')
print('18. Delete patient details')
print('19. Delete worker details')
print('20. Bill_details')
print('21. Enter Charges of Patient for Bill_details')
print('22. Show records of Bill')
print('23. Delete bill details')
ans='y'
while ans.lower()=='y':
    def about():
        print('You are working HOSPITAL MANAGEMENT PROJECT. It has 23 options in it')
      
    def create_doctor_details():
        c1=con.cursor()
        c1.execute("create table doctor_details(d_id int, d_name varchar(20),d_age int,d_department varchar(20),d_phono int(10))")
        print('table created')

    def insert_doctor_details():
        print('Enter Details of new doctor:')
        d_id=int(input('Enter ID of Doctor:'))
        d_name=input('Enter Doctor Name:')
        d_age=int(input("Enter age:"))
        d_department=input("Enter the department:")
        d_phono=int(input('Enter phone number:'))
        sql_insert= "insert into doctor_details values({},'{}','{}','{}','{}')".format(d_id,d_name,d_age,d_department,d_phono)
        c1.execute(sql_insert)
        print('Registered new Doctor')
        con.commit()

    def show_records_doctor_details():
        print('Create table for Doctors')
        c1.execute("select * from doctor_details")
        data=c1.fetchall()
        for i in data:
                print(i)
        con.commit()
        print(data)


    def create_patient_details():
        print('Create table for Patients')
        c1=con.cursor()
        c1.execute("create table patient_details(p_id int primary key , p_name varchar(25) ,p_age int(3),p_problems varchar(40),p_phono int)")
        print('table created')

    def insert_patient_details():
        print('Enter New patient Information')
        p_id=int(input('Enter ID of Patient:'))
        p_name=input('Enter Patient Name:')
        p_age=int(input('Enter age:'))
        p_problems=input("Enter problem/disease")
        p_phono=int(input('Enter the phone number:'))
        sql_insert= "insert into patient_details values({},'{}','{}','{}','{}')".format(p_id,p_name,p_age,p_problems,p_phono)
        c1.execute(sql_insert)
        print('SUCCESSFULLY REGISTERED')
        con.commit()

    def show_records_patient_details():
        print('Create table for Patients')
        c1.execute("select * from patient_details")
        data=c1.fetchall()
        for i in data:
                print(i)
        con.commit()
        print(data)

    def create_worker_details():
        print('Create table for Workers')
        c1=con.cursor()
        c1.execute("create table worker_details(w_id int primary key ,w_name varchar(25) ,w_age int,w_workname varchar(40),p_phono int)")
        print('Table created')

    def insert_worker_details():
        print('Enter New patient Information')
        w_id=int(input("Enter ID of the Worker:"))
        w_name=input('Enter Worker Name:')
        w_age=int(input('Enter the age:'))
        w_workname=input('Enter the type of work:')
        w_phono=int(input('Enter phone number :'))
        sql_insert= "insert into worker_details values({},'{}','{}','{}','{}')".format(w_id,w_name,w_age,w_workname,w_phono)
        c1.execute(sql_insert)
        print('SUCCESSFULLY REGISTERED')
        con.commit()

    def show_records_worker_details():
        print('Create table for Workers')
        c1.execute("select * from worker_details")
        data=c1.fetchall()
        for i in data:
                print(i)
        con.commit()
        print(data)

    def search_doctor_details():
        ans='y'
        while ans.lower()=='y':
            d_id= int(input("Search Doctor Record by entering ID :"))
            query="select * from doctor_details where d_id={}".format(d_id)
            c1.execute(query)
            result = c1.fetchall()
            if c1.rowcount==0:
                print("Sorry ! d_id not found")
            else:
                print("%10s"%"d_id","%20s"%"d_name","%10s"%"d_age","%20s"%"d_department","%10s"%"d_phono")
            for row in result :
                print("%10s"%row[0],"%20s"%row[1],"%10s"%row[2],"%20s"%row[3],"%10s"%row[4])


            ans=input("SEARCH MORE (Y):")


    def search_patient_details():
        ans='y'
        while ans.lower()=='y':
            p_id= int(input("Search Patients Record by entering ID :"))
            query="select * from patient_details where p_id={}".format(p_id)
            c1.execute(query)
            result = c1.fetchall()
            if c1.rowcount==0:
                print("Sorry ! p_id not found")
            else:
                print("%10s"%"p_id","%20s"%"p_name","%10s"%"p_age","%20s"%"p_problems","%10s"%"p_phono")
            for row in result :
                print("%10s"%row[0],"%20s"%row[1],"%10s"%row[2],"%20s"%row[3],"%10s"%row[4])
            ans=input("SEARCH MORE (Y):")

    def search_worker_details():
        ans='y'
        while ans.lower()=='y':
            w_id= int(input("Search Workers Record by entering ID :"))
            query="select * from worker_details where w_id={}".format(w_id)
            c1.execute(query)
            result = c1.fetchall()
            if c1.rowcount==0:
                print("Sorry ! w_id not found")
            else:
                print("%10s"%"w_id","%20s"%"w_name","%10s"%"w_age","%20s"%"w_workname","%10s"%"w_phono")
            for row in result :
                print("%10s"%row[0],"%20s"%row[1],"%10s"%row[2],"%20s"%row[3],"%10s"%row[4])
            ans=input("SEARCH MORE (Y):")


        
    def update_patient_details():
        ans='y'
        choice='n'
        while ans.lower()=='y':
            p_id=int(input("ENTER Patient ID TO UPDATE:"))
            query="select * from patient_details where p_id={}".format(p_id)
            c1.execute(query)
            result=c1.fetchall()
            if c1.rowcount==0:
                print("Sorry! p_id not found")
            else:
                print("%10s"%"p_id","%20s"%"p_name","%10s"%"p_age","%20s"%"p_problems","%10s"%"p_phono")
            for row in result:
                print("%10s"%row[0],"%20s"%row[1],"%10s"%row[2],"%20s"%row[3],"%10s"%row[4])
                choice=input("\n##ARE YOU SURE TO UPDATE?[y]:")
                if choice.lower()=='y':
                    print("==YOU CAN UPDATE ONLY PHONE NUMBER==")
                    d=int(input("ENTER NEW PHONE NUMBER="))
                    query="update patient_details set p_phono='{}' where p_id={}".format(p_id,d)
                    c1.execute(query)
                    con.commit()
                    print("##RECORD UPDATED##")
                else:
                    exit(0)
                ans=input("UPDATE MORE[Y]:")

    def update_doctor_details():
        ans='y'
        choice='n'
        while ans.lower()=='y':
            d_id=int(input("ENTER Doctor ID TO UPDATE:"))
            query="select * from doctor_details where d_id={}".format(d_id)
            c1.execute(query)
            result=c1.fetchall()
            if c1.rowcount==0:
                print("Sorry! d_id not found")
            else:
                print("%10s"%"d_id","%20s"%"d_name","%10s"%"d_age","%20s"%"d_department","%10s"%"d_phono")
            for row in result:
                print("%10s"%row[0],"%20s"%row[1],"%10s"%row[2],"%20s"%row[3],"%9ss"%row[4])
                choice=input("\n##ARE YOU SURE TO UPDATE?[y]:")
            if choice.lower()=='y':
                    print("==YOU CAN UPDATE ONLY PHONE NUMBER AND DEPARTMENT==")
                    d=int(input("ENTER NEW PHONE NUMBER="))
                    query="update doctor_details set d_phono='{}' where d_id={}".format(d_id,d)
                    c1.execute(query)
                    con.commit()
                    print("##RECORD UPDATED##")
            else:
                    exit(0)
            ans=input("UPDATE MORE[Y]:")

    def update_worker_details():
        ans='y'
        choice='n'
        while ans.lower()=='y':
            w_id=int(input("ENTER Worker ID TO UPDATE:"))
            query="select * from worker_details where w_id={}".format(w_id)
            c1.execute(query)
            result=c1.fetchall()
            if c1.rowcount==0:
                print("Sorry! w_id not found")
            else:
                print("%10s"%"w_id","%20s"%"w_name","%10s"%"w_age","%20s"%"w_workname","%10s"%"w_phono")
            for row in result:
                print("%10s"%row[0],"%20s"%row[1],"%10s"%row[2],"%20s"%row[3],"%10s"%row[4])
                choice=input("\n##ARE YOU SURE TO UPDATE?[y]:")
                if choice.lower()=='y':
                    print("==YOU CAN UPDATE ONLY AGE==")
                    d=int(input("ENTER NEW AGE="))
                    query="update worker_details set w_age='{}' where w_id={}".format(w_id,d)
                    c1.execute(query)
                    con.commit()
                    print("##RECORD UPDATED##")
                else:
                    exit(0)
                ans=input("UPDATE MORE[Y]:")

    def delete_doctor_details():
        ans='y'
        while ans.lower()=='y':
            d_id = int(input("ENTER d_id TO SEARCH :"))
            query="select * from doctor_details where d_id={}".format(d_id)
            c1.execute(query)
            result = c1.fetchall()
            if c1.rowcount==0:
                print("Sorry ! d_id not found")
            else:
                print("%10s"%"d_id","%20s"%"d_name","%10s"%"d_age","%20s"%"d_department","%10s"%"d_phono")
            for row in result :
                print("%10s"%row[0],"%20s"%row[1],"%10s"%row[2],"%20s"%row[3],"%10s"%row[4])
                choice=input("\n## ARE YOU SURE TO DELETE??(Y):")
            if choice.lower()=='y':
                query="delete from doctor_details where d_id={}".format(d_id)
                c1.execute(query)
                con.commit()
            print("=== RECORD DELETED SUCCESSFULLY! ===")
            ans=input("DELETE MORE ?(Y):")  

    def delete_patient_details():
        ans='y'
        while ans.lower()=='y':
            p_id = int(input("ENTER p_id TO SEARCH :"))
            query="select * from patient_details where p_id={}".format(p_id)
            c1.execute(query)
            result = c1.fetchall()
            if c1.rowcount==0:
                print("Sorry ! p_id not found")
            else:
                print("%10s"%"p_id","%20s"%"p_name","%10s"%"p_age","%20s"%"p_problems","%10s"%"p_phono")
            for row in result:
                print("%10s"%row[0],"%20s"%row[1],"%10s"%row[2],"%20s"%row[3],"%10s"%row[4])
                choice=input("\n## ARE YOU SURE TO DELETE??(Y):")
            if choice.lower()=='y':
                query="delete from patient_details where p_id={}".format(p_id)
                c1.execute(query)
                con.commit()
            print("=== RECORD DELETED SUCCESSFULLY! ===")
            ans=input("DELETE MORE ?(Y):")  

    def delete_worker_details():
        ans='y'
        while ans.lower()=='y':
            w_id = int(input("ENTER w_id TO SEARCH :"))
            query="select * from worker_details where w_id={}".format(w_id)
            c1.execute(query)
            result = c1.fetchall()
            if c1.rowcount==0:
                print("Sorry ! w_id not found")
            else:
                print("%10s"%"w_id","%20s"%"w_name","%10s"%"w_age","%20s"%"w_workname","%10s"%"w_phono")
            for row in result:
                print("%10s"%row[0],"%20s"%row[1],"%10s"%row[2],"%20s"%row[3],"%10s"%row[4])
                choice=input("\n## ARE YOU SURE TO DELETE??(Y):")
            if choice.lower()=='y':
                query="delete from worker_details where w_id={}".format(w_id)
                c1.execute(query)
                con.commit()
            print("=== RECORD DELETED SUCCESSFULLY! ===")
            ans=input("DELETE MORE ?(Y):")  



            
    def create_bill_details():
        c1=con.cursor()
        c1.execute("create table bill_details(p_id int(5), p_name varchar(25) primary key ,p_age int(3),drvisit int(15),medicines int(15),room int(15))")
        print('table created')

    def insert_bill_details():
        print('Enter Charges of patient in Bill')
        p_id=int(input('Enter Patient ID:'))
        p_name=input('Enter Patient Name:')
        p_age=int(input('Enter Age:'))
        drvisit=int(input('Enter the fees of doctor visit:'))
        medicines=int(input('Enter the cost of medicines:'))
        room=int(input('Enter Room Charges:'))
        sql_insert= "insert into bill_details values({},'{}','{}','{}','{}','{}')".format(p_id,p_name,p_age,drvisit,medicines,room)
        c1.execute(sql_insert)
        print("SUCCESSFULLY REGISTERED")
        con.commit()

    def show_records_bill():
        print('Create table for Records Bills')
        c1.execute("select * from bill_details")
        data=c1.fetchall()
        for i in data:
            print(i)
        con.commit()
        print(data)

    def delete_bill_details():
        ans='y'
        while ans.lower()=='y':
            p_id = int(input("ENTER p_id TO SEARCH :"))
            query="select * from bill_details where p_id={}".format(p_id)
            c1.execute(query)
            result = c1.fetchall()
            if c1.rowcount==0:
                print("Sorry ! p_id not found")
            else:
                print("%10s"%"p_id","%20s"%"p_name","%10s"%"p_age","%20s"%"drvisit","%20s"%"medicines","%20s"%"room")
            for row in result:
                print("%10s"%row[0],"%20s"%row[1],"%10s"%row[2],"%20s"%row[3],"%20s"%row[4],"%20s"%row[5])
                choice=input("\n## ARE YOU SURE TO DELETE??(Y):")
            if choice.lower()=='y':
                query="delete from bill_details where p_id={}".format(p_id)
                c1.execute(query)
                con.commit()
            print("=== RECORD DELETED SUCCESSFULLY! ===")
            ans=input("DELETE MORE ?(Y):")  

        

    opt=""
    opt=int(input("enter your choice:"))
    if opt==1:
        about()
    elif opt==2:
        create_doctor_details()
    elif opt==3:
        insert_doctor_details()
    elif opt==4:
        show_records_doctor_details()
    elif opt==5:
        create_patient_details()
    elif opt==6:
        insert_patient_details()
    elif opt==7:
        show_records_patient_details()
    elif opt==8:
        create_worker_details()
    elif opt==9:
        insert_worker_details()
    elif opt==10:
        show_records_worker_details()
    elif opt==11:
        search_doctor_details()
    elif opt==12:
        search_patient_details()
    elif opt==13:
        search_worker_details()
    elif opt==14:
        update_patient_details()
    elif opt==15:
        update_doctor_details()
    elif opt==16:
        update_worker_details()
    elif opt==17:
        delete_doctor_details()
    elif opt==18:
        delete_patient_details()
    elif opt==19:
        delete_worker_details()
    elif opt==20:
        create_bill_details()
    elif opt==21:
        insert_bill_details()
    elif opt==22:
        show_records_bill()
    elif opt==23:
        delete_bill_details()

    else:
        print('invalid option')

    ans=input("Press y to continue:")
    
    

    



