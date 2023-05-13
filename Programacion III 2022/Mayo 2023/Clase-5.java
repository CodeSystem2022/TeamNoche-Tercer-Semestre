//Soria Ezequiel
   //Creamos la clase TEST
package Test;

/**
 * @author ezequiel
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
----------------------------------------------------------------------------------
