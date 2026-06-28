import random

# Lista donde se almacenará el historial de las partidas
historial = []


# ---------------- FUNCIONES ---------------- #

def mostrar_menu():
    print("\n==============================")
    print("     ADIVINA EL NÚMERO")
    print("==============================")
    print("1. Jugar")
    print("2. Ver historial")
    print("3. Ver mejor puntuación")
    print("4. Salir")


def seleccionar_dificultad():

    print("\nSeleccione un nivel de dificultad")
    print("1. Fácil (1 - 50)")
    print("2. Medio (1 - 100)")
    print("3. Difícil (1 - 200)")

    while True:

        opcion = input("Opción: ")

        if opcion == "1":
            return 50

        elif opcion == "2":
            return 100

        elif opcion == "3":
            return 200

        else:
            print("Seleccione una opción válida.")


def jugar():

    limite = seleccionar_dificultad()

    numero_secreto = random.randint(1, limite)

    intentos = 0

    print(f"\nDebes adivinar un número entre 1 y {limite}")

    while True:

        try:

            numero = int(input("Ingrese un número: "))

            intentos += 1

            if numero < numero_secreto:

                print("El número es mayor.")

            elif numero > numero_secreto:

                print("El número es menor.")

            else:

                print("\n¡FELICIDADES!")

                print("Adivinaste el número en", intentos, "intentos.")

                nombre = input("Ingrese su nombre: ")

                partida = {

                    "Jugador": nombre,
                    "Intentos": intentos,
                    "Nivel": limite

                }

                historial.append(partida)

                break

        except ValueError:

            print("Debe ingresar únicamente números.")


def ver_historial():

    print("\n======= HISTORIAL =======")

    if len(historial) == 0:

        print("Todavía no existen partidas registradas.")

    else:

        contador = 1

        for partida in historial:

            print("----------------------------------")

            print("Partida", contador)

            print("Jugador :", partida["Jugador"])

            print("Intentos:", partida["Intentos"])

            if partida["Nivel"] == 50:

                print("Nivel   : Fácil")

            elif partida["Nivel"] == 100:

                print("Nivel   : Medio")

            else:

                print("Nivel   : Difícil")

            contador += 1


def mejor_puntuacion():

    print("\n===== MEJOR PUNTUACIÓN =====")

    if len(historial) == 0:

        print("No existen partidas registradas.")

    else:

        mejor = historial[0]

        for partida in historial:

            if partida["Intentos"] < mejor["Intentos"]:

                mejor = partida

        print("Jugador :", mejor["Jugador"])

        print("Intentos:", mejor["Intentos"])

        if mejor["Nivel"] == 50:

            print("Nivel   : Fácil")

        elif mejor["Nivel"] == 100:

            print("Nivel   : Medio")

        else:

            print("Nivel   : Difícil")


# ---------------- PROGRAMA PRINCIPAL ---------------- #

while True:

    mostrar_menu()

    opcion = input("\nSeleccione una opción: ")

    if opcion == "1":

        jugar()

    elif opcion == "2":

        ver_historial()

    elif opcion == "3":

        mejor_puntuacion()

    elif opcion == "4":

        print("\nGracias por utilizar el programa.")

        break

    else:

        print("Opción incorrecta.")
