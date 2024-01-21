print("-----------------------------")
print("Arithmatic Operator")
a = 10
b = 20
print("Addition :",a+b)
print("Subtraction: ",a-b)
print("Multiplication: ",a*b)
print("Division: ",a/b)
print("Modulus/Reminder: ",a%b)
print("Floor Division: ",a//b)
print("Exponent: ",a**b)
print("-----------------------------")

print("Logical Operator: ")
age = True
married = True
Man = age and married
Student = not married
Human = age or married
print("-----------------------------")

print("Comparision Operator: ")
p = a>=b
print("a Greater than b: ",p)
q = a<=b
print("a Less than equal to b :",q)
print("-----------------------------")

print("Bitwise Operator: ")
c = a &b
print("A biwise and b: ",c)
c = a|b
print("A bitwise OR b: ",c)
c = ~a
print("Not a: ",c)
c = a^b
print("a exor b: ",c)
c = a>>2
print("A leftshift by 2: ",c)
c = a<<2
print("A righshift by 2: ",c)

#Typcasting
#1 implicit typcasting: this is inbuilt
print('*'*50)
n = 10
floatnumber = 15.5
s = 'Name'
j = 10+5j
a = True
print("Implicit type casting \n1. int: {}\n2. float: {}\n3. String:{}\n4. Complex: {}\n5. Boolean: {}".format(n,floatnumber,s,j,a))
print('*'*50)
#2 explicit typecasting
intn = int(floatnumber)
dec = float(n)
int_bool = int(a)
print("integer typcast: {}\nfloat typecast:{}\nboolean typecast:{} ".format(intn,dec,int_bool))

#typcasting in colllection
tup1 = (10,15,30,50)
lsr = [15,25,62,70]
set1 ={10,20,30,40}


