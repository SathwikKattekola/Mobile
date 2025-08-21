# # import keyword
# # #using underscore in a variable makes it private to the class
# # print(keyword.kwlist)  # 33 keywords--3 have first letter cap: ['False', 'None', 'True', 'and', 'as', 'assert', 'async', 'await', 'break', 'class', 'continue', 'def', 'del', 'elif', 
# # #'else', 'except', 'finally', 'for', 'from', 'global', 'if', 'import', 'in', 'is', 'lambda', 'nonlocal', 'not', 'or', 'pass', 'raise', 'return',
# # # 'try', 'while', 'with', 'yield']
# print(0 and 1)
# print(0 or 1)
# print((not 1))
#-----------------------------------------------------------------------------------------
# print(7 and 9)   #prints 9
"""Explanation:

The and operator in Python doesn’t just return True or False — it returns one of the operands.

Rule:
If the first value is falsy (like 0, None, "", False), it returns the first value.

Otherwise, it returns the second value.

Here:

7 is truthy → so it evaluates and returns the second operand → 9.

So result = 9."""
#--------------------------------------------------------------------------------------------
# # class man:
# #     height=input()
# # m1=man()
# # m2=man()
# # m1.height
# # m2.height="5ft"
# # print(m1.height)
# # print(m2.height)
# class man:
#     def __init__(self,height):
#         self.height=height
# m1=man(7)
# print(m1.height)
# print(8&7)
# print(8|7)
# print(8^7)
# print(1<<2)
# print(4>>2)
# print(1>>1)              #prints 0
# print(~6)       #prints -7                                                           *
# """Why ~6 = -7

# 6 in 8-bit → 00000110

# ~6 flips bits → 11111001

# That binary 11111001 is -7 in two’s complement."""
# k=5
# print(type(k))
# n=str(k)
# print(type(n))
# '''
# string
# list
# tuple
# set
# frozenset ---> immutable set
# dictionary
# range
# '''
# #STRINGS-------------------------------------------------------------
# # print(dir(str))
# '''
# string concat and multip
# string capitalize and title
# split and max split
# string count, replce, upper, lower
# string swap case, string reverse,
# '''
# # s1="sathwik netha"
# # s2="kattekola"
# # s=s1+s2
# # print(s1*3)
# # s3=s1.capitalize()
# # s4=s1.title()
# # print(s3,s4)
# # s5=s1.split()
# # print(s5)
# # s5 = s1.split('t')
# # print(s5)
# # print(len(s1),"count of 't':", s1.count('t'))
# #SETS--------------------------------------------------------------------------
# s1={1,2,3,4}
# s2={4,6,7,8}
# print(s1,s2)
# print(s1.intersection(s2))
# print(s1.union(s2))
# print(s1.difference(s2))
# print(s1.symmetric_difference(s2))
# arr=([1,2,3],[4,5,6])
# del arr[0][1]
# print(arr)

#bytes and byte array---------------------------------------------------------------------------------------
j={1,2,3,8}
b=bytes(j)
print(b)
for i in b:
    print(i)
k=bytearray("hello", 'utf-8')
print(k)
print(b)
o=b"hi"
print(o)
print((o+b"!"))