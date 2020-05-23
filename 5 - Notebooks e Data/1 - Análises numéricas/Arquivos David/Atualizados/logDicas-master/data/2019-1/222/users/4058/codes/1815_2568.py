num = int(input("Numero: "))
str = "*"
o = "o"
for i in range(num):
	print (str*(num-i)+o*i+o*i+str*(num-i))