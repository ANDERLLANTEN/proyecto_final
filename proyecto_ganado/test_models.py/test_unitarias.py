# Importa el módulo unittest para crear pruebas automatizadas.
import unittest
# Importa la clase MagicMock de unittest.mock para crear objetos simulados (mock) durante las pruebas.
from unittest.mock import MagicMock
# Importa las clases GestorGANADO y Ganado desde el módulo models para probar la lógica de negocio.
from models import GestorGANADO, Ganado
# Clase que contiene las pruebas para la clase GestorGANADO, hereda de unittest.TestCase.
class TestGestorGANADO(unittest.TestCase):

    # Método que se ejecuta antes de cada prueba para configurar el entorno de prueba.
    def setUp(self):
        # Crea un objeto simulado (mock) para la conexión a la base de datos.
        self.mock_connection = MagicMock()
        # Crea una instancia de GestorGANADO con la conexión simulada.
        self.gestor = GestorGANADO(self.mock_connection)

    # Prueba que verifica que el método agregar_GANADO funcione correctamente.
    def test_agregar_ganado(self):
        # Llama al método agregar_GANADO con parámetros de prueba.
        self.gestor.agregar_GANADO(1, 'Vaca', 'Holstein', 500, 'Saludable')
        
        # Verifica que el método 'execute' haya sido llamado una vez en el cursor de la conexión.
        self.mock_connection.cursor.return_value.execute.assert_called_once()
        
        # Verifica que el método 'commit' haya sido llamado una vez, lo que indica que la transacción fue confirmada.
        self.mock_connection.commit.assert_called_once()

# Bloque principal que ejecuta las pruebas si el archivo es ejecutado directamente.
if __name__ == '__main__':
    unittest.main()


#python test_models.py/test_units.py
