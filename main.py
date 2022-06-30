from random import randint
respuesta = "s"
puntajejugador = 0
puntajecomputadora = 0
while respuesta == "s":
    print("|" * 55)
    print("         ( Piedra, Papel o Tijera )")
    print("|" * 55)
    jugador = input(("Escribir tu jugada: piedra, papel o tijera: "))

    eleccion = ["piedra", "papel", "tijera"]
    computadora = eleccion[randint(0, 2)]
    print("La computadora elige: ", computadora)

    if computadora == jugador:
        print("Hay un empate")
    elif computadora == "piedra" and jugador == "tijera":
        print("La computadora gana. La piedra gana a tijera")
        puntajecomputadora += 1
    elif computadora == "papel" and jugador == "piedra":
        print("La computadora gana. El papel gana a piedra")
        puntajecomputadora += 1
    elif computadora == "papel" and jugador == "tijera":
        print("El jugador gana. La tijera gana a papel")
        puntajejugador += 1
    elif computadora == "tijera" and jugador == "papel":
        print("El judador gana. La tijera gana a papel")
        puntajejugador += 1
    print("El puntaje de la computadora: ", puntajecomputadora)
    print("El puntaje del jugador es: ", puntajejugador)
    print("¿Desea continuar? Si (s) o No (n)")
    respuesta = input()
