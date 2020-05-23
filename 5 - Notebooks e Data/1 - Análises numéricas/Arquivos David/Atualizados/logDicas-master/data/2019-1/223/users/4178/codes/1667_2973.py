var1= int(input("S: "))
var2= int(input("V: "))
var3= int(input("T: "))
s= var1 + (var2*var3)
if s < 100 :
	msg = 'OK'
else:
	msg = 'ACIMA'
print(s)
print(msg)