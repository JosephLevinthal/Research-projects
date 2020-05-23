from numpy import*

v = array(eval(input("digite as notas: ")))
a =min(v)
b = sum(v)
t = size(v)
y = (b - a)/(t - 1)
print(round(y, 2))