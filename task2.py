'''
num = float(input("Enter the number you wanna check for it's nature. \n"))
if num>0:
    print(f"The number '{num}' is positive.")
elif num<0:
    print(f"The number '{num}' is Negative. ")
else:
    print(f"The number '{num}' is andda. ")
'''
'''
def checker(divident_p , divisor_p):
    if divident_p % divisor_p == 0:
        print(f'Yes! It does, {divident_p} is completely divisible by {divisor_p} ...')
    else:
        print(f'No! Man, {divident_p} is not completely divisible by {divisor_p} ...')


divident= float(input("enter divident. \n"))
divisor = float(input("enter divisor \n"))
checker(divident , divisor)
'''
'''
in_put = float(input("enter n: \n"))
r = round(in_put + (in_put **2) + (in_put**3) , 3)
                                                        # p = round(r, 2)
                                                        # print(p)
print(r)
'''
'''
user = int(input("Enter a number: \n"))
if user >= 17:
    print(f"the difference is : {user-17}")
else:
    print(f"The difference is:  {17-user}")

'''

st = input("enter a string: ")
n = int(input("How many copies do yu want of this string. \n"))

if st[0].lower() == 'l' and st[1].lower() == 's':
    print("Let's leave it unchanged.")
else:
    new_st = 'ls'+ st
    print(new_st)
#copies of st
thelist=[]
for i in range(0 , n):
    a = st
    print(a)













