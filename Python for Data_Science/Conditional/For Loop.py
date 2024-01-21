## for loop

#1. using range function
topic = 'Range'
print(topic.center(50,'*'))
n = int(input('Enter a number:\n'))
for i in range(n):
    print('Value: {}'.format(i))
print('*'*50)
#2. iterating string:
s = 'Om Praksah'
for i in s:
    print('Character of s: {}'.format(i))
print('*'*50)

# 3 iterating a collection:
    #3.1 iterating a list:
lst = [10,15,20,30]
for i in lst:
    print('Element of list: {}'.format(i))
print('*'*50)
print('Iterating list using list funciton: ')
for i in range(len(lst)):
    print('Element of list at position {} : {}'.format(i+1,lst[i]))

print('*'*50)
##3.2 iterating a dictionary using for loop
# print('Using for loop in dictionary:  ' )
# dict:{1:'Om',2:'Rahul',3:'Raj'}
# for i in dict:
#     print("{}:{}".format(i,dict[key]))
# print('*'*50)
## 3.2 itwerating a dictionary using for loop but using key method fo riteration
# print('Accessing using key method')
# for i in dict.keys():
#     print('{}: {}'.format(i,dict[i],))

print('#'*50)

## Nested for loop
row = 4
col = 5
for i in range(row):
    for j in range(col):
        print(i+j,sep=" ")
    print("\n")
