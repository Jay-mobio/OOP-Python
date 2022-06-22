f = open("C:\\Users\jayka\OneDrive\Desktop\git\OOP-Python\First.txt", "a")
f.write("Now the file is edited")
f.close()

f = open(r"C:\\Users\jayka\OneDrive\Desktop\git\OOP-Python\First.txt")
print(f.read())