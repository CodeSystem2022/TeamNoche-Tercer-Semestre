// Franco J. Videla
// Agregar metodos al constructor del objeto

function Persona3(nombre, apellido, email){ //contructor
    this.nombre = nombre;
    this.apellido = apellido;
    this.email = email;
    this.nombreCompleto = function(){
        return this.nombre+' '+this.apellido;
    }
}
let padre = new Persona3('Franco','Videla','francojvidela@gmail.com');
padre.nombre = 'Juan Carlos';
padre.telefono = '5492604372581'; // Una propiedad exclusiva del objeto padre
console.log(padre);
console.log(padre.nombreCompleto()); // Utilizamos la funcion
let madre = new Persona3('Francisca','Gimenez','gimenezfrancisca@gmail.com');
console.log(madre);
console.log(madre.telefono); // La propiedad no esta definida
console.log(madre.nombreCompleto());

//-------------------------------------------------------------------------------------------------------------------------------------------

// Marlene Soriano
// Distintas formas de crear objetos
// Caso numero 1

let miObjeto = new Object(); // Esto es una opcion formal
// Caso numero 2
let miObjeto2 = {}; // Esta opcion es breve y recomendada

// Caso String 1 
let miCadena1 = new String('Hola'); // Sintaxis formal
// Caso String 2
let miCadena2 = 'Hola'; // Esta es la sintaxis simplificada y recomendada

// Caso con numeros 1
let miNumero = new Number(1); // Es formal no recomendable
// Caso con numeros 2
let miNumero2 = 1; // Sintaxis recomendada

// Caso boolean 1
let miBoolean1 = new Boolean(false); // Formal
// Caso boolean 2
let miBoolean2 = false; // Sintaxis recomendada

// Caso Arreglos 1
let miArreglo1 = new Array(); // Formal
// Caso Arreglos 2
let miArreglo2 = []; // Sintaxis recomendada

// Caso function 1
let miFuncion1 = new function(){}; // Todo despues de new es  considerado objeto
// Caso function 2
let miFuncion2 = function(){}; // Notacion simplificada y recomendada

//-------------------------------------------------------------------------------------------------------------------------------------------