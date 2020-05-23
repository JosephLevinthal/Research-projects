from numpy import*
v = array(eval(input("v:")))
n = size(v)
m = (sum(v)**1/2)
x = m + (n-1)**1/2 
z= x / n
y= z**2

print(round(y, 2))


