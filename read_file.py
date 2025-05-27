try:
    file = open("sample.txt", 'r')
    print("File content:")
    for line in file:
        print(line.strip())
    file.close()
except FileNotFoundError:
    print("the file 'Sample.txt' was not found.")
