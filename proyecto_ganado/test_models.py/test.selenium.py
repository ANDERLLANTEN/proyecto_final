# Importa el módulo selenium.webdriver para interactuar con un navegador web y realizar pruebas automatizadas.
from selenium import webdriver

# Importa el módulo By para localizar elementos en la página web mediante diferentes métodos de búsqueda (por ejemplo, nombre, id).
from selenium.webdriver.common.by import By

# Importa el módulo unittest para crear pruebas automatizadas.
import unittest

# Clase que contiene las pruebas de extremo a extremo (E2E), hereda de unittest.TestCase.
class TestE2E(unittest.TestCase):

    # Método que se ejecuta antes de cada prueba para configurar el entorno de prueba.
    def setUp(self):
        # Inicializa un nuevo navegador Chrome. Este será usado para interactuar con la aplicación web.
        self.driver = webdriver.Chrome()

    # Método de prueba para agregar un ganado en la aplicación web.
    def test_add_ganado(self):
        # Accede a la URL local donde se está ejecutando la aplicación Flask.
        self.driver.get('http://localhost:5000')
        
        # Encuentra el campo de entrada por el nombre 'id_etiqueta' y llena el campo con el valor '1'.
        self.driver.find_element(By.NAME, 'id_etiqueta').send_keys('1')
        
        # Encuentra el campo de entrada por el nombre 'nombre' y llena el campo con el valor 'Vaca'.
        self.driver.find_element(By.NAME, 'nombre').send_keys('Vaca')
        
        # Encuentra el campo de entrada por el nombre 'raza' y llena el campo con el valor 'Holstein'.
        self.driver.find_element(By.NAME, 'raza').send_keys('Holstein')
        
        # Encuentra el campo de entrada por el nombre 'peso' y llena el campo con el valor '500'.
        self.driver.find_element(By.NAME, 'peso').send_keys('500')
        
        # Encuentra el campo de entrada por el nombre 'estado_salud' y llena el campo con el valor 'Saludable'.
        self.driver.find_element(By.NAME, 'estado_salud').send_keys('Saludable')
        
        # Encuentra el botón con el ID 'submit-button' y simula un clic en él para enviar el formulario.
        self.driver.find_element(By.ID, 'submit-button').click()
        
        # Verifica que la página fuente contenga el mensaje 'Ganado agregado exitosamente', lo que indica que el ganado fue agregado.
        self.assertIn('Ganado agregado exitosamente', self.driver.page_source)

    # Método que se ejecuta después de cada prueba para limpiar y cerrar el entorno de prueba.
    def tearDown(self):
        # Cierra el navegador después de cada prueba.
        self.driver.quit()

# Bloque principal que ejecuta las pruebas si el archivo es ejecutado directamente.
if __name__ == '__main__':
    unittest.main()


#python test_models.py/test_e2e.py

#En el contexto de las pruebas 
# de software, Selenium se usa principalmente 
# para realizar pruebas de extremo a extremo (E2E). 
# Estas pruebas verifican que una aplicación web funcione 
# correctamente desde el punto de vista del usuario final, 
# simulando interacciones como hacer clic en botones, completar formularios, 
# navegar entre páginas y verificar que los resultados sean correctos.