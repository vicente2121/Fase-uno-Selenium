# aca es la biblioteca selenium
from selenium import webdriver
# este propociona la simulacion de acciones sobre la web
from selenium.webdriver.common.keys import Keys
# esta linea es para identificar ID,name,class o atributos para la web
from selenium.webdriver.common.by import By
# tomar tiempo para python 
import time

# aca va la ruta donde generamos la descarga del driver en este caso para microsoft edge
Ruta='C:/Users/Downloads/msedgedriver.exe'

driver = webdriver.Edge(Ruta)

driver.get('https://acme-test.uipath.com/login')

time.sleep(5)
# En este caso estamos buscando el correo
input_usuario=driver.find_element(By.NAME,"email")
#Aca damos clic dodne realizaremos el clic al input
input_usuario.click()
#Es enviar una palabra al input 
input_usuario.send_keys("USUARIO ACA VA ESCRITO")

time.sleep(5)

driver.quit()



