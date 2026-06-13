str1= "name"
str2= "hello"
str3=  str1 +  str2
"""print(str3)
print(len(str3))
print(str3[0])
print(str3[1: ])
print(str3[:-1])
print(str3.endswith("loo"))"""#--->it print False 
                                #because str3 is "namehello" and it does not '
                                #end with "loo"
#print(str3.endswith("llo"))-->it print True because str3 is "namehello" and it does end with "llo"
#print(str3.capitalize())#--->it print "Namehello" because it capitalize the first letter of the string and make the rest of the letters lowercase
#print(str3.replace("hello", "manish"))#--->it print "namemanish" because it replace "hello" with "manish" in the string str3
#print(str3.replace("l", "o"))#--->it print "nameheooo" because it replace "l" with "o" in the string str3



# WAP to input user's first namr and print its lengths.

"""firstname = input("enter your first name")
print("length of first name is ", len(firstname))"""

# WAP to count how many $ in the given string.
"""
str= "my name is manish and i love print $$$$$$ in computer"
print(str.count("$"))

"""
"""marks= int(input("enter your marks"))
if (marks >= 90):
    grade = "A"
elif (90> marks >80):
    grade = "B"
elif(80>marks>=70):
    grade = "C"
else:
    grade = "D"

print("grade of student is ", grade)"""

# NESTING (ek statement ke andar dusra statement)

"""age= 3

if(age >= 18):
    
    if(age >= 80):
        print("cannot drive")
    else:
        print("can drive")
else:
    print("cannot drive")"""


# WAP to input a number and check whether it is even or odd.
"""number = int(input("enter a number:"))
if (number%2 ==0):
    print("number is even")
else:
        print("number is odd")
"""

# WAP to find the greatest of 3 numbers by the user.
"""
num1 = int(input("enter first number:"))
num2 = int(input("enter second number:"))
num3 = int(input("enter third number:"))    
if (num1 > num2 and num1 > num3):
    print("num1 is greatest")
elif (num2 > num1 and num2 > num3):
    print("num2 is greatest")
else:    print("num3 is greatest")  
"""
    
#WAP TO CHECK IF A NUMBER IS A MULTIPLE OF 7.   
"""number = int(input("enter a number:"))
if (number%7 == 0):
    print("number is a multiple of 7")  
else:
    print("number is not a multiple of 7")
    """