from numpy import*
v=input("digite a vogal:")
copy=0
copy2=0
for i in v:
	if(i== "a" or i=="e" or i=="i" or i== "o" or i=="u"):
		copy=copy+1
print(copy)

print(len(v)-copy)

