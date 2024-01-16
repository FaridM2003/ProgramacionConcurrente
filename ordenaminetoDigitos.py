a = int(input("Enter the first number: "))
vector = []
for i in range(1,a):
  vector.append(int(input("agregue %i: ")))
vector.sort()
print(vector)