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
//
