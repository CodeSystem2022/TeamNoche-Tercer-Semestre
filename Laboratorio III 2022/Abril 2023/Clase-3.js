//Florencia Pons
//Funciones y return
miFuncion(8, 2); //Esto se lo conoce como hosting

function miFuncion(a, b){
    //console.log("Sumamos: "+ (a+ b));
    return a + b;
}

//Llamando la funcion 
miFuncion(5, 4);

let resultado = miFuncion(6, 7);
console.log(resultado);
-----------------------------------------------------------------------------------------------------------------------------------------------------------------------

//Julio Ezequiel Soria
//Paso por referencia
const persona = {
    nombre: 'juan',
    apellido: 'Lepez'
}
console.log(typeof persona)

function cambiarValorObjeto(p1) {//la variable p1 reasigna los datos a los parametros de nombre y apellido, luego es eliminada.
    console.log(persona)
    p1.nombre = 'Eze'
    p1.apellido = 'Soria'
    console.log(persona)
}

cambiarValorObjeto(persona)
console.log(persona)
