#!/usr/bin/env python
# coding: utf-8

# In[923]:


file1 = open('Inventory.txt','r')
data_set = file1.read()
sale = open('Sales_report.txt','a')


# In[ ]:





# In[924]:


id_lst = []
nam_list=[]
price_list =[]
quantity_list=[]
updated_lst = []


# In[925]:


for i in data_set.split('\n'):
        prod_details = i.split(',')
        try:
            id_lst.append(prod_details[0])
            nam_list.append(prod_details[1])
            price_list.append(prod_details[2])
            quantity_list.append(prod_details[3])
        except:
            print('')


# In[926]:


# for i in data.split('\n'):
#     prod_lists = i.split(',')
#     print(prod_lists)
print(id_lst)
print('-'*60)
print(nam_list)
print('-'*60)
print(price_list)
print('-'*60)
print(quantity_list)
print('-'*60)
print(updated_lst)


# In[927]:


def bill(c_name,id,name,price,q):
    
    print('Bill'.center(60,'-'))
    print('Customer_name: \t{}'.format(c_name))
    print('-'*60)
    print('{}\t{}\t\t{}\t{}'.format('Id','Product_Name'.ljust(8,' '),'Price','Quantity'))
    print(' {}\t {}\t\t{}\t\t {}'.format(id,name.ljust(18,' '),price,q))
    print('-'*30)
    print('Total Amount:\t {}'.format(int(price)*int(q)))
    print('-'*60)


# In[928]:


def report(c_name,c_no,c_mail,o_id,q):
    s = c_name+','+c_no+','+c_mail+','+str(o_id)+','+str(q)+'\n'
    sale.write(s)
    sale.write('\n')


# In[929]:


def update(id,q):
    id =int(id)
    file = open('Inventory.txt','w')
    if (int(id_lst[int(id)-1]) == int(id)):
        for i in range((len(data_set.split('\n')))):
#             print(i)
            if i== id+1:
                
#                 print('Quantity: {} -{} = {}'.format((int(quantity_list[id])),int(q),(int(quantity_list[id]))-int(q)))
                quantity_list[id]=str(int(quantity_list[id])-int(q))
                s=id_lst[id]+','+nam_list[id]+','+price_list[id]+','+str(quantity_list[id])
#                 print(str(quantity_list[id]))
                file.write(s)
                if i !=len(data_set.split('\n')):
                    file.write('\n')
            else:
                s=id_lst[i]+','+nam_list[i]+','+price_list[i]+','+str(quantity_list[i])
                file.write(s)
                if i !=len(data_set.split('\n')):
                    file.write('\n')
    else:
        print(int(id_lst[id]),id)
        print('Not in')


# In[930]:


#update(4,10)


# In[931]:


def order(c_name,c_no,c_mail,id,q):
    
        if (int(id_lst[id-1]) == int(id)):
            if (int(quantity_list[id-1]))>=q:
                update(prod_detail[0],q)
                bill(c_name,id_lst[id-1],nam_list[id-1],price_list[id-1],q)
                report(c_name,c_no,c_mail,id,q)
            else:
                response = input('We have only {} {} would you like to purchase(Y/N)'.format(prod_detail[3],prod_detail[1]))
                if response.lower() =='y':
                    
                    update(prod_detail[0],prod_detail[3])
                    bill(c_name,id_lst[id-1],nam_list[id-1],price_list[id-1],quantity_list[id-1])
                    report(c_name,c_no,c_mail,id,quantity_list[id-1])
                else:
                    print('Thanks!')
        else:
            print('Please Select a Valid product id')


# In[932]:


def query():
    c_name = input('Enter your Name:')
    c_no = input('Enter your contact number:')
    c_mail = input('Enter your Mail:')
    o_id = int(input('Enter the product id: '))
    o_q = int(input('Enter the quantity: '))
    order(c_name,c_no,c_mail,o_id,o_q)


# In[ ]:





# In[933]:


def menu():
    print('Items'.center(50,'-'))
    print('{}\t{}\t     {}'.format('Id','Product_Name'.ljust(20,' '),'Price'))
    print('-'*52)
    for i in data_set.split('\n'):
        prod_details = i.split(',')
#         id_lst.append(prod_details[0])
#         nam_list.append(prod_details[1])
#         price_list.append(prod_details[2])
#         quantity_list.append(prod_details[3])
        print('{}    \t    {}\t{}\t'.format(prod_details[0],prod_details[1].ljust(25,' '),prod_details[2]))
    print('_'*35)
    query()


# In[934]:


# print(updated_lst)
# for i in updated_lst:
#     print(i)


# In[935]:


# report('Om','r3947309','3hwekfho',5,10)


# In[936]:


menu()


# In[ ]:





# In[937]:


sale.close()


# In[ ]:





# In[938]:


file.close()


# In[939]:


file.close()


# In[ ]:





# In[ ]:




