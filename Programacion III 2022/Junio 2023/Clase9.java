//Florencia Pons
//Creamos CalculadoraUTN
//Definimos las variables
public class CalculadoraUTN {
    public static void main(String[] args){
        System.out.println("****** Aplicaci[on Calculadora ******");
        var operando1 = 10;
        var operando2 = 20;
        var resultado = operando1 + operando2;
        System.out.println("Resultado = " + resultado);
    }

}
//BRUNO MARCHETTI
import java.util.Scanner;

public class CalculadoraUTN {
    public static void main(String[] args) {
        Scanner entrada = new Scanner(System.in);
        while (true) { //Ciclo while
            System.out.println("******* Aplicacion Calculadora *******");
            mostarMenu();

            try {
                var operacion = Integer.parseInt(entrada.nextLine());
                if(operacion >= 1 && operacion <= 4){
                    ejecutarOperacion(operacion, entrada);
            } //Fin del if
