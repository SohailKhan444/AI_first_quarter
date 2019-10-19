# sum n positive integers
'''
num_upto = int (input("how many positive integers you want to sum up. Enter last number! \n"))
if num_upto == 1 or num_upto == 0:
    print("Very unfair number bruh! Enter more than that. I can do it don't worry! ")
    num_upto = int (input(" Enter last number! \n"))
sum = 0
for i in range(1, num_upto+1):
    sum = sum + i
print(f"the sum of {num_upto} integers is : {sum} ")
'''

# sum of digits in an integer
num_upto = int (input(" Enter a number of which you want to add each of it's digits! \n"))

'''
Errors while I was tring direct indexing from a number rather than converting
it into string:::

1)
# print(len(num_upto))
# TypeError: object of type 'int' has no len()

2)
# Enter a number of which you want to add each of it's digits!
# 55
# Traceback (most recent call last):
#   File "task4.py", line 15, in <module>
#     print(num_upto[0])
# TypeError: 'int' object is not subscriptable

3) 
# Enter a number of which you want to add each of it's digits!
# 555
# Traceback (most recent call last):
#  File "task4.py", line 20, in <module>
#    sum = sum + string_num[i]
# TypeError: unsupported operand type(s) for +: 'int' and 'str'


'''


# converting number e.g 555 to string '555' len = 3 , indices 0, 1 ,2
string_num = str(num_upto)
length = len(string_num)

sum = 0
for i in range(length):   # len is 3 but here 3 not included
    sum = sum + int(string_num[i]) # converting first string value into int

print("sum is : " + str(sum))










