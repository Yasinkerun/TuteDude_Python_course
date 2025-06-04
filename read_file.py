try:
    with open("sample.txt", 'r') as file:
        print("File content:")
        for line in file:
            print(line.strip())
except FileNotFoundError:
    print("The file 'sample.txt' was not found.")
