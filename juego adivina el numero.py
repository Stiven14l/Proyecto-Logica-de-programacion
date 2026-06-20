import random

numero_secreto = random.randint(1, 100)
intentos = 0

print("Adivina el número")

while True:

    numero = int(input("Ingrese un número: "))
    intentos += 1

    if numero < numero_secreto:
        print("El número es mayor")
        
    elif numero > numero_secreto:
        print("El número es menor")
    else:
        print("¡Felicidades! Adivinaste el número en", intentos, "intentos")
        break