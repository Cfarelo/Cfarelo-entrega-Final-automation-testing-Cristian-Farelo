# Entrega final -automation-testing--Cristian-Farelo-.

Proposito del proyecto: realizar testeos de prueba automatizados en el sitio "https://www.saucedemo.com"

tecnologias utilizadas: python - pytest - selenium web driver - git - conceptos de html y css
Test de API Http requests: GET, POST, PUT, PATCH, DELETE utlizando diferentes origenes de datos (CSV y JSON).

herramientas auxiliares utilizadas
Markers, Fixtures, Captura de pantalla y Logging

para ejecucion de test especificos utilizamos los comandos:

pytest tests\test_carrito_carga_productos.py
pytest tests\test_catalogo.py
pytest tests\test_login.py
pytest tests\test_Navegar_a_pagina_carrito.py
pytest tests\test_remover_producto_carrito.py

en caso de querer ejecutar todos de forma detallada utilizamos:

pytest -v

para realizar un reporte html utilizamos el comando:

pytest -v --html=reporte.html
