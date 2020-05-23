s=int(input("metros:"))
v= int(input("metros por segundo:"))
t= int(input("tempo:"))
s1= int(s+(v*t))
print(s1)
if(v<=100):
   print("OK")
else:
	print("ACIMA")