# def moverTorre(altura, origen, destino, intermedio, memo):
#     if altura == 1:
#         print("mover disco de", origen, "a", destino)
#         return
#     if (altura, origen, destino, intermedio) in memo:
#         return memo[(altura, origen, destino, intermedio)]
    
#     moverTorre(altura-1, origen, intermedio, destino, memo)
#     print("mover disco de", origen, "a", destino)
#     memo[(altura, origen, destino, intermedio)] = True
#     moverTorre(altura-1, intermedio, destino, origen, memo)

# memo = {}
# moverTorre(5, "A", "B", "C", memo)

def hanoi(n, origen, destino, auxiliar):
    if n == 1:
        print(f"Mover disco 1 desde {origen} hacia {destino}")
        return 1  # Retorna 1 movimiento
    movimientos = 0
    movimientos += hanoi(n-1, origen, auxiliar, destino)
    print(f"Mover disco {n} desde {origen} hacia {destino}")
    movimientos += 1  # Añade 1 movimiento
    movimientos += hanoi(n-1, auxiliar, destino, origen)
    return movimientos

# Ejemplo de uso
movimientos = hanoi(10, "Torre A", "Torre C", "Torre B")
print(f"Se necesitaron {movimientos} movimientos.")
