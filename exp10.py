import datetime

class Person:
    def __init__(self,name,surname,birth,address,phone,email):
        self.name=name
        self.surname=surname
        self.birth=birth
        self.address=address
        self.phone=phone
        self.email=email

    def __str__(self):
        return "%s %s,born on %s\naddress:%s\nPhone:%s\n,Email:%s\n"%(self.name,self.surname,self.birth,self.address,self.phone,self.email)

    def __add__(self,other):
        return Person(self.name,self.surname,self.birth,self.address,self.phone,self.email+other)

p1=Person('Ashwin','Tauro',datetime.date('2003-02-05'),'abc colony','34242','abc@gmail.com')
p2=Person('Rohan','Tauro',datetime.date('2001-02-05'),'def colony','846452','def@gmail.com')
print(p1+'\n is a Professor')
print(p2+'\n is a Student')