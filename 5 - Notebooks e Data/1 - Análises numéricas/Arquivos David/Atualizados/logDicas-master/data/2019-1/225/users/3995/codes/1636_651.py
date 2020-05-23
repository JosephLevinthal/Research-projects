a=float(input("altura:"))
s=input("M/F?")
if(s=="M"):
	pi=(72.7*a)-58
else:
	pi=(62.1*a)-44.7
print(round(pi, 2))