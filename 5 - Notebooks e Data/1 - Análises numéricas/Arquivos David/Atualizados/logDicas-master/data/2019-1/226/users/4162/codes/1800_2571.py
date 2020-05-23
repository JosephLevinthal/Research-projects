st = input("Digite uma srt: :")
s = ""
for i in range(len(st)):
	if(st[i].upper() != "A"):
		s = s+st[i]
print(s)