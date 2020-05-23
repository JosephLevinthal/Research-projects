N = int(input("numero de linhas "))
s = input("digite uma sequencia STRING: ")
g = ""
j = 0
for i in range(0,N):
	while:
		if(i < len(s)):
			if(s[i]== s[i + 1]):
				j = j + 1 
				f = str(j)
				l = f + s[i]
	print(l)
	s = input("digite uma sequencia STRING: ")