import time
import csv
import os.path

headers = ["Discos", "Tiempo"]
file_exists = os.path.isfile("registros_dac.csv")
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

print("\nDaC")
n = int(input("Ingrese la cantidad de discos que desea resolver: "))

start_time = time.time()
movimientos = hanoi_divide_and_conquer(n, "A", "C", "B")
end_time = time.time()
tiempo = end_time - start_time


print(f"Para {n} discos se necesitaron {movimientos} movimientos y {tiempo} segundos.")

with open("registros_dac.csv", "a", newline="") as csvfile:
    writer = csv.DictWriter(csvfile, fieldnames=headers)
    if not file_exists:
        writer.writeheader()
    writer.writerow({"Discos": n, "Tiempo": tiempo})