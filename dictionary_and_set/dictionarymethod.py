# dictionary have a few usefull methods such as

info = {
    "name" : "dhananjay tayade",
    "subject" : ["phy", "maths", "chem"],
    "age" : 20,
    "cgpa" : 8.90,
    "god" : True,
    "goals" : ("money", "fame", "kitties")
}

#myDict.keys()  # returns all keys

print(info.keys())

#myDict.values()  # returns all values

print(info.values())

#myDict.items()  # returns all (key, val) pairs as tuples

print(info.items())

#myDict.get( "key"" )  # returns the key according to value

print(info.get("name"))

#myDict.update( newDict )  # inserts the specified items to the dictionary

info.update({"user" : "windows"})

print(info)