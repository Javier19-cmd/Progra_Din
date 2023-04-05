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

import time
import csv
import time
import csv
import os.path

headers = ["Discos", "Tiempo"]
file_exists = os.path.isfile("registros.csv")

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

# for x in range()
cantidad_discos = int(input("Ingrese la cantidad de discos que desea resolver: "))

start_time = time.time()
movimientos = hanoi(cantidad_discos, "Torre A", "Torre C", "Torre B")
end_time = time.time()
tiempo = end_time - start_time

print(f"Para {cantidad_discos} discos se necesitaron {movimientos} movimientos y {tiempo} segundos.")

with open("registros.csv", "a", newline="") as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=headers)
    if not file_exists:
        writer.writeheader()
    writer.writerow({"Discos": cantidad_discos, "Tiempo": tiempo})
