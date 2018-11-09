/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package leccion1;

/**
 *
 * @author Bryan
 */
public class Empleado {

    String nombre;
    String apellido;
    int cedula;
    double comision_fija;

    public void setNombre(String nombre) {
        this.nombre = nombre;
    }

    public void setApellido(String apellido) {
        this.apellido = apellido;
    }

    public void setCedula(int cedula) {
        this.cedula = cedula;
    }

    public void setComision_fija(double comision_fija) {
        this.comision_fija = comision_fija;
    }

    public String getNombre() {
        return nombre;
    }

    public String getApellido() {
        return apellido;
    }

    public int getCedula() {
        return cedula;
    }

    public double getComision_fija() {
        return comision_fija;
    }

    @Override
    public String toString() {
        return String.format("Informacion de %s %s\n\tCEDULA: %d", getNombre(), getApellido(), getCedula());
    }

    public Empleado(String nombre, String apellido, int cedula) {
        setNombre(nombre);
        setApellido(apellido);
        setCedula(cedula);
    }

}

