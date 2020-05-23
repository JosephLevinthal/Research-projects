from numpy import*
S = input("Digite uma string: ")
k = ""
i = 0
while(i < len(S)):
	if(S[i] != " "):
		k = k + S[i]
	i = i + 1
print(k.upper())

j = ""
i = -1 
while(i >= -len(S)):
	if(S[i] != " "):
		j = j + S[i]
	i = i - 1
n = 0
if(j == k):
	n = n + 1
print(n)
			


