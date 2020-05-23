from numpy import*
v = array(eval(input("digite numeros: ")))
n = sum(v[0:])
m = (((v[0]**(1/6) + v[1]**(1/6) + v[2]**(1/6) + v[n-1]**(1/6))**6)/n)
print(round(m, 2))