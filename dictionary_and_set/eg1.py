# store following word meaning in a dictionary.
#cat : "is a small animal"
#table : "a piece of furniture" , "list of facts and figures"

meaning = {
    "cat" : "is a small animal",
    "table" : ["a piece of furniture", "list of facts and figures"]
}

print(meaning)
print(type(meaning["table"]))