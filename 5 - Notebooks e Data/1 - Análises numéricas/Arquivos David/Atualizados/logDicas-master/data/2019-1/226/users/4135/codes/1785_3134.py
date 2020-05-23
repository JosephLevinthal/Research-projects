from numpy import*
v = array(eval(input("Insira um vetor:")))
n = size(v)
v1 = arange(n)

m = ((v*vt**2)/n)**0.5
print(round(m,2))

