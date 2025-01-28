# Once we declare the string we cannot modify it if we try to modify it it will create nre string.
# if new string does not have reference variable it will be removed
#python internally uses string interning
# string interning is the process of checking the string intern pool before creating any new object
# whenever we want to create new object, python first will check yhe string intern pool, whether
#  the object already exits or not
# when object already exist in the string intern records then address of exixting object will be reused



#s1 ="kodnest"
#s1 = s1.upper()
#print(s1)

#s1 ='K'
#print(s1, id(s1))

s1 = "Hello"
s2 ="world"
print(s1, id(s1))
print(s2, id(s2))
print(s1, s1[0])
print(s2, s1[-1])
