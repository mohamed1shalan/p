# sec1.py
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 27 20:44:29 2023

@author: Computec
"""
# creating a text file with the command function "x"
f = open("mydata.txt", "r")

# f.write("\nPRevious  Line")
# f.write("\nnew  Line")

lines = ["\nThis is first line \n", "This is second line \n", "Third line \n"]

# f.writelines(lines)

print(f.read(5))
print(f.tell())
f.seek(0)
print(f.tell())
print(f.readline())
print(f.tell())
f.close()

# f.write("Change \n")

# print(f.read(4))
#
# print(f.tell())
# print(f.readline())
# print(f.tell())

# print(len(f.readline()))

# print(f.tell())
# f.seek(0)
# print(f.readline())
# print(f.readline())
"""
#creating a text file with the command function "w" if it is not exists
#f = open("newfile.txt", "w")
lines=["This is first line \n","This is second line \n","Third line \n"]

#This "w" command can also be used create a new file but 
#unlike the the "x" command the "w" command will overwrite any existing file found with the same file name.
f.write("Hello 2\n")
f.write("New Line 2\n")
f.write("New new Line 2\n")
f.writelines(lines)
f.write("overwrite 2\n")


f.write("Again overwrite 2\n")"""

# print(f.read())
# print(f.readline())
# print(f.readline()
# f.seek(0)
# print(f.read(12))
# f.close()
