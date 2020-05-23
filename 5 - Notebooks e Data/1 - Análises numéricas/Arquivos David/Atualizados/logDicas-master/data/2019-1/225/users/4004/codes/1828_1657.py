from numpy import*
x = str(input("pessoas por estado: ")).split(',')
y = zeros(5, dtype=int) #[AZ,CA,FL,PA,WI]

for i in x:
	if i == "AZ":
		y[0] = y[0] + 1
	elif i == "CA":
		y[1] = y[1] + 1
	elif i == "FL":
		y[2] = y[2] + 1
	elif i == "PA":
		y[3] = y[3] + 1
	elif i == "WI":
		y[4] = y[4] + 1
print(max(y))
print(y)