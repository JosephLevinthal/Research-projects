h = float(input("altura: "))
sex = input("sexo:(M/F) ")

if sex =="M" or "F":
	if sex == "F":
		p_ideal = (62.1 * h) - 44.7
		print(round(p_ideal, 2))
	else:
		p_ideal = (72.7 * h) - 58
		print(round(p_ideal, 2))