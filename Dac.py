def hanoi_divide_and_conquer(n, origen, destino, auxiliar):
    if n == 1:
        print(f"Mover disco 1 desde {origen} hacia {destino}")
        return 1  # Retorna 1 movimiento
    
    movimientos = 0
    # Mover los primeros n-1 discos desde la torre A hasta la torre B, utilizando la torre C como auxiliar
    movimientos += hanoi_divide_and_conquer(n-1, origen, auxiliar, destino)
    # Mover el disco n desde la torre A hasta la torre C
    print(f"Mover disco {n} desde {origen} hacia {destino}")
    movimientos += 1
    # Mover los n-1 discos restantes desde la torre B hasta la torre C, utilizando la torre A como auxiliar
    movimientos += hanoi_divide_and_conquer(n-1, auxiliar, destino, origen)
    
    return movimientos

n = 10
origen = "A"
destino = "C"
auxiliar = "B"

movimientos = hanoi_divide_and_conquer(n, origen, destino, auxiliar)

print(f"Se necesitaron {movimientos} movimientos para resolver el problema de las Torres de Hanoi con {n} discos.")
