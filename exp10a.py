import datetime
class Person:
    def __init__(self,name,surname,birthdate,email,address):
        self.name=name
        self.email=email
        self.address=address
        self.surname=surname
        self.birthdate=birthdate
    
    def __str__(self):
        return "%s %s,Born on:%s\n Email:%s\n Address:%s\n"%(self.name,self.surname,self.birthdate,self.email,self.address)

    def __add__(self,other):
        return Person(self.name,self.surname,self.birthdate,self.email,self.address+other)

p1=Person('suresh','chandra',datetime.date(2003,12,2),'abc@gmail.com','abc colony')
p2=Person('marina','bethany',datetime.date(2004,2,6),'aefg@gmail.com','egd colony')

print(p1+'\n is a Professor')
print(p2+'\n is a Student')