import sys
try :
    a = int(input("Enter the number: "))
except(ValueError):
    print("Error.. Number only")
    sys.exit()
