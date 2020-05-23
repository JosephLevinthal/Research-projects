from numpy import *
v = array(eval(input("insira os numeros:")))

a = 0
i = 0
m = (sum(v))**5
n = size(v)
o = (m/n)**1/5
print(round(o,2))