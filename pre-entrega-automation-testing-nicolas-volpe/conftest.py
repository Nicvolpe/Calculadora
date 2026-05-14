import pytest
from selenium import webdriver

@pytest.fixture(scope="function")
def driver():
    # Setup: Se abre el navegador antes de cada test
    driver = webdriver.Chrome() 
    driver.maximize_window()
    driver.implicitly_wait(10) # Espera hasta 10 seg si un elemento no aparece
    yield driver
    # Teardown: Se cierra al terminar
    driver.quit()