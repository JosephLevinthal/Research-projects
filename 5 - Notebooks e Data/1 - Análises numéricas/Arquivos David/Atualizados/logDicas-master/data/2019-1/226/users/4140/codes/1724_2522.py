n=int(input())
total=1
i=1

while(i<=n ):
	calc=(1+(i/(i+2)))
	total=(calc*total)
	i=i+1
final=2*(total)
print(round(final,10))