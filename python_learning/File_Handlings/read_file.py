# using read() -> read entire file at once
with open("students.txt", 'r') as f1:
    print("-----Using read()-----")
    print(f1.read())

# -------------------------------------
# using readline -> reads line by line(one line each call)
with open("students.txt", 'r') as f2:
    line1 = f2.readline()
    line2 = f2.readline()
    print("-----Using readline()-----")
    print(line1.strip())
    print(line2.strip())
    print("\n")
# -------------------------------------
# using readlines -> reads all lines and stores them in a list
with open("students.txt", 'r') as f3:
    print("-----Using readline()-----")
    lines = f3.readlines()
    for line in lines:
        print(line.strip())
