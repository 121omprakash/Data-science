#opening file in read format to get data from file
file = open('Mark.txt','r')
txt = file.read()
txt

#text processing
##paragraph
per = txt.split('\n\n')
print('no of paragraph: ',len(per))

#lines
line = txt.split(".")
print('No of line: ',len(line))

#words
word = txt.split(',')
print('No of words: ',len(word))

#advance text processing:
for i in range(7,17):
    pt = '[{}]'.format(i)
    txt = txt.replace(pt,'')

#writing into file
file = open('Write_data.txt','w')
file.write('\n\n this is a new line')
file.close()

# reading file
def read1(filename):
    file = open(filename,'r')
    txt = file.read()
    
    file.close()
    return txt

#appending lines in file:
file = open('Write_data.txt','a')
file.write('\n\n hi this is appended line')
txt = read1('Write_data.txt')
print('Append text: {}'.format(txt))

#appending or write the data into next line:
file = open('Multiple_Write.txt','a')
# string = input('Enter the detail of student')
# string.append('.\n')
# file.write(string)
txt = read1('Multiple_Write.txt')
file.close()


file = open('Multiple string.txt','w+')

# file.writelines(l) for l = ['Om','Praksh','Kumar'] 
txt = file.read()
print(txt)

# closing a file
file.close()