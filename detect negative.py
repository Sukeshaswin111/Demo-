'''3. Create a Python program that continuously asks the user to enter a number. If the user
enters a negative number, print "Negative number detected. Exiting loop." and break the
loop.
'''
n=1
while n>0:
    num=int(input("Enter the number:"))
    if num>0:
        continue
    elif num<0:
        print("Negative number detected")
        break
