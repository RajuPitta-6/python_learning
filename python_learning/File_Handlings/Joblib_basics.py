import joblib
import os
FileName = 'student.pkl'
data = {
        "name": "Raju",
        "section": "c1",
        "college ": "AU",
        "marks": [95, 80, 92]}


if os.path.exists(FileName):
    old_data = joblib.load(FileName)
    print("Before adding data using joblib :")
    print(old_data)

    if isinstance(old_data, dict):
         old_data = [old_data]
    else:
         old_data = []
else:
     old_data = data

old_data.append(data)
joblib.dump(old_data, FileName)
new_data = joblib.load(FileName)
print("After adding/updating data using joblib :")
print(new_data)

# output:
'''
Before adding data using joblib :
{'name': 'Ram', 'section': 'c2', 'college ': 'AU', 'marks': [65, 70, 92]}
After adding/updating data using joblib :
[{'name': 'Ram', 'section': 'c2', 'college ': 'AU', 'marks': [65, 70, 92]}, {'name': 'Raju', 'section': 'c1', 'college ': 'AU', 'marks': [95, 80, 92]}]
'''