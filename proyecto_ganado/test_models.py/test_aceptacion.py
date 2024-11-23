# Importa el módulo unittest para crear pruebas automatizadas.
import unittest

# Importa la aplicación Flask desde el archivo app.py para realizar las pruebas.
from app import app

# Clase que contiene las pruebas de aceptación, hereda de unittest.TestCase.
class TestAcceptance(unittest.TestCase):

    # Método que se ejecuta antes de cada prueba para configurar el entorno de prueba.
    def setUp(self):
        # Configura la aplicación Flask para ejecutar en modo de prueba.
        app.config['TESTING'] = True
        # Crea un cliente de prueba para simular solicitudes HTTP a la aplicación.
        self.client = app.test_client()

    # Prueba de aceptación para verificar que la página de inicio de sesión funcione correctamente.
    def test_login_page(self):
        # Realiza una solicitud GET a la ruta '/login'.
        response = self.client.get('/login')
        # Verifica que el código de estado HTTP sea 200 (OK).
        self.assertEqual(response.status_code, 200)
        # Verifica que el contenido de la página incluya la palabra "Login".
        self.assertIn(b'Login', response.data)

# Bloque principal que ejecuta las pruebas si el archivo es ejecutado directamente.
if __name__ == '__main__':
    unittest.main()
    


#python test_models.py/test_acceptance.py

# si pasan todas las pruebas
#.
#----------------------------------------------------------------------
#Ran 1 test in 0.XXXs

#OK
