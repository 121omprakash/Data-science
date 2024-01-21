#Opening file to read or access inventory.txt file in read mode
file = open('Data Toolkit/Inventory Management/Inventory.txt','r')
products = file.read() # reading the file data
pro = products.split('\n') #spliting the data in list where new line starts

#opening file sale to store the customer data
sale = open('Data Toolkit/Inventory Management/Sales.txt','a')

#creating list for storing data
prod_id =[]
pro_name = []
pro_price=[]
pro_quantity=[]

updated_list =[] 

#opening file inventory to access the inventory data
def Catelogue():
    
    print('Catelogue'.center(50,'_')) # printing catelogu in the centre with the help of centre string method
    print("Pro.Id  Product  Price")

    for i in pro:
        pri = i.split(',')
        print(pri[0]+"\t"+pri[1]+"  :  "+pri[2]+'\n')
        prod_id.append(int(pri[0]))
        pro_name.append(pri[1])
        pro_price.append(int(pri[2]))
        pro_quantity.append(int(pri[3]))
        print('-'*30)
    print('_'*50)

# function for print bill 
def bill(id,q):
    print('Bill'.center(50,'_'))
    print("Pro.Id  Product  \tPrice   Quantity")
    print("\n"+str(id)+"\t"+(pro_name[id-1])+"      "+"\t"+str(pro_price[id-1])+"\t"+str(q))
    total = pro_price[id-1]*q
    print('_'*50)
    print('Total Amount: {} '.format(float(total)))
    print('-'*50)

def update(id,quantity):
    
    for i in pro:
        pri = i.split(',')
        if str(pri[0]) == id:
            pri[3] =str(int(pri[3])-quantity)
        updated_list.append(pri)
    # file1 = open(file = open('Data Toolkit/Inventory Management/Inventory.txt','w'))
    
    for i in updated_list:
       
       pat =','.join(i)
       print(pat)
    #    file.write(pat)

def order():
    name = input('Enter your name: ')
    phone = input('Enter your phone number: ')
    email = input('Enter your email: ')
    pro_id = int(input('Enter the id of product: '))
    quantity = int(input("Enter the quantity of product: "))
    sales = name+","+phone+","+email+","+str(pro_id)+","+str(quantity)
    if pro_id in prod_id:
        if quantity<=pro_quantity[pro_id-1]:
            bill(pro_id,quantity)
            update(pro_id,quantity)
            sale.write(sales)
            sale.write('\n')
        else:
            print("we have only {} units of {}".format(pro_quantity[pro_id-1],pro_name[pro_id-1]))
            res = input('Would you like to purchase Enter (Y/N)')
            if res.lower() == 'y':
                bill(pro_id,pro_quantity[pro_id-1])
                update(pro_id,quantity)
                sale.write(sales)
                sale.write('\n')
                
            else:
                print('Thanks')
        
    else:
        print("Sorry we don't have that product")

#function call
Catelogue()
order()
file.close()