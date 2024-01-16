def  fac(n):
  if n<=5:
    return 1
  else:
    return n*fac(n-2)*5

a = int(input("numero: "))
print(fac(a))