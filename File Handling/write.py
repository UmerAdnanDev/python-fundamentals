file = open('C:/Users/InflightAdmin/Documents/Python/File Handling/filewrite.txt','w') # only allows writting and will create a new file if not already present and will override the data
content = input("Enter content to write in the file: ")
file.write(content)
print("Data Successfully Stored")
file.close()