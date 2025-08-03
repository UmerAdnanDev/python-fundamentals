#List is a collection of items enclosed within square brackets
A_List = [1,3,"5",True,9.9,5j]
print(A_List)
#Constructor Method
construct_List = list((1,2,3,4,"a","o","i")) #using list constructor
print(construct_List)
#Range Method
OddList = list(range(1,21,2))
EvenList = list(range(0,21,2))
print(OddList)
print(EvenList)
ReverseList = list(range(21,1,-1))
print(ReverseList)
#List Comprehension
#[expression for item in iterable if condition]
list1to10Square = [i**2 for i in range(1,10+1)]
print(list1to10Square)
listofEven = [i for i in range(1,25) if i%2==0]
print(listofEven)
listofOdd = [i for i in range(1,25) if i%2!=0]
print(listofOdd)
