/* Florencia Pons
Creación de clase DispositivoEntrada*/

package ar.com.system2023.mundopc;

public class DispositivoEntrada {
    private String tipoEntrada;
    private String marca;
    
    public DispositivoEntrada(String tipoEntrada, String marca){
        this.tipoEntrada = tipoEntrada;
        this.marca = marca;
    }

    public String getTipoEntrada() {
        return this.tipoEntrada;
    }

    public void setTipoEntrada(String tipoEntrada) {
        this.tipoEntrada = tipoEntrada;
    }

    public String getMarca() {
        return this.marca;
    }

    public void setMarca(String marca) {
        this.marca = marca;
    }

    @Override
    public String toString() {
        return "DispositivoEntrada{" + "tipoEntrada=" + tipoEntrada + ", marca=" + marca + '}';
    }
    
}
--------------------------------------------------------------------------------------------------------------------------------------------------------------------
/**
Julio Ezequiel Soria
Creacion de clase main de Mundo Pc
 */
package mundopc;

import ar.com.system2023.mundopc.*;


public class MundoPc {
    public static void main(String[] args) {
        
        Monitor monitorHP = new Monitor("HP", 13);
        Teclado tecladoHP = new Teclado("Bluetooth", "HP");
        Raton ratonHP = new Raton("Bluetooth", "HP");
        Computadora computadoraHP = new Computadora("Computadora HP", monitorHP, tecladoHP, ratonHP);
        
        Monitor monitorAcer = new Monitor("Acer", 18);
        Teclado tecladoAcer = new Teclado("Bluetooth", "Acer");
        Raton ratonAcer = new Raton("Bluetooth", "Acer");
        Computadora computadoraAcer = new Computadora("Computadora Acer", monitorAcer, tecladoAcer, ratonAcer);
        
        Monitor monitorSamsung = new Monitor("Samsung", 19);
        Teclado tecladoSamsung = new Teclado("Bluetooth", "Samsung");
        Raton ratonSamsung = new Raton("Bluetooth", "Samsung");
        Computadora computadoraSamsung = new Computadora("Computadora Samsung", monitorSamsung, tecladoSamsung, ratonSamsung);
        
        Monitor monitorGamer = new Monitor("Gamer", 24);
        Teclado tecladoGamer = new Teclado("Bluetooth", "Gamer");
        Raton ratonGamer = new Raton("Bluetooth", "Gamer");
        Computadora computadoraGamer = new Computadora("Computadora Gamer", monitorGamer, tecladoGamer, ratonGamer);
        
        Orden orden1 = new Orden();
        orden1.agregarComputadora(computadoraHP);
        orden1.agregarComputadora(computadoraAcer);
        orden1.agregarComputadora(computadoraAcer);
        orden1.agregarComputadora(computadoraAcer);
        orden1.agregarComputadora(computadoraAcer);
        orden1.agregarComputadora(computadoraAcer);
        orden1.agregarComputadora(computadoraAcer);
        orden1.agregarComputadora(computadoraAcer);
        orden1.agregarComputadora(computadoraAcer);
        orden1.agregarComputadora(computadoraAcer);
        orden1.agregarComputadora(computadoraAcer);
       
        orden1.mostrarOrden();
        
        Computadora computadoraArmada = new Computadora("PC Armada", monitorSamsung, tecladoGamer, ratonGamer);
        Orden orden2 = new Orden();
        orden2.agregarComputadora(computadoraArmada);
        
        orden2.mostrarOrden();
     }
    
}

--------------------------------------------------------------------------------------------------------------------------------------------------------------------
/**
Carlos Hernan Suarez
Creacion de clase Monitor
 */


package ar.com.system2023.mundopc

public  class Monitor {
    private final int idMonitor;
    private String marca;
    private double tamanio;
    private static int contadorMonitores;
    
    private Monitor(){
        this.idMonitor = ++Monitor.contadorMonitores;
    }
    
    public Monitor(String marca, double tamanio){
        this(); //llamado al constructor vacio
        this.marca = marca;
        this.tamanio = tamanio;        
    }
    
    public String getMarca(){
        return marca;
    }
    
    public void setMarca(String marca){
        this.marca = marca;
    }
        
    public double getTamanio(){
        return this.tamanio;
    }
    
    public void setTamanio(double tamanio){
        this.tamanio = tamanio;
    }
    //Ingresamos manualmente el getIdMonitor
    
    public int getIdMonitor(){
        return this.idMonitor;
    }
    
    @Override    
    public String toString(){
        return "Monitor{" + "idMonitor=" + idMonitor + ", marca=" + marca + ", tamanio=" + tamanio + '}'
    }
}



--------------------------------------------------------------------------------------------------------------------------------------------------------------------
/**
Carlos Hernan Suarez
Creacion de clase Computadora
 */


package ar.com.system2023.mundopc;


public class Computadora {
    private final int idComputadora;
    private String nombre;
    private Monitor monitor;
    private Teclado teclado;
    private Raton raton;
    private static int contadorComputadoras;



    //Constructor vacio
    private Computadora(){
        this.idComputadora = ++Computadora.contadorComputadoras;
    }


    //Contructor 2
    public Computadora(String nombre, Monitor monitor, Teclado teclado, Raton raton) {
        this();
        this.nombre = nombre;
        this.monitor = monitor;
        this.teclado = teclado;
        this.raton = raton;
    }


    public int getIdComputadora() {
        return idComputadora;
    }


    public String getNombre() {
        return nombre;
    }


    public void setNombre(String nombre) {
        this.nombre = nombre;
    }


    public Monitor getMonitor() {
        return monitor;
    }


    public void setMonitor(Monitor monitor) {
        this.monitor = monitor;
    }


    public Teclado getTeclado() {
        return teclado;
    }


    public void setTeclado(Teclado teclado) {
        this.teclado = teclado;
    }


    public Raton getRaton() {
        return raton;
    }


    public void setRaton(Raton raton) {
        this.raton = raton;
    }


    @Override
    public String toString() {
        return "Computadora [idComputadora=" + idComputadora + ", nombre=" + nombre + ", monitor=" + monitor
            
            
            
--------------------------------------------------------------------------------------------------------------------------------------------------------------------
/**
Carlos Hernan Suarez
Creacion de clase Orden 1 y 2
 */
            
package ar.com.system2023.mundopc;


public class Orden {
    private final int idOrden;
    private Computadora computadora[]; //arreglo de objetos
    private static int contadorOrdenes;
    private static final int MAX_COMPUTADORAS = 10;
    private int contadorComputadora;
    
    //Contructor Vacío
    public Orden(){
        this.idOrden = ++Orden.contadorOrdenes;
        this.computadora = new Computadora[Orden.MAX_COMPUTADORAS];
    }
    
    //Método para agregar una nueva computadora al arreglo
    public void agregarComputadora(Computadora computadora){
        if(this.contadorComputadora < Orden.MAX_COMPUTADORAS){
            this.computadora[this.contadorComputadora++] = computadora;
        }
        else{
            System.out.println("Has superado el limite: "+Orden.MAX_COMPUTADORAS);
        }
    }
    //Mostrar orden
    public void mostrarOrden(){
        System.out.println("Orden #: "+this.idOrden);
        System.out.println("Computadoras de la orden #: "+this.idOrden);
        for(int i = 0; i < this.contadorComputadora; i++){
            System.out.println(this.computadora[i]);
        }
    }
}            
                + ", teclado=" + teclado + ", raton=" + raton + "]";
    }

}







