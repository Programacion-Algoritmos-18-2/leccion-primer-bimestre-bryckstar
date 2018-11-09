class Empleado(object):
    def __init__(self):
        self.nombre = ""
        self.apelldio = ''
        self.cedula = ''
        self.comision_fija = 0

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

    def presentar_datos(self):
        cadena = 'Informacion de %s %s\n\tCEDULA: %d' % (self.getNombre(), self.getApellido(), self.getCedula())
        return cadena