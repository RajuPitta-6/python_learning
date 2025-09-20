import pickle

Data = {
    "Name":"Raju",
    "Section" :"C1",
    "College" : "AU",
    "Marks" : [99, 85, 96]
}

# save the object to the binary file
with open("student.pkl", "wb") as file:
    pickle.dump(Data, file)

print("student.pkl file created and data stored")

# Load object back
with open("student.pkl", "rb") as file:
   data =  pickle.load(file)
print("Loaded student data :", data)