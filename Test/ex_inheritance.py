"""
Name: {chonticha.ai}
SID: {363411760004}
Group: {MIT431}
"""

# class relations - inheritance

class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def person_info(self):
        print(f'Name: {self.name} Age: {self.age}')

class Student(Person): # Student inherited form Person
    def __init__(self,name,age,major,gpa):
        # 1
        Person.__init__(self,name,age)
        # 2
        #super().__init__(name,age)

        self.major = major
        self.gpa = gpa
    def student_info(self):
        print(f'Name: {self.name} Age: {self.age}'
              f'Major: {self.major}'
              f'GPA: {self.gpa}')



# create obgect
s1 = Student("Kulaphassorn",36,"MIT",3.00)
s1.person_info()
s1.student_info()
