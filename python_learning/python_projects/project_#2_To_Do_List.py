def add_student_data():
    Roll = input("Enter Roll number of a Student : ")
    find = find_student(Roll)
    if find:
        print(f"Student with Roll number {Roll} already exist")
    else:
        Name = input("Enter Name of the student : ")
        Marks = input("Enter Marks of the student : ")
        phn = input("Enter phone number of the student : ")
        Data[Roll] = {'Name':Name,"Marks":Marks,"Contact":phn}
        print("Student data added successfully!")
def Display_student_data():
    Roll = input("Enter Roll number of a Student : ")
    find = find_student(Roll)
    if find:
        print(f"Name : {Data[Roll]['Name']}, Roll :{Roll}, Marks : {Data[Roll]['Marks']}, Phn : {Data[Roll]['Contact']}")
    else :
        print("Student not found!")
def Display_all_data():
    if not Data:
        print("Data is empty!")
    else:
        print("---------- Student Records -----------\n")
        for roll, info in Data.items():
            print(f"Roll_no : {roll}, Name : {info['Name']}, Marks : {info['Marks']}, ph_no : {info['Contact']}")
def Delete_student():
    Roll = input("Enter Roll number of a Student : ")
    find = find_student(Roll)
    if find:
        del Data[Roll]
        print("Deleted student sucessfully .")
    else:
        print("Student not found")
def find_student(roll):
   return roll in Data
Data = {}
print("+"*6 + "Welcome my To DO List project" + "+"*6)
while True:
    

    print("1.Add new student")
    print("2.Display a particular student data")
    print("3.Diplay all students data")
    print("4.delete a student data")
    print("5.Exit")

    choice = int(input("Enter your choice : "))
    if choice == 1:
        add_student_data()
    elif choice == 2:
        Display_student_data()
    elif choice == 3:
        Display_all_data()
    elif choice == 4:
        Delete_student()
    elif choice == 5:
        print("Thank you for using my project.")
        break
    else :
        print("Enter valid choice")


'''
Smaple output:
++++++Welcome my To DO List project++++++
1.Add new student
2.Display a particular student data
3.Diplay all students data
4.delete a student data
5.Exit
Enter your choice : 1
Enter Roll number of a Student : 23
Enter Name of the student : Raz
Enter Marks of the student : 875
Enter phone number of the student : 79899
Student data added successfully!
1.Add new student
2.Display a particular student data
3.Diplay all students data
4.delete a student data
5.Exit
Enter your choice : 1
Enter Roll number of a Student : 56
Enter Name of the student : Bujji
Enter Marks of the student : 805
Enter phone number of the student : 93988
Student data added successfully!
1.Add new student
2.Display a particular student data
3.Diplay all students data
4.delete a student data
5.Exit
Enter your choice : 1
Enter Roll number of a Student : 16
Enter Name of the student : xxxxxi
Enter Marks of the student : 9xx
Enter phone number of the student : xxx49
Student data added successfully!
1.Add new student
2.Display a particular student data
3.Diplay all students data
4.delete a student data
5.Exit
Enter your choice : 2
Enter Roll number of a Student : 23
Name : Raz, Roll :23, Marks : 875, Phn : 79899
1.Add new student
2.Display a particular student data
3.Diplay all students data
4.delete a student data
5.Exit
Enter your choice : 3
---------- Student Records -----------

Roll_no : 23, Name : Raz, Marks : 875, ph_no : 79899
Roll_no : 56, Name : Bujji, Marks : 805, ph_no : 93988
Roll_no : 16, Name : xxxxxi, Marks : 9xx, ph_no : xxx49
1.Add new student
2.Display a particular student data
3.Diplay all students data
4.delete a student data
5.Exit
Enter your choice : 4
Enter Roll number of a Student : 56
Deleted student sucessfully .
1.Add new student
2.Display a particular student data
3.Diplay all students data
4.delete a student data
5.Exit
Enter your choice : 3
---------- Student Records -----------

Roll_no : 23, Name : Raz, Marks : 875, ph_no : 79899
Roll_no : 16, Name : xxxxxi, Marks : 9xx, ph_no : xxx49
1.Add new student
2.Display a particular student data
3.Diplay all students data
4.delete a student data
5.Exit
Enter your choice : 5
Thank you for using my project.
'''