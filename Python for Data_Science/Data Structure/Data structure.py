# using queue
from collections import deque
people =(['Om','Prakash','Kumar'])
people.append('Raj')
print(people)
print(people.pop())
print(people)
print(people.pop())
print(people)

# matrix=[[10,12,15],
#         [14,16,23],
#         [6,8,9]]
# sum = 0
# for i in range(len(matrix)):
#     for j in range(len(matrix[i])):
#         if j==len(matrix[j])-1:
#             sum+=matrix[i][j]
# print("Sum of diagonal of matrix: ",sum)
# i=0
# sum  =0
# j = len(matrix)-1
# while(i<len(matrix)):
#     while(j>=0):
#         sum+=matrix[i][j]
#         j-=1
#     i+=1
# print("Sum of anti diagonal: ",sum)

def prime(n):
    i=2
    while(i<n):
        if n%i==0:
            return False
        i+=1
    return True
# lst = [10,11,19,22,23]
# print(lst)
# res = [prime(x) for x in lst]
# print(res)
# lst = [[i*j for j in range(4)]for i in range(3)]
# print(lst)
# print('-'*30)
# lst = [[i*j for i in range(3)]for j in range(4)]
# print(lst)
# st = ['Om Prakash','Kumar','Raj','Singh','Prasad']
# lst = [i.upper() for i in st]
# print(lst)

# num = [10,25,30]
# for n in num:
#     res=[]
#     while(n>2):
#         if prime(n)==True:
#             res.append(n)
#         n-=1
#     print(res) 
# lst = [[j for j in range(5)]for i in range(4)]
# print(lst)

dict = {1:'Om Prakash',2:'Kumar',3:'Ram'}
print(dict)
# print(dict.pop(2))
# print(dict)
# print(dict.keys())
# print(dict.values())
# for i in dict:
#     print(i,":",dict[i])

# s= dict.has_key(1)
# # print(S)
# dict2 = {1:'Rahul',2:'raj',3:'BBA'}
# for i in dict:
#     dict2[i] = dict[i]
# print(dict2)
# print(dict)

def greet(name,word='Hello'):
    print(word+name)
greet('om')
greet('om','Good morning')