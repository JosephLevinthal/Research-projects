n1 = int(input())
n2 = int(input())
n3 = int(input())

if(n1 < n2 < n3):
	print(n1)
if(n1 < n3 < n2):
	print(n1)
if(n2 < n1 < n3):
	print(n2)
if(n2 < n3 < n1):
	print(n2)
if(n3 < n2 < n1):
	print(n3)
if(n3 < n1 < n1):
	print(n3)
	