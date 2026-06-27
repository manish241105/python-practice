#function 

"""
def calulategmean(a,b):
    mean= (a*b)/(a+b)
    print (mean)


def isgreater(a,b):#this is code for if else statement in porgrome we donot write 
                   #many time in this code. we write only one time in the code and define this as a fnction use so many time.
    if(a>b):
        print("first number is greater")
    elif(a==b):
        print("both number is equal ")
    else:
        print("second number is greaater")
def islower(a,b):
    pass# pass mean do noting and go to next part.


a=int(input("enter a number value"))
b=int(input("enter b number value"))
isgreater(a,b)
calulategmean(a,b)


c=int(input("enter c number value"))
d=int(input("enter d number value"))
isgreater(c,d) 
calulategmean(c,d)


f= int(input("enter f number value"))
e=int(input("enter eororngg E is number value"))
calulategmean(f,e)
"""

#function argument:-
"""
There are 4 type of function argument :-

1. Default argument :- value na do toh default use ho
                        def average (a=4,b=4):in this part a or b ki value 4
                                              hai toh average hoga 4.0.
                            print("the averahe is ",(a+b)/2)
                            average(4,6) par yah a or b ki value 4 or 6 ho jagi ir agar mai a ye b 
                                        ki value na du toh value default le lega jo first number pe hogi.

                                                            


2. keyword argumnet :- naam se value do, order nahi matter 
                       def info(name, age):
    print(name, age)

info("Manish", 20)   # name=Manish, age=20 ye default hai first pe name or second pa age.
info(age=20, name="Manish")   # same result, order change kiya is mai age frist or name second.



3. variable length argument:- add multiple number in this argument 
                        def total(*numbers):--->this make tuple after wrute (*number),, (**number)-->this is make dictinory
    print(sum(numbers))

total(1, 2, 3, 4)    # output: 10



4. required argument:-yeh basic positional argument hi hai jisme value dena zaroori hai, warna error aa jaata hai.
                    def greet(name):
    print("Hello", name)

greet("Manish")    # ✅ kaam karega
greet()             # ❌ ERROR - kyunki 'name' required hai

 """





#question

#Q1 WAP to print the length of a list.
"""
list1=["om","oren" , "idf","nurgmu","inv","gnvi","gv"]


def print_len(list):
    print(len(list))



print_len(list1)"""

#Q2 WAP to print the elements of a list in a single line.
"""
name = ["ram", "sam", "sarthak", "manish", "gagan", "gaurav"]

def print_name(name1):
    for naam in name1:
        print(naam, end=" ")

print_name(name) 
"""

#Q3 WAP TO FIND THE FACTORIAL OF N.
"""def cal_fact(n):
    fact =1
    for i in range(1,n+1):
        fact *=i
    print(fact)
    return fact 

cal_fact(5)"""

#Q4 WAP to conert USD TO INR

"""def usd_coversion(usd):
    inr= usd*94.78
    print(usd,"USD = " , inr , "Rupees")

usd_coversion(100)

"""

#Q5 number is odd or even
"""
def number_system(numb):
      if(numb%2==0):
        print("number is even")
      else:
        print("number is odd")


num=int(input("enter your number"))
number_system(num)

"""


#RECURSION 

"""def ahow(n):
    if(n==0):
        return
    print(n)
    ahow(n-1)
    print("end")
ahow(5)"""


"""def fact(num):
    if(num ==0 or num ==1):
        return 1
    return num * fact(num-1)
print(fact(5))"""


#Q1 WAP TO PRINT SUM OF FRIST NATURAL NUMBER

"""def sum_natural(num):
    if(num==0):
        return 0
    return num + sum_natural(num-1)

print(sum_natural(10))"""


#Q2 WAPA TO PRINT ALLL ELEMENTS IN A LIST

list=["a","b","c","d"]
def list_1(list,idx=0):
    if(idx == len(list)):
        return
    print(list[idx]) 
    list_1(list, idx +1)


list_1(list)