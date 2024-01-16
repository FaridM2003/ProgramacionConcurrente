a = int(input("Enter the first number: "))
vector = []
for i in range(0,a):
  valor = int(input("Enter the number: "))
  vector.append(valor)
vector.sort()
print(vector)