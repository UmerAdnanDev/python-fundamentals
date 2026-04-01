file = open('C:/Users/InflightAdmin/Documents/GitHub/python-fundamentals/File Handling/filetype.txt','r') # path,mode make sure the path has / not \
content = file.read()
print(content)
file.close()
print()
