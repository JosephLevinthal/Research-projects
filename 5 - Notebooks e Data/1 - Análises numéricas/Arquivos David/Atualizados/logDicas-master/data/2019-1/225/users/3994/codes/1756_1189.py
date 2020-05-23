s=input("Digite a frase: ")
s= s.replace(' ','')
n=""
c=0
i=-1
j=1 #palindromo (supondo)
while(i>=-len(s)):
	n= n+s[i]
	if(s[i]!=s[c]):
		j=0
	c=c+1
	i=i-1
print(s.upper())
print(j)
	