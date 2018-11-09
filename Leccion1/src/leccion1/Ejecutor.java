/*
 * To change this license header, choose License Headers in Project Properties.
 * To change this template file, choose Tools | Templates
 * and open the template in the editor.
 */
package leccion1;
import java.util.Scanner;

/**
 *
 * @author Bryan
 */
public class Ejecutor {

    /**
     * @param args the command line arguments
     */
    public static void main(String[] args) {
        
        Scanner entrada = new Scanner(System.in);
        
        Empleado e = new Empleado("Luis", "Benitez", 1110001);
        System.out.println(e.toString());
        
        
        System.out.println("Ingrese el nombre: ");
        String nombre = entrada.nextLine();
        
        EmpleadoPorHoras e1 = new EmpleadoPorHoras(20.2, 15, nombre, "Andrade", 112233);
        System.out.println(e1.toString());
        
        System.out.println("Ingrese la comision fija:");
        double c =  entrada.nextDouble();
        e.setComision_fija(c);
        EmpleadoFijo e2 = new EmpleadoFijo(300.2, 10, "Ana", "Dias", 1101238);
        System.out.println(e2.toString());
        
    }
    
}
