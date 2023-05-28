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
/*Marino afredo
MODIFICADORES DE ACCESO PÚBLICO */

package paquete1;

public class Clase1 {
    public String atributoPublic = "Valor atributo public";
    
    public Clase1(){
        System.out.println("Constructor public");
    }
    
 
    public void metodoPublico(){
        System.out.println("Método públic");
  
    }
}
----------------------------------------------------------------------------------------------------------------------------------------------------------
//Bruno Marchetti
//1.3 Modificadores de acceso public
package test;
import paquete1.Clase1;

public class TestModificadoresAcceso {
    public static void main(String[] args) {
        Clase1 clase1 = new Clase1();
        System.out.println(" Clase1 = " + clase1.atributoPublic);
        clase1.metodoPublico();
        
----------------------------------------------------------------------------------------------------------------------------------------------------------
//Bruno Marchetti
//1.4 Modificadores de acceso protected
            package paquete2;

import paquete1.Clase1;

public class Clase3 extends Clase1{
    public Clase3(){
      super("protected");
      this.atributoProtected = "Accedemos desde la clase hija";
        System.out.println("AtributoProtected = " + this.atributoProtected);
        this.atributoPublic = "es totalmente publico";
        
    }
    
}


#MODIFICACION A LA CLASE 1
package paquete1;

public class Clase1 {
    public String atributoPublic = "Valor atributo public";
    protected String atributoProtected = "Valor atributo protected";
    
    public Clase1 (){
        System.out.println("Constructor public");
    }
    
    protected Clase1(String atributoPublic){
        System.out.println("Constructor protected");
    }
    
    public void metodopublico(){
        System.out.println("Metodo public");
    }
    
protected void metodoProtected(){
    System.out.println("Metodo protected");
}
    
}

package test;

import paquete1.Clase1;
import paquete2.Clase3;

public class TestModificadoresdeAcceso {
    public static void main(String[] args) {
        Clase1 clase1 = new Clase1();
        System.out.println("clase1 = " + clase1.atributoPublic);
        clase1.metodopublico();
        Clase3 claseHija = new Clase3();
        System.out.println("claseHija = " + claseHija);
    }
    
}
----------------------------------------------------------------------------------------------------------------------------------------------------------
//Bruno Marchetti
//1.4 Modificadores de acceso protected
        package paquete1;

public class TestDefault {
  public static void main(String[] args){
    ClaseHija2 claseH2 = new ClaseHija2();
    claseH2.atributoDefault = "Cambio desde la prueba";
    System.out.println("claseH2 atributo default = " + claseH2.atributoDefault9;
