import mysql.connector
mydb= mysql.connector.connect(host = 'localhost' , user = 'root' , password = '' , database = 'studentdb')
mycursor = mydb.cursor()
while True:

     print("Select an option from the menu ")
     print("1. Add student")
     print("2. View all student")
     print("3. Search a student")
     print("4. Update a student")
     print("5. Delete a student")
     print("6. Insert marks")
     print("7. View all mark")
     print("8. View subject wise marks")
     print("9. Individual student marks")
     print("10.exit")


     choice = int(input("Enter an option: "))
     if(choice == 1):
        print("Student enter selected")
        name = input("Enter name: ")
        rollno = input("Enter the rollnumber: ")
        admnum = input("Enter the admission number: ")
        college = input("Enter the college: ")
        sql = 'INSERT INTO `students`(`name`, `rollnumber`, `admno`, `college`) VALUES (%s,%s,%s,%s)'
        data = (name,rollno,admnum,college)
        mycursor.execute(sql,data)
        mydb.commit()
        print("Data inserted successfully.")
     elif(choice == 2):
        sql = 'SELECT * FROM `students`'
        mycursor.execute(sql)
        result = mycursor.fetchall()
        for i in result:
            print(i)

     elif(choice == 3):
        print("Searching a student")
        adm = input("Enter the admission number: ")
        sql = 'SELECT `id`, `name`, `rollnumber`, `admno`, `college` FROM `students` WHERE `admno` =  '+adm
        mycursor.execute(sql)
        result = mycursor.fetchall()
        print(result)
     elif (choice == 4):
        print("updating student")
        admnum = input("Enter the admission number: ")
        name = input("Enter name to be updated: ")
        rollno = input("Enter the rollnumber to be updated: ")
        
        college = input("Enter the college name to be updated: ")
        sql = "UPDATE `students` SET `name`='"+name+"',`rollnumber`='"+rollno+"',`college`='"+college+"' WHERE `admno`=" +admnum
        mycursor.execute(sql)
        mydb.commit()
        print("Updated successfully.")
     elif(choice == 5):
        print("delete a student")
        adm = input("Enter the admissionnumber: ")
        sql = 'DELETE FROM `students` WHERE `admno` = '+adm
        mycursor.execute(sql)
        mydb.commit()
        print("Data deleted successfully.")
     elif( choice ==6):
        print("Insert marks")
        adm = input("Enter the student admission number: ")
        sql = 'SELECT `id` FROM `students` WHERE `admno` =  '+adm
        mycursor.execute(sql)
        result = mycursor.fetchall()
        id = 0
        for i in result:
            id = str(i[0])
        print("Student id is: ",id)

        physics = input("Enter the physics marks: ")
        chemistry = input("Enter the chemistry marks:")
        maths  = input("Enter the maths mark: ")
        sql = "INSERT INTO `marks`(`studentid`, `physicsmark`, `chemistrymark`, `mathsmark`) VALUES (%s,%s,%s,%s)"
        data = (id,physics,chemistry,maths)
        mycursor.execute(sql,data)
        mydb.commit()
        print("Marks data inserted successfully.")

     elif(choice==7):
        print("View all marks")
        sql = "SELECT s.`name`, s.`rollnumber`, s.`admno`, s.`college`,m.physicsmark,m.chemistrymark,m.mathsmark FROM `students` s JOIN marks m ON s.id = m.studentid"
        mycursor.execute(sql)
        result = mycursor.fetchall()
        for i in result:
            print(i)

     elif(choice == 10):
        break