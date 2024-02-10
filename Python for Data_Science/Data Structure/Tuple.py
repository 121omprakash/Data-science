# creting a tuple
tupl = (10,20,30,40,50,40,20)
# Acessing the tuple's single or specfic  element:
print('Acessing a specfic element of tuple: ')
print(tupl[0])

#acessing the tuple whole elements:
print('Acessing the whole element of tuple:  ')
print('Method_1'.center(50,'-'))
for  i in tupl:
    print(i)

print('Method_2'.center(50,'-'))
print('Using range function:')
for i in range(len(tupl)):
    print(tupl[i])

#tuple methods:
print('Count() find the occurance of a specfic elements: ')
print('Occurance of 20 in tuple: {}'.format(tupl.count(20)))
#index method:
print('index() finds the first occurance of the specfic elements: ')
print('Index of 40 in tuple: {}'.format(tupl.index(40)))

lst = [1,2,3,4]
name = ['Om','Prakash','Kumar']
#packing and unpacking