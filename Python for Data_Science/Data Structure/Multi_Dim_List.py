#creating of multidimension list
a = [[1,15,20,40],
     [21,39,65,89],
     [40,50,90,65]
     ]


#acessing the all list of multi dim list
for i in range(len(a)):
    print('{} th row: {}'.format(i+1,a[i]))
print('-'*50)


#acessing each and every element of multi_dim_list:
for row in range(len(a)):
    print('{} th row elements: {}'.format(row+1,a[row]))
    print('-'*50)
    for col in range(len(a[row])):
        print('Element at {} th row and {} column: {}'.format(row+1,col+1,a[row][col]))
    print('_'*50)

# method in multi_dim_list:
r = [10,45,69,70]
print('_'*50)


#1 append(): it appends elements in the last list or if paremeter is list then append in the form of list
a.append(r)
print(a)

# extend is commented because at the time of accessing each element it is going to creating problem
# 2. Extend(): it appends the iterable elements in the form of elements
# r = [20,320,890,70]
# a.extend(i for i in r)
# print('_'*50)
# print(a)
print('-'*50)

#3.reverse: reverse a multi_dim_list:
a[0] = [54,25,769,70]
print('Before: {}'.format(a[0]))
a[0].reverse()
print('After Reverse: {}'.format(a[0]))
print('-'*50)


# flattern a multi_dim_list:
lst = [j for row in range(len(a)) for j in a[row] ]
print('Befor Flattern: \n{}'.format(a))
print('After Flattern: \n{}'.format(lst))


## serching a key in multi dim:

key = int(input('Enter a number to find in multilist: '))
for i in range(len(a)):
    for j in (a[i]):
        if j == key:
            print('Key:{} is found at {}th row'.format(key,i))
print('_'*50)  



#deleting a key or list from multi dim list:
print(a)
n = int(input('Enter the row you want to delete'))
del a[n-1]
print('List after Deleting {}th row: {}'.format(n,a))
print('_'*50)