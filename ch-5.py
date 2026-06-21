"""i=1
while i <= 5:
    print("manish",i)
    i+=1

# print number from 1 to 5

i=1
while i<=5:
    print(i)
    i+=1
"""
#Q1 print number from 1 to 100

"""i=1
while i<=100:
    print(i)
    i+=1"""

#Q2 print number from 100 to 1
"""
i=100
while i>=1:
    print(i)
    i-=1
"""

#Q3 print the multiplication table of a number n
"""
n=int(input("enter the n number"))
i=1
while i <=10:
    print(n*i)
    i +=1
"""
#Q4 print the element of the follwing list using a loop:
# [1,4,9,16,25,36,49,64,81,100]

"""nums = [1,4,9,16,25,36,49,64,81,100]
idx=0
while idx < len(nums):
    print(nums[idx])
    idx +=1
"""

#Q5 search for a number x in this tuple using loop:
#(1,4,9,16,25,36,49,64,81,100)


"""nums = (1,4,9,16,25,36,49,64,81,100)
x=int(input("enter a number for search"))

i=0
while i< len(nums):
    if(nums[i] == x):
        print("found",i)
    i+=1
"""

#FOR LOOPS

#Q search for a number x in this tuple using loop:
#(1,4,9,16,25,36,49,64,81,100)
"""
nums = (1,4,9,16,25,36,49,64,81,100)
x=9
idx=0
for el in nums:
    if(el==x):
     print("we found x",idx)
     break
    idx+=1

else:
    print("end")
"""
#RANGE
"""for i in range(5):
 print(i)

for i in range(2,10):# (start ,stop)
 print(i)
"""
"""for i in range(2,10,2):#    (start, stop , step)
 print(i)"""

# ONLY EVEN NUMBER

"""for i in range(2,100,2):
  print(i)

# odd number
for i in range(1,100,2):
    print(i)"""

#print number from 1 to 100
"""
for i in range(1,101):
    print(i)"""
#print number from 100 to 1
"""for  i in range(100,0,-1):
    print(i)"""

# print the multiplication table of a number n.
"""n = int(input("give the value of n"))
for i in range(1,11,):
    print(n*i)"""

# pass statement
#pass is a null statent that does nothing.

"""for i in range(5):
    pass
  
print("do nothing")
"""

#Q WAP TO FIND THE SUM OF FIRST N natural NUMBER.(using while)
"""
n=8
sum=0
i=1
while i <=n:
    sum +=i
    i +=1
    print("total sum =",sum)
"""

#Q WAP TO FIND THE FACTORIAL OF FIRST N NUMBER.(USING FOR)

n=6
mult =1
i=1
for i in range(1,n+1):
    mult*=i

    print(mult)