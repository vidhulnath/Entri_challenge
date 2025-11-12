###c Check weather a number is amstrong number or not


# checking whether a number is armstrong number or not by user input
arm_num = int(input('Enter a Number  :')) ## input taken from user

armstrong = arm_num ## storing input number to another variable to apply boolean principle

arm_strn = str(arm_num) ## converting int number to string to count total charectors to apply factorial

l =len(arm_strn) ## total number of char in the string

total = 0 

for i in range (l):
    total = total + (arm_num% 10)**l 
    arm_num = arm_num // 10

if armstrong == total:
    print('Armstrong Number')
else:
    print('Not Armstrong Number')



