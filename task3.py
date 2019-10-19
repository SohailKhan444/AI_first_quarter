'''
letter = input("Enter a letter! : \n")
if letter.lower() == 'a':
    print(f" {letter} is a vowel")
elif letter.lower() == 'e':
    print(f" {letter} is a vowel")
elif letter.lower() == 'i':
    print(f" {letter} is a vowel")
elif letter.lower() == 'o':
    print(f" {letter} is a vowel")
elif letter.lower() == 'u':
    print(f" {letter} is a vowel")
else:
    print(f" {letter} is not a vowel. ")
'''
'''
a = int(input("Enter a value: \n"))
b = int(input("Enter 2nd number: \n"))
if a == b:
    print("Numbers are equal. ")
else:
    first = max(a, b)
    second = min (a , b)
    diff = first - second
    sum = first + second
    if diff == 5:
        print("Difference is equal to 5 ") 
    elif sum == 5:
        print("Sum is equal to 5")
    else:
        print("Sorry! no such things...")

'''
'''
# height 'feet and inches ' conversion to centimeter

feet_height = int(input("""enter your height: feet part. i.e 5 8" so just type 5. \n """))
inches_height = float(input("enter the inches part: "))

ConOf_feet = 12*feet_height
total_inches = ConOf_feet + inches_height

result = total_inches * 2.54
print(result)
'''
'''
# conversion
distance = int(input("Enter distance in feet. \n"))
to_inches = distance * 12      # 1 feet = 12 inches
print(f"{distance} in feet is converted into inches: {to_inches}inches \n")

to_yards = round(distance / 3.0 , 3)      # 3 feet = 1 yard so  1 feet = 1/3 yards
print(f"{distance} in feet is converted into yards: {to_yards}yards \n")

to_miles = round( distance / 5280.0 , 3)
print(f"{distance} in feet is converted into miles: {to_miles}miles \n")

 '''
while True:
    print("Convert any kind of below choices into seconds. ! \n")
    choice = int(input(""" choose one. what do you want to convert:
                            1) months
                            2) Days
                            3) hours
                            4) minutes


    """))

    if choice == 1:
        unit = 'months'

    if choice == 2:
        unit = 'Days'

    if choice == 3:
        unit = 'hours'

    if choice == 4:
        unit = 'minutes'


    info = int(input( f" Enter number of {unit}: \n "))


    if choice == 1:
        result = info * 30 * 24 * 60 * 60 
        break


    elif choice == 2:
        result = info * 24 * 60 * 60 
        break

    elif choice == 3:
        result = info * 60 * 60
        break

    elif choice == 4:
        result = info * 60 
        break
    else:
        print ("Wrong choice! please re enter")

print(str(result) + ' sec')








