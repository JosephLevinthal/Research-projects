na = int(input("numero a ")) 
nb = int(input("numero b ")) 
nc = int(input("numero c ")) 
vlmax = max(na,nb,nc)
vlmim = min(na,nb,nc)
vlint = (na+nb+nc)-(vlmax+vlmim)
print(vlmim)
print(vlint)
print(vlmax)