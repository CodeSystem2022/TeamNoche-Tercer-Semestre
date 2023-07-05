//Analia Alvarenga (Luna)
//POM.XML
<?xml version="1.0" encoding="UTF-8"?>
<project xmlns="http://maven.apache.org/POM/4.0.0"
         xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
         xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 http://maven.apache.org/xsd/maven-4.0.0.xsd">
    <modelVersion>4.0.0</modelVersion>

    <groupId>UTN</groupId>
    <artifactId>Estudiante</artifactId>
    <version>1.0-SNAPSHOT</version>

    <dependencies>
        <!-- https://mvnrepository.com/artifact/com.mysql/mysql-connector-j -->
        <dependency>
            <groupId>com.mysql</groupId>
            <artifactId>mysql-connector-j</artifactId>
            <version>8.0.33</version>
        </dependency>
    </dependencies>

    <properties>
        <maven.compiler.source>18</maven.compiler.source>
        <maven.compiler.target>18</maven.compiler.target>
        <project.build.sourceEncoding>UTF-8</project.build.sourceEncoding>
    </properties>

</project>

//--------------------------------------------------------------------------------------------------------------------------------------
//ESTUDIANTES.SQL
//Conexion Java MySQL

-- Comenzamos con CRUD: create(insertar), reed(leer), update(actualizar)
-- Listar los estudiantes (read)
SELECT * FROM estudiantes2022;
-- Insertar estudiante
INSERT INTO estudiantes2022 (nombre, apellido, telefono, email) VALUES ("Juan", "Perez", "260444664", "Juan@gmail.com");
UPDATE estudiantes2022 SET nombre="Juan Carlos", apellido="Garcia" WHERE idestudiantes2022= 1;
-- Delate(eliminar)

DELETE FROM estudantes2022 WHERE idestuantes2022=3;

-- Para modificar el id estudiantes2022 y comience en 1
ALTER TABLE estudiantes2022 AUTO_INCREMENT = 1;
