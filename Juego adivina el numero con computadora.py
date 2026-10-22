import random
number_computer = random.randint(1, 100)
try_player = 7
while try_player > 0:
    player = int(input("Inserta un numero del 1 al 100:"))
    if player == number_computer:
        print("Ganaste has encontrado el numero")
        break
    elif player > number_computer:
        try_player = try_player - 1
        print("NUMERO MAs bajo")
        print(f"Te quedan {try_player} intentos")
    elif player < number_computer:
        try_player = try_player - 1
        print("Numero mas alto")
        print(f"Te quedan {try_player} intentos")
if try_player <= 0:
    print(f"Perdiste el numero secreto era {number_computer}")