'''
string
list
tuple
set
frozenset ---> immutable set
dictionary
range
'''
#STRINGS-------------------------------------------------------------
# print(dir(str))
'''
string concat and multip
string capitalize and title
split and max split
string count, replce, upper, lower
string swap case, string reverse,
'''
# s1="sathwik netha"
# s2="kattekola"
# s=s1+s2
# print(s1*3)
# s3=s1.capitalize()
# s4=s1.title()
# print(s3,s4)
# s5=s1.split()
# print(s5)
# s5 = s1.split('t')
# print(s5)
# print(len(s1),"count of 't':", s1.count('t'))
#SETS--------------------------------------------------------------------------
s1={1,2,3,4}
s2={4,6,7,8}
print(s1,s2)
print(s1.intersection(s2))
print(s1.union(s2))
print(s1.difference(s2))
print(s1.symmetric_difference(s2))
arr=([1,2,3],[4,5,6])
del arr[0][1]
print(arr)
#commiting changes