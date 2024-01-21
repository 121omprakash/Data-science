#creating list
pat = 'Creating List'
print(pat.center(50,'_'))
print('creating empty list: ')
l =[]
print('Empty list{}'.format(l))
print('*'*50)
print('Creating a list of integer: ')
lst = [10,20,30,40]
print('Full List: {}'.format(lst))
print('*'*50)

## List element acessing
pat = "Accessing list's items"
print(pat.center(50,'_'))
print(pat+' using for loop')
for i in range(len(lst)):
    print('Lst[{}]: {}'.format(i,lst[i]))
print('*'*50)
print('Acessing a specfic character in python: \n')
print('First element of Lst: '.format(lst[0]))
print('*'*50)

##List Slicing
pat = 'Slicing'
print(pat.center(50,'_'))
print('Last element of lst :{}'.format(lst[-1]))
print('Element of list from index 1 to 3: {} '.format(lst[-3::]))
print('*'*50)

##List Modification
pat = 'List Modification'
print(pat.center(50,'_'))
print('\nModifying a single element')
a = lst[0]
lst[0]=50
print('Before Modification: {}\nAfter Modification: {}'.format(a,lst[0]))

print("\nModifying Multiple list's elements using for loop: ")

ls = [i for i in lst]
for i in range(len(lst)):
    lst[i] =lst[i]+10
print('List elements before Modification: {}\nList elements after Modification: {}'.format(ls,lst))
print('*'*50)
## adding elements
pat = 'Adding elements in list'
print("\n",pat.center(50,'_'))
c = 110
ls = [i for i in lst]
lst.append(c)
print('Before adding element: {}\nAfter adding elements: {}'.format(ls,lst))

print('Appending/Adding multiple elements in lst: \n')
lst1 = [9,12,35,56]
ls = [i for i in lst]
for i in lst1:
    lst.append(i)
print("List: {}".format(lst1))
print('Before appending lst1: {}\nAfter Appending lst1: {}'.format(ls,lst))


## List Operation
pat = 'List Operation'
print(pat.center(50,'_'))
##concatenation
print('\n1.Concatenation'.ljust(50,'_'))
name = ['Om','Prakash','Kumar','Rahul','Raj']
reg = [131,134,123,145,189]
print('Concationated list: {}'.format(name+reg))
##2.Repetation
print('\n2. Repeatation'.ljust(50,'-'))
print('Repeated list:{}\n Original List: {}'.format(name,name*2))
print('X'*50)
## Common List method
print('Common List Method'.ljust(50,'-'))
#1. len():- it tells the lenght of the list
print('Lenght of name List: {}'.format(len(name)))
print('_'*50)
#2. sorted(num):sort the array is ascending order
num = [10,9,6,8,40,56,32]
sorted_num = sorted(num)
print('Original List: {}\nSorted List: {}'.format(num,sorted_num))
print('_'*50)

#reverse(): reverse the list
reverse_lst = list(reversed(sorted_num))
print('Reversed List in Desc: {}'.format(reverse_lst))

print('_'*50)
#list.index('element'):- return the index of element
print('Finding the index of 6:  {}'.format(num.index(6)))
print('Index of 6 in sorted list : {}'.format(sorted_num.index(6)))
print('Index of 6 in Reversed list: {}'.format(reverse_lst.index(6)))
print('_'*50)
# lst.extend(lst)-> add another list
res = (num.extend(sorted_num))
print('Extended list: {}'.format((res)))

print('-'*50)
#max(list),min(list)
print('Maximum = {}'.format(max(num)))
print('Minimum Element = {}'.format(min(num)))