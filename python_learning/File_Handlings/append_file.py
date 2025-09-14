# Before append data 
with open("students.txt",'r') as f:
    data = f.read()
    print("-----Old data before appending new data-----")
    print(data)

# Append new data
with open("students.txt", "a+") as file:
    New_data = ["Name : potti\n","Branch : Bpharmcy\n","college: Teliyadhu\n\n","Name : Bujji\n", "Branch : AI\n", "College : RK\n\n"]

    file.writelines(New_data)
    file.seek(0)
    print("-----New data after appending new data-----")
    data = file.read()
    print("This\n",data)


# output: 
'''

-----Old data before appending new data-----
Name: Razu
Branch: cse
College: RK

Name: swathi
Branch: physics
College: C4

Name: Jr
Branch: Teliyadhu
College: RK




-----New data after appending new data-----
This
 Name: Razu
Branch: cse
College: RK

Name: swathi
Branch: physics
College: C4

Name: Jr
Branch: Teliyadhu
College: RK

Name : potti
Branch : Bpharmcy
college: Teliyadhu

Name : Bujji
Branch : AI
College : RK


'''