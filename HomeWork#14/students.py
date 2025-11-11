

class Student:
    status = True
    pay = 1000

    def __init__(self,first_name,last_name,age,grade):
        
        self.first_name= first_name
        self.last_name= last_name
        self.age= age
        self.grade= grade
        

    def get_full_name(self):
        
        return f"{self.first_name} {self.last_name}"  

    def get_discount(self):
        
        if self.age < 18:
            self.pay = 1000*0.8
        return self.pay
    
    def calculate_average(self):
        
        average =sum(self.grade)/len(self.grade)
        return average
    
    def get_status(self):
        
        if self.calculate_average()>=90:
            self.status = True
            return f"Excelent, your status is {self.status}"
        
        elif self.calculate_average() > 70: 
            self.status = True
            return f"Good, your status is {self.status}"
        elif self.calculate_average() > 50 and self.calculate_average() <= 70:
            self.status = True
            return f"Average, your status is {self.status}"
        elif self.calculate_average() <=50:
            self.status = False
            return f"Poor.  Unfortunately, your status is {self.status}"

    

    

student1=Student(first_name="Alex", last_name="Todua",age=34,grade=[80,75,96,85,95])
student2=Student(first_name="John", last_name="Wick",age=21,grade=[71,76,85,90,81])
student3=Student(first_name="Ana", last_name="De Armas",age=17,grade=[100,90,96,90,91])
student4=Student(first_name="Joe", last_name="Doe",age=19,grade=[41,45,46,45,35])
student5=Student(first_name="Dakota", last_name="Johnson",age=16,grade=[50,65,56,45,55])
student6=Student(first_name="William", last_name="Baldwin",age=25,grade=[77,68,59,85,65])
student7=Student(first_name="Samuel", last_name="Jackson",age=54,grade=[51,51,51,51,51])
student8=Student(first_name="Christoph", last_name="Woltz",age=55,grade=[52,52,52,52,52])

print(f"Student's full name: {student1.get_full_name()}")
print(f"Cost of training: {student1.get_discount()}")
print(f"Your grade point average is: {student1.calculate_average()} {student1.get_status()}")
print(student1.status)


print()

print(f"Student's full name: {student2.get_full_name()}")
print(f"Cost of training: {student2.get_discount()}")
print(f"Your grade point average is: {student2.calculate_average()} {student2.get_status()}")


print()

print(f"Student's full name: {student3.get_full_name()}")
print(f"Cost of training: {student3.get_discount()}")
print(f"Your grade point average is: {student3.calculate_average()} {student3.get_status()}")


print()

print(f"Student's full name: {student4.get_full_name()}")
print(f"Cost of training: {student4.get_discount()}")
print(f"Your grade point average is: {student4.calculate_average()} {student4.get_status()}")
print(student4.status)

print()

print(f"Student's full name: {student5.get_full_name()}")
print(f"Cost of training: {student5.get_discount()}")
print(f"Your grade point average is: {student5.calculate_average()} {student5.get_status()}")

print()

print(f"Student's full name: {student6.get_full_name()}")
print(f"Cost of training: {student6.get_discount()}")
print(f"Your grade point average is: {student6.calculate_average()} {student6.get_status()}")

print()

print(f"Student's full name: {student7.get_full_name()}")
print(f"Cost of training: {student7.get_discount()}")
print(f"Your grade point average is: {student7.calculate_average()} {student7.get_status()}")

print(student7.status)

print()
print(f"Student's full name: {student8.get_full_name()}")
print(f"Cost of training: {student8.get_discount()}")
print(f"Your grade point average is: {student8.calculate_average()} {student8.get_status()}")

print(student8.status)