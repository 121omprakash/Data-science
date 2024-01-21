##while loop
i  =10
while i>0:
    print(i)
    i-=1
PAT = ' Break '
print(PAT.center(50,'^'))
##break in while loop
while i<=10:
    print(i)
    if i == 9:
        break
    i+=1
##continue statement
pat = ' Continue '
print(pat.center(50,'_'))

## user input validation
pat = 'user input validation'
print(pat.center(50,'_'))
while True:
    n = int(input('Enter a number'))
    if n>0:
       print(n)
    else:
        n+=1
    print(n)