

i = s = 0

while 1:
	n = input()
	r = len(n)
	i = s = 0
	if int(n)<0:
		break
	for i in range(0,r):
		s += int(n[int(i)])**r
	if s == int(n):
		print("ARMSTRONG")
	else:
		print("NAO ARMSTRONG")
