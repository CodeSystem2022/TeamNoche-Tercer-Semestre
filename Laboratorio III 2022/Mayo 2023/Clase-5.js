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
    edad : 30
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
