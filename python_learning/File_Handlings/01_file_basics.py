# File handling modes in python 
'''
'r' - Read mode
'w' - write mode
'a' append mode
'x' create mode
'r+' - Read + write mode 
'w+' - write + read mode 
'a+' - Append + read mode
 '''

# 1.Create & Write File
f = open("sample.txt", "w")
f.write("Hello mama! File handlings start ayyindhi \n")
f.close() # AT the end closing the file is important 

# 2.Read File
f = open("sample.txt", "r")
print(f.read()) 
f.close()
# Hello mama! File handlings start ayyindhi 

# 3.Append File
f = open('sample.txt', 'a')
f.write("Next line add ayyindhi.")
f.close()

