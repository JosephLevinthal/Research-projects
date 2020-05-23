base = int(input("base: "))
for i in range(0,base):
	print(("*"*(base-i)) + ("o"*(2*i)) + ("*"*(base-i)))