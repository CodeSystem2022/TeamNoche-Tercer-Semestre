//Clase 5 - Objetos parte 2. Uso del get ↓//

console.log("Clase 5 - 'Objetos' parte 2");
console.log("5.1 Uso del get en Creación de una persona nueva↓");

let personanueva = {
    primernombre: "Gustavo",
    segundonombre: "Emanuel",
    apellido: "Gimenez",
    edad: 31,
    domicilio: "Rivadadvia 816",
    telefono: 53277235,
    entrecalles: "Moreno y Misiones",
    get primernombreEdad(){
    return this.primernombre+' y su edad es: '+this.edad;
    }
        }
        console.log(personanueva.primernombreEdad);

        //Uso del set ↓ //

        let persona2 = {
            primernombre: "Gustavo",
            segundonombre: "Emanuel",
            apellido: "Gimenez",
            edad: 28,
            domicilio: "Rivadadvia 816",
            telefono: 53277235,
            entrecalles: "Moreno y Misiones",
            idioma: 'es', //mínuscula//
            get primernombreEdad(){
            return this.primernombre+' y su edad es: '+this.edad;
            },
            get lang(){
                return this.idioma.toUpperCase(); //el método upercase convierte minusculas a mayusculas/*
            },
            set lang(lang){
                this.idioma = lang.toUpperCase();
                }
            }
                console.log("metodo get para idiomas")
                persona2.lang ='en';
                console.log(persona2.lang);

    //5.2 Constructores de objetos/

      function Persona3(nombre,apellido,email){ //ésta parte es el constructor//
        this.nombre = nombre;
        this.apellido = apellido;
        this.email = email;
     //5.3 agregando metodos ↓
        this.nombreCompleto = function() {
            return this.nombre+ ' '+this.apellido;
        }
                    }
                    let padre = new Persona3('Leo','Lopez','Lopezleo@gmail.com');
                    console.log(padre)
                    padre.telefono = '54128795';
                    console.log(padre.telefono);
                    let madre = new Persona3('Laura','Rothchild','Rotchildlory@live.com');
                    console.log(madre)
                    console.log(padre.nombreCompleto());
                    console.log(madre.nombreCompleto());


    //5.4 Distintas formas de crear objetos ↓
                    //Forma 1 :
                    //let miObjeto = new object();//
                    //Forma 2:
                    let miObjeto2 = {};
                    //caso String 1
                    //let miCadena1 = new string();
                    //Casi String 2
                    let miCadena2 = 'Hola';
                    //Caso con numeros 1:
                    //let miNumero = new number(1);
                    //Caso con numeros 2
                    let miNumero2 = 1;

                    //caso boolean 1 //
                    //let miBoolean1 = new boolean(true);
                    //Forma 2 de hacer un boolean:
                    ///let miBoolean2 = true;
                    //Caso de arreglos 1
                    //let miArreglo1 = new array();
                    //Caso arreglo 2
                    let miArreglo2 = [];
                    //Funciones ↓
                    //let miFuncion1 = new function (){};
                    //Funcion 2
                    let miFuncion2 = function(){};

                    //Uso de prototype
                    Persona3.prototype.telefono = '1125489136';
                    console.log(padre);
                    console.log(padre.telefono);

                    //Uso del call
                    let persona4 = {
                        nombre: 'Juan',
                        apellido: 'Perez',

                        nombreCompleto2: function(titulo,telefono){
                            return titulo+' '+this.nombre+' '+this.apellido+' '+this.telefono;
                        }
                    }
                    let persona5 = {
                        nombre: 'Carlos',
                        apellido: 'Lara'
                    }

                    console.log(persona4.nombreCompleto2('Lic.','1152148932'));
                    console.log(persona4.nombreCompleto2.call(persona5,'Ing.'));

                    //Uso de apply. Para este ejemplo voy a crear 2 personas nuevas por comodidad//

                    let persona6 = {
                        nombre: 'Ezequiel',
                        apellido: 'Blasco',

                        nombreCompleto3: function(titulo,telefono){
                           return this.nombre+' '+this.apellido+','+'  '+titulo+'.' +"Telefono de contacto:"+telefono
                        }
                    }

                    let persona7 = {
                        nombre: 'Mike',
                        apellido: 'Ross'
                    }
                    console.log(persona6.nombreCompleto3());
                    console.log(persona6.nombreCompleto3.call(persona7));

                    //método apply ↓ 
                   

                     let arreglo = ['Ingeniero en sistemas','02204991240'];
                     console.log(persona6.nombreCompleto3.apply(persona6,arreglo));


-----------------------------------------------------------------------------------------------

    //6.1 - Clase 6 

class Persona{ //clase padre
    constructor(nombre,apellido){
        this.nombre = nombre;
        this.apellido = apellido;
        
    }
}

let persona1 = new Persona('Martin','Perez');
console.log(persona1);

let persona2 = new Persona ('Franco','Da Cruz');

console.log(persona2);

//clase hija - herencia  ↓

class Empleado extends Persona { //clase hija
    constructor(nombreempleado,apellidoempleado,departamento){
        super(nombreempleado,apellidoempleado); //super se usa para definir el constructor de la clase hija
        this._departamento = departamento;

    }
    get departamento(){
        return this._departamento;
    }
    set departamento(departamento){
        this._departamento = departamento;

    } //Listos sus métodos get y set para la clase hija con un solo atributo
};

//6.2 Get & Set 
class Persona2{
    constructor(nombre,apellido){
        this._nombre = nombre;
        this._apellido = apellido;
        
    }
    get nombre(){
        return this._nombre;
    }
    set nombre(nombre){
        this._nombre = nombre;
    }
}

let persona3 = new Persona2('Tomas','Shelby');
//console.log(persona3);
console.log(persona3.nombre);
persona3.nombre = 'Arhur';
console.log(persona3.nombre)

let persona4 = new Persona2 ('Harvey','Specter');
console.log(persona4.nombre);
//console.log(persona4);
persona4.nombre = "Poly";
console.log(persona4.nombre);

//Ejercicio Crear el método get y set para el atributo de apellido//
//luego modificar el apellido a través del  set y mostrar con un console.log lo que es el get donde muestra el resultado obtenido//

class persona2a {
    constructor(nombre,apellido){
        this._nombre = nombre;
        this._apellido = apellido;
    }

    get apellido() {
        this._apellido = apellido;
    }

    set apellido(apellido){
        this._apellido = apellido;
    }
//set con el cual  cambié el apellido ↓
    set apellido(apellido2)
    {this._apellido = apellido2};
}

let persona5 = new persona2a ('Julian','Alvarez');
console.log(persona5._apellido);
persona5.apellido2 = 'Martinez';
console.log(persona5.apellido2);


//6.3 hoisting y clases: Parte 1 y 2. No se puede crear una persona sin antes inicializar lo que es la persona.
//Es decir queno funciona el hoisting. No se puede crear un objeto antes de haber defiido la clase //
//Primero se crea la clase, luego el sujeto/persona, luego su constructor y sus métodos junto con su set y get. 
//El console para imprimir va fuera del objeto.



//6.4 Herencia: Let de la clase hija ↓

let empleado1 = new Empleado('Maria','Gimenez','Sistemas');
console.log(empleado1);




           
