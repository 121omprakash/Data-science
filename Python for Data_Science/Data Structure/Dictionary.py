print('Dictionary'.center(75,'⭐'))

# creating a dictionary:
dict = {'Name':'Om Prakash'}
print('Sigle dimension Disctionary:{}'.format(dict))
print('='*80)

## Acessing a  dictionary's value:
key = 'Name'
val = dict[key]
print('Value of key {}: {} in the dict'.format(key,val))
print('='*80)
# adding new element
key = 'Age'
val = 21
print('Before adding new key in dictionary:{}'.format(dict))
dict[key] =val
print('After the adding new key and value in dictionar: {}'.format(dict))
print('='*80)

#deleting the key from dict:
print('Before deleting the key in dictiopnary: {}'.format(dict))
del dict[key]
print('After the deletion of the key in the dictionary: {}'.format(dict))
print('\n\n')
print('Dicttionary method'.center(90,'*'))

# 1. clear
newdict = dict.copy()
print('Before deleting the key in dictionary: {}'.format(dict))
dict.clear()
print('After deleting the key in dictionary: {}'.format(dict))
print('='*80)

#2.copy
print('Before creating copy of dict :{}'.format(dict))
dict = newdict.copy()
print('After creating copy: {}'.format(dict))
print('='*80)

#get()
key = 'Name'
print('Value of {} in dict:{}'.format(key,dict.get(key)))
print('='*50)

#dict.items:returns a list of tuple(key:value) that contains all items in dictionary

for key,value in dict.items():
    print('{}:{}'.format(key,value))
print('='*50)

#dict.keys(): returns a list that containing all keys of dictionary
key = dict.keys()
for i in key:
    print('{}: {}'.format(i,dict.get(i)))
print('='*50)

#dict.values: returns a list that containing all vaue of dictionary
value = dict.values()
print('All Values in dictionary: {}'.format(value))
print('='*50)

#dict.pop(key) = remove the specified key provided in parameter
dict['Age'] =70
dict['Course'] = 'BCA'
dict['Dept'] = 'AIIT'
dict.pop('Age')
print('After removing age from dictionary: {}'.format(dict))
print('='*50)

#dict.popitem() = remove the last item from dictionary

print('Before using popitems method:{}'.format(dict))
dict.popitem()
print('After using popitems method:{}'.format(dict))

print('='*50)

#key in dict: check whether key is present or not
print('Age in dict: {}'.format('Age' in dict))
print('Name in dict: {}'.format('Name' in dict))
print('='*50)

#dict.setdefaultkey(key)

#dict.has_key(key): this check whether dict has that specfic key or not . it only works on python 2