n  = int(input(""))
string=''
for i in range(n):
	string+='*'
for i in range(n):
	print(string[0:(len(string)-i)])
for i in range(1,n+1):
	print(string[0:i])
