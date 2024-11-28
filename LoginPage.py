from selenium.webdriver.common.by import By

class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.username_input = (By.ID, "username")
        self.password_input = (By.ID, "password")
        self.login_button = (By.CSS_SELECTOR, "button[type='submit']")
        self.flash_message = (By.ID, "flash")

    def enter_username(self, username):
        """Introduce el nombre de usuario en el campo correspondiente."""
        self.driver.find_element(*self.username_input).send_keys(username)

    def enter_password(self, password):
        """Introduce la contraseña en el campo correspondiente."""
        self.driver.find_element(*self.password_input).send_keys(password)

    def click_login_button(self):
        """Haz clic en el botón de inicio de sesión."""
        self.driver.find_element(*self.login_button).click()

    def get_flash_message(self):
        """Obtiene el mensaje de flash (éxito o error)."""
        return self.driver.find_element(*self.flash_message).text
