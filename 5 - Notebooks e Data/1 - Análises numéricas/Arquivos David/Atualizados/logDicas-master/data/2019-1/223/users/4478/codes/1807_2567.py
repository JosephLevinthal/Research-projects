base = int(input("base do desenho: "))

for ast in range(0, base):
	for i in range(0, base -ast):
		print("*", end ="")
	print("\n", end ="")
for ast in range(0, base):
	for i in range(0, ast+1):
		print("*", end ="")
	print("\n", end ="")
