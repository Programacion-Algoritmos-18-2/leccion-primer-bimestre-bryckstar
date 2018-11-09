from mipaquete.modelo import *

#Crear empleado
e = Empleado()
e.setNombre('Luis')
e.setApellido('Benitez')
e.setCedula(1110001)
print(e.presentar_datos())