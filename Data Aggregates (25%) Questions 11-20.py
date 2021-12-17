print("---------------Q_11----------------------------------------------------------------")
#  Which of the following  statements are true ?  (Select all that apply)
# A. UNICODE is the name of an operating system
# B. UTF-8 is the name of a data transmission device
# C. ASCII is an acronym for Automatic Systems of Computer Inner
# Interoperability
# D. The Python Language Reference is the official reference manual that
# describes the syntax and semantics of the Python language
# E. Python strings are immutable, which means they cannot be sliced
# F. Python strings are mutable, which means they can be sliced
# G. Lists and strings in Python can be sliced

# ans : D, G

print("---------------Q_12----------------------------------------------------------------")
# What is the result of the following comparison ?
x="20"
y="30"
print(x>y)
# ans : False

print("---------------Q_13----------------------------------------------------------------")
# What is the expected output of the following snipped ?
s="Hello, Python!"
print(len(s))
print(s[-14:15])
# ans : Hello, Python!

print("---------------Q_14----------------------------------------------------------------")
# What is the expected output of the following snipped ?
lst=["A","B","C",2,4]
del lst[0:-2]
print(lst)
# ans : [2,4]

print("---------------Q_15----------------------------------------------------------------")
# What is the expected output of the following snipped ?
dict={'a':1,'b':2,'c':3}
for item in dict:
    print(item)
# ans :
# a
# b
# c

print("---------------Q_16----------------------------------------------------------------")
# What is the expected output of the following snipped ?
s='python'
for i in range(len(s)):
    i=s[i].upper()
print(s, end="")
# ans : python

print("---------------Q_17----------------------------------------------------------------")
# What is the expected output of the following snipped ?
# lst = [i // i for i in range(0,4)]
# sum = 0
# for n in lst:
#     sum += n
# print(sum)
# # ans : The program will cause a runtime exception

print("---------------Q_18----------------------------------------------------------------")
# How many stars (*) will the following snipped send to the console?
lst=[[c for c in range(r)] for r in range(3)]
for x in lst:
    for y in x:
        if y<2:
            print('*',end='')
# ans : three

print("---------------Q_19----------------------------------------------------------------")
# What would you insert of  ??? so that the program prints 1024to the monitor?
# Code:
lst=[2**x for x in range(0,11)]
# print(lst???)
# Expected output : 1024
# print(lst) [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024]
print(lst[-1])
# ans : 1024

print("---------------Q_20----------------------------------------------------------------")
# What is the expected output of the following snipped ?
lst1="12,34"
lst2=lst1.split(',')
print(len(lst1))
print(len(lst2))
print(len(lst1)<len(lst2))
# ans : python


