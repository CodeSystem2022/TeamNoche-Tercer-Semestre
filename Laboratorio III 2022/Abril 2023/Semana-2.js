//Florencia Pons
//Creamos Array o arreglos en Java Script
//let autos = Array('Ferrari', 'Reanult', 'BMW'); esta es la sintaxis vieja

const autos = ['Ferrari', 'Reanult', 'BMW'];
console.log(autos);

//Recorremos los elementos de un arreglo
console.log(autos[0]);
console.log(autos[2]);

for(let i = 0; i < autos.length; i++){
    console.log(i+':'+autos[i]);
}
------------------------------------------------------------------------------------------------------------------------------------------------------------------------
//Julio Ezequiel Soria
//Como preguntar si es un array

const autos2 = ['Ferrari', 'Reanult', 'BMW']

console.log(typeof(autos2))// no podemos usar el metodo typeof ya que solo muestra que es un objeto

console.log(Array.isArray(autos2)) //usamos la clase Array.isArray que devuelve un booleano

console.log(autos2 instanceof Array) //Devuelve un booleano
-------------------------------------------------------------------------------------------------------------------------------------------------------------
