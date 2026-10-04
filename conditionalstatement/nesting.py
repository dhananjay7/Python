#it means creating an condition inside a condition 

age = 19

if(age>= 18):
    if(age>= 70):
        print("cannot drive at this age")
    else:
        print("Can get a license")
elif(age < 18):
    print("cannot get a license")