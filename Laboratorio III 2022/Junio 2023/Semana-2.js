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
           