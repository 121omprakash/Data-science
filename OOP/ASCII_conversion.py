#character to acii
print(ord('A'))
#integer to character
print(chr(68))

#Iterating through string
#converting string to cipher
res = "Rahul"
lst =[]
for i in res:
    lst.append(ord(i))
print(lst)
for i in range(len(lst)):
    lst[i] = lst[i]+2
print('After modify: {}'.format(lst))
mod=""
for i in lst:
    mod+=(chr(i))
print(mod)
print(chr(65))