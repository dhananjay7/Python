#Dictionary are used to store data in a key : value pair
#they are unordered , mutable(changeable), & dont allow duplicate keys

info = {
    "name" : "dhananjay tayade",
    "subject" : ["phy", "maths", "chem"],
    "age" : 20,
    "cgpa" : 8.90,
    "god" : True,
    "goals" : ("money", "fame", "kitties")
}

print(info["name"])
print(type(info["subject"]))

info["age"] = 9
info["surname"] = "brahmin"
#cannot create a same name key again because python overwrites it and doesnt create a new one
print(info)


#Nested Dictionary

student = {
    "name" : "gopal wadhwani",
    "subjects" : {
        "maths" : 97, 
        "physics" : 90, 
        "chemistry" : 98
        },
    "clg" : "jit"
}

print(student)
print(student["subjects"]["chemistry"])
print(len(student["subjects"]))