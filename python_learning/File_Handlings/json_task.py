import os
import json


# To check file is existed or not
Filename = "Student_data.json"
if not os.path.exists(Filename):
    with open(Filename, 'w') as file:
        pass
    print(f"{Filename} is automatically created!")

# Add student
def add():
    try:
        roll = input("Enter Roll number:")
        try:
            with open(Filename, 'r' ) as file:
                data = json.load(file)
        except json.JSONDecodeError:
            data = {}
        
        if roll not in data:
            name = input("Enter student Name :")
            branch = input("Enter branch :")
            phy_m = float(input("Enter physics marks :"))
            com_m = float(input("Enter computer marks :"))
            chem_m = float(input("Enter chemistry marks :"))
            marks = {"physics": phy_m, "computer" : com_m, "chemistry" : chem_m}
            data[roll] =  {"name" : name, "branch" : branch, "marks" : marks}
            with open(Filename, 'r+' ) as file:
                json.dump(data, file, indent=4)
            os.system('cls')
            print(f"Roll.no {roll} is added !")
        else:
            print(f"Roll.No: {roll} already  existed")
    except ValueError:
        print("Enter valid input!")
    except Exception as e:
        print(f"Unexpected error :{e}")
    
# Display single student details
def display_student():
    try:
        roll = input("Enter student roll number : ")
        with open(Filename, 'r' ) as file:
            data = json.load(file)
        if data[roll]:
            print(f"Name : {data[roll]['name']},\nRoll.no :\n{roll}, Branch :\n{data[roll]['branch']}")
            print("Marks :")
            for sub, marks in data[roll]['marks'].items():
                print(f"{" " * 7}{sub} : {marks}")


            # print(data[roll])
        else:
             print("student not found!")
    except Exception as e:
        print(f"Unexpected error : {e}")

# To check student is existed or not
def check(roll):
    with open(Filename, 'r' ) as file:
        data = json.load(file)
    if roll  in data:
        return True
    else:
        return False

# To update details of student

