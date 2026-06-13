#list

"""marks= [89.2,85.69,85,95.8,99.8]
print(marks)
print(type(marks))
print(marks[0]) 
"""
"""
student = ["manish",98,19,"male"]
print(student[0])
student[0] = "manish kumar"
print(student)"""


# list=[2,1,3,1]
"""
print(list.append(4))#append() method adds one element to the end of the list.
print(list.sort())#sort() method sorts the list in ascending order by default.
print(list.sort(reverse=True))#sort() method sorts the list in descending order."""
"""
print(list.reverse())#reverse() method reverses the order of the list in original list.
list.insert(1,5)#insert() method inserts an element at the specified position in the list.
list.remove(1)#remove() method removes the first occurrence of the specified element from the list.

"""
"""
list.pop(2)#pop() method removes and returns the last element of the list.
print(list)"""
 
#WAP to ask the user to enter their 3 favourite movies and store them in a list and print the list.
"""
list=[]
print("Enter your 3 favourite movies")
movies=input("movie 1:\n, movie 2:\n, movie 3:\n")
list.append(movies)
print(list)

"""
#WAP to check if a list contains a palindrone of element.
"""
list1=[1,2,3]

copylist1= list1.copy()
copylist1.reverse()

if(copylist1== list1):
    print("list1 is palindrome")
else:
    print("list1 is not palindrome")

"""

#WAP to count the number of studentt with "A" grade of the following tuple.


tup=("C","D","A","A","B","B","A")
print("the no of student with A grade")
tup1=tup.count("A")
print(tup1)

