# Built-in functions/ Standard library functions
# max
y = max(67, 374, 64, 728, 78)
print("The maximum value is: ", y)

#min
a = min(45,72,83,78,19)
print("The minum value is: ", a)

#User-defined functions
def name():
    print("Joseph Billy")

name() #Calling a function

def multiply():
    x = 10
    b = 7
    print(x * b)

multiply()

#Parameter(variable) and Argument(value)
def add(w, z) :
    print(w + z)

add(12, 45)

def employee(name, position, gender, salary, age) :
    print(name, position,gender, salary, age)

employee("Paul", "Manager", "Male", 40000, 32)

#A program that displays details of 5 students(Full name, age, course, gender)
#Use a user defined function with the parameter and argument
def student(Firstname, Lastname, Age, Course, Gender) :
    print(Firstname, Lastname, Age, Course, Gender)

student("Paul","Collins","15","MIT", "Male")
student("John","Higgins","14","MIT","Male")
student("Alexa","Paterson","16","Cyber Security","Female")
student("Jane","Catherine","15","Data science","Female")
student("June","Quirke","16","Data science","Female")
