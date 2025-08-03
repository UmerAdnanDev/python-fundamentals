#Adding items to List
#append(item): adds item at the end of the list
sweets = ["cupcake","donut","pudding"]
sweets.append("pancake")
print(sweets)
#insert(index,item)
name = ["Oliver","Chris","Daniel"]
name.insert(0,"Thomas")
#Deleting items from the list 
#remove(item)
pets = ["cat","dog","sheep","rooster"]
pets.remove("dog")
print(pets)
#pop(index)
color = ["red","blue","green","white"]
color.pop() #removes last one
print(color)
color.pop(1)
print(color)
#Other Methods
#count(item) -> no of items
num = [1,1,2,3,2,1,1,]
print(num.count(1))
#index(item) -> index
flower = ["sunflower","rose","jasmine","tulip"]
print(flower.index("jasmine"))
#len(list) -> no of items 
print(len(flower))
#minimum,maximum
list_num =[1,2,-2,34]
print(min(list_num))
print(max(list_num))
list_alpha = ["a","A","b","B"]
print(min(list_alpha)) #by ASCII value 
print(max(list_alpha))
#Sorting
mixedup_list = [1,4,2,3,5]
mixedup_list.sort()
print(mixedup_list)
mixedup_list.reverse()
print(mixedup_list)
''' print(mixedup_list.sort()) returns None
print(mixedup_list.reverse())'''
#Clear()
Alist = [1,2,3,4,5]
Alist.clear()
print(Alist)
#Commom
A = [1,2,3]
B = [2,5,1]
Sa = set(A)
Sb =set(B)
C = Sa.intersection(Sb)
print(list(C))