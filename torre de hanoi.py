def hanoi(n):
  if n == 1:
    return 1
  else:
    return 2 * hanoi(n - 1) + 1

n = int(input("Ingrese un numero: "))
cont = hanoi(n)
print("El numero de movimientos es: ", cont)
