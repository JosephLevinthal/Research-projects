n = int(input())
o = int(input())
i = 1
s1 = s2 = 0

while i<n:
	if n%i == 0:
		s1+=i
	i+=1
i = 1
while i<o:
	if o%i == 0:
		s2+=i
	i+=1
print(s1)
print(s2)
if s1==o and s2==n:
	print("AMIGOS")
else:
	print("NAO AMIGOS")
	