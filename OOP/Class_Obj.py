#class is blueprint or structure of an object
# it has two vlaue 1. Attribute 2.Mehtod
#Object: Object is an entity of an class,it is real world entity

#creating a class:
class Student:
    #constructor: it is the first method which executed when any object is created
    def __init__(self,name,age,id,course):
        self.name = name
        self.age = age
        self.id = id
        self.course = course
    def Details(self):
        detail = self.name+','+str(self.age)+','+str(self.id)+','+str(self.course)
        return detail
#creating main method
def main():
    om = Student('Om Prakash',20,131,'BCA')
    #calling calss method
    print(om.Details())
    #modifying object property
    om.age = 25
    om.course= 'MCA'
    #deleting object properties
    del om.course
    #deleting object
    del om
#calling main method
if __name__=='__main__':
    main()

