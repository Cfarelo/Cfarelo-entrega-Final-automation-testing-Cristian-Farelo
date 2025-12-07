from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from utils.helpers import URL, USERNAME, PASSWORD
import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__),'..')))

# Clase que encapsula funciones y credenciales para el login

class Login:
    
    IMPUT_USER_NAME =(By.NAME, "user-name")
    IMPUT_PASSWORD = (By.NAME, "password")
    LOGINBUTTON = (By.NAME, "login-button")
    
    def __init__(self, driver):
        self.driver = driver
        
    def open(self):
        self.driver.get(URL)
        #time.sleep (10)

    def login(self, username=USERNAME, password=PASSWORD):
        WebDriverWait(self.driver, 4).until(EC.element_to_be_clickable(self.IMPUT_USER_NAME)).send_keys(username)
        WebDriverWait(self.driver, 4).until(EC.element_to_be_clickable(self.IMPUT_PASSWORD)).send_keys(password)
        WebDriverWait(self.driver, 4).until(EC.element_to_be_clickable(self.LOGINBUTTON)).click()
    
   
        


        
