#
courses = ["MIT", "Cyber Security", "Data Science"]
print(courses)

#Accessing an element
print(courses[2])

#Looping through an array
for r in courses:
    print("Course is", r)

#Adding a new element into an array
courses.append("Laravel")
print(courses)

#Deleting an element from an array
courses.remove("MIT")
print(courses)
