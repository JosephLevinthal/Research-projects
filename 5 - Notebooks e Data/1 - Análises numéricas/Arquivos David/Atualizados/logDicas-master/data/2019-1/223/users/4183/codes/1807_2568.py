from numpy import *
x = int(input("Digite: "))
st1 = "*"
st2 = "o"
for i in range(x): 
	c = st1*(x-i) + st2*(x - (x - i)) + st1*(x-i)
print(c)