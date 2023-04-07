# def moverTorre(altura, origen, destino, intermedio, tabla_movimientos):
#     if altura == 1:
#         print("mover disco de", origen, "a", destino)
#         return
#     if (altura, origen, destino, intermedio) in tabla_movimientos:
#         return tabla_movimientos[(altura, origen, destino, intermedio)]
    
#     moverTorre(altura-1, origen, intermedio, destino, tabla_movimientos)
#     print("mover disco de", origen, "a", destino)
#     tabla_movimientos[(altura, origen, destino, intermedio)] = True
#     moverTorre(altura-1, intermedio, destino, origen, tabla_movimientos)

# tabla_movimientos = {}
# moverTorre(5, "A", "B", "C", tabla_movimientos)

def hanoi(n, origen, destino, auxiliar, tabla_movimientos={}):
    if n == 1:
        print(f"Mover disco 1 desde {origen} hacia {destino}")
        return 1  # Retorna 1 movimiento
    key = (n, origen, destino, auxiliar)
    if key in tabla_movimientos:
        return tabla_movimientos[key]
    movimientos = 0
    movimientos += hanoi(n-1, origen, auxiliar, destino, tabla_movimientos)
    print(f"Mover disco {n} desde {origen} hacia {destino}")
    movimientos += 1  # Añade 1 movimiento
    movimientos += hanoi(n-1, auxiliar, destino, origen, tabla_movimientos)
    tabla_movimientos[key] = movimientos
    return movimientos
