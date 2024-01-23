# dictionary cretion using list
name = ['om','prakash','kumar','rahul','raj']
roll = [131,156,489,456,569]
dict = {k:v for k,v in zip(name,roll) }
print(dict)
print('-'*80)
#using conditional statement in dictionary
dict_condition = {key:value for key,value in zip(name,roll) if value!=569 }
print(dict_condition)
print('-'*50)
#creating dictionary using artithmatic operation
lst = [i for i in range(10)]
square_dict = {x:x**2 for x in lst}
print(square_dict)
print('-'*50)
# creating multidimension list

# university = ['Amity_Patna','Amtiy_Jaipur','Amity_Noida']
# dep = ['AIIT','ABS','ASET','AIC']
# course = ['BCA','MCA','B.tech','Mtech','BBA','MBA','BJMc','Mjmc']

# university_dict = {key:value for key in university for value in dep }
# print(university_dict)
