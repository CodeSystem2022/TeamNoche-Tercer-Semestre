//Forencia Pons
//Sobreescritura de métodos Overriding- 
package domain;

public class Empleado {
    protected String nombre;
    protected double sueldo;
    
    public Empleado(String nombre, double sueldo){
        this.nombre = nombre;
        this.sueldo = sueldo;
    }
    
    //Método para la sobreescritura
    public String obtenerDetalles(){
        return "Nombre: "+this.nombre+", Sueldo: "+this.sueldo;
    }    

    public String getNombre() {
        return nombre;
    }

    public void setNombre(String nombre) {
        this.nombre = nombre;
    }

    public double getSueldo() {
        return sueldo;
    }

    public void setSueldo(double sueldo) {
        this.sueldo = sueldo;
    }
    
    
}
---------------------------------------------------------------------------------------------------------------------------------------------------------------------
/**
* ezequiel Soria
* Ejercicio con instanceof Parte 1 y 2
*/
package Test;

import domain.*;



public class TestIstanceOF {
    public static void main(String[] args) {
        Empleado empleado1 = new Empleado("Juan", 10000);//clase padre
        determinaTipo(empleado1);
        empleado1 = new Gerente("Julio", 5000, "Sistema");//clase hija
        //determinaTipo(empleado1);
    }
    
    public static void determinaTipo(Empleado empleado){
        if(empleado instanceof Gerente){
            System.out.println("Es de tipo Gerente");
            Gerente gerente = (Gerente)empleado;
            //((Gerente) empleado).getDepartamento();
            System.out.println("gerente = " + gerente.getDepartamento());
        }
        else if(empleado instanceof Empleado){
            System.out.println("Es de tipo Empleado");
            // Gerente gerente = (Gerente)empleado;
            //System.out.println("gerente = " + gerente.getDepartamento());
        }
        else if(empleado instanceof Object){
            System.out.println("Es de tipo Object");
        }
    }
}
