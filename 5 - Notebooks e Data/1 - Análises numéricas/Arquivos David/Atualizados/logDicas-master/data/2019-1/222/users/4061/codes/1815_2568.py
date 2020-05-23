num = int(input("Numero: "))
str = "*"
str1 = "o"
for i in range(num):
	print (str*(num-i)+str1*i+str1*i+str*(num-i))