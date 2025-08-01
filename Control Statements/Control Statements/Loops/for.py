#for loop: it is used with sequences or count controlled environments
for i in range(1,10):#(include,exclude)
    print(i)
print()
for i in range(1,10,2):#(include,exclude,step)
    print(i)
print()
for i in range(10,0,-1):
    print(i)
print()
subjects = ["Maths","English","History","Science"]
print("Subjects:")
for subject in subjects:
    print("-"+subject)
print("range")
a = list(range(1,23))
b = list(range(1,57,2))
print(a)
print(b)
    
