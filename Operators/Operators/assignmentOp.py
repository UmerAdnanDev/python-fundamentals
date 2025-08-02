#Assignment Operator
# +=,-=,*=,/=,//=,%=,**=
"""
For Example: x+=1 == x=x+1
"""
# can't print as print(2+=3) or o = 4 , print(o+=3)
# value changes after each assignment operator
'''
for example: a = 2 -> a+=2 -> a = a + 2 -> a = 4 ->a/=2 -> a = 2
'''
o1 = 2 
o2 = 4 
o3 = 56 
o4 = 3.12
o5 = 8 
o6 = 6
o1+=4 
o2 -= 3
o3/=2
o4//=3
o5**=2
o6%=2
print(o1)
print(o2)
print(o3)
print(o4)
print(o5)
print(o6)
# 6
# 1
# 28.0
# 1.0
# 64
# 0