score = float(input("Ingresa tu puntaje en numeros: "))

if 4.5 <= score <= 5:
    grade = "E"
elif 4 <= score < 4.5:
    grade = "S"
elif 3 <= score < 4:
    grade = "A"
elif 2 <= score < 3:
    grade = "I"
elif 0 <= score < 2:
    grade = "D"
else:
    grade = "Puntaje Invalido"

grades = {
    "E": "Excelente",
    "S": "Sobresaliente",
    "A": "Aceptable",
    "I": "Insuficiente",
    "D": "Deficiente",
}

print(f"Tu puntaje es -> {grade}: {grades.get(grade) or '.'}")


# Juego de Piedra, Papel o Tijera.

import random

player_choice_input = input(
    "Piedra (Rock), Papel (Paper), Tijera (Scissors) -> (r/p/s):"
)

player_choice = player_choice_input.lower()

if player_choice not in ["r", "p", "s"]:
    raise Exception("Opcion Invalida!")

computer_choice = random.choice(["r", "p", "s"])

print(f"Eleccion del computador (Computer's Choice): {computer_choice}")

if player_choice == computer_choice:
    print("Empate (Tie)")
elif player_choice == "r" and computer_choice == "s":
    print("Humano gana! (Player wins!)")
elif player_choice == "s" and computer_choice == "p":
    print("Humano gana! (Player wins!)")
elif player_choice == "p" and computer_choice == "r":
    print("Humano gana! (Player wins!)")
else:
    print("Computador gana! (Computer wins!)")


# Match Case - Ejemplo de validacion


def provide_access(user):
    return {"username": user, "password": "admin"}


user = str(input("Escribe tu usuario: "))

match user:
    case "ana":
        print(
            "Ana no tiene acceso a la base de datos, "
            "Solo tiene acceso al backend"
        )
    case "carlos":
        print(
            "Carlos no tiene acceso a la base de datos, "
            "solo tiene acceso al frontend"
        )
    case "caro":
        print("Caro tiene acceso a la base de datos")
        print(provide_access(user))
    case _:
        print("No tienes acceso al sistema")


# Ejemplo usando or
match user:
    case "ana" | "carlos" | "juan":
        print("No tienes acceso a la base de datos")
    case "caro":
        print("Caro tiene acceso a la base de datos")
        print(provide_access(user))
    case _:
        print("No tienes acceso al sistema")

# Ejemplo usando expresion compleja

allowed_users = ["caro", "ana"]
match user:
    case user if user in allowed_users:
        print(f"{user} tiene acceso a la base de datos 😊")
        print(provide_access(user))
    case _:
        print("No tienes acceso al sistema")
