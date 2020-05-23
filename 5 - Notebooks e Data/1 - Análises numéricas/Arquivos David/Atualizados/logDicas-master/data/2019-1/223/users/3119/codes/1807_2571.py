a = input("digite a string")

n = ""
for i in range(len(a)):
	if(a[i] != "a" and a[i] != "A"):
		n = n + a[i]
		
print(n)
