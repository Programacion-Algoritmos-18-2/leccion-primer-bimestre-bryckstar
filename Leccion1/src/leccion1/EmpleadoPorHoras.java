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
public class EmpleadoPorHoras extends Empleado {
    double numero_horas;
    double valor_hora;

    public void setNumero_horas(double numero_horas) {
        this.numero_horas = numero_horas;
    }

    public void setVaor_hora(double vaor_hora) {
        this.valor_hora = vaor_hora;
    }

    public double getNumero_horas() {
        return numero_horas;
    }

    public double getValor_hora() {
        return valor_hora;
    }
    
    public double sueldo_final(){
        double sf = getNumero_horas() * getValor_hora();
        return sf;
    }
    
    @Override
    public String toString() {
        return String.format("%s\nNumero de Horas: %.1f\nValor de Hora: %.2f$\nSueldo Final: %.2f\n", super.toString(),getNumero_horas(), getValor_hora(), sueldo_final());
    }

    public EmpleadoPorHoras(double numero_horas, double valor_hora, String nombre, String apellido, int cedula) {
        super(nombre, apellido, cedula);
        this.numero_horas = numero_horas;
        this.valor_hora = valor_hora;
    }
    
    
    
}
