"""
Hernández Robles Bruce de Bary 
18/09/2025

El siguiente programa determina si dos números enteros son múltiplos uno del otro.
"""

# Declaraciones

# Entradas
a = int(input("Ingresa el primer número entero"))
b = int(input("Ingresa el segundo número entero"))

# Proceso
if a==0 or b==0:
    print("No se pueden determinar múltiplos con cero.")
else:
    if a % b == 0:
        print(f"{a} es múltiplo de {b}")
    elif b % a == 0:
        print(f"{b} es múltiplo de {a}")
    else:
        print("Ninguno de los números es múltiplo del otro")




# Salidas
