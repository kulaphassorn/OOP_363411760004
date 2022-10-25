Name: {chonticha.ai}
SID: {363411760004}
Group: {MIT431}
"""

from module import Person,Student,Vaccine,Vaccine_Passport

p1 = Person("Kulaphassorn",50,25,0,250)

v1 = Vaccine("Astrazeneca")
d1 = "10/7/2565"

vp1 = Vaccine_Passport(p1)

vp1.vaccine_passport_info()

vp1.add_vaccine(v1)
vp1.add_date(d1)

vp1.vaccine_passport_info()

v2 = Vaccine("Pfizer")
d2 = "10/8/2565"

vp1.add_vaccine(v2)
vp1.add_date(d2)

vp1.vaccine_passport_info()

# Student
s1 = Student("Kulaphassorn",50,25,250)

v3 = Vaccine("Sinovac")
d3 = "12/08/2565"

vp2 = Vaccine_Passport(s1)
vp2.add_vaccine(v3)
vp2.add_date(d3)

vp2.vaccine_passport_info()