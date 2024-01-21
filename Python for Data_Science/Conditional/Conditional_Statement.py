## if statement:
n =int(input('Enter a number'))
if n<=10:
    print('{} is grater than 10'.format(n))
print('*'*50)
## if-else statement:
if n>0:
    print('{} is positive'.format(n))
else:
    print('{} is negative'.format(n))
print('*'*50)
#short hand if else statement:
a = 'Positive' if(n>0) else 'Negative'
print('Positive and greater than 10') if (n>10) else print('Negative or less than 10')
print('*'*50)
## the elif statement

n = int(input("Enter a number to find whether it's a positive or negative"))
if n>0:
    print('{} is Positive'.format(n))
elif n<0:
    print("{} is negative".format(n))
else:
    print('{} is zero'.format(n))
print('*'*50)
