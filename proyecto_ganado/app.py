from flask import Flask, render_template, request, redirect, url_for, flash, session, g
from werkzeug.security import generate_password_hash, check_password_hash
import oracledb

app = Flask(__name__)

# Configuración de Flask
app.secret_key = '12345'  # Cambiar por una clave segura en producción

# Configuración de la conexión a Oracle
oracle_host = 'localhost'
oracle_port = 1521
oracle_sid = 'ORCL'
oracle_user = 'ANDERSONN'
oracle_password = '12345'

# Crear cadena de conexión
dsn = oracledb.makedsn(oracle_host, oracle_port, sid=oracle_sid)

# Conexión a la base de datos
def get_db():
    if 'db' not in g:
        try:
            g.db = oracledb.connect(user=oracle_user, password=oracle_password, dsn=dsn)
            print("Conexión exitosa a la base de datos Oracle.")
        except oracledb.DatabaseError as e:
            error, = e.args
            print(f"Error de conexión: {error.message}")
            g.db = None
    return g.db

@app.teardown_appcontext
def close_connection(exception):
    db = g.pop('db', None)
    if db:
        db.close()
        print("Conexión cerrada correctamente.")
    else:
        print("No había conexión abierta.")


# ----- Clases y lógica del negocio -----
class Ganado:
    def __init__(self, id_etiqueta, nombre, raza, peso, estado_salud):
        self.id_etiqueta = id_etiqueta
        self.nombre = nombre
        self.raza = raza
        self.peso = peso
        self.estado_salud = estado_salud

class GestorGANADO:
    def __init__(self, connection):
        self.connection = connection

    def agregar_GANADO(self, id_etiqueta, nombre, raza, peso, estado_salud):
        try:
            cursor = self.connection.cursor()
            query = """
                INSERT INTO GANADO (id_etiqueta, nombre, raza, peso, estado_salud)
                VALUES (:1, :2, :3, :4, :5)
            """
            cursor.execute(query, (id_etiqueta, nombre, raza, peso, estado_salud))
            self.connection.commit()
        except oracledb.DatabaseError as e:
            error, = e.args
            self.connection.rollback()
            print(f"Error al agregar GANADO: {error.message}")
        finally:
            cursor.close()

    def mostrar_GANADO(self):
        try:
            cursor = self.connection.cursor()
            query = "SELECT id_etiqueta, nombre, raza, peso, estado_salud FROM ganado"
            cursor.execute(query)
            rows = cursor.fetchall()
            return [Ganado(*row) for row in rows]
        except oracledb.DatabaseError as e:
            error, = e.args
            print(f"Error al obtener GANADO: {error.message}")
            return []
        finally:
            cursor.close()

    def eliminar_GANADO(self, id_etiqueta):
        try:
            cursor = self.connection.cursor()
            query = "DELETE FROM GANADO WHERE id_etiqueta = :1"
            cursor.execute(query, (id_etiqueta,))
            if cursor.rowcount > 0:
                self.connection.commit()
            else:
                print(f"Ganado con ID {id_etiqueta} no encontrado.")
        except oracledb.DatabaseError as e:
            error, = e.args
            self.connection.rollback()
            print(f"Error al eliminar GANADO: {error.message}")
        finally:
            cursor.close()

    def actualizar_peso(self, id_etiqueta, nuevo_peso):
        try:
            cursor = self.connection.cursor()
            query = "UPDATE GANADO SET peso = :1 WHERE id_etiqueta = :2"
            cursor.execute(query, (nuevo_peso, id_etiqueta))
            self.connection.commit()
        except oracledb.DatabaseError as e:
            error, = e.args
            self.connection.rollback()
            print(f"Error al actualizar peso: {error.message}")
        finally:
            cursor.close()

    def actualizar_estado_salud(self, id_etiqueta, nuevo_estado):
        try:
            cursor = self.connection.cursor()
            query = "UPDATE GANADO SET estado_salud = :1 WHERE id_etiqueta = :2"
            cursor.execute(query, (nuevo_estado, id_etiqueta))
            self.connection.commit()
        except oracledb.DatabaseError as e:
            error, = e.args
            self.connection.rollback()
            print(f"Error al actualizar estado de salud: {error.message}")
        finally:
            cursor.close()


            


# ----- Rutas -----
@app.route('/')
def index():
    db = get_db()
    if db:
        gestor = GestorGANADO(db)
        ganado = gestor.mostrar_GANADO()
        return render_template('index.html', ganado=ganado)
    flash("Error de conexión a la base de datos.")
    return redirect(url_for('login.html'))

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        # Implementar lógica de validación de usuario
    return render_template('login.html')

@app.route('/logout')
def logout():
    session.pop('user_id', None)
    flash("Sesión cerrada.")
    return redirect(url_for('login.html'))


@app.route('/agregar', methods=['POST'])
def agregar():
    id_etiqueta = request.form['id_etiqueta']
    nombre = request.form['nombre']
    raza = request.form['raza']
    peso = request.form['peso']
    estado_salud = request.form['estado_salud']
    db = get_db()
    gestor = GestorGANADO(db)
    gestor.agregar_GANADO(id_etiqueta, nombre, raza, peso, estado_salud)
    flash("Ganado agregado exitosamente.")
    return redirect(url_for('index'))

@app.route('/eliminar/<id_etiqueta>', methods=['POST'])
def eliminar(id_etiqueta):
    db = get_db()
    gestor = GestorGANADO(db)
    gestor.eliminar_GANADO(id_etiqueta)
    flash(f"Ganado con ID {id_etiqueta} eliminado.")
    return redirect(url_for('index'))

@app.route('/actualizar_peso', methods=['POST'])
def actualizar_peso():
    id_etiqueta = request.form['id_etiqueta']
    nuevo_peso = request.form['nuevo_peso']
    db = get_db()
    gestor = GestorGANADO(db)
    gestor.actualizar_peso(id_etiqueta, nuevo_peso)
    flash("Peso actualizado.")
    return redirect(url_for('index'))

@app.route('/actualizar_estado_salud', methods=['POST'])
def actualizar_estado_salud():
    id_etiqueta = request.form['id_etiqueta']
    nuevo_estado = request.form['nuevo_estado']
    db = get_db()
    gestor = GestorGANADO(db)
    gestor.actualizar_estado_salud(id_etiqueta, nuevo_estado)
    flash("Estado de salud actualizado.")
    return redirect(url_for('index'))

if __name__ == "__main__":
    app.run(debug=True)
