//Ezequiel Soria
//clase 10.2 de js

class Producto{

    static contadorProducto=0;

    constructor(nombre, precio){
        this._idProducto = ++Producto.contadorProducto;
        this._nombre = nombre;
        this._precio = precio;
    }

    get idProducto(){
        return this._idProducto;
    }

    get nombre(){
        return this._nombre;
    }

    set nombre(nombre){
        this._nombre = nombre;
    }

    get precio(){
        return this._precio;
    }

    set precio(precio){
        this._precio = precio;
    }

    toString(){
        return `
        Id Producto: ${this._idProducto} 
        Nombre: ${this._nombre} 
        Precio: ${this._precio}`; 
    }

}// Fin clase producto

//Ezequiel Soria
//Clase 10.3 de js

//prueba clase producto
let producto1 = new Producto('Teclado', 4000);
let producto2 = new Producto('Mouse', 1500);
let producto3 = new Producto('Monitor', 15000);
console.log(producto1.toString());

//Ezequiel Soria
//clase 10.4 de js

class Orden{
    
    static contadorOrdenes = 0;
    static getMAX_PRODUCTOS(){
        return 5;
    }

    constructor(){
        this._idOrden = ++Orden.contadorOrdenes;
        this._productos = [];
        this._contadorProductosAgregados=0;
    }

    get idOrden(){
        return this._idOrden
    }

    agregarProducto(producto){
        if(this._productos.length < Orden.getMAX_PRODUCTOS()){
            this._productos.push(producto); //Tenemos 2 formas de sintaxis
            //this._productos[this._contadorProductosAgregados++] = producto; //segunda forma

        }
        else{
            console.log('No se puede agregar mas productos')
        }
    }//fin metodo agregarProducto

    calcularTotal(){
        let totalVenta = 0;
        for(let producto of this._productos){
            totalVenta += producto.precio;
        }
        return totalVenta;
    }//fin metodo calcularTotal

    mostrarOrden(){
        let productoorden=' ';
        for(let producto of this._productos){
            productoorden += producto.toString()+' ';
        }
        console.log(`
        Orden: ${this._idOrden} 
        Total: $${this.calcularTotal()} 
        Productos: ${productoorden}`
        )
    }// fin metodo mostrarOrden
}//fin clase orden

//Ezequiel Soria
//Clase 10.5

let orden1 = new Orden();
let orden2 = new Orden();
orden1.agregarProducto(producto1);
orden1.agregarProducto(producto2);
orden1.agregarProducto(producto3);
orden1.agregarProducto(producto1);
orden1.agregarProducto(producto2);
orden1.agregarProducto(producto3);
orden2.agregarProducto(producto3);

orden1.mostrarOrden();
orden2.mostrarOrden();
