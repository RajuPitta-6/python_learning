# creating and writing data into file
with open("demo.txt", 'w') as file:
    file.write("Hello world\n")
    file.writelines(["Python file handlings.\n","This is demo file\n"])

# Reaading and using file pointer
with open("demo.txt", 'r') as file:
    print("Intitial pointer position :", file.tell())
    data = file.read(5) # Read first 5 chars
    print("Data Read :",data)
    print("pointer after reading 5 chars :", file.tell())
    file.seek(0) # pointer moves to starting 
    print("pointer after seek(0) :",file.tell())
    full_data = file.read()
    print(f"---------Full data ---------\n{full_data}")

# Output:
'''
Intitial pointer position : 0
Data Read : Hello
pointer after reading 5 chars : 5
pointer after seek(0) : 0
---------Full data ---------
Hello world
Python file handlings.
This is demo file
'''