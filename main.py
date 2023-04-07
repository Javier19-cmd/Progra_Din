import time
import csv
import os.path
import subprocess
import pandas as pd
import matplotlib.pyplot as plt
from Dac import *
from PrograDinamica import *

headers = ["Discos", "Tiempo"]

print()
print("-"*32)
print("\tTorres de Hanoi")
print("-"*32)

ver = True

while ver:
    
    print("\nMenu\n1) Ejecucion algoritmos (1 vez)\n2) Ejecucion algoritmos n veces\n3) Graficas\n4) Salir")
    opc = int(input("Ingrese opcion: "))
    
    if(opc == 1):
        cantidad_discos = int(input("Ingrese la cantidad de discos que desea resolver: "))

        # Divide and Conquer
        print()
        print("-"*30)
        print("Divide and Conquer")
        print("-"*30)
        print()

        file_exists_dac = os.path.isfile("registros_dac.csv")

        start_time = time.time()
        movimientos = hanoi_divide_and_conquer(cantidad_discos, "A", "C", "B")
        end_time = time.time()
        tiempo = end_time - start_time

        print(f"Para {cantidad_discos} discos se necesitaron {movimientos} movimientos y {tiempo} segundos.")

        with open("registros_dac.csv", "a", newline="") as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=headers)
            if not file_exists_dac:
                writer.writeheader()
            writer.writerow({"Discos": cantidad_discos, "Tiempo": tiempo})

        print()
        print("-"*30)
        print("Programación dinámica")
        print("-"*30)
        print()

        # Programación dinámica
        file_exists_pd = os.path.isfile("registros_pd.csv")

        start_time = time.time()
        movimientos = hanoi(cantidad_discos, "Torre A", "Torre C", "Torre B")
        end_time = time.time()
        tiempo = end_time - start_time

        print(f"Para {cantidad_discos} discos se necesitaron {movimientos} movimientos y {tiempo} segundos.")

        with open("registros_pd.csv", "a", newline="") as csvfile:
            writer = csv.DictWriter(csvfile, fieldnames=headers)
            if not file_exists_pd:
                writer.writeheader()
            writer.writerow({"Discos": cantidad_discos, "Tiempo": tiempo})
            
    elif(opc == 2):
        cantidad_discos = int(input("Ingrese la cantidad de veces que se ejecutaran los programas: "))
        for i in range(cantidad_discos):
            subprocess.run(['python', 'DaCSubprocess.py', str(15*i)])
            subprocess.run(['python', 'PrograDinamicaSubprocess.py', str(15*i)])
        
    elif(opc == 3):
        # Carga los datos de los archivos CSV
        df_dac = pd.read_csv('registros_dac.csv')
        df_pd = pd.read_csv('registros_pd.csv')

        # Crea la gráfica combinada
        plt.scatter(df_dac['Discos'], df_dac['Tiempo'], label='Divide and Conquer')
        plt.scatter(df_pd['Discos'], df_pd['Tiempo'], label='Programacion Dinámica')
        plt.xlabel('Discos')
        plt.ylabel('Tiempo')
        plt.legend()
        plt.show()

    elif(opc == 4):
        print("\nGracias por utilizar este programa\n")
        ver = False
        
    else:
        print("Opcion invalida")
        