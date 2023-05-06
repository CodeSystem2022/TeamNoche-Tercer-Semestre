/*Florencia Pons
Argumentos variables*/


package test;

public class testArgumentosVariables {
    public static void main(String[] args){
        imprimirNumeros(3, 4, 5);
        imprimirNumeros(1, 2);
        variosParametros("Juan", "Perez", 7, 8, 9);
        
    }
    
    private static void variosParametros(String nombre, String apellido, int ...numeros){
        System.out.println("Nombre: "+nombre);
        System.out.println("Apellido: "+apellido);
        imprimirNumeros (numeros);
    
    }
    private static void imprimirNumeros(int ...numeros){
        for (int i = 0; i < numeros.length; i++) {
            System.out.println("Elementos: "+numeros[i]);
        }
    }
}
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------
/**
 Julio Ezequiel Soria
 Creación de bloques de inicialización, estaticos y no estaticos
 */

    package domain;

public class Persona {
    private final int idPersona;
    private static int contadorPersonas;
    
    static{ //Bloque de inicializacion estatico, solo se puede utilizar atributos estaticos.
        System.out.println("Inicia el bloque STATIC");
        ++Persona.contadorPersonas;
    }
    
    { //Bloque de inicializacion no estatico (Contexto dinamico)
        System.out.println("Ejecucion del bloque No estatico");
        this.idPersona = Persona.contadorPersonas++; //Incrementamos el atributo
    }
    //Los bloeque de inicializacion se ejecutan antes del constructor

    public Persona() {
        System.out.println("Esta es la ejecución del constructor");
    }

    public int getIdPersona() {
        return this.idPersona;
    }

    @Override
    public String toString() {
        return "Persona{" + "idPersona=" + idPersona + '}';
    }
    
    
}
----------------------------------------------------------------------------------------------------------------------------------------------------------
