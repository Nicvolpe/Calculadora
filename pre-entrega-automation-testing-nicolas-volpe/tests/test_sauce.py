import pytest
from selenium.webdriver.common.by import By

def test_full_saucedemo_flow(driver):
    # 1. Login
    driver.get("https://www.saucedemo.com/")
    driver.find_element(By.ID, "user-name").send_keys("standard_user")
    driver.find_element(By.ID, "password").send_keys("secret_sauce")
    driver.find_element(By.ID, "login-button").click()

    # 2. Validación de Catálogo (Puntos 2.18 y 2.19 del PDF)
    assert "inventory.html" in driver.current_url
    # Verificar presencia de productos y filtros
    items = driver.find_elements(By.CLASS_NAME, "inventory_item")
    assert len(items) > 0  # Comprobar que hay productos visibles [cite: 218]
    assert driver.find_element(By.CLASS_NAME, "product_sort_container").is_displayed() # Filtros [cite: 219]
    assert driver.find_element(By.ID, "react-burger-menu-btn").is_displayed() # Menú [cite: 219]

    # 3. Interacción con Productos (Punto 2.22 y 2.23)
    driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack").click()
    badge = driver.find_element(By.CLASS_NAME, "shopping_cart_badge").text
    assert badge == "1"

    # 4. Navegación al carrito y verificación (Punto 2.24 y 2.25)
    driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
    assert "cart.html" in driver.current_url
    producto_en_carrito = driver.find_element(By.CLASS_NAME, "inventory_item_name").text
    assert "Sauce Labs Backpack" in producto_en_carrito # Comprobar producto en carrito [cite: 225]
    
    print("Test OK: Flujo completo verificado según consigna") # Requisito de Matías