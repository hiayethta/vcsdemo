"""
CP1404 - Practical
File reading applications and practice
"""

"""Ask user for name and print to text file"""
FILENAME = 'name.txt'

out_file = open(FILENAME, 'w')
name = input("Enter name: ").upper()
print(name, file=out_file)
out_file.close()

out_file = open(FILENAME, 'r')
for line in open(FILENAME):
    print(f"Hi {name}!")
out_file.close()
