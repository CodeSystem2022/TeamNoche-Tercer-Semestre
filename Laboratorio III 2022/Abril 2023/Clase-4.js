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

-----------------------------------------------------------------------------------------------------------------------------------------------------------------------
//Julio Ezequiel Soria
//Crea un nuevo objeto en memoria

let perosna2 = new Object() 
perosna2.nombre = 'Juan'
perosna2.direccion = 'Salada 14'
perosna2.telefono = '02000100'

console.log(perosna2.telefono)
-------------------------------------------------------------------------------------------------------------------------------------------------------------
// Alfredo Marino
// agregar y eliminar propiedades de un objeto

console.log(persona.apellido);
persona.apellido = "Marino"; // cambio dinamico de un valor del objeto
console.log(persona.apellido);
