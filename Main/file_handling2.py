# FILE HANDLING WITH READLINE AND WITH BLOCK

# Why readline()? Because readline() reads one line at a time,
# which is useful for large files where you don't want to 
# read the entire file into memory.
'''
with open("sample_data.txt","r") as file1:
    while True:
        lines=file1.readline()
        if not lines:
            break
        elif "Strawberry" in lines:
            print(lines.strip())
'''          
# This will print only the lines containing 
# "Strawberry" from sample_data.txt

# IF YOU WANT TO INCLUDE CONDITION USE WHILE LOOP FOR FILE HANDLING
# OR ELSE THE BELOW IS THE BEST WAY TO READ FILES - FOR LOOP
lines = int(input("Enter the number of lines to read: "))
with open("data.txt", "r") as file3:
    for _ in range(lines):
        print(file3.readline().strip())

# Keep in mind that if you are not using file in for loop,
# Then you can follow this for _ in range(lines):
# But if you are using file in for loop,
# Then you can directly use for line in file3: like below
'''
with open("feedback.txt", "r") as file2:
    for lines in file2:
        print(lines.strip())
'''