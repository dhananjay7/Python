#WAP to enter marks of 3 subjects from the user and store them in a dictionary. Start with an empty dictionary & add one by one. Use subject name as key & marks as value.

Student = {}

x = int(input("The marks of phy is : "))
Student.update({"phy" : x})

y = int(input("The marks of maths is : "))
Student.update({"maths" : x})

z = int(input("The marks of chem is : "))
Student.update({"chem" : x})


print(Student)