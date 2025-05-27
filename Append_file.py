line1 = input("Enter text to write to the file: ")

file1 = open("output.txt","w")
file1.write(line1)
print("Data Successfully Written to output.txt")
file1.close()

line2 = input("Enter text to append to the file: ")
file2 = open("output.txt","a")
file2.write(line2 + "\n")
print("Data Successfully Appended")
file2.close()

file3 = open("output.txt","r")
print(file3.read())
file3.close()