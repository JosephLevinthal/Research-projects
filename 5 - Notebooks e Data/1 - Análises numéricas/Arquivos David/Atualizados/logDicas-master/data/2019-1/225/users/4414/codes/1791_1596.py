from numpy import*

v = array(eval(input("notas:")))


m =(sum(v) - min(v))
y= size(v)-1
x = (m/y)
print(round(x,2))