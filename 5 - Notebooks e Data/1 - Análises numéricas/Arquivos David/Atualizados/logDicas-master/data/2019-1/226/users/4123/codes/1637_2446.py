s = str(input())
while len(s) < 6:
	s += "0"
s = list(map(int, s))
if (s[0]+s[2]+s[4])%(s[1]+s[3]+s[5])==0 or (s[1]+s[3]+s[5])%(s[0]+s[2]+s[4])==0:
	print("acesso liberado")
else:
	print("senha invalida")
#print((s[0]+s[2]+s[4])%(s[1]+s[3]+s[5]))
#for i in range(0,6):
#	print(s[i], "em",i,";", end=' ')