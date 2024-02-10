# creating a functio:
def sum(a,b):
    return a+b

print(sum(10,20))
print('-'*80)
print('Function based upon Arument: ')

print('1. Default  argument: ')
def sum(a = 10,b = 25):
    return a+b
print('Default Argument based function after calling only sum(): {}'.format(sum()))
print('-'*80)
print('2. Keyword argument: ')
def name(lname,fname):
    return(fname+' '+lname)

print("After calling name(fname ='Om',lname = 'Prakash)")
a = name(fname='Om',lname='Prakash')
print('After calling function: {}'.format(a))
print('-'*50)

print('3. Variable lenght function: ')
# there are two variable lenght argument: 
#1.*arg: it takes such as value(1,2,3) that is not with a defined keyword
#2. **kwargs: it takes the value with keyword such as name = 'Om Prakash'

def detail(*args,**kwargs):
    print('Marks in math:{}\nmarks in science:'.format(args))
    # args takes the outptut in the form of list,tuple,set
    print('Kwars: First name : {}\n Last Name:'.format(kwargs))
    #kwars print the output in the form of dictionary
print(detail(80,85,fname = 'Om',lname ='Prakash'))

print('-'*50)

##Nested function:
print('Nested Function'.center(50,'-'))

def num(n):
        def even(n):
            if n%2==0:
                return ('Even')
        def odd(n):
            if n%2 ==1:
                return ('Odd')

n =10
if n>0:
    print(num(n))
print('Recursive function'.center(50,'-'))
def factorial(n):
    if n==0 or n ==1:
        return 1
    else:
        return factorial(n-1)*n

print('Factorial of 10: {} '.format(factorial(10)))
if __name__ == '__main__':
    print('Total executed')