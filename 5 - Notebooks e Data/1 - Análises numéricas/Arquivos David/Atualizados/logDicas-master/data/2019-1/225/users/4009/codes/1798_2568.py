string=""
n = int(input(""))
o =''
for i in range(n):
	string+="*"
for i in range(n):
	aux = string[0:(len(string)-i)]+o+o+string[i::]
	print(aux)
	o+='o'