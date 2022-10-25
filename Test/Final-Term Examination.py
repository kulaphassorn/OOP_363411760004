"""
Name: {chonticha.ai}
SID: {363411760004}
Group: {MIT431}
"""

class Person:

    def __init__(self,name,age,email):
        self.name = name
        self.age = age
        self.email = email
    def person_info(self):
        print(f'Name: {self.name}'
              f'Age: {self.age}'
              f'Email: {self.email}'

    # getter and setter
    def get_name(self):
        return  self.__name
    def set_name(self,name):
        self.__name = name
    def get_age(self):
        return self.__age
    def set_age(self):
        self.__age = age
    def get_email(self):
        return  self.__email
    def set_email(self,email):
        self.__email = email

class Student(Person):
    def __init__(self,name,age,email,major):
        super().__init__(name,age,email)
        self.major = major
    def studen_info(self):
        super().
        print(f'Major: {self.major}')

        Student id: Name:Kulaphassorn:MIT Age:27
        Email:chonticha.ai@rmutsvmail.com

class Employee:
    Employee id : Kulaphassorn : Head office Age:27
    Email:chonticha.ai@rmutsvmail.com

class Devices:
    all_Devices = ["brand","model","price"]

    def __init__("Mobile","Tablet","Laptop"):
    self.Mobile = Mobile
    self.Tablet = Tablet
    self.Laptop = Laptop

    def __init__(self,dev_name):
        self.dev_name = dev_name

    def Devices_info(self):
        print(f'Devices name: {self.__dev_name}')

    def get_name(self):
        return self.__dev_name

    def get_all_Devices(self):
        for x in self.all_devices:
            print(x)

class Mobile:
    Mobile Brand: Apple Mobile: IPhone 13 Pro Price: 35000

    def __init__(self,Laptop):
        self.Laptop = Laptop


class Tablet:
    Tablet Brand: Samsung Mobile: Galaxy Tab Price: 45000

    def __init__(self,Tablet):
        self.Tablet = Tablet

class Laptop:
    Laptop Brand: Asus Model: Vivobook 14x Price:42000

    def __init__(self,Model):
        self.Model = Model

class Device_Report:

    def __init__(self,owner):
        self.owner = owner

    def add_devices(self,Devices):
        self.Device.append(Devices)

    def add_date(self,date):
        self.date.append(date)

    def Device_Report_info(self):
        print(f'Devices Peport')
        self.owner.person_info()
        c = 1
        if len(self.Devices) == 0:
            print(f'\t No  datedevices.')
        else:
            for x in self.devices:
                print(f'{c}. {self.x.get_name()}')
                c += 1
                if len(self.devices) == 0:
                    print(f'\t No devices data.')
                else:
                   for x in range(len(self.devices)):
                       print(f'{c}.{self.devices[x].get_name()}'
                                    f'date:{self.date[x]}')
                       c +=1








