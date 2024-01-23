#creating a set
myset = {10,23,15,50}
print('Myset ceated: {}'.format(myset))


# adding an element into set:
print('Adding Element'.center(50,'_'))
print('Set Before add operation:{}'.format(myset))
myset.add(40)
print('Set after operation: {}'.format(myset))

# removing item from set
print('Removing Elements'.center(50,'_'))
print('Method 1'.center(50,'-'))
print('Set Before operation: {}'.format(myset))
myset.pop()
print('Set after pop operation: {}'.format(myset))
print('Method 2'.center(50,'-'))
myset.remove(15)
print('Set after applying remove(15) operation: {}'.format(myset))
print('Method 3'.center(50,'-'))
myset.discard(23)
print('Set after applying discard(23)operation :{}'.format(myset))

#iterating the set elements
print('Iterating the set elements'.center(50,'_'))
for i in myset:
    print(i)
#checking the value in the 
print('Checking elements'.center(50,'_'))
print(50 in myset)

#performing the sets operation:
print('Set Operations'.center(50,'_'))
set1 = {15,20,56}
set2 = {90,56,89}
print('Set1: {}'.format(set1))
print('set2: {}'.format(set2))

# it return that set which is containing all elements of differnt sets
print('set1 union set2:{}'.format(set1.union(set2)))


# it returns those elements which are common in both sets
print('set1 intersection set2: {}'.format(set1.intersection(set2)))

# difference returns those value which are not presents in the other set
print('Difference of set1 and set2: {}'.format(set1 - set2))
# symmetric operation returns those value which is not common in both set
print('Symmetric difference of set1 and set2: {}'.format(set1^set2))

#clearing the set elements
print('Clearing the set'.center(50,'_'))
print('after clearing set: {}'.format(set.clear()))

#copy the set
print('Copying the set'.center(40,'-'))