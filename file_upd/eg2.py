#WAF that replaces all the occurences of "Java" with "Python" in the file created in eg1.py


def replace_word(filename, old_word, new_word):
    with open(filename , "r") as f:
        data = f.read()

    new_word = data.replace(old_word,new_word)
    print(new_word)

    with open(filename, "w") as f:
        f.write(new_word)



replace_word("practice.txt","Java","Python")