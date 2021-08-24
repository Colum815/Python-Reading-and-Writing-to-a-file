"""
First I open a file called members. Then I read in the file using file.readlines().
This produces a \n at the end of each string except the last string.
To fix this is used line.strip() in a list comprehension which removes any spaces
at the start and end of a string. To get the intersection of read_file and user_input,
both variables must be converted to a set. I then store the intersection in a variable called common.
I then write the intersection of the too variables (common) to a new txt file called already_members.
To do this I iterate through common and write each line to already_members.txt.
"""

with open ("members.txt", "r") as file:
    read_file = [line.strip() for line in file.readlines()]
user_input = input("Enter some friends to see if they are members ").title().split()

user_input_set = set(user_input)
read_file_set = set(read_file)

common = user_input_set.intersection(read_file_set)
print(common)

open_file = open("already_members.txt", "w")
for line in common:
    open_file.write(line)