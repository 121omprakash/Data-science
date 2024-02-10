#polymorhisim --> poly+morphisim
#poly --> many and phisim --> form (single entity mutiple form)
class Addition:
    def __init__(self,a,b):
        self.a = a 
        self.b = b
    def result(self):
        return self.a+self.b

#main method:
def main():
    add = Addition(20,30)
    concate = Addition('20','30')
    print('result after Providing integer: {}'.format(add.result()))
    print('result after Providing string: {}'.format(concate.result()))

#calling main function
if __name__ == '__main__':
    main()