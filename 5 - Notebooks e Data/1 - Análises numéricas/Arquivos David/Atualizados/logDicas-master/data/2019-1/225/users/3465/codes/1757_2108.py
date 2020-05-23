string = input("")
string = string.lower()
vogal = 0
consoante = 0
for i in range(len(string)):
	if not(string[i] == 'a' or string[i] == 'e' or string[i] == 'i' or string[i] == 'o' or string[i] == 'u' or string == ' '):
		string = string.replace(string[i],'p')
print(string)