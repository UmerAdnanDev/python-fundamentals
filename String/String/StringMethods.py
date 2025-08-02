#Methos used with Strings which is a Sequence of characters
#all characters are indexed and are iterable but immutable
text = "Python is the best language for Ai"
print(len(text))# count of all characters including white space
print(text.lower())#all characters in lower case
print(text.upper())#all characters in upper case
print(text.title())#all first characters of each word in upper and rest in lower
print(text.capitalize())#only 1st letter in upper case
print(text.replace("Ai","Data Science")) # replacing characters
print(text.count("a"))#counts characters
print(text.find("P"))#returns index of character
print(text.swapcase())#changes case lower with upper and vice versa
print(text.startswith("P"))# returns boolean (True or False)
print(text.endswith("i"))# returns boolean (True or False)
print(text.index("y"))#returns index of character
print(text.isalnum())
print(text.istitle())
print(text.islower())
print(text.isupper())
print(text.isalpha())
chr1 = "1cdksaj6"
print(chr1.isalnum())#checks whether it contains both numbers and characters
chr2 = "12344"
print(chr1.isdigit())
print(chr2.isdigit())
chr3 = "3.142"
print(chr3.isdecimal())
