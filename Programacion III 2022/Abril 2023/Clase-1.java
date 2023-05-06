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
