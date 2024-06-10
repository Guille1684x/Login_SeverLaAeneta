from model.conexion import conexion
from views.notify import notify


def alumno(nombre, apellido, correo_electronico, facultad, contraseña):
    # Conectar a la base de datos
    connection = conexion()
    
    try:
        with connection.cursor() as cursor:
            # SQL para insertar un nuevo estudiante
            sql = "INSERT INTO estudiantes (Nombre, Apellido, CorreoElectronico, Facultad, contrasenia) VALUES (%s, %s, %s, %s, %s)"
            # Ejecutar la consulta
            cursor.execute(sql, (nombre, apellido, correo_electronico, facultad, contraseña))
            # Confirmar los cambios
            connection.commit()
            print("Estudiante registrado exitosamente.")
            notify("Estudiante registrado exitosamente.")
    except Exception as e:
        print(f"Error al registrar el estudiante: {e}")
        notify("Error al registrar el estudiante.")
    finally:
        # Cerrar la conexión
        connection.close()

def docente(nombre, apellido, especialidad, correo_electronico, facultad, contraseña):
    # Conectar a la base de datos
    connection = conexion()
    
    try:
        with connection.cursor() as cursor:
            # SQL para insertar un nuevo docente
            sql = "INSERT INTO docentes (Nombre, Apellido, Especialidad, CorreoElectronico, Facultad, contrasenia) VALUES (%s, %s, %s, %s, %s, %s)"
            # Ejecutar la consulta
            cursor.execute(sql, (nombre, apellido, especialidad, correo_electronico, facultad, contraseña))
            # Confirmar los cambios
            connection.commit()
            print("Docente registrado exitosamente.")
            notify("Docente registrado exitosamente.")
    except Exception as e:
        print(f"Error al registrar el docente: {e}")
        notify("Error al registrar el docente.")
    finally:
        # Cerrar la conexión
        connection.close()