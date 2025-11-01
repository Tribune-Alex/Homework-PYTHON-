import random

class Student:
    status = True
    pay = 1000

    def __init__(self, first_name, last_name, age, grade):
        
        self.first_name= first_name
        self.last_name= last_name
        self.age= age
        self.grade= grade
        

    def get_full_name(self):
        pass
        return f"{self.first_name} {self.last_name}"  

    def get_discount(self):
        pass
        if self.age < 18:
            Student.pay = 1000-(1000 * 0.2)
        return Student.pay
    
    def calculate_average(self):
        pass
        average =sum(self.grade)/len(self.grade)
        return average
    
    def get_status(self):
        pass
        if self.calculate_average()>90:
            return f"Excelent"
        elif self.calculate_average() > 70 and self.calculate_average() < 90:
            return f"Good"
        elif self.calculate_average() > 50 and self.calculate_average() < 70:
            return f"Average"
        elif self.calculate_average() < 50:
            return f"Poor  Unfortunately, your status is {Student.status==False}"

    

    

student1=Student(first_name="Alex", last_name="Todua",age=34,grade=[80,75,96,85,95])
student2=Student(first_name="John", last_name="Wick",age=21,grade=[71,76,85,90,81])
student3=Student(first_name="Ana", last_name="De Armas",age=17,grade=[100,90,96,90,91])
student4=Student(first_name="Joe", last_name="Doe",age=21,grade=[41,45,46,45,35])
student5=Student(first_name="Dakota", last_name="Johnson",age=16,grade=[50,65,56,45,55])

print(f"Student's full name: {student1.get_full_name()}")
print(f"Cost of training: {student1.get_discount()}")
print(f"Your grade point average is: {student1.calculate_average()} {student1.get_status()}")


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


print()

print(f"Student's full name: {student5.get_full_name()}")
print(f"Cost of training: {student5.get_discount()}")
print(f"Your grade point average is: {student5.calculate_average()} {student5.get_status()}")

