from numpy import*
s = input("digite os paises das pessoas: ").split(',')
z = zeros(5, dtype=int)
for i in range(size(s)):
	if s[i].upper() == "BE":
		z[0] = z[0] + 1
	if s[i].upper() == "ES":
		z[1] = z[1] + 1
	if s[i].upper() == "FR":
		z[2] = z[2] + 1
	if s[i].upper() == "IT":
		z[3] = z[3] + 1
	if s[i].upper() == "PT":
		z[4] = z[4] + 1
print(max(z))
print(z)