#String has a lot of functions for specific tasks such as 

# 1.)str.endswith("er.") #returns true if string ends with substring
 
name = "dhananjay tayade"
endswith = name.endswith("ade")
print(endswith)

# 2.)str.capitalize( ) #capitalizes [1st] char

branch = "computer science engineering"
print(branch.capitalize())

#it only capitalizes for the first time after that if i try printing it again it wont work

# 3.)str.replace( old, new ) #replaces all occurrences of old with new

before = "apple is dangerous"
print(before)
after = before.replace("dangerous" , "healthy")
print(after)

# 4.)str.find( word ) #returns 1st index of 1st occurrence

index = "Caulliflower auggghhh"
print(index.find("f"))

# 5.)str.count("am") #counts the occurrence of substr in string

occurence_time = "python has a symbol snake and snake lay eggs"
print(occurence_time.count("s"))