//Analia Alvarenga (Luna)
//CONEXION.JAVA

package UTN.conexion;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.SQLException;

public class Conexion {
    public static Connection getCONNECTION(){
        Connection conexion = null;
        //variable para conectarnos a la bd
        var baseDatos = "estudiantes";
        var url = "jdbc:mysql://localhost:3306/"+baseDatos;
        var usuario= "root";
        var password="mysql";

        //cargamos la clase del driver de mysql en memoria
        try{
            Class.forName("com.mysql.jdbc.Driver");
            conexion = DriverManager.getConnection(url,usuario,password);
        }catch(ClassNotFoundException | SQLException e){
            System.out.println("ocurrio un error en la conexion:"+e.getMessage());
        }//fin catch
        return conexion;
    }//fin metodo connection
}

//---------------------------------------------------------------------------------------------------------------------------------
//ESTUDIANTE.JAVA

package UTN.dominio;

public class Estudiante {
    private int idEstudiante;
    private String nombre;
    private String apellido;
    private String telefono;
    private String email;

    public Estudiante(){}
    public Estudiante(int idEstudiante){
        this.idEstudiante=idEstudiante;
    }
    //constructor para insertar un nuevo estudiante
    public Estudiante(String nombre,String apellido,String telefono,String email){
        this.nombre=nombre;
        this.apellido=apellido;
        this.telefono=telefono;
        this.email=email;
    }
    //constructor para modificar
    public Estudiante(int idEstudiante,String nombre,String apellido,String telefono,String email){
        this.idEstudiante=idEstudiante;
        this.nombre=nombre;
        this.apellido=apellido;
        this.telefono=telefono;
        this.email=email;
    }
    public int getIdEstudiante() {
        return idEstudiante;
    }

    public void setIdEstudiante(int idEstudiante) {
        this.idEstudiante = idEstudiante;
    }

    public String getNombre() {
        return nombre;
    }
    
    public void setNombre(String nombre) {
        this.nombre = nombre;
    }

    public String getApellido() {
        return apellido;
    }

    public void setApellido(String apellido) {
        this.apellido = apellido;
    }

    public String getTelefono() {
        return telefono;
    }

    public void setTelefono(String telefono) {
        this.telefono = telefono;
    }

    public String getEmail() {
        return email;
    }

    public void setEmail(String email) {
        this.email = email;
    }

    @Override
    public String toString() {
        return "Estudiante{" +
                "idEstudiante=" + idEstudiante +
                ", nombre='" + nombre + '\'' +
                ", apellido='" + apellido + '\'' +
                ", telefono='" + telefono + '\'' +
                ", email='" + email + '\'' +
                '}';
    }
}


//----------------------------------------------------------------------------------------------------------------------------------
//ESTUDIANTEDAO.JAVA

package UTN.datos;

import UTN.dominio.Estudiante;
import static UTN.conexion.Conexion.getCONNECTION;
import java.sql.Connection;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLOutput;
import java.util.ArrayList;
import java.util.List;

public class EstudianteDAO {
    //método listar
    public List<Estudiante>listarEstudiantes(){
        List<Estudiante>estudiantes = new ArrayList<>();
        //creamos algunos objetos que son necesarios para comunicarnos con la bd
        PreparedStatement ps;//nos ayuda a preparar(introduce) la sentencia sql
        ResultSet rs;//nos permite almacenar (obtener) el resultado obtenido desde la bd
        //creamos un objeto de tipo conexion
        Connection con = getCONNECTION();
        String sql = "SELECT * FROM estudiantes ORDER BY idestudiante";
        try{
            ps = con.prepareStatement(sql);
            rs = ps.executeQuery();
            while(rs.next()){
                var estudiante = new Estudiante();
                estudiante.setIdEstudiante(rs.getInt("idestudiantes"));
                estudiante.setNombre(rs.getString("nombre"));
                estudiante.setApellido(rs.getString("apellido"));
                estudiante.setTelefono(rs.getString("telefono"));
                estudiante.setEmail(rs.getString("email"));
                //falta agregarlo a la lista
                estudiantes.add(estudiante);

            }
        }catch(Exception e){
            System.out.println("ocurrio un error al seleccionar  datos:"+e.getMessage());
        }
        finally {
           try{
               con.close();
           }catch(Exception e){
               System.out.println("ocurrio un error al cerrar la conexion:"+e.getMessage());
           }
        }//fin finally
        return estudiantes;
    }//fin metodo listar

    
    //método por id-> fin by id
    public boolean buscarEstudianteporId(Estudiante estudiante){
        PreparedStatement ps;
        ResultSet rs;
        Connection con = getCONNECTION();
        String sql = "SELECT * FROM estudiantes WWHERE idestudiantes=?";
        try {
            ps = con.prepareStatement(sql);
            ps.setInt(1, estudiante.getIdEstudiante());
            rs = ps.executeQuery();
            if (rs.next()){
                estudiante.setNombre(rs.getString("nombre"));
                estudiante.setApellido(rs.getString("apellido"));
                estudiante.setTelefono(rs.getString("telefono"));
                estudiante.setEmail(rs.getString("email"));
                return true;//se encontro un registro
            }//fin if
        }catch(Exception e){
            System.out.println("Ocurrio un error al buscar estudiante:"+e.getMessage());
        }//fin catch
        finally {
            try{
                con.close();
            }catch (Exception e){
                System.out.println("ocurrio un error al cerrar conexion:"+e.getMessage());
            }//fin catch
        }//fin finally
        return false;
    }
    //Metodo agregar un nuevo estudiante
    public boolean agregarEstudiante(Estudiante estudiante){
        PreparedStatement ps;
        Connection con = getCONNECTION();
        String sql = "INSERT INTO estudiantes(nombre,apellido,telefono,email)VALUES (?,?,?,?)";
        try{
            ps = con.prepareStatement(sql);
            ps.setString(1, estudiante.getNombre());
            ps.setString(2, estudiante.getApellido());
            ps.setString(3, estudiante.getTelefono());
            ps.setString(4, estudiante.getEmail());
            ps.execute();
            return  true;

        }catch(Exception e){
            System.out.println("ocurrio un error ");
        }//fin catch
        finally{
          try{
              con.close();
          }catch(Exception e){
              System.out.println("error al cerrar la conexion:"+e.getMessage());
          }//fin catch
        }//fin finally
        return false;
    }//fin metodo agregar estudiante

  //metodo para modificar
    public boolean modificarEstudiante(Estudiante estudiante){
        PreparedStatement ps;
        Connection con = getCONNECTION();
        String sql = "UPDATE estudiante SET nombre =?,apellido=?,telefono=?,email=? WHERE idestudiantes=?";
        try{
            ps= con.prepareStatement(sql);
            ps.setString(1, estudiante.getNombre());
            ps.setString(2,estudiante.getApellido());
            ps.setString(3,estudiante.getTelefono());
            ps.setString(4,estudiante.getEmail());
            ps.setInt(5,estudiante.getIdEstudiante());
            ps.execute();
            return  true;
        }catch(Exception e){
            System.out.println("error al modificarse estudiante:"+e.getMessage());
        }//fin catch
        finally {
            try{
                con.close();
            }catch (Exception e){
                System.out.println("error al cerrar conexion:"+e.getMessage());
            }//fin catch
        }//fin finally
        return false;
    }//fin metodo modificar estudiante


    public static void main(String[] args) {
        var estudianteDao =  new EstudianteDAO();

        //modificar estudiante
        var estuduanteModificado = new Estudiante(1,"juan","perez","456123","jperez@email.com");
        var modificado = estudianteDao.modificarEstudiante(estuduanteModificado);
        if(modificado)
            System.out.println("estudiante modificado:"+estuduanteModificado);
        else
            System.out.println("no se modifico el estudiante: "+estuduanteModificado);

        //agregar estudiante
       // var nuevoEstudiante = new Estudiante("Carlos","Lara","5465544223","clara@gmail.com");
        //var agregado = estudianteDao.agregarEstudiante(nuevoEstudiante);
        //if(agregado)
          //  System.out.println("estudiante agregado:"+nuevoEstudiante);
        //else
        //    System.out.println("no se ha agregado estudiante:"+ nuevoEstudiante);

        // listar los estudiantes
        System.out.println("listado de estudiantes: ");
        List<Estudiante> estudiantes = estudianteDao.listarEstudiantes();
        estudiantes.forEach(System.out::println);//FUNCION LAMBDA para imprimir

        //buscar por id
        //var estudiante1 = new Estudiante(1);
        //System.out.println("Estudiantes antes de la busqueda :"+estudiante1);
        //var encontrado = estudianteDao.buscarEstudianteporId(estudiante1);
        //if(encontrado)
        //    System.out.println("estudiante encontrado:"+estudiante1);
        //else
        //    System.out.println("no se encontro el estudiante: "+estudiante1.getIdEstudiante());


    }
}


//MAIN.JAVA
package UTN;


public class Main {
    public static void main(String[] args) {
        var conexion = Conexion.getConnection();
        if(conexion != null)
            System.out.println("Conexion exitosa: "+conexion);
        else
            System.out.println("Error al conectarse");
    }//Fi1n  main
}// Fin clase

