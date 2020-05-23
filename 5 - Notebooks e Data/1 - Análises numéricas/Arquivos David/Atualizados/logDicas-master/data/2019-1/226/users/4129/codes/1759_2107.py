s = input("Digite sua string:").lower()

i = 0
vogais = 0
consoantes = 0
while(i < len(s)):
	if(s[i] == "a" or s[i] == "e" or s[i] =="i" or s[i] == "o" or s[i] == "u"):
		vogais = vogais + 1
	else:
		consoantes = consoantes + 1
	i = i + 1
print(vogais)
print(consoantes)