//Analia Alvarenga (Luna)
//PERSONA.UXF
//Creamos la carpeta persona

<diagram program="umletino" version="15.1"><zoom_level>10</zoom_level><element><id>UMLClass</id><coordinates><x>160</x><y>80</y><w>210</w><h>310</h></coordinates><panel_attributes>&lt;&lt;Persona&gt;&gt;

--
-id: Int
-nombre: String
-tel: String
-email: String
-numeroPersona: Int
--
+getId()
+setId(id:int)
+getNombre()
+setNombre(nombre:string)
+getTel()
+setTel(tel:String)
+getemail()
setemail(email:string)
+toString()
--
Responsibilities
-Creación de objetos de tipo Persona</panel_attributes><additional_attributes></additional_attributes></element></diagram>


//--------------------------------------------------------------------------------------------------------------------------
//PERSONA.JAVA
//Creamos la clase persona

public class Persona {
    private int id;
    private String nombre;
    private String tel;
    private String email;
    private static int numeroPersonas = 0;

    //constructor vacio
    public Persona(){
        this.id=++Persona.numeroPersonas;
    }
    //constructor con parámetros(sobrecarga de constructores)
    public Persona(String nombre,String tel,String email){
        this();//llamamos al constructor vacio
        this.nombre = nombre;
        this.tel = tel;
        this.email=email;
    }

    public int getId() {
        return id;
    }

    public void setId(int id) {
        this.id = id;
    }

    public String getNombre() {
        return nombre;
    }

    public void setNombre(String nombre) {
        this.nombre = nombre;
    }

    public String getTel() {
        return tel;
    }

    public void setTel(String tel) {
        this.tel = tel;
    }

    public String getEmail() {
        return email;
    }

    public void setEmail(String email) {
        this.email = email;
    }

    @Override
    public String toString() {
        return "Persona{" +
                "id=" + id +
                ", nombre='" + nombre + '\'' +
                ", tel='" + tel + '\'' +
                ", email='" + email + '\'' +
                '}';
    }



    public static void main(String[] args) {
        Persona persona1 = new Persona("Juan Perez","123456","jperez@gmail.com");
        System.out.println(persona1);
    }
}

//----------------------------------------------------------------------------------------------------------------------------------
//LISTADOPERSONASAPP.JAVA
// Creamos el menu parte 1 y 2 
import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

public class ListadoPersonasApp {
    public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);
        // Definimos la lista fuera del ciclo while
        List<Persona> personas = new ArrayList<>();
        //Empezamos con el menu
        var salir = false;
        while (!salir){
            mostrarMenu();
            try{
                salir = ejecutarOperacion(entrada, personas);
            } catch (Exception e){
                System.out.println("Ocurrió un error: "+ e.getMessage());
            }
            System.out.println();
        }//Fin del ciclo while
    } //Fin del metodo main

    private static void mostrarMenu(){
        //mostramos las opciones
        System.out.println("""
                ********Listado de Personas********
                1. Agregar 
                2. Listar
                3.Salir
                """);
        System.out.println("Digite una de las opciones: ");
    }//Fin metodo mostrarMenu

    //Añadimos el metodo de ejecutar operacion y lambda. Lujan Rebolledo
    private static boolean ejecutarOperacion(Scanner entrada, List<Persona> personas){
        var opcion = Integer.parseInt(entrada.nextLine());
        var salir = false;
        //Revisamos la opcion a través de un switch
        switch (opcion){
            case 1 -> {// Agregar una persona a la lista
                System.out.println("Digite el nombre: ");
                var nombre = entrada.nextLine();
                System.out.println("Digite el telefono: ");
                var tel = entrada.nextLine();
                System.out.println("Digite el correo: ");
                var email = entrada.nextLine();
                //Creamos el objeto persona
                var persona = new Persona(nombre, tel, email);
                //Agregamos la persona a la lista
                personas.add(persona);
                System.out.println("La lista tiene: "+personas.size()+" elementos");
            }//Fin caso 1
            case 2 ->{ //Listar a las personas
                System.out.println("Listado de personas: ");
                //Mejoras con lambda y el metodo de referencia
                //personas.forEach((persona) -> System.out.println(persona));
                personas.forEach(System.out::println);
            } //Fin caso 2
            case 3 -> {//Salir del ciclo
                System.out.println("Hasta pronto...");
                salir = true;
            }//Fin caso 3
            default -> System.out.println("Opción incorrecta: "+opcion);
        }//Fin del switch
        return salir;
    }//Fin del metodo ejecutarOperacion
}// Fin de la clase ListadoPersonasApp
