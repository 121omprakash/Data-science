n =10
name = "Om Prakash"
j = 10+20j
price =10.15
details = True
married = False
s =(10,20,30,40,10,20)
j ={15,20,33,22,33,22}
l = [10,20,30,40]
dict = {'Name':'Om Prakash',
        'Id':131,
        'Course':'BCA',
        'Sec':'C'}
#sep keyword
print(type(n),n,sep=":")
print(type(name),name,sep = ":")
print(type(j),j,sep=":")
print(type(price),price,sep=":")
print(type(details),details,sep=":")
print(type(married),married,sep=":")
print("-----------------------------")
print(type(dict))
for i in dict:
    print(i,":",dict[i])
print("-----------------------------")
print(type(j))
for i in j:
    print(i ,sep=",")
print("-----------------------------")
print(type(s))
for i in s:
    print(i)
print("-----------------------------")
print(type(l))
for i in l:
    print(i)
print("-----------------------------")
#End keyword
print('This is end keyword',end="/")