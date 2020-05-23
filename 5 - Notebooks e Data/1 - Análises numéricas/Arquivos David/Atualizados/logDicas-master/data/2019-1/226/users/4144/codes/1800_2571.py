a = input("digite bro: ")
b = ""
for i in range(len(a)):
	if(a[i].upper() != "A"):
		b = b + a[i]
print(b)