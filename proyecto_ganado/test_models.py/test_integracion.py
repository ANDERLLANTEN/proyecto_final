# Importa el módulo unittest para crear pruebas automatizadas.
import unittest

# Importa las herramientas de unittest.mock para crear objetos simulados (mock) y controlarlos durante las pruebas.
from unittest.mock import patch, MagicMock

# Importa la aplicación Flask desde el archivo app.py para realizar las pruebas.
from app import app

# Clase que contiene las pruebas de integración de Flask, hereda de unittest.TestCase.
class TestFlaskIntegration(unittest.TestCase):

    # Método que se ejecuta antes de cada prueba para configurar el entorno de prueba.
    def setUp(self):
        # Configura la aplicación Flask para ejecutar en modo de prueba.
        app.config['TESTING'] = True
        # Crea un cliente de prueba para simular solicitudes HTTP a la aplicación.
        self.client = app.test_client()

    # Método de prueba que simula la conexión a la base de datos y prueba la ruta '/'.
    @patch('app.get_db')  # Parchea la función 'get_db' en el módulo 'app'.
    def test_index_route(self, mock_get_db):
        # Crea un objeto simulado para la base de datos que se utilizará en lugar de la conexión real.
        mock_get_db.return_value = MagicMock()
        
        # Realiza una solicitud GET a la ruta principal '/' de la aplicación.
        response = self.client.get('/')
        
        # Verifica que el código de estado HTTP de la respuesta sea 200 (OK).
        self.assertEqual(response.status_code, 200)

# Bloque principal que ejecuta las pruebas si el archivo es ejecutado directamente.
if __name__ == '__main__':
    unittest.main()


#python test_models.py/test_integration.py
