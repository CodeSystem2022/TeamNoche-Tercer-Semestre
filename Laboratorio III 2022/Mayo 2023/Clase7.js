//Soria Ezequiel
//Codigo de la clase 7 de js

class Persona{ //clase padre
    //definimos un constructor
    constructor(nombre, apellido){
        this._nombre = nombre
        this._apellido = apellido
    }
    
    //añadimos los get y set
    get nombre(){
        return this._nombre
    }

    set nombre(nombre){
        this._nombre = nombre
    }

    get apellido(){
        return this._apellido
    }

    set apellido(apellido){
        this._apellido = apellido
    }
//
    nombreCompleto(){
        return this._nombre+' '+this._apellido 
    }

    //Sobreescribiendo el metodo de la clase padre (object)
    toStrig(){
        //se aplica el polimorfismo que significa: multiples formas en tiempo de ejecucion
        //El metodo que se ejecuta depende de la referencia del tipo padre o hija.
        return this.nombreCompleto()
    }

   
}

@ -41,7 +51,12 @@ class Empleado extends Persona{ //clase hija que extiende de Persona
    set departamento(departamento){
        this._departamento = departamento
    }
//

    //Sobreescritura
    nombreCompleto(){
        return super.nombreCompleto()+', '+this._departamento
    }
    
}

let persona1 = new Persona('Martin', 'Perez')
@ -67,4 +82,7 @@ let empleado1 = new Empleado('Emma', 'Soria', 'Sistemas')
console.log(empleado1)
console.log(empleado1.nombreCompleto())

//
//Object.prototype.toString esta es la manera de acceder a atributos y metodos de forma dinamica

console.log(empleado1.toStrig()) //al llamar al toString desde una instacia de la clase hija se ejecutara la funcion nombreCompleto de la clase hija, por eso se muestra el nombre y el departamento.
console.log(persona1.toStrig()) //al llamar al toString desde la clase padre solo mostra el nombre y apellido sin el departamento.
