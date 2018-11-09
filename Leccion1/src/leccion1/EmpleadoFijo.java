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
public class EmpleadoFijo extends Empleado {
    
    double sueldo_fijo;
    int descuento_seguro;

    public void setSueldo_fijo(double sueldo_fijo) {
        this.sueldo_fijo = sueldo_fijo;
    }

    public void setDescuento_seguro(int descuento_seguro) {
        this.descuento_seguro = descuento_seguro;
    }

    public double getSueldo_fijo() {
        return sueldo_fijo;
    }

    public int getDescuento_seguro() {
        return descuento_seguro;
    }
    
    public double sueldo_final(){
        double sf = getSueldo_fijo() - (getSueldo_fijo() * (getDescuento_seguro()/ 100)) + super.getComision_fija();
        return sf;
    }
    
    @Override
    public String toString() {
        return String.format("%s\nSueldo fijo: %.2f$\nDescuento del seguro: %d\nComision FIja: %.2f\nSueldo Final: %.2f\n", super.toString(), getSueldo_fijo(), getDescuento_seguro(), super.getComision_fija(), sueldo_final());
    }

    public EmpleadoFijo(double sueldo_fijo, int descuento_seguro, String nombre, String apellido, int cedula) {
        super(nombre, apellido, cedula);
        this.sueldo_fijo = sueldo_fijo;
        this.descuento_seguro = descuento_seguro;
    }
    
    

    
}
