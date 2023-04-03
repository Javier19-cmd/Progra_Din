def moverTorre(altura, origen, destino, intermedio, memo):
    if altura == 1:
        print("mover disco de", origen, "a", destino)
        return
    if (altura, origen, destino, intermedio) in memo:
        return memo[(altura, origen, destino, intermedio)]
    
    moverTorre(altura-1, origen, intermedio, destino, memo)
    print("mover disco de", origen, "a", destino)
    memo[(altura, origen, destino, intermedio)] = True
    moverTorre(altura-1, intermedio, destino, origen, memo)

memo = {}
moverTorre(5, "A", "B", "C", memo)
