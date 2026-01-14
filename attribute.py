class Employee:
    language ="python"# this is a class attribute
    salary=1200 
harry = Employee()
harry.language = "java"# this is a instance attribute
print(harry.language,harry.salary)