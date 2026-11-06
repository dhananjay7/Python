# Write a recursive function to print all characters of a string in reverse order (from last character to first), one per line.

def pri_char(string ,idx ):
    if(idx < 0):
        return
    print(string[idx])
    pri_char(string , idx - 1)

string = "RAM"
pri_char(string , len(string)-1)