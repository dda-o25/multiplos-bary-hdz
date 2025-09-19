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
if a%b==0 or b%a==0:
    print(f"{a} es un múltiplo de {b}")
else:
    print(f"Ninguno de los números es múltiplo del otro")




# Salidas
