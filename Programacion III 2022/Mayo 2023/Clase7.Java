#Contreras, Yamila Belen

#7.2 Manejo de Interfaces. Parte 2

//IAccesoDatos        

package accesodatos;

public interface IAccesoDatos {
    int MAX_REGISTRO = 10;
    
    //Método insertar es abstracto y sin cuerpo
    void insertar();
    
    void listar();
    
    void actualizar(); 
    
    void eliminar();
}

--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#Contreras, Yamila Belen

#7.3 Manejo de Interfaces. Parte 3
    
//Implementación Mysql

package accesodatos;

public class ImplementacionMySql implements IAccesoDatos{
    
    @Override
    public void insertar() {
        System.out.println("Insertar desde MySql");
    }
    
     @Override
    public void listar() {
        System.out.println("Listar desde MySql");
    }
    
     @Override
    public void actualizar() {
        System.out.println("Actualizar desde MySql");
    }
    
     @Override
    public void eliminar() {
        System.out.println("Eliminar desde MySql");
    }
    
}

--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
#Contreras, Yamila Belen

#7.4 Manejo de Interfaces. Parte 4

//Implementación Oracle

package accesodatos;

public class ImplementacionOracle implements IAccesoDatos{
    
    @Override
    public void insertar() {
        System.out.println("Insertar desde Oracle");
    }
    
     @Override
    public void listar() {
        System.out.println("Listar desde Oracle");
    }
    
     @Override
    public void actualizar() {
        System.out.println("Actualizar desde Oracle");
    }
    
     @Override
    public void eliminar() {
        System.out.println("Eliminar desde Oracle");
    }
    
}
