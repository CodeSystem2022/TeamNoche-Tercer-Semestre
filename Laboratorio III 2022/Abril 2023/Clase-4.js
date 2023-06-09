//Florencia Pons
//Creación de objetos en JavaScript
let x = 10; //variable de tipo primitiva
console.log(x.length);

//objeto
let persona = {
    nombre:'Carlos',
    apellido: 'Gil',
    email: 'cgil@gmail.com',
    edad : 30
}

console.log(persona.nombre);
console.log(persona.apellido);
console.log(persona.email);
console.log(persona.edad);
console.log(persona);

//------------------------------------------------------------------------------------------------------------------------------------------------------------
//Julio Ezequiel Soria
//Crea un nuevo objeto en memoria

let perosna2 = new Object() 
perosna2.nombre = 'Juan'
perosna2.direccion = 'Salada 14'
perosna2.telefono = '02000100'

console.log(perosna2.telefono)
//-------------------------------------------------------------------------------------------------------------------------------------------------------------
// Alfredo Marino
// agregar y eliminar propiedades de un objeto

console.log(persona.apellido);
persona.apellido = "Marino"; // cambio dinamico de un valor del objeto
console.log(persona.apellido);

//-------------------------------------------------------------------------------------------------------------------------------------------------------------

// Franco J. Videla

// Imprime el objeto como un arreglo con la funcion Object.values()

console.log("\nDistintas formas de imprimir un objeto: Forma 3")
let personaArray = Object.values(persona); // pasamos el objeto persona como parámetro
console.log(personaArray)

// Utilizaremos el método JSON.stringify()

console.log("\nDistintas formas de imprimir un objeto: Forma 4")
let personaString = JSON.stringify(persona); // convierte el objeto en una cadena
console.log(personaString);

//--------------------------------------------------------------------------------------------------------------------------------------------------------------
// Marino Alfredo.
//Como acceder a propiedades de los objetos 

let persona2 = new Object();//Debe crear un nuevo objeto en memoria 
persona2.nombre = 'Juan';
persona2.direccion = 'Salada 14';
persona2.telefono = '5492618282821';
console.log(persona2.telefono); '5492618282821';

console.log(persona['apellido']);// accedemos como si fuera un arreglo de Gil
//for in
for(propidad in persona){
    console.log(propidad); nombre, apellido, email, edad, nombreCompleto
    console.log(persona[propidad]); Carlos, Gil, cgil@gmail.com, 30, 
}

//--------------------------------------------------------------------------------------------------------------------------------------------------------------
// carlos hernan suarez.
// Agregamos métodos a  los objetos 
Let X = 10; //variable de tipo primitivo
console.log(x.lenght;

//objeto
let persona ={
    nombre: 'carlos',
    apellido: 'gil',
    email: 'cgil@gmail.com',
    edad: 30,
    nombreCompleto: function(){    
        return this.nombre+' '+this.apellido;
    }
}

console.log(persona.nombre);
console.log(persona.apellido);
console.log(persona.email);
console.log(persona.edad);
console.log(persona);
console.log(persona.nombreCompleto());

//--------------------------------------------------------------------------------------------------------------------------------------------------------------
// carlos hernan suarez.
// ejecutamos desde el navegador
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Clases en Javascript</title>
</head>
<body>
    <script src="./01-04-objetos.js"></script>
</body>
</html>
