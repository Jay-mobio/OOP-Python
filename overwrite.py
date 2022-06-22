f = open("C:\\Users\jayka\OneDrive\Desktop\git\OOP-Python\Second.txt", "w")
f.write("oops I have deleted the content")
f.close()

f = open("C:\\Users\jayka\OneDrive\Desktop\git\OOP-Python\Second.txt", "r")
print(f.read())
