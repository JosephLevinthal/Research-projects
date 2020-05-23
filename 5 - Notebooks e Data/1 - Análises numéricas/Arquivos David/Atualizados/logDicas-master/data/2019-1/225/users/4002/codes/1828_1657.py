from numpy import*

string = input(" ")
string = string.split(",")
v = zeros(5, dtype = int)

for i in string:
	if i == "AZ":
		V[0] = v[0] + 1
	elif i == "CA" :
		v[1] = v[1] + 1
	elif i == "FL":
		v[2] = v[2] + 1
	elif i == "PA":
		V[3] = v[3] + 1
	elif i == "WI":
		v[4] = v[4] + 1
print(v.max())
print(v)