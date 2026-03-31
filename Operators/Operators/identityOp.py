#IdentityOp(is , is not)
#used to compare memory location of object rather than value
a = [1,2,3] 
b = [1,2,3]
c = a
print(b is a)
print(c is a)
# False
# True