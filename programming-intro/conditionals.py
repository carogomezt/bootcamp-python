num = int(input("Ingresa un número: "))

if num > 5:
    print("El número ingresado es mayor a 5")


num = int(input("Ingresa un número par: "))
if num % 2 != 0:
    print("ERROR: El número ingresado no es par")
print(f"El número ingresado fue: {num}")


edad = int(input("¿Cuántos años tiene? "))
print(edad < 18)
if edad < 18:
    print("Es usted menor de edad.")
    print("Espere unos a;os")
else:
    print("Es usted mayor de edad.")

print("¡Hasta la próxima!")

numero = int(input("Escriba un número: "))

if numero >= 0:
    print("Ha escrito un número positivo")
else:
    print("Ha escrito un número negativo")

numero = int(input("Escriba un número: "))

if numero % 2 != 0:
    doble = f"{numero * 2} doble"
    print(f"{numero + 1} es impar y {doble}")
    print(numero + 1, ", es impar", numero - 1, "-", numero * 2)
else:
    print(f"{numero} es par")


lloviendo = False
action = "playa" if not lloviendo else "biblioteca"
print("Vamos a la", action)
