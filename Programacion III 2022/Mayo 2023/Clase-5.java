
//Florecia Pons
//Proyecto Conversión de Objetos
//Creamos la clase Empleado

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

// Creamos la clase Escritor 

package domain;

public class Escritor extends Empleado{
    final TipoEscritura tipoEscritura;
    
    public Escritor(String nombre, double sueldo, TipoEscritura tipoEscritura){
        super(nombre, sueldo);
        this.tipoEscritura = tipoEscritura;
    }
    
    //Metodo para sobreescribir
    @Override
    public String obtenerDetalles(){
        return super.obtenerDetalles()+", Tipo Escritura: "+tipoEscritura.getDescripcion();
         
    }
    
    @Override
    public String toString(){
        return "Escritor(" + "tipoEscritura=" + tipoEscritura + '}' + " "+super.toString();
    }
    
    public TipoEscritura getTipoEscritura(){
        return this.tipoEscritura;
    }
    
}

//Creamos enumeración TipoEscritura

package domain;

public enum TipoEscritura {
    CLASICO ("Escritura a mano"),
    MODERNO ("Escritura digital");
    
    private final String descripcion;
    
    private TipoEscritura(String descripcion){ //Constructor
        this.descripcion = descripcion;

    }
    
    //Metodo get
    public String getDescripcion(){
        return this.descripcion;
    }
}
------------------------------------------------------------------
//Carga de la clase TEST
  package Test;

/**
 * @author Soria ezequiel
 */
import domain.*;

public class TestConversionObjetos {
    public static void main(String[] args) {
        Empleado empleado;
        empleado = new Escritor("Juan", 5000, TipoEscritura.CLASICO);
        //System.out.println("empleado = " + empleado);
        //System.out.println(empleado.obtenerDetalles());
        
        //Downcasting
        ((Escritor)empleado).getTipoEscritura(); //una forma de hacerlo
        
        Escritor escritor = (Escritor)empleado; //Segunda forma
        escritor.getTipoEscritura();
        
        //Upcasting
        Empleado empleado2 = escritor;
        System.out.println(empleado2.obtenerDetalles());
    }
}
-----------------------------------------------------------------------------
   //5.4 Hashcode y Equals:
// Marino Alfredo

    @Override
    public int hashCode() {
        int hash = 7;
        hash = 53 * hash + Objects.hashCode(this.nombre);
        hash = 53 * hash + (int) (Double.doubleToLongBits(this.sueldo) ^ (Double.doubleToLongBits(this.sueldo) >>> 32));
        return hash;
    }

    @Override
    public boolean equals(Object obj) {
        if (this == obj) {
            return true;
        }
        if (obj == null) {
            return false;
        }
        if (getClass() != obj.getClass()) {
            return false;
        }
        final Empleado other = (Empleado) obj;
        if (Double.doubleToLongBits(this.sueldo) != Double.doubleToLongBits(other.sueldo)) {
            return false;
        }
        if (!Objects.equals(this.nombre, other.nombre)) {
            return false;
        }
        return true;
    }
}
-----------------------------------------------------------------------------
   //Creamos Clase Object 
   //Bruno Marchetti
   
   package test;

import domain. *;

public class TestClaseObject {
    public static void main(String[] args) {
        Empleado empleado1 = new Empleado("Bruno", 5000);
        Empleado empleado2 = new Empleado("Bruno", 5000);
        if(empleado1 == empleado2){
            System.out.println("Tienen la misma referencia en memoria" );
        }
        else{
            System.out.println("Tienen distinta referencia en memoria");
        }
        
        if(empleado1.equals(empleado2)){
            System.out.println("Los objetos son iguales en contenido");
        }
        else{
            System.out.println("Los objetos son distintos en contenido");
        }
        
        if(empleado1.hashCode() == empleado2.hashCode()){
            System.out.println("El valor hashCode es igual");
        }
        else{
            System.out.println("El valor hashCode es diferente");
        }
    }
}
