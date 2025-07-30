# Ejemplos de ciclos For

# Iterar en un rango de 1 a 11
for i in range(1, 11):
    print(i)

# Iterar en una lista
numbers = [0, 1, 2, 3, 4, 5]
for num in numbers:
    print(num)

# Iterar sobre un diccionario
fruits = {
    "Fresa": "roja",
    "Limon": "verde",
    "Papaya": "naranja",
    "Guayaba": "rosa",
}

for name, color in fruits.items():
    print(f"{name} es de color {color}")

# Ejemplos de ciclos while

want_greet = "S"  # importante dar un valor inicial

while want_greet == "S":
    print("Hola qué tal!")
    want_greet = input("¿Quiere otro saludo? [S/N] ")
print("Que tenga un buen día")

# Ejemplo con contador
day = 0
week = [
    "Lunes",
    "Martes",
    "Miércoles",
    "Jueves",
    "Viernes",
    "Sabado",
    "Domingo",
]
while day < 7:
    print(f"Hoy es {week[day]}")
    day += 1


# Ejemplo de break
animals = ["cat", "dog", "rabbit", "horse", "dolphin"]
for animal in animals:
    if "o" in animal:
        break
    print(animal)

# Ejemplo de continue
animals = ["cat", "dog", "rabbit", "horse", "dolphin"]
for animal in animals:
    if "o" in animal:
        continue
    print(animal)

# Ejemplo de else
animals = ["cat", "dog", "rabbit", "horse", "dolphin"]
for animal in animals:
    print(animal)
else:
    print("Done!")


animals = ["cat", "dog", "rabbit", "horse", "dolphin"]
for animal in animals:
    if animal == "dog":
        break
    print(animal)
else:
    print("Done!")


# Ejemplo FizzBuzz
# Escriba un programa que imprima los numeros del 1 al 100.
# Si el numero es multiplo de 3 imprimir Fizz
# Si el numero es multiplo de 5 imprimir Buzz
# Si el numero es multiplo de 3 y 5 imprimir FizzBuzz

for num in range(1, 101):
    if num % 3 == 0 and num % 5 == 0:
        print(f"FizzBuzz -> {num}")
    elif num % 3 == 0:
        print(f"Fizz -> {num}")
    elif num % 5 == 0:
        print(f"Buzz -> {num}")
    else:
        print(f"-> {num}")
