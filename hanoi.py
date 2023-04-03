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

import time
import csv
import time
import csv
import os.path

headers = ["Discos", "Tiempo"]
file_exists = os.path.isfile("registros.csv")

def hanoi(n, origen, destino, auxiliar, memo={}):
    if n == 1:
        print(f"Mover disco 1 desde {origen} hacia {destino}")
        return 1  # Retorna 1 movimiento
    key = (n, origen, destino, auxiliar)
    if key in memo:
        return memo[key]
    movimientos = 0
    movimientos += hanoi(n-1, origen, auxiliar, destino, memo)
    print(f"Mover disco {n} desde {origen} hacia {destino}")
    movimientos += 1  # Añade 1 movimiento
    movimientos += hanoi(n-1, auxiliar, destino, origen, memo)
    memo[key] = movimientos
    return movimientos

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
