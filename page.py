import time
from selenium import webdriver
from LoginPage import LoginPage  # Asegúrate de que LoginPage esté en el mismo directorio o en el path adecuado

class LoginTest:
    """
    La clase LoginTest agrupa las pruebas automatizadas para verificar el comportamiento de la página de inicio de sesión.

    Atributos:
    - driver: El controlador del navegador (WebDriver) que permite interactuar con la página web.
    """

    def __init__(self, driver):
        """
        Constructor que inicializa el controlador del navegador para las pruebas.
        
        Parámetros:
        - driver: El controlador del navegador (WebDriver).
        """
        self.driver = driver

    def test_valid_login(self):
        """
        Realiza una prueba de inicio de sesión con credenciales válidas.
        
        Pasos:
        - Navega a la página de inicio de sesión.
        - Introduce credenciales válidas (usuario: "tomsmith", contraseña: "SuperSecretPassword!").
        - Haz clic en el botón de inicio de sesión.
        - Verifica que el mensaje de éxito aparezca en la página después del inicio de sesión.
        """
        # Navega a la página de inicio de sesión
        self.driver.get("http://the-internet.herokuapp.com/login")
        
        # Crea una instancia de LoginPage para interactuar con los elementos de la página
        login_page = LoginPage(self.driver)

        # Introduce credenciales correctas
        login_page.enter_username("tomsmith")
        login_page.enter_password("SuperSecretPassword!")
        login_page.click_login_button()

        # Verifica el mensaje de éxito después del inicio de sesión
        flash_message = login_page.get_flash_message()
        assert "You logged into a secure area!" in flash_message, "Error: Inicio de sesión fallido con credenciales válidas."
        print("Prueba de login válida exitosa.")

    def test_invalid_login(self):
        """
        Realiza una prueba de inicio de sesión con credenciales inválidas.
        
        Pasos:
        - Navega a la página de inicio de sesión.
        - Introduce credenciales incorrectas (usuario: "invalid_user", contraseña: "invalid_password").
        - Haz clic en el botón de inicio de sesión.
        - Verifica que el mensaje de error aparezca en la página después del intento fallido de inicio de sesión.
        """
        # Navega a la página de inicio de sesión
        self.driver.get("http://the-internet.herokuapp.com/login")
        
        # Crea una instancia de LoginPage para interactuar con los elementos de la página
        login_page = LoginPage(self.driver)

        # Introduce credenciales incorrectas
        login_page.enter_username("invalid_user")
        login_page.enter_password("invalid_password")
        login_page.click_login_button()

        # Verifica el mensaje de error después del inicio de sesión fallido
        flash_message = login_page.get_flash_message()
        assert "Your username is invalid!" in flash_message, "Error: No se mostró el mensaje de error esperado para credenciales inválidas."
        print("Prueba de login inválida exitosa.")

# Ejecutando las pruebas
if __name__ == "__main__":
    """
    Este bloque se ejecuta solo si el script se ejecuta directamente (no si se importa como módulo).

    Pasos:
    - Crea una instancia del controlador Chrome.
    - Crea una instancia de LoginTest para ejecutar las pruebas.
    - Ejecuta las pruebas de inicio de sesión con credenciales válidas e inválidas.
    - Pausa brevemente entre las pruebas para ver los resultados.
    - Finalmente, cierra el navegador.
    """
    # Crea una instancia del controlador Chrome (asegúrate de tener ChromeDriver instalado y configurado en tu PATH)
    driver = webdriver.Chrome()

    # Crea una instancia de LoginTest con el controlador del navegador
    login_test = LoginTest(driver)

    try:
        # Ejecuta la prueba con un login válido
        login_test.test_valid_login()
        time.sleep(2)  # Pausa para ver los resultados

        # Ejecuta la prueba con un login inválido
        login_test.test_invalid_login()
        time.sleep(2)

    finally:
        # Cierra el navegador después de las pruebas
        driver.quit()
 