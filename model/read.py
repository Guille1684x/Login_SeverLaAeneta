from model.conexion import conexion

class Read:
    def __init__(self) -> None:
        self.connection = conexion()
        self._resultado = False

    def alumnos(self, usuario, contrasenia):
        self.__consulta("estudiantes", usuario, contrasenia)
        pass

    def docente(self, usuario, contrasenia):
        self.__consulta("docentes", usuario, contrasenia)
        pass

    def __consulta(self, table, usuario, contrasenia):
        try:
            with self.connection.cursor() as cursor:
                sql = "SELECT * FROM {} WHERE Nombre = %s AND contrasenia = %s".format(table)
                cursor.execute(sql, (usuario, contrasenia))
                result = cursor.fetchall()
                if result:
                    self._resultado = True
                else:
                    self._resultado = False
        except Exception as e:
            print(f"Error en el usuario o contraseña: {e}")
            self._resultado = False
        finally:
            self.connection.close()

    def get_result(self):
        return self._resultado