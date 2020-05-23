from numpy import*
v = eval(input(" "))
acu = 1.0
for i in v:
	acu*=i
print(round(acu**(1/len(v)),2))