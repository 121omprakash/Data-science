file = open('Data Toolkit/Inventory Management/Inventory.txt','r')
data = file.read()
# print(data)
updated_lst = []
pro = data.split('\n')
def prin():
    for i in updated_lst:
        
        print(str(i))
    print('-'*50)

def update(id,q):
    for i in pro:
        pri = i.split(',')
        if int(pri[0]) ==id:
            pri[3] = str(int(pri[3])-q)
        updated_lst.append(pri)



update(5,80)
# prin()
for i in updated_lst:
    
    result=','.join(i)
    print(result,sep=',')