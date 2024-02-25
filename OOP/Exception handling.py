# there are generally two keyword for eception handling in python: 1. try 2. Except 3. else 4. finnaly

#try --> used to put those code which can generate error
try:
    print(10/0)
except:
    print('Enter another number apart from zero')

#catching sepecfic condition
a = [10,20,30,40]
try:
    print(a[10])
except IndexError as IE:
    print('Enter a valid index: ',IE)
except ValueError as VE:
    print(VE)

# try except-else
# try: it is used to put those code which can generate error

#except: it is used to put those statement which should have execute if there any error occurs.

# else: this block exectute if there is no exception occured in the code.

#finally: this block execute no matter there is any exception occured or not.
#syntax:
a = 100
b =0
try:
    print(a/b)
except:
    print('Enter a valid b')
else:
    print('Value of a/b: ',a/b)
finally:
    print('Result:') 

# assertion is used to check whether expression is true or false.
# it there is any error then it genrerate "ASSERTIONERROR"
# syntax: assert (expression),"text" --> text will execute if expression is false.
assert 10<0,"10 is grater than 20"