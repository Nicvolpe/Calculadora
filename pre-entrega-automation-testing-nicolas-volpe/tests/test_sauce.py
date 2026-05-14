import pytest
from selenium.webdriver.common.by import By

def test_login_and_add_to_cart(driver):
    # 1. Abrir la página
    driver.get("https://www.saucedemo.com/")

    # 2. Login (standard_user / secret_sauce)
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()

    # 3. Validación: ¿Entramos al catálogo?
    assert "inventory.html" in driver.current_url
    header = driver.find_element(By.CLASS_NAME, "title").text
    assert header == "Products"

    # 4. Agregar la mochila (Backpack) al carrito
    driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()

    # 5. Validación: ¿El badge del carrito marca 1?
    badge = driver.find_element(By.CLASS_NAME, "shopping_cart_badge").text
    assert badge == "1"