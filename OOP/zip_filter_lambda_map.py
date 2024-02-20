#zip function
lst = [10,20,30,40,60]
tupl = ('Om','Rahul','Shayam','Sonu','Monu')
zip_tupl = zip(lst,tupl)
for i,j in zip_tupl:
    print(i,j)
#filter function
def odd(n):
    if n%6==0:
        return True
    else:
        return False
res = list(filter(odd,lst))
print(res)
#lambda function

div_7 =lambda x: x*7
print(div_7(10))