def update():
     roll = input("Enter student roll number : ")
     with open(Filename, 'r' ) as file:
            data = json.load(file)
     Data = check(roll)
     if Data:
        print("What you want to do update?")
        print("1.Roll Number")
        print("2.Name")
        print("3.Branch")
        print("4.marks")
        choice = input("Enter what you want to update :")
        os.system('cls')
        if choice == '1':
            new_roll = input("Enter new roll number : ")
            old_data = data[roll]
            del data[roll]
            data[new_roll] = old_data
            with open(Filename, 'w' ) as file:
                data = json.dump(data,file, indent = 4)
            print(f"Roll.no : {roll} changed to New roll.no :{new_roll}")
        elif choice == '2':
            new_name = input(f"Enter new name to Roll.no{roll} ")
            old_name = data[roll]['name']
            data[roll]['name'] = new_name
            with open(Filename, 'w' ) as file:
                data = json.dump(data,file, indent = 4)
            print(f"Roll.no : {roll}, Name {old_name} changed to {new_name}")

        elif choice == '3':
            new_branch = input(f"Enter new branch to Roll.no :{roll} ")
            old_branch = data[roll]['branch']
            data[roll]['branch'] = new_branch
            with open(Filename, 'w' ) as file:
                data = json.dump(data,file, indent = 4)
            print(f"Roll.no : {roll}, Branch {old_branch} changed to {new_branch}")

        elif choice == '4':
            try:
                print("1.specific subject")
                print("2.All subjects")
                choose = input("Enter your choice :")
                os.system('cls')
                if choose == '1':
                    print("1.physics")
                    print("2.computer")
                    print("3.chemistry")
                    option = input("choose one subject 1 to 3 :")
                    os.system('cls')
                    if option == '1':
                        new_p_marks  = float(input("Enter new physics marks :"))
                        old_marks =  data[roll]['marks']['physics']
                        data[roll]['marks']['physics'] = new_p_marks
                        with open(Filename, 'w' ) as file:
                            data = json.dump(data,file, indent = 4)
                        print(f"Roll.no :{roll} Marks : {old_marks} changed to {new_p_marks}")
                    elif option == '2':
                        new_c_marks  = float(input("Enter new computer marks :"))
                        old_marks =  data[roll]['marks']['computer']
                        data[roll]['marks']['computer'] = new_c_marks
                        with open(Filename, 'w' ) as file:
                            data = json.dump(data,file, indent = 4)
                        print(f"Roll.no :{roll} Marks : {old_marks} changed to {new_c_marks}")
                    elif option == '3':
                        new_ch_marks  = float(input("Enter new chemistry marks :"))
                        old_marks =  data[roll]['marks']['chemistry']
                        data[roll]['marks']['chemistry'] = new_ch_marks
                        with open(Filename, 'w' ) as file:
                            data = json.dump(data,file, indent = 4)
                        print(f"Roll.no :{roll} Marks : {old_marks} changed to {new_ch_marks}")
                    else:
                        print("Enter valid choice!")
                elif choose == '2':
                    try:
                        old_mar = data[roll]['marks']
                        print("Enter marks respectively in this order (physics/computer/chemistry)")
                        new_marks = list(map(float, input("Enter marks separted by ',' :").split(',')))
                        data[roll]['marks']['physics'] = new_marks[0]
                        data[roll]['marks']['computer'] = new_marks[1]
                        data[roll]['marks']['chemistry'] = new_marks[2]
                        with open(Filename, 'w' ) as file:
                            data = json.dump(data,file, indent = 4)
                        with open(Filename, 'r' ) as file:
                            data = json.load(file)
                            new_mar = data[roll]['marks']
                        print(f"Roll.no :{roll} old marks = {old_mar} changed to {new_mar}")
                    except Exception as e:
                        print(f"Unexcepted error : {e}")
            except Exception as e:
                print(f"Unexpected error : {e}")
            else:
                print(" Enter valid choice!")      
        else:
            print("Enter valid choice!")
     else:
         print(f"Student with Roll.no {roll} is not found to update details!")
    

# To delete student
def delete():
    try:
        roll_num = input("Enter roll to delete :")
        with open(Filename, 'r') as file:
            data = json.load(file)
        if data[roll_num]:
            del data[roll_num]
            with open(Filename, 'w') as file:
                json.dump(data, file, indent = 4)
            print(f"Student with Roll.no:{roll_num} is deleted!")
        else:
            print(f"Opps! student not found.")
    except Exception as e:
        print(f"Unexpected error : {e}")

# To display all students
def display():
    try:
        with open(Filename, 'r')  as file:
            data = json.load(file)
        for roll, details in data.items():
                print(f"Name : {details['name']}\nRoll.no : {roll}\nBranch : {details['branch']}")
                print("Marks :")
                for sub, marks in details['marks'].items():
                    print(f"{" " * 7}{sub} : {marks}")
    except Exception as e:
        print(f"Unexcepted error : {e}")

def main_menu():
    print("------Welcome to student management system----------- ")

    while True:
        print(f"\n{'-' * 30}")
        print("1.Add student")
        print("2.Display particular student")
        print("3.Update student details")
        print("4.Delete a student")
        print("5.Display all students")
        print("6.Exit")

        choice = input("Enter your choice(1 to 6) :")
        if choice == '1':
            os.system('cls')
            add()
        elif choice =='2':
            os.system('cls')

            display_student()
        elif choice =='3':
            os.system('cls')
            update()
        elif choice =='4':
            os.system('cls')
            delete()
        elif choice =='5':
            os.system('cls')
            display()
        elif choice =='6':
            os.system('cls')
            print("Thank you for using our student management system")
            break
        else:
            os.system('cls')
            print("Enter valid choice")

if __name__ =="__main__":
    main_menu()




