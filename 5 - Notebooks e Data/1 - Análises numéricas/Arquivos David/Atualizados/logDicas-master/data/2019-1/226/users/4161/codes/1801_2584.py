n = int(input("serie: "))
r = 0
for x in range(1,n + 1):
	if x%2 != 0:
		r = r + 1/x
	else:
		r = r - 1/x
print("H =",round(r,6))