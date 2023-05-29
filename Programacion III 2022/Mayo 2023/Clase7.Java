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
