a = int(input("numero: "))
b = int(input("numero: "))
c = int(input("numero: "))
if ( b < c):
	if( a < b ):
		d = a
	else:
		d = b
if(c < b):
	if(a < c):
		d = a
	else:
		d = c
if(b < a):
	if( c < b):
		d = c
	else:
		d = b
print(d)