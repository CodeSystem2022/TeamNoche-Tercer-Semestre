//Florencia Pons 
//Ciclo While
let contador = 0;
while(contador < 3){
    console.log(contador);
    contador++;
}
console.log("Fin del ciclo while");


------------------------------------------------------------------------------------------------------------------------------------------------------------------------

//Julio Ezequiel Soria
//do while
let conteo = 0;
do{
    console.log(conteo);
    conteo++;
}while(conteo <3);
console.log("Fin del ciclo do while");

------------------------------------------------------------------------------------------------------------------------------------------------------------------------
//Carlos Hernan Suarez
////Palabra reservada break
for(i=0; i <= 10; i++){
    if (i % 2 == 0) {
        console.log(i)
        break //termina al encontrar el primer numero par       
    }
}
console.log('Termina el ciclo al encontrar el primer par')

-----------------------------------------------------------------------------------------------------------------------------------------------------------

//Carlos Hernan Suarez
//Usamos la palabra reservada Labels en javascript

inicio:
for(let contando = 0; contando <= 10; contando++){
    if(contando % 2 !== 0){
        break inicio; //ir a la siguiente iteracion
    }
console.log(contando); 0
}
console.log("Termina el ciclor"); Termina el ciclo

   
    
-----------------------------------------------------------------------------------------------------------------------------------------------------------

//Carlos Hernan Suarez
//Usamos la palabra reservada continue en Js    
    
for(let contando = 0; contando <= 10; contando++){
    if(contando % 2 !== 0){
        continue; //ir a la siguiente iteraccion
    }
console.log(contando); 0, 2, 4, 6, 8, 10
}
console.log("Termina el ciclo"); Termina el ciclo    
       
    
    
 -----------------------------------------------------------------------------------------------------------------------------------------------------------

//Carlos Hernan Suarez
// Creamos el ciclo for en Js    
    
for(let contando = 0: contando < 3; contando++){
    console.log(contando); 0, 1, 2
    }
console.log("Fin del ciclo for"); Fin ciclo for
    
    
    
    

