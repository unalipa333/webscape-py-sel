#oop 
# position, name , age , level, salary






se1 = ["Software Engineer", "Max", 20, "Junior, 5000"]

se2 = ["Software Engineer", "Lisa", 25, "Associate", 7000]

def mouse(se):
    print(f"{se[1]} is a mouse")
#classes are used for more complex data structures and contain functions
#mouse(se2)
#class
class Software_Engineer:
    
    #class object
    alias="Keyboard Magician"

    def __init__(self,name,age,level,salary):
        self.name=name
        self.age=age
        self.level=level
        self.salary=salary

    


    #instance method
    def  code(self,language):
        print(f"{self.name} is a smart engineer with {language}")

    #__str__  is able to replace the information function. 
    # def  information(self):
    #     information = f"My name is {self.name}. My age is {self.age}. My level is {self.level}"

    #return information
    
    
    #dunder methods.2
    def __str__(self):
        information = f"My name is {self.name}. My age is {self.age}. My level is {self.level}"

        return information

    def __eq__(self,other):
        
        return self.name == other.name, self.age == other.age

    @staticmethod     #decorator that is a built in. It the "self" argument out of the function
    def animals(age):
        if age > 20:
            return 111
        if age < 20:
            return 222
       

#instance or object(same thing) that is instantiated 
se1 = Software_Engineer("Max", 20, "Junior", 5000)
se2 = Software_Engineer("Lisa", 25, "Associate", 7000)
se3 = Software_Engineer("Lisa", 27, "Associate", 7000)
# print(se1.animals(3))
# print(Software_Engineer.animals(99))



# print(se1.name, se1.salary)
# print(se1.alias)
# print(S_E.alias)

# print(se1)

# print(se2 == se3)



employees = [Software_Engineer("Max", 20, "Jr", 5000),
             Software_Engineer("Lisa", 27, "Sr", 9000),
             Software_Engineer("Doug", 35, "Jr", 5000)]





def motivate_emp():
    for employee in employees:
        employee.code("c++")

    



motivate_emp()