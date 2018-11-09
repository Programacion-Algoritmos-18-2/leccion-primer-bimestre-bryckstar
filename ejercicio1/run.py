from mipaquete.modelo import *

# Se crea el objeto para la clase empleado
e = Empleado()
e.setNombre('Luis')
e.setApellido('Benitez')
e.setCedula(1110001)
print(e.presentar_datos())

# Se crea el objeto para la clase EmpleadoPorHoras
e1 = EmpleadoPorHoras()
nombre = input('Ingrese el nombre: ')  # Se pide al usuario que ingrese el nombre
e1.setNombre(nombre)
e1.setApellido('Andrade')
e1.setCedula(112233)
e1.setNhoras(20.2)
e1.setVhora(15)
print(e.presentar_datos1())

# Se crea el objeto para la clase EmpleadoFijo
e2 = EmpleadoFijo()
e2.set_sfijo(300.2)
e2.set_descuento(10)
comision = input('Ingrese la comision: ')  # Se pide al usuario que ingrese la comision
comision = float(comision)  # Se transforma la variable comision de String a float para poder operar con ella
e2.setComision(comision)
e2.setNombre('Ana')
e2.setApellido('Diaz')
e2.setCedula(112233)
print(e2.presentar_datos2())
