v= input("srt")
t=0
n=len(v)
a=""
while t<n:
	if n-t!=3:
		a=a + v[t]+v[t+1]+v[t+2]+"."
		t=t+3
	else:
		a=a + v[t]+v[t+1]+v[t+2]
		t=t+3
print(a)