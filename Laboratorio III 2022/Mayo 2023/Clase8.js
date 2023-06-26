//Soria Ezequiel
//Carga completa de la clase 8 de JS

// no se puede hacer hosting con las clases, no podemos definir 
// un objeto de un constructor que no ha sido declarado.
// let persona3 = new Persona('Clara', 'Ponce') 

class Persona{ //clase padre
    
    //atributo static de clase 
    static contadorPersona = 0
    //atributo no estatico
    //email = 'Valor default email'

    //Metodo que simula una constante
    static get MAX_OBJ(){
        return 5
    }

    //definimos un constructor
    constructor(nombre, apellido){
        this._nombre = nombre
        this._apellido = apellido
        if (Persona.contadorPersona < Persona.MAX_OBJ) {
            this.idPersona = ++Persona.contadorPersona
        }
        else{
            console.log('Se ha superado el maximo de objetos permitidos')
        }
        
        console.log('Se incrementa el contador: '+Persona.contadorPersona)
    }
    
    //añadimos los get y set
@ -26,7 +45,7 @@ class Persona{ //clase padre
        this._apellido = apellido
    }
    nombreCompleto(){
        return this._nombre+' '+this._apellido 
        return this.idPersona+' '+this._nombre+' '+this._apellido 
    }

    //Sobreescribiendo el metodo de la clase padre (object)
@ -36,7 +55,13 @@ class Persona{ //clase padre
        return this.nombreCompleto()
    }

    static saludar(){
        console.log('Saludos desde este metodo ')
    }
    
    static saludar2(persona){
        console.log(persona.nombre+' '+persona.apellido)
    }
}

class Empleado extends Persona{ //clase hija que extiende de Persona
@ -86,3 +111,40 @@ console.log(empleado1.nombreCompleto())

console.log(empleado1.toStrig()) //al llamar al toString desde una instacia de la clase hija se ejecutara la funcion nombreCompleto de la clase hija, por eso se muestra el nombre y el departamento.
console.log(persona1.toStrig()) //al llamar al toString desde la clase padre solo mostra el nombre y apellido sin el departamento.

//persona1.saludar() solo se puede llamar a una funcion static desde su clase. 
//llamamos a la clase antes de llamar al metodo static
Persona.saludar()
Persona.saludar2(persona1)

//tambien se pueden llamar desde la clase hija.
Empleado.saludar()
Empleado.saludar2(empleado1)

//console.log(persona1.contadorPersona) no se puede acceder a un atributo static desde un objeto solo desde la clase.
console.log(Persona.contadorPersona)

//los valores no estaticos se pueden acceder desde los objetos ya sean de la clase padre o hija
console.log(persona1.email)
console.log(empleado1.email)
// No se puede acceder desde la clase, solo desde los objetos
//console.log(Persona.email)

console.log(persona1.toStrig())
console.log(persona2.toStrig())
console.log(empleado1.toStrig())
console.log(Persona.contadorPersona)

let persona3 = new Persona('Marta', 'Lopez')
console.log(persona3.toStrig())
console.log(Persona.contadorPersona)

console.log(Persona.MAX_OBJ)
Persona.MAX_OBJ = 10 //no se puede modificar
console.log(Persona.MAX_OBJ)

let persona4 = new Persona('Franco', 'Diaz')
console.log(persona4.toStrig())

let persona5 = new Persona('Liliana', 'Paz')
console.log(persona5.toStrig())
