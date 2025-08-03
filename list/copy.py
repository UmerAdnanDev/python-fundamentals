#Alias way
print("Alias Method")
list1 = [1,2,3,4,5]
list2 = list1 #meaning both sharing the same value at same memory location meaning change in one will result 
              #in change in another
list2[::] =6,7,8,9,10
print(list1)
print(list2)
print()
#copying
print("Copy Method")
list3 = [1,2,3,4,5]
list4 =list3.copy()
list3[::] =6,7,8,9,10
print(list3)
print(list4)