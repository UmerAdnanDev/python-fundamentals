#split() method divides a string into a list of substrings
text = "Python Programming Language"
print(text.split()) #['Python', 'Programming', 'Language']
text2 = "1,2,3,4,5"
print(text2.split(","))#splits w.r.t ,
text3 = "Umer:Ali:Hammad:Alishba"
print(text3.split(":"))
nameslist = input("Enter a name seperated with , : ").split(",")
print(nameslist) #['ali ', ' hassan', 'kamal ', 'jamal']
for name in nameslist:
    print(name)
#string.split(separator, maxsplit)
# separator (optional): The delimiter to split on (default is whitespace)
# maxsplit (optional): Maximum number of splits (default is -1, meaning all possible splits)    
