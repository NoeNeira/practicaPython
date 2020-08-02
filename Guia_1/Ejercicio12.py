"""
Crear un programa que almacene los vectores (1,2,3) y (-1,0,2) en dos listas 
y muestre por pantalla su producto escalar.
"""

vectorUno = [1,2,3]
vectorDos = [-1,0,2]

productoEscalar = []
    
# for i in range(len(vectorUno)): ## equivalente a for(int i = 0; i < n; i++) en Java
#     productoEscalar.append(vectorUno[i]*vectorDos[i])

i = 0

while i < len(vectorUno):
    productoEscalar.append(vectorUno[i]*vectorDos[i])
    i += 1

# productoEscalar.append(vectorUno[0]*vectorDos[0])
# productoEscalar.append(vectorUno[1]*vectorDos[1])
# productoEscalar.append(vectorUno[2]*vectorDos[2])

suma = 0

for i in productoEscalar:
     suma += i

print(productoEscalar)

print(suma)


 


