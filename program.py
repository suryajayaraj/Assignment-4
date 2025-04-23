#

def read_file(filename):
    try:
     file = open(filename, 'r')
     print("File content:\n")
     for line in file:
         print(line.strip())
    except FileNotFoundError:
        print(f"Error: The file '{filename}' does not exist.")
read_file('sample.txt')

