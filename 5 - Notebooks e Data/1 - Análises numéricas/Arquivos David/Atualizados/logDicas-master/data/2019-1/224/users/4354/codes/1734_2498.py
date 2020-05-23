hab_A = int(input("numero de habitantes de A: "))
hab_B = int(input("numero de habitantes de B: "))
p_A = float(input("percentual de crescimento de A: "))
p_B = float(input("percentual de crescimento de B: "))
t = 0 
while (hab_A < hab_B):
	hab_A = hab_A + hab_A*(p_A/100)
	hab_B = hab_B + hab_B*(p_B/100)
	t = t + 1
	print(t)
	