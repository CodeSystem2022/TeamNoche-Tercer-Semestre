/*Florencia Pons
Ciclo ForEach*/


package test;

public class testForEach {
    public static void main(String[] args) {
        int edades[] = {5, 6, 8, 9}; //Sintaxis resumida
        for (int edad: edades) { //Sintaxis del ForEach
            System.out.println("edad = "+edad);
            
        }
    }
    
}
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------
/**
Julio Ezequiel Soria
Modificador de acceso PROTECTED
 */
package paquete1;

public class Clase1 {
    public String atributoPublico = "Valor atributo publico";
    protected String atributoProtected = "Valor atributo protected";

    public Clase1() {
        System.out.println("Constructor publico");
    }
    
    protected Clase1(String atributoPublico){
        System.out.println("Constructor protected");
    }
    
    public void metodoPublico(){
        System.out.println("Metodo publico");
    }
    
    protected void metodoProtected(){
        System.out.println("Metodo protected");
    }
}
----------------------------------------------------------------------------------------------------------------------------------------------------------
