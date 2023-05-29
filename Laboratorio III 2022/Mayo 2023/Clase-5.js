//Florencia Pons
//Metodo get y set parte 1 

let x = 10; //variable de tipo primitiva
console.log(x.length);
console.log('Tipos primitivos');
//objeto
let persona = {
    nombre:'Carlos',
    apellido: 'Gil',
    email: 'cgil@gmail.com',
    edad : 28,
    idioma: 'ES',
    get lang(){
        return this.idioma.toUpperCase();//Convierte las minusculas en mayusculas
    },
    set lang(lang){
        this.idioma = lang.toUpperCase();
    },
    nombreCompleto: function(){ //metodo o funcion en JavaScript
        return this.nombre+''+this.apellido;
    },
    get nombreEdad(){// Este es el metodo get
        return 'El nombre es: '+this.nombre+', Edad: '+this.edad;
    }
}

console.log(persona.nombre);
console.log(persona.apellido);
console.log(persona.email);
console.log(persona.edad);
console.log(persona);
console.log(persona.nombreCompleto());
console.log('Ejecutando con un objeto');
let persona2 = new Object(); //Debe crear un nuevo objeto en memoria
persona2.nombre = 'Juan';
persona2.direccion = 'Salada 14';
persona2.telefono = '5492618282821';
console.log(persona2.telefono);
console.log('Creamos un nuevo objeto');
console.log(persona['apellido']);
console.log('Usamos el ciclo for in');
//for in y accedemos al objeto como si fuera un arreglo
for(propiedad in persona){
    console.log(propiedad);
    console.log(persona[propiedad]);
}
consol.log('Cambiamos y eliminamos un error');
persona.apellida = 'Betancud';
delete persona.apellida;
console.log(persona);

//Distintas formas de imprimir un objeto
//Numero 1: la mas sencilla, concatenar cada valor con cada propiedad
console.log('Distintas formas de imprimir un objeto: forma 1');
console.log(persona.nombre+''+persona.apellido);

//Numero 2: a traves del ciclo for in
console.log('Distintas formas de imprimir un objeto: forma 2');
for(nombrePropiedad in persona){
    console.log(persona[nombrePropiedad]);
}

//Numero 3: funcion object.values()
console.log('Distintas formas de imprimir un objeto: forma 3');
let personaArray = Object.values(persona);
console.log(personaArray);

//Numero 4: metodo JSON.stringify
console.log('Distintas formas de imprimir un objeto: forma 4');
let personaString = JSON.stringify(persona);
console.log(personaString);

console.log('Comenzamos a utilizar el metodo get');
console.log(persona.nombreEdad);
console.log('Comenzamos con el metodo get y set para idiomas');
persona.lang = 'en';
console.log(persona.lang);
  ------------------------------------------------------------------------------------------------------------------------------------------------------
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

// Marlene Soriano
// El uso de apply

let arreglo = ['Esp.', '5498888888'];
console.log(persona4.nombreCompleto2.apply(persona5, arreglo));

//-------------------------------------------------------------------------------------------------------------------------------------------

//Métodos get y set  Parte 2 - 
//Marino Alfredo 

let persona = {
    nombre: 'Carlos',
    apellido: 'Gil',
    email: 'cgil@gmail.com',
    edad:28,
    idioma: 'es'
    get lang(){
        return this.idioma.toUpperCase(); //Convierte las minusculas a mayusculas
    },
    set lang(lang){
        this.idioma = lang.toUpperCase();
    },
    nombreCompleto: Function(){ //Metodo o funcion en javascript
        return this.nombre+' '+this.apellido;
    },
    get nombreEdad(){ // este es el metodo get
 	return 'El nombre es: '+this.nombre+', Edad: '+this.edad; 
    }
}
---------------------------------------------------------------------------------------------------------------
