//9.1 Introducción a lo que es la herencia en JavaScript
//Carlos Hernan Suarez

Explicación UML de Herencia - en la clase persona se define atributos y objetos  En clases hijas cliente y empleado 

//----------------------------------------------------------------------------------------------------------------------------------------------------------------
//9.2 Creacion de clase Persona


class Persona {
    static contadorPersonas = 0;

    constructor(nombre, apellido, edad) {
        this._idPersona = ++Persona.contadorPersonas;
        this._nombre = nombre;
        this._apellido = apellido;
        this._edad = edad;
    }

    get _idPersona() {
        return this._idPersona;
    }

    get nombre() {
        return this._nombre;
    }

    set nombre(Nombre) {
        this._nombre = Nombre;
    }

    get apellido() {
        return this._apellido;
    }

    set apellido(Apellido) {
        this._apellido = Apellido;
    }

    get edad() {
        return this._edad;
    }

    set edad(Edad) {
        this._edad = Edad;
    }

    toString(){
        return `${this._idPersona} 
        ${this._nombre} 
        ${this._apellido} 
        ${this._edad}`;
    }

}
//----------------------------------------------------------------------------------------------------------------------------------------------------------------
//9.3 clase empleado
class Empleado extends Persona{

    static contadorEmpleados = 0;

    constructor(nombre, apellido, edad, sueldo){
        super(nombre, apellido, edad);
        this._idEmpleado = ++Empleado.contadosEmpleados;
        this._sueldo = sueldo;
    }

    get idEmpleado() {
        return this._idEmpleado;
    }

    get sueldo() {
        return this._sueldo;
    }

    set sueldo(Sueldo) {
        this._sueldo = Sueldo;
    }

    toString(){
        return `
        ${super.toString()} 
        ${this._idEmpleado} 
        ${this._sueldo}`;
    }
}

//----------------------------------------------------------------------------------------------------------------------------------------------------------------
//9.4 Creación de la Clase Cliente
class Empleado extends Persona{

    static contadorClientes = 0;

    constructor(nombre, apellido, edad, fecharegistro){
        super(nombre, apellido, edad);
        this._idCliente = ++Cliente.contadosClientes;
        this._fecharegistro = fecharegistro;
    }

    get _idCliente() {
        return this._idCliente;
    }

    get fecharegistro() {
        return this._fecharegistro;
    }

    set fecharegistro(fecharegistro) {
        this._fecharegistro = Fecharegistro;
    }

    toString(){
        return `
        ${super.toString()} 
        ${this._idCliente} 
        ${this._fecharegistro}`;
    }
}

//----------------------------------------------------------------------------------------------------------------------------------------------------------------
// 9.5 Cargando todo en una sola plantilla
class Persona {
    static contadorPersonas = 0;

    constructor(nombre, apellido, edad) {
        this._idPersona = ++Persona.contadorPersonas;
        this._nombre = nombre;
        this._apellido = apellido;
        this._edad = edad;
    }

    get _idPersona() {
        return this._idPersona;
    }

    get nombre() {
        return this._nombre;
    }

    set nombre(Nombre) {
        this._nombre = Nombre;
    }

    get apellido() {
        return this._apellido;
    }

    set apellido(Apellido) {
        this._apellido = Apellido;
    }

    get edad() {
        return this._edad;
    }

    set edad(Edad) {
        this._edad = Edad;
    }

    toString(){
        return `${this._idPersona} 
        ${this._nombre} 
        ${this._apellido} 
        ${this._edad}`;
    }

}


class Empleado extends Persona{

    static contadorEmpleados = 0;

    constructor(nombre, apellido, edad, sueldo){
        super(nombre, apellido, edad);
        this._idEmpleado = ++Empleado.contadosEmpleados;
        this._sueldo = sueldo;
    }

    get idEmpleado() {
        return this._idEmpleado;
    }

    get sueldo() {
        return this._sueldo;
    }

    set sueldo(Sueldo) {
        this._sueldo = Sueldo;
    }

    toString(){
        return `
        ${super.toString()} 
        ${this._idEmpleado} 
        ${this._sueldo}`;
    }
}



class Cliente extends Persona{

    static contadorClientes = 0;

    constructor(nombre, apellido, edad, fecharegistro){
        super(nombre, apellido, edad);
        this._idCliente = ++Cliente.contadosClientes;
        this._fecharegistro = fecharegistro;
    }

    get _idCliente() {
        return this._idCliente;
    }

    get fecharegistro() {
        return this._fecharegistro;
    }

    set fecharegistro(fecharegistro) {
        this._fecharegistro = Fecharegistro;
    }

    toString(){
        return `
        ${super.toString()} 
        ${this._idCliente} 
        ${this._fecharegistro}`;
    }
}

//----------------------------------------------------------------------------------------------------------------------------------------------------------------
//9.6 Prueba Clase Persona

let Persona1 = new Persona('juan', 'Perez', 32);
console.log(Persona1.toString()); 1 juan perez 32

let Persona2 = new Persona('carla', 'ortega', 22);
console.log(Persona2.toString()); 2 carla ortega 22

//----------------------------------------------------------------------------------------------------------------------------------------------------------------
//9.7  Prueba Clase Empleado
//Prueba clase Empleado

let Empleado1 = new Empleado('pedro', 'roman', 18, 5000);
console.log(Empleado1.toString()); 3 pedro roman 18 1 5000

let Empleado2 = new Empleado('jonas', 'torres', 30, 7000);
console.log(Empleado2.toString()); 4 jonas torres 30 2 7000

//----------------------------------------------------------------------------------------------------------------------------------------------------------------
//9.8 Preueba clase  cliente

//Prueba clase Cliente

let Cliente1 = new Cliente('Miguel', 'Zala', 29, new Data());
console.log(Cliente1.toString());

let Cliente2 = new Cliente('natalia', 'ortega', 22, new Data());
console.log(Cliente2.toString());
