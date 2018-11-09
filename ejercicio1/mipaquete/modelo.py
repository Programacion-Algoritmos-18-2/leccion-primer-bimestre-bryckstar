class Empleado(object):  # se crea la clase 'padre' empleado
    def __init__(self):  # Se crea el init con las variables de la clase
        self.nombre = ""
        self.apelldio = ''
        self.cedula = ''
        self.comision_fija = 0

    # Se crean los metodos para agregar y obtener las variables de la clase
    def setNombre(self, n):
        self.nombre = n

    def getNombre(self):
        return self.nombre

    def setApellido(self, n):
        self.apelldio = n

    def getApellido(self):
        return self.apelldio

    def setCedula(self, n):
        self.cedula = n

    def getCedula(self):
        return self.cedula

    def setComision(self, n):
        self.comision_fija = n

    def getComision(self):
        return self.comision_fija

    # Se presentan los datos
    def presentar_datos(self):
        cadena = 'Informacion de %s %s\n\tCEDULA: %d' % (self.getNombre(), self.getApellido(), self.getCedula())
        return cadena


# Se crea la clase empleado por hora, que hereda de la clase Empleado
class EmpleadoPorHoras(Empleado):
    def __init__(self):  # Se crea el init con las variables de la clase
        super(EmpleadoPorHoras, self).__init__()
        self.numero_horas = 0
        self.valor_hora = 0

    # Se crean los metodos para agregar y obtener las variables de la clase
    def setNhoras(self, n):
        self.numero_horas = n

    def getNhoras(self):
        return self.numero_horas

    def setVhora(self, n):
        self.valor_hora = n

    def getVhora(self):
        return self.valor_hora

    def calcular_sueldo_final(self):  # Se crea el metodo para poder calcular el sueldo final
        sf = self.getVhora() * self.getNhoras()
        return sf

    # Se presentan los datos
    def presentar_datos1(self):
        cadena = '%s\nNumero de Horas: %.1f\nValor de Hora: %.2f$\nSueldo Final: %.2f\n' % \
                 (super(EmpleadoPorHoras, self).presentar_datos(), self.getNhoras(), self.getVhora(),
                  self.calcular_sueldo_final())
        return cadena


class EmpleadoFijo(Empleado):
    def __init__(self):  # Se crea el init con las variables de la clase
        super(EmpleadoFijo, self).__init__()
        self.sueldo_fijo = 0
        self.descuento_seguro = 0

    # Se crean los metodos para agregar y obtener las variables de la clase
    def set_sfijo(self, n):
        self.sueldo_fijo = n

    def get_sfijo(self):
        return self.sueldo_fijo

    def set_descuento(self, n):
        self.descuento_seguro = n

    def get_descuento(self):
        return self.descuento_seguro

    # Se calcula el sueldo de acuerdo al descuento ingresado, se resta el porncentaje y se suma la comision fija
    def calcular_sueldo(self):
        sf = self.sueldo_fijo - (self.sueldo_fijo * (self.get_descuento() / 100)) + self.getComision()
        return sf

    # Se presentan los datos
    def presentar_datos2(self):
        cadena = '%s\nSueldo fijo: %2.f$\nDescuento del seguro: %d%%\nComision FIja: %.2f\nSueldo Final: %2.f\n' % \
                 (super(EmpleadoFijo, self).presentar_datos(), self.get_sfijo(), self.get_descuento(),
                  self.getComision(), self.calcular_sueldo())
        return cadena


class EmpleadoPorSemana(Empleado):

    def _init__(self):  # Se crea el init con las variables de la clase
        super(EmpleadoPorSemana, self).__init__()
        self.numeroSemanas = 0
        self.valorSemanal = 0

    # Se crean los metodos para agregar y obtener las variables de la clase
    def setNumeroSemanas(self, semanas):
        self.numeroSemanas = semanas

    def getNumeroSemanas(self):
        return numeroSemanas

    def setValorSemanal(self, valor):
        self.valorSemanal = valor

    def getValorSemanal(self):
        return valorSemanal

    def calcular_sueldo_final(self):  # Se calcula el sueldo final
        return self.obtenerNumeroSemanas() * self.obtenerValorSemanal() + self.obtenerComisionFija()

    # Se presentan los datos
    def presentar_datos3(self):
        cadena = ("%s\nNumero Semanas: %.2f\nValor semanal: %.2f\nSueldo final: %.2f\n" % (
            super(EmpleadoPorSemana, self).presentar_datos(), self.getNumeroSemanas(), self.getValorSemanal(),
            self.calcular_sueldo_final()))
        return cadena
