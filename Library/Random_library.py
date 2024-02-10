import random
#random.random() --> returns a random value btw 0 and 1
print('Value btw 0 and 1 :{}'.format(random.random()))
#random.randint(start ,end ) --> retrurns a random value btw start and end.
print('Value btw 10 and 20: {}'.format(random.randint(10,20)))
#random.uniform(start,end) --> returns a float n btw start and end.
print('Float value btw 10 and 20: {}'.format(random.uniform(10,20)))
#random.shuffle(collection) --> it is used to shuffle the collections
lst = [10,20,30,40,50,60,70]
lst1 = lst.copy()
shuffled_lst = random.shuffle(lst)
print('Lidt befor shuffle: {}\nAfter Shuffle: {}'.format(lst1,lst))
#random.choice(lst)--> select a random value from list or collection
print('Random value from lst: {}'.format(random.choice(lst)))
#radnom.sample(collection,item) --> create a collection of n items from provided colloection
sample_lst = random.sample(lst,3)
print('Sample collection from Lst:{}'.format(sample_lst))
