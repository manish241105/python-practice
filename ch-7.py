#file Input/Output

# read mode 
"""f= open("demo.txt","r")
data= f.read()# read entire file
print(data)
f.close() 
"""

#for line by line at a time we use f.readline()
"""f=open("demo.txt","r")
line1 = f.readline()
print(line1)

line2= f.readline()
print(line2)"""

#write mode
"""f=open("demo.txt","w")
data =f.write("this is my new line and i complte python in june")

f.close()"""

#append

"""f=open ("demo.txt","a")
data = f.write("\nplease also add this")#fro new line add in front of line "\n".
f.close()

"""
#with syntax

"""with open("demo.txt","r")as f:
    data = f.read()
    print(data)#this is not importaant
"""
#deleting a file-->we use os mosdule usse import os
"""import os
os.remove("demo.txt")#--> delete a demo .txt file in a system.
"""

#Qusetion 

#Q1 create a new file "practice.txt" using python. add the following data in it.
"""
hi everyone 
we are learning file I/O
using java 
i like programming in java.
"""
#solution 
"""
f=open("practice.txt","w")
data= f.write("hi everyone\nwe are learning file I/O\nusing java\ni like programmming in java\n")
print(data)
f.close()
"""

#Q2 WAF that replace all ocurrenes of "java" with "python" in above file.
"""
f=open("practice.txt","r")
data = f.read()
new_data=data.replace("java","python")
print(new_data)
f.close()


f=open("practice.txt","w")
data = f.write(new_data)

f.close()
"""

#Q3 search if the world "learning" exists in the fileor not.
"""

f=open("practice.txt","r")
data=f.read()
new_data=data.find("learning")
print(new_data)
f.close()#--> this code give number not a answer in yes or no fir this swe use this code in lower side.
"""
#this code give claude 
"""f = open("practice.txt", "r")
data = f.read()

if "learning" in data:
    print("Yes, learning word exists in the file")
else:
    print("No, learning word does not exist in the file")

f.close()"""

f=open("practice.txt","r")
data=f.read()
new_data=data.count("learning")
print(new_data)
f.close()



