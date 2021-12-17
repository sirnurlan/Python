print("--------------------------Q_21--------------------------------------------------------------")
# What is the expected behaviour of the following snippet?
def fun(a,b=0, c=5, d=1):
    return a**b**c
print(fun(b=2,a=2,c=3))
# It will print :
# ans : 256

print("--------------------------Q_22--------------------------------------------------------------")
# What is the expected behaviour of the following snippet?
x=5
f=lambda x:1+2
print(f(x))
# It will print :
# ans : 3

print("--------------------------Q_23--------------------------------------------------------------")
# What can we deduce from the following snipped? Select the true sentences.(select all that apply)
from math import pi as xyz   # line 01
# print(pi)                    # line 02
# print(xyz)
# A. The program will print the mathematical constant π = 3.141592…, to
# available precision
# B. The program will cause a runtime exception/error
# C. The program makes an alias for the name pi in the form of xyz
# D. The original name pi will become inaccessible
# E. Replacing line 02 with print(xyz) will cause the program to run
# without errors
# ans : B, C, D, E

print("--------------------------Q_24--------------------------------------------------------------")
# What is true about the __init__.py file? (Select all that apply)
# A. It cannot be an empty file
# B. It can execute an initialization code for a package
# C. It is required to make Python treat a given directory as a Python
# package directory
# D. It is required to make Python treat a given directory containing
# packages as a directory without packages
# ans : B,C

print("--------------------------Q_25--------------------------------------------------------------")
# What is the expected behaviour of the following code snippet?
from random import randint
# for i in range(10):
#     print(random(1,5))
# A. The program will generate a sequence of ten (pseudo)random integers
# from 1 to 5
# B. The program will generate a sequence of ten (pseudo)random integers
# from 1 to 4
# C. The program will generate a sequence of ten (pseudo)random
# numbers from 1 to 5
# D. The program will generate a sequence of ten (pseudo)random
# numbers from 1 to 4
# E. The result cannot be predicted
# F. The program will cause a runtime exception/error
# ans : F (NameError: name 'random' is not defined)

print("--------------------------Q_26--------------------------------------------------------------")
# What is the expected behaviour of the following snippet?
x=1               # line 1
def a(x):         # line 2
    return 2*x    # line 3
x=2+a(x)          # line 4
print(a(x))       # line 5
# It will print :
# ans : 8

print("--------------------------Q_27--------------------------------------------------------------")
# What is the expected behaviour of the following snippet?
# a='hello'           # line 1
# def x(a,b):         # line 2
#     z=a[0]          # line 3
#     return z        # line 4
# print(x(a))         # line 5
# It will print :
# ans : G.cause a runtime exception on line 5

print("--------------------------Q_28--------------------------------------------------------------")
# What is the expected behaviour of the following snippet?
s='SPAM'
def f(x):
    return s+'MAPS'
print(f(s))
# It will print :
# ans : SPAMMAPS

print("--------------------------Q_29--------------------------------------------------------------")
# Select the true statements: (Select all that apply)
# A. Positional arguments are also called keyword arguments
# B. The order of arguments matters when they are passed positionally
# C. The order of arguments matters when they are passed by their name
# D. A function can be called with a mix of positional and keyword
# arguments
# ans : B,D

print("--------------------------Q_30--------------------------------------------------------------")
# What is the expected behaviour of the following snippet?
def gen():
    lst=range(5)
    for i in lst:
        yield i*i
for i in gen():
    print(i,end="")

# ans : 014916




