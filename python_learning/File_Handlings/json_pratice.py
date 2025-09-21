import json

student = {
    "ID" : 23,
    "Name":"Raju",
    "Branch":"AI/ML",
    "Marks" : {"Maths" : 85, "Python":99,"Ds":89},
    "email" : "raju123@gamil.com"
}
# Writing into json file
with open("Student.json", "w") as file:
    json.dump(student, file, indent=4)

print("Student data added into json file!")

# Reading from json file
with open("Student.json", "r") as file:
   data =  json.load(file)

print("Student data is reded from student.json file :\n", data)

# Updating in json file

with open("Student.json", "r") as file:
   data =  json.load(file)

data["Branch"] = "Data science"
print("Branch updated AI/ML to Data science")

# Deleting from json file
with open("Student.json", "r") as file:
   data =  json.load(file)
del data["email"]
print("email deletd from student.json file")
print(data)