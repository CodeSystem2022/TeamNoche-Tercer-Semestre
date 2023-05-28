//Florencia Pons
//Funciones y return
miFuncion(8, 2); //Esto se lo conoce como hosting

function miFuncion(a, b){
    //console.log("Sumamos: "+ (a+ b));
    return a + b;
}

//Llamando la funcion 
miFuncion(5, 4);

let resultado = miFuncion(6, 7);
console.log(resultado);
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------

//Julio Ezequiel Soria
//Paso por referencia
const persona = {
    nombre: 'juan',
    apellido: 'Lepez'
}
console.log(typeof persona)

function cambiarValorObjeto(p1) {//la variable p1 reasigna los datos a los parametros de nombre y apellido, luego es eliminada.
    console.log(persona)
    p1.nombre = 'Eze'
    p1.apellido = 'Soria'
    console.log(persona)
}

cambiarValorObjeto(persona)
console.log(persona)
---------------------------------------------------------------------------------------------------------------------------------------------------------
    // Marino Alfredo
// Funciones de tipo expresion o anonima
let x = function(a, b){return a + b};
resultado2 = x(5, 6);          // AL LLAMARLA SE PONE LA VARIABLE Y PARENTESIS
console.log(resultado); 

---------------------------------------------------------------------------------------------------------------------------------------------------------
    //Bruno Marchetti
    // 3.4 Funciones del tipo self e invoking
(function(a,b){
    console.log('Ejecutando la funcion: '+(a+b));
})(9, 6);

console.log(typeof miFuncion);
function miFuncionDos(a, b){
    console.log(arguments.length);
}
miFuncionDos(5, 7, 3, 6);

// toString
var miFuncionTexto = miFuncionDos.toString();
console.log(miFuncionTexto); 

// 3.5 Tipos de Datos de Una Funcion

console.log(typeof miFuncion); function
function miFuncionDos(a, b){
    console.log(arguments.length)
}

miFuncionDos(5, 7, 3, 6);

//toString
var miFuncionTexto = miFuncionDos.toString();
console.log(miFuncionTexto); ... ionDos(a, b) { var $_$c = $_$wf(1); $_$w(1, 12, $_
  
// 3.6 Funciones Flecha
                                                                          
//Funciones flecha
const sumarFuncionFlecha = (a, b) => a + b;
resultado = sumarFuncionFlecha(3,7); //Asignamos el valor a una variable
console.log(resultado);

// 3.7 Argumentos y Parametros                                                                                            

let sumar = function(a = 4, b = 8){
    console.log(arguments[0]); //Muestra el parámetro de: a
    console.log(arguments[1]); //muestra el parámetro de: b
    return a + b + arguments[2];
}
resultado = sumar(3, 2, 9);
console.log(resultado);    
                                               
// 3.8 Concepto Hoisting
                                               
let respuesta = sumarTodo(5, 4, 13, 10, 9);
console.log(respuesta);
function sumarTodo(){
    let suma = 0;
    for(let i = 0; i < arguments.length; i++){
        suma += arguments[i]; //arguments es para arreglos
    }
    return suma;
}
                                               
// 3.9 Paso Por Valor
                                               
//Tipos primitivos
let k = 10;
function cambiarValor(a){ //Paso por valor
    a = 20;
}
cambiarValor(k);
console.log(k);                                               
                                                                          
