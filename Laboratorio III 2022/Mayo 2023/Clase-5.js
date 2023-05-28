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

