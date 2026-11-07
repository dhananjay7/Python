#WAF to search if the word "learning" exists in the file or not

def search_word(filename,word):
    with open(filename, "r") as f:
        data = f.read()

        if(data.find(word) != -1):
            print("FOUND")
        else:
            print("NOT FOUND")

search_word("practice.txt", "learning")