#wap to check if a list contains a palindrome of elements 

pali = [1,2,3,2,1]
print("the palindrome list is ", pali )

copy = pali.copy()
copy.reverse() #directly changes the copy to reverse and if printed it would say none

if(copy == pali):
    print("the list is palindromic ", copy)
else :
    print("the list is not palindromic")