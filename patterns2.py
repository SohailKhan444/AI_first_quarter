'''  ****
     ***
     **
     *
     *
     **
     ***
     ****
    
'''

'''
for r in range(1, 6):
    for c in range(5,r-1 , -1):
        print('*' , end= '')
    print("")
for r in range(1,6):
    for c in range(1, r+1):
        print("*" , end='')
    print("")
'''

'''
num = 2
for r in range(1,5):  # number of rows and nothing else
    num= num-1    
    for c in range(4 , r-1 , -1):    # means 4 cols , then down to r-1 which is 0, but 0 not included so upto 1
        print(num , end=' ')
        num +=1
    
    print('')                        # then new line 

'''
'''
for i in range(1,7):
    for j in range(i,7):
        print(j , end='')     # we can type any character in end='hahaha' or _ or & or * in the end of print()
    print('')
'''



n= 6
k=3*n-3
num=1

for r in range(1,n):
    for s in range(1,k):
        print(end='')
    k=k-2

    for c in range(1,r+1):
        print(num , end=' ')
        num +=1
    print("")
    




