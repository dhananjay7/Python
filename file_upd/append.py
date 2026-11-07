# appending a file 

f = open("demo.txt", "a")

f.write("this is the new content written \nthis is in the next line")
# we can also add a next line
f.close()