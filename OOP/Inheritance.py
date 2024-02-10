import random
#creating parent class
class Human:
    def __init__(self,name,age,food):
        self.Name = name
        self.Age = age
        self.Food = food
    def detail(self):
        print('My Name is {}'.format(self.Name))
        print("I'm {} years old".format(self.Age))
        print('I love to eat {}'.format(random.choice(self.Food)))
    def Dance(self):
        print('{} is dancing on stage'.format(self.Name))
    
    def Eat(self):
        print('{} is eating {}'.format(self.Name,random.choice(self.Food)))
#creating child class
class Student(Human):
    def __init__(self, name, age, food,course,roll,specialization):
        super().__init__(name, age, food)
        self.course = course
        self.roll = roll
        self.specialization = specialization
    def detail(self):
        print('My Name is {}'.format(self.Name))
        print("I'm {} years old".format(self.Age))
        print('I study in {}'.format(self.course))
        print('My specialization is {}'.format(self.specialization))
#main method
def main():
    lst = ['Gauva','Mango','Orange','Pineapple','Banana']
    om_human = Human('Om Prakash',19,lst)
    om_human.detail()
    om_human.Dance
    om_human.Eat
    #creating object for student(child) class
    om_student = Student('Om Praksh',22,lst,'BCA',131,'Computer_Science')
    om_student.detail()

#calling main function
if __name__ =='__main__':
    main()