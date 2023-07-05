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
//
