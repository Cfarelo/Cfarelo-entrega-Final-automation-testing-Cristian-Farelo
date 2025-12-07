from page.login_Page import Login
from selenium.webdriver.common.by import By
import time
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

#test de login utilizando credenciales validas - verificacion de landing page y sus titulos principales

def test_login1(driver):
    nuevo_login = Login(driver)
    nuevo_login.open()
    nuevo_login.login()
    assert "https://www.saucedemo.com/inventory.html" in driver.current_url
    titulo  = driver.find_element(By.CSS_SELECTOR, 'div.header_label .app_logo').text
    assert titulo == 'Swag Labs'
    titulo  = driver.find_element(By.CSS_SELECTOR, 'div.header_secondary_container .title').text
    assert titulo == 'Products'
        
    driver.find_element(By.ID, "react-burger-menu-btn").click()

# Esperar a que el botón de logout esté presente y sea clickeable
    WebDriverWait(driver, 5).until(EC.element_to_be_clickable((By.ID, "logout_sidebar_link"))).click()

    time.sleep(3)
# Esperar a que la página de inicio de sesión se cargue
    WebDriverWait(driver, 10).until(EC.url_contains("https://www.saucedemo.com/"))



    

    time.sleep(5)