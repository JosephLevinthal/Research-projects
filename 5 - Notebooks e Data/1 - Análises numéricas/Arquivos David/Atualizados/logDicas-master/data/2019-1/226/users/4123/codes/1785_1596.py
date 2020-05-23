from numpy import*
nt = array(eval(input()))
n = sum(nt)
o = min(nt)
m = (n-o)/(len(nt)-1)
print(round(m,2))