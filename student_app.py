import mysql.connector
mydb= mysql.connector.connect(host = 'localhost' , user = 'root' , password = '' , database = 'studentdb')
mycursor = mydb.cursor()
while True:

    print("select an option from menu")

    print("1 add student")

    print("2 view all student")


    print("3 search a student")

    print("4 update the student")

    print("5 delete a student")

    print("6 exit")
    choice = int(input("Enter an option: "))
    if(choice==1):

        print("add student details ")
        name=input("enter the name")
        rollnumber=input("enter the rollno")
        admno = input("enter the adminno")
        college = input("enter the college name")
        sql ='INSERT INTO `studentS`(`name`, `rollnumber`, `admno`, `college`)VALUES(%s,%s,%s,%s)'
        data = (name,rollnumber,admno,college)
        mycursor.execute(sql , data)
        mydb.commit()


        
    elif(choice==2):

        print('view all student')


        sql = 'SELECT * FROM `students`'

        mycursor.execute(sql)

        result = mycursor.fetchall()

        for i in result:

            print(i)

    elif(choice==3):

        print("search student selected")
        admo = input('enter the adm number you needed : ')
        sql = 'SELECT `name`, `admno`, `rollnumber`, `college` FROM `students` WHERE `admno`= '+admo
        mycursor.execute(sql)
        result = mycursor.fetchall()
        print(result)

    elif(choice==4):

        print("update student selected")
        admno = input('enter the adminnumber to be updated : ')
        name = input('enter the name for the update: ')
        #admo = input('enter the adminnumber')
        rollno = input('enter the roll no to be updated : ')
        college = input('enter the college name to be updated : ')
        sql=  "UPDATE `students` SET `name`='"+name+"',`rollnumber`='"+rollno+"',`admno`='"+admno+"',`college`='"+college+"' WHERE 'admno'="+admno
        mycursor.execute(sql)
        mydb.commit()
        print('Succesfully updated !!!')

    elif(choice==5):

        print("delete student selected")

    elif(choice==6):

        break