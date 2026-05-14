# Pre-Entrega: Automatización SauceDemo
**Alumno:** Nicolás Volpe Bonola

## Descripción
Este proyecto automatiza un flujo básico de compra en la web de SauceDemo utilizando **Python**, **Selenium** y **Pytest**.

## Casos de Prueba
1. **Login:** Verifica el acceso con credenciales válidas.
2. **Catálogo:** Valida que el usuario sea redirigido a la pantalla de productos.
3. **Carrito:** Verifica que al añadir un producto, el contador del carrito se actualice correctamente.

## Requisitos
* Python 3.13+
* Chrome Browser & ChromeDriver
* Librerías: `selenium`, `pytest`, `pytest-html`

## Ejecución
Para correr los tests y generar el reporte:
```bash
py -m pytest tests/test_sauce.py --html=reports/reporte.html --self-contained-html
