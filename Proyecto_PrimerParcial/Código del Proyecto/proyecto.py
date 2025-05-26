#Generador de matriz de relaciones binarias
conjunto = [2, 3, 4, 5, 6]

# Inicializamos una matriz de ceros (relación vacía)
matriz = [[0 for _ in conjunto] for _ in conjunto]

# Pedimos al usuario que ingrese las parejas que forman la relación
print("Introduce las parejas que forman la relación binaria (ej: 1 2). Escribe 'fin' para terminar.")
while True:
    entrada = input("Pareja: ")
    if entrada.lower() == 'fin':
        break
    try:
        a, b = map(int, entrada.split())
        if a in conjunto and b in conjunto:
            i = conjunto.index(a)
            j = conjunto.index(b)
            matriz[i][j] = 1 
        else:
            print("Los valores deben pertenecer al conjunto.")
    except:
        print("Entrada inválida. Escribe dos números separados por espacio.")

#Matriz de relación
print("\nMatriz de relación:")
print("   ", end="")
for x in conjunto:
    print(f"{x} ", end="")
print()
for i in range(len(conjunto)):
    print(f"{conjunto[i]}: ", end="")
    for j in range(len(conjunto)):
        print(f"{matriz[i][j]} ", end="")
    print()

#Propiedades
# Reflexiva 
es_reflexiva = True
for i in range(len(conjunto)):
    if matriz[i][i] != 1:
        es_reflexiva = False
        print(f"No es reflexiva porque falta la pareja ({conjunto[i]}, {conjunto[i]})")

#Simetrica
es_simetrica = True
for i in range(len(conjunto)):
    for j in range(len(conjunto)):
        if matriz[i][j] != matriz[j][i]:
            es_simetrica = False
            break

#Resultados 
print("\nPropiedades de la relación:")
print("Reflexiva:" , "Sí" if es_reflexiva else "No")
print("Simétrica:", "Sí" if es_simetrica else "No")