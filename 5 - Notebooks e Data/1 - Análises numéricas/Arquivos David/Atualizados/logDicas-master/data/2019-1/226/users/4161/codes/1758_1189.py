from numpy import*
v = input("str: ").upper()
print(v.replace(" ",""))
a = ""
t = 0
n = len(v)
while t < n:
	a = v[t] + a
	t = t + 1
a = a.replace(" ", "")
a = str(a)
v = v.replace(" ", "")
if v==a:
	print(1)
else:
	print(0)
