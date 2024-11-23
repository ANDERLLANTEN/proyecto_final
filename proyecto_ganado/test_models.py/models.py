# Clase que representa un objeto Ganado con atributos básicos.
class Ganado:
    def __init__(self, id_etiqueta, nombre, raza, peso, estado_salud):
        # Inicializa un objeto Ganado con su identificador único, nombre, raza, peso y estado de salud.
        self.id_etiqueta = id_etiqueta
        self.nombre = nombre
        self.raza = raza
        self.peso = peso
        self.estado_salud = estado_salud

# Clase para gestionar las operaciones relacionadas con la tabla GANADO en la base de datos.
class GestorGANADO:
    def __init__(self, connection):
        # Inicializa la clase con una conexión a la base de datos.
        self.connection = connection

    # Método para agregar un nuevo registro de ganado a la base de datos.
    def agregar_GANADO(self, id_etiqueta, nombre, raza, peso, estado_salud):
        try:
            # Obtiene un cursor para ejecutar consultas SQL.
            cursor = self.connection.cursor()
            
            # Consulta SQL para insertar un nuevo registro en la tabla GANADO.
            query = """
                INSERT INTO GANADO (id_etiqueta, nombre, raza, peso, estado_salud)
                VALUES (:1, :2, :3, :4, :5)
            """
            
            # Ejecuta la consulta, pasando los valores como parámetros.
            cursor.execute(query, (id_etiqueta, nombre, raza, peso, estado_salud))
            
            # Confirma (commit) los cambios en la base de datos.
            self.connection.commit()
        except Exception as e:
            # En caso de error, revierte (rollback) los cambios para evitar inconsistencias.
            self.connection.rollback()
            # Imprime un mensaje de error para ayudar en la depuración.
            print(f"Error al agregar ganado: {e}")
        finally:
            # Asegura que el cursor se cierre al final del bloque, incluso si ocurre un error.
            cursor.close()
