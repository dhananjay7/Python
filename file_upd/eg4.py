# WAF to find in which line of the file does the word "learning" occur first. print -1 if the word does not exist or not found

def find_line(filename,word):
    line_no = 1
    data = True
    with open(filename, "r") as f:
        while(data):
            data = f.readline()
            if(data.find(word) != -1):
                print(line_no)
            line_no += 1
        else:
            return -1


find_line("practice.txt","like")
