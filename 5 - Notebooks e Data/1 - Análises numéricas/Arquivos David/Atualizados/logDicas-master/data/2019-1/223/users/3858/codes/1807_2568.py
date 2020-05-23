num = int(input())
for x in range (0,num,1):
	print((num-x)*'*' + 2*x*'o' + (num-x)*'*')
