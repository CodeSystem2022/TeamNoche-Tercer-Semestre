
//do while
//este ciclo se ejecuta al menos una vez.
let conteo = 0
do{
    console.log(conteo)
    conteo++
}while(conteo < 3)
console.log('Fin del ciclo do while')

//Juego adivinador
 const nSec = Math.round(Math. random()*10)
 let intentos = 1
 let numero
console.log("Digita un numero entre el 0 y el 10.")
console.log("Tienes 5 intentos...")

do {
    console.log("Intento nº "+intentos)
    numero = parseInt("Digita un número: ")
    intentos ++
} while (nSec == numero || intentos == 5)
if (nSec == numero){
    console.log("Ganaste")
}else{
    console.log("Perdiste el numero secreto es: "+nSec);
}
