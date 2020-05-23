qi = int(input(":"))
p = float(input(":"))
qf = int(input(":"))

i = 0

while(qi > 0 and qi < 12000):
	qi = qi + ((qi * p)/100)-qf
	i = i + 1
if(qi >= 12000):
	print("LIMITE")
else:
	print("EXTINCAO")
print(i)
	