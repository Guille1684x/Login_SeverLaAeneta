-- Creación de la base de datos
CREATE DATABASE IF NOT EXISTS Universidad;
USE Universidad;

-- Creación de tabla Estudiantes
CREATE TABLE IF NOT EXISTS Estudiantes (
    ID_Estudiante INT AUTO_INCREMENT PRIMARY KEY,
    Nombre VARCHAR(255),
    Apellido VARCHAR(255),
    CorreoElectronico VARCHAR(255),
    Facultad VARCHAR(255)
);

-- Creación de tabla Docentes
CREATE TABLE IF NOT EXISTS Docentes (
    ID_Docente INT AUTO_INCREMENT PRIMARY KEY,
    Nombre VARCHAR(255),
    Apellido VARCHAR(255),
    Especialidad VARCHAR(255),
    CorreoElectronico VARCHAR(255),
    Facultad VARCHAR(255)
);

-- Creación de tabla Áreas de Estudio
CREATE TABLE IF NOT EXISTS Areas_Estudio (
    ID_AreaEstudio INT AUTO_INCREMENT PRIMARY KEY,
    NombreArea VARCHAR(255),
    Descripcion TEXT
);

-- Creación de tabla Trabajos de Titulación
CREATE TABLE IF NOT EXISTS Trabajos_Titulacion (
    ID_Trabajo INT AUTO_INCREMENT PRIMARY KEY,
    Titulo VARCHAR(255),
    Resumen TEXT,
    FechaInicio DATE,
    FechaFin DATE,
    Estado VARCHAR(50),
    ID_Estudiante INT,
    ID_DocenteDirector INT,
    ID_DocenteCoDirector INT,
    ID_AreaEstudio INT,
    FOREIGN KEY (ID_Estudiante) REFERENCES Estudiantes(ID_Estudiante),
    FOREIGN KEY (ID_DocenteDirector) REFERENCES Docentes(ID_Docente),
    FOREIGN KEY (ID_DocenteCoDirector) REFERENCES Docentes(ID_Docente),
    FOREIGN KEY (ID_AreaEstudio) REFERENCES Areas_Estudio(ID_AreaEstudio)
);

-- Creación de tabla Palabras Clave
CREATE TABLE IF NOT EXISTS Palabras_Clave (
    ID_PalabraClave INT AUTO_INCREMENT PRIMARY KEY,
    Palabra VARCHAR(100)
);

-- Creación de tabla Trabajos_PalabrasClave (relación muchos a muchos)
CREATE TABLE IF NOT EXISTS Trabajos_PalabrasClave (
    ID_Trabajo INT,
    ID_PalabraClave INT,
    FOREIGN KEY (ID_Trabajo) REFERENCES Trabajos_Titulacion(ID_Trabajo),
    FOREIGN KEY (ID_PalabraClave) REFERENCES Palabras_Clave(ID_PalabraClave),
    PRIMARY KEY (ID_Trabajo, ID_PalabraClave)
);

-- Creación de tabla Historial de Modificaciones
CREATE TABLE IF NOT EXISTS Historial_Modificaciones (
    ID_Modificacion INT AUTO_INCREMENT PRIMARY KEY,
    ID_Trabajo INT,
    FechaModificacion DATE,
    DescripcionModificacion TEXT,
    ID_Docente INT,
    FOREIGN KEY (ID_Trabajo) REFERENCES Trabajos_Titulacion(ID_Trabajo),
    FOREIGN KEY (ID_Docente) REFERENCES Docentes(ID_Docente)
);

-- Creación de tabla Accesos
CREATE TABLE IF NOT EXISTS Accesos (
    ID_Acceso INT AUTO_INCREMENT PRIMARY KEY,
    ID_Trabajo INT,
    ID_Usuario INT,
    FechaAcceso DATE,
    TipoUsuario VARCHAR(50),
    FOREIGN KEY (ID_Trabajo) REFERENCES Trabajos_Titulacion(ID_Trabajo)
);

ALTER TABLE estudiantes ADD COLUMN contrasenia VARCHAR(22);
ALTER TABLE docentes ADD COLUMN contrasenia VARCHAR(22);


