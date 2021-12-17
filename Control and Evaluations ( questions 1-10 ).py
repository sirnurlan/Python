print("---------------Q_1 :-----------------------------------------------------------------------------")
# 2 ** 3 ** 2 ** 1 is :?
#ans : 512
print(2 ** 3 ** 2 ** 1)

print("---------------Q_2 :-----------------------------------------------------------------------------")
# If you want to build a string that reads:?
# Peter's sister's name's  "Anna"
# Which of the following literals would you use (SELECT all that apply)
#ans :
print("Peter's sister's name's  \"Anna\"")
print('Peter\'s sister\'s name\'s "Anna"')


print("---------------Q_3 :-----------------------------------------------------------------------------")
# What is the expected output of the following snipped?
i=250
while len(str(i))>72:
    i*=2
else:
    i//=2
print(i)
#ans : 512
print("---------------Q_4 :-----------------------------------------------------------------------------")
# What snipped would you insert in the line indicated below:
n=0
while n<4:
    n+=1
    # insert your code here
    print(n, end=" ")

# to print the following string to the monitor after the loop finishes its execution: 1 2 3 4
# ans : print(n, end=" ")

print("---------------Q_5 :-----------------------------------------------------------------------------")
# What is the value type returned after executing the following snippet? :
x=0
y=2
z=len("Python")
x=y>z
print(x)
# ans : False

print("---------------Q_6 :-----------------------------------------------------------------------------")
# What will the final value of the Val variable be when the following snippet finishes its execution? :
Val =1
Val2=0
Val =Val^Val2
Val2=Val^Val2
Val =Val^Val2
print(Val)
# ans : 0

print("---------------Q_7 :-----------------------------------------------------------------------------")
# What line can be used instead of the comment to cause the snipped to produce the following
# expected output? (Select all that apply) :
# Code:
z,y,x=2,1,0
x,z  =z,y
y    =y-z
# put line here
# A)x,y,z=y,z,x
z,y,x=x,z,y
print(x,y,z)

print("---------------Q_8 :-----------------------------------------------------------------------------")
# What is the expected output of the following snippet ? :
a=0
b=a**0
if b<a+1:
    c=1
elif b==1:
    c=2
else:
    c=3
print(a+b+c)
# ans : 3

print("---------------Q_9 :-----------------------------------------------------------------------------")
# How many stars (*) does the following snipped print ? :
i=10
while i>0:
    i-=3
    print("*")
    if i<=3:
        break
else:
    print("*")
# ans : three (*)

print("---------------Q_10 :-----------------------------------------------------------------------------")
# How many lines does each of the following code examples output when run separately ? :
# Example 1
print("example_1----------------")
for i in range(1,4,2):
    print("*")
print("example_1----------------")
# Example 2
print("example_2----------------")
for i in range(1,4,2):
    print("*", end="")
print("example_2----------------")
# Example 3
for i in range(1,4,2):
    print("*",end="**")
print("example_3----------------")
# Example 4
for i in range(1,4,2):
    print("*",end="**")
print("***")
print("example_4----------------")
# ans : three (*)






