'''
n=6    # 5 rows
k = 3*n - 3   # initially space "K" is 3*5-3 = 12 spaces   3 is subtracted for the shape to be drawn in the p_shell easily


for r in range(1,n+1): 


    # for each outer loop iteration , both these 2 for inner loops will execute.

    for s in range(1,k):    # go upto 12 spaces at a row or iteration , 10 spaces 2nd row , 8 spaces  at 3rd row,  6 spaces at 4th and 4 space at last 5th row
        print(end=' ')
    k= k-2       # outer loop when renewed, it executes because every new line will have lesser spaces than one above it.

    for c in range(1, r+1):
        print("* " , end="")
    print("")

'''

# triangle 
num=1
n=5
k= 3*n-3
for r in range(1, n):
    for s in range(1,k):
        print(end=' ')
    k=k-1              # in this pattern I just cut the spaces of each line in half. so half spaces at left and half at right of the triangle
    for c in range(1,r+1):
        print(num , end=' ')
        num +=1
    print("")


'''
    # right angle triangle of numbers      1
                                           1 2
                                           1 2 3
                                           1 2 3 4
                                           1 2 3 4 5


'''
num = 1

for r in range(1,6):
    num = 1
    for col in range(1, r+1):
        print(num , end='')
        num = num + 1
    
    print("")


'''
for r in range(1,6):
    for col in range(1, r+1):
        print(num , end='')
        num = num+1
        
    print("")
'''

'''
for r in range(1,6):
    for col in range(1, r+1):
        print(num , end='')
    num = num+1
        
    print("")
'''
'''
num = 65
for r in range(1,6):
    
    for col in range(1, r+1):
        char = chr(num)
        print(char , end='')
        
    num = num+1
        
    print("")

'''

'''
num = 65
for r in range(1,6):
    
    for col in range(1, r+1):
        char = chr(num)
        print(char , end='')
        num = num+1
    
        
    print("")

'''
'''
num = 65
for r in range(1,6):
    num = 65
    for col in range(1, r+1):
        char = chr(num)
        print(char , end='')
        
    num = num+1
        
    print("")

'''

