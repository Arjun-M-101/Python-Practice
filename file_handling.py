# file=open("sample.txt","w")
# file.write("Hello, World!\n")
# file.close()
# sample.txt is created simply

# file=open("sample.txt","r")
# content=file.read()
# print("File content:\n",content)
# file.close()
# sample.txt is read and its content is printed

# file=open("sample.txt","a")
# file.write("This is a new line.\n")
# file.close()
# sample.txt is opened in append mode and a new line is added

#STANDARD WAY OF FILE HANDLING USING WITH BLOCK
# with open("sample.txt", "r") as file:
#     for line in file:
#         print(line.strip())
        
# If we use with, we don't need to explicitly close the file.
# The file is automatically closed when the block is exited.

# feedback = input("Please provide your feedback: ")

# with open("feedback.txt", "a") as file:
#     file.write(feedback+"\n")
# print("Feedback saved successfully!")
# With with block, we can write feedback 
# to a file without worrying about closing it.

with open("feedback.txt", "r") as file2:
    for lines in file2:
        print(lines.strip())