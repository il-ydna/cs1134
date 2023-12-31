class Student:
    def __init__(self, name = "student", age = 18):
        self.name = name
        self.age = age
        self.courses = []

    def add_course(self, course):
        self.courses.append(course)

    def remove_course(self, course):
        if course in self.courses:
            self.courses.remove(course)
            print("Removed Course:", course)
        else:
            print("Course Not Found:", course)


def __repr__(self): #str representation needed for print( )
    info = "Name: " + self.name
    info += "\nAge: " + str(self.age)
    info += "\nCourses: " + " , ".join(self.courses)
    return info + "\n"

peter = Student("Peter Parker")
print(peter.name, peter.age)
peter = Student(age = 16)
print(peter.name, peter.age)
peter.name = "Peter Parker"
print(peter)
peter.add_course("Algebra")
peter.add_course("Chemistry")
print(peter)
peter.add_course("Physics")
peter.remove_course("Spanish")
tom = Student("Tom Holland")
tom.courses = peter.courses
tom.add_course("Economics")
peter.remove_course("Chemistry")
print(peter.courses)
print(tom.courses)
peter.name, tom.name = tom.name, peter.name
print(peter.name, peter.age)
print(tom.name, tom.age)