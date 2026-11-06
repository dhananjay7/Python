#WAF to print elements of a list in a single line (list is the parameter)

nums = [7,3,65,2,0]

def print_ele(nums):
    for i in nums:
        print(i,end = " ")

print_ele(nums)