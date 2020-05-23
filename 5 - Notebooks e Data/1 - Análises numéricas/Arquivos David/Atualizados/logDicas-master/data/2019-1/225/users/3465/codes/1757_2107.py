string = input("")
string = string.lower()
vogal = 0
consoante = 0
for i in range(len(string)):
	if string[i] == 'a' or string[i] == 'e' or string[i] == 'i' or string[i] == 'o' or string[i] == 'u':
		vogal+=1
	else:
		consoante+=1
print(vogal)
print(consoante)
	