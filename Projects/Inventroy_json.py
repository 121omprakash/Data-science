#importing Libraries

import json
import time

#loading data from Json
file = open('/home/om/Desktop/Data science/Projects/Inventory_record.json','r')
data = file.read()
record =json.loads(data)
file.close()
# head = 'Name'+','+'Email'+','+'Phone'+','+'Pro_ID'+','+'Quantity'+','+'Total'+','+'Discount'+','+'Total_Amount'+','+'Date'+','+'\n'

# file = open('/home/om/Desktop/Data science/Data Toolkit/Inventory Management/Sales.csv','w')
# file.write(head)
# file.close()


#menu
print('Menu'.center(45,'-'))
key = record.keys()
print('Pro_Id'.center(10,' '),'Name'.ljust(20,' '),'Price(RS)'.center(20,' '),'\n')
for i in key:
    print(str(i).center(10,' '),record[i]['Name'].ljust(20,' '),record[i]['Price'].center(20,' '))
print('-'*45)
usr_detail =' '
usr_name = input('Enter your name: ')
usr_email = input('Enter your emai: ')
usr_phone = input('Enter the phone number: ')
Pro_Id = str((input('Enter the product id: ')))
quantity= int(input('Enter the quantity of the product: '))
#checking for product availablity
if Pro_Id in record.keys():
    if quantity <= int(record[Pro_Id]['Qn']):
        #printing bill
        print('_'*50)
        print('Bill'.center(50,'-'))
        print(usr_name.center(50,' '))
        print('-'*50)
        print('Pro_Id'.center(10,' '),'Name'.ljust(10,' '),'Price(RS)'.center(10,' '),'Quantity'.center(10,' '),'\n')
        print(str(Pro_Id).center(10,' '),record[Pro_Id]['Name'].ljust(10,' '),record[Pro_Id]['Price'].center(10,' '),str(quantity).center(10,' '))
        amount = int(record[Pro_Id]['Price'])*quantity
        print('\n\n')
        if  amount>= 500:  
            per = amount/20
            total = amount - per
            print('Total Amount(RS): {}'.format(amount))
            print('Discount(RS): {}'.format(per))
            print('-'*50)
            print('Net Amount: {}'.format(total))
            record[Pro_Id]['Qn'] = record[Pro_Id]['Qn'] -quantity

            usr_detail=usr_name+','+usr_email+','+usr_phone+','+str(Pro_Id)+','+str(quantity)+','+str(amount)+','+str(per)+','+str(total)+','+str(time.ctime())+'\n'
        elif amount >= 1000:
            per = amount/10
            total = amount-per
            print('Total Amount(RS): {}'.format(amount))
            print('Discount(RS): {}'.format(per))
            print('-'*50)
            print('Net Amount: {}'.format(total))
            record[Pro_Id]['Qn'] = record[Pro_Id]['Qn'] -quantity

            usr_detail=usr_name+','+usr_email+','+usr_phone+','+str(Pro_Id)+','+str(quantity)+','+str(amount)+','+str(per)+','+str(total)+','+str(time.ctime())+'\n'
        else:
            print('Total Amount(RS): {}'.format(amount))
                    #updating the value
            record[Pro_Id]['Qn'] = record[Pro_Id]['Qn'] -quantity
            usr_detail=usr_name+','+usr_email+','+usr_phone+','+str(Pro_Id)+','+str(quantity)+','+str(amount)+','+str(0)+','+str(amount)+','+str(time.ctime())+'\n'
    else:
        print('We have only {} quantity of {}'.format(record[Pro_Id]['Qn'],record[Pro_Id]['Name']))
        response = input('Enter (Y/N) for purchase:')
        if response.lower() == 'y':

            print('_'*50)
            print('Bill'.center(50,'-'))
            print(usr_name.center(50,' '))

            print('Pro_Id'.center(10,' '),'Name'.ljust(20,' '),'Price(RS)'.center(20,' '),'Quantity'.center(20,' '),'\n')
            print(str(Pro_Id).center(10,' '),record[Pro_Id]['Name'].ljust(20,' '),record[Pro_Id]['Price'].center(20,' '),str(record[Pro_Id]['Qn']).center(20,' '))
            print('\n\n')
            amount = int(record[Pro_Id]['Price'])*int(record[Pro_Id]['Qn'])
            if  amount>= 500:  
                per = amount/20
                total = amount - per
                print('Total Amount(RS): {}'.format(amount))
                print('Discount(RS): {}'.format(per))
                print('-'*50)
                print('Net Amount: {}'.format(total))

                record[Pro_Id]['Qn'] = record[Pro_Id]['Qn'] -record[Pro_Id]['Qn']
                usr_detail=usr_name+','+usr_email+','+usr_phone+','+str(Pro_Id)+','+str(record[Pro_Id]['Qn'])+','+str(amount)+','+str(per)+','+str(total)+','+str(time.ctime())+'\n'

            elif amount >= 1000:
                per = amount/10
                total = amount-per
                print('Total Amount(RS): {}'.format(amount))
                print('Discount(RS): {}'.format(per))
                print('-'*50)
                print('Net Amount: {}'.format(total))

                record[Pro_Id]['Qn'] = record[Pro_Id]['Qn'] -record[Pro_Id]['Qn']
                usr_detail=usr_name+','+usr_email+','+usr_phone+','+str(Pro_Id)+','+str(record[Pro_Id]['Qn'])+','+str(amount)+','+str(per)+','+str(total)+','+str(time.ctime())+'\n'
            else:
                print('Total Amount(RS): {}'.format(amount))


            #updating the value
            record[Pro_Id]['Qn'] = record[Pro_Id]['Qn'] -record[Pro_Id]['Qn']
            usr_detail=usr_name+','+usr_email+','+usr_phone+','+str(Pro_Id)+','+str(record[Pro_Id]['Qn'])+','+str(amount)+','+str(0)+','+str(amount)+','+str(time.ctime())+'\n'
else:
    print('Sorry we do not have that product')

#updating sale
file = open('/home/om/Desktop/Data science/Projects/Sales.csv','a')
file.write(usr_detail)
file.close()





#updating inventory
obj = json.dumps(record)
file = open('/home/om/Desktop/Data science/Projects/Inventory_record.json','w')
file.write(obj)