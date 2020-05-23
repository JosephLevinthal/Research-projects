from numpy import*
cli = input("Digite os tons de pele mc/c/cm/em/e/me: ").split(',')

c = zeros(6, dtype = int)

for i in range(size(cli)):
	if cli[i] == "mc":
		c[0] = c[0] + 1
		print(c)
	if cli[i] == "c":
		c[1] = c[1] + 1
		print(c)
	if cli[i] == "cm":
		c[2] = c[2] + 1
		print(c)
	if cli[i] == "em":
		c[3] = c[3] + 1
		print(c)
	if cli[i] == "e":
		c[4] = c[4] + 1
		print(c)
	if cli[i] == "me":
		c[5] = c[5] + 1
		print(c)
print(c[0] or c[1] or c[2] or c[3] or c[4] or c[5])


	

		