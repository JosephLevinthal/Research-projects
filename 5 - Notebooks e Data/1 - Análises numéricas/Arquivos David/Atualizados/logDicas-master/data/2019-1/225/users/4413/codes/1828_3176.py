string = input(" ")
string = string.lower()
vog = 0
con = 0 
for i in string:
	if i=="a" or i=="e" or i=="i" or i=="o" or i=="u":
		vog+=1 
	else:
		con+=1
print(vog)
print(con)