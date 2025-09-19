import json
Data = {
    "Name":"Raju",
    "Section" :"C1",
    "College" : "AU",
    "Marks" : [99, 85, 96]
}

json_string = json.dumps(Data, indent=5)
print("Python dict converted into json string")
print(json_string)

# Write JSON into file
with open("student.json", 'w') as f:
    json.dump(Data, f, indent=5)

print("\nstudent.json file created !")

# Read JSON from file
with open("student.json", 'r') as f:
    data = json.load(f)

print("Reading JSON file:")
print(data)
print(data["Marks"])