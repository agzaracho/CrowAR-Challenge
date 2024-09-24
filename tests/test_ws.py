import requests
import pytest
from allure_commons.types import AttachmentType
import allure

def api_request(endpoint, method="GET", validation_key=None):
    """
    Función genérica para interactuar con servicios web.
    
    Parámetros:
    - endpoint: URL del servicio web.
    - method: Método HTTP a utilizar (GET por defecto).
    - validation_key: Clave opcional para validar que exista en la respuesta JSON.
    """
    
    # Hacer la solicitud HTTP según el método especificado
    if method == "GET":
        response = requests.get(endpoint)
    elif method == "POST":
        response = requests.post(endpoint)
    # Puedes agregar más métodos como PUT, DELETE, etc.
    else:
        raise ValueError(f"Método HTTP no soportado: {method}")

    # Adjuntar el cuerpo de la respuesta al reporte de Allure
    allure.attach(response.text, name="API Response", attachment_type=AttachmentType.JSON)

    # Verificar que el estado de la respuesta sea 200 (éxito)
    assert response.status_code == 200, f"Error en la solicitud, código de estado: {response.status_code}"

    # Si se proporciona una clave de validación, verificamos que esté en la respuesta JSON
    if validation_key:
        response_data = response.json()
        assert validation_key in response_data, f"La clave '{validation_key}' no está presente en la respuesta"

# Caso de prueba específico para Mercado Libre usando la función genérica
@pytest.mark.web
@allure.title("Validación de respuesta a Servicio Web")
@allure.description("Este test verifica la correcta conexión y respuesta de un  Servicio Web")
@allure.tag("ws", "medium")
def test_mercadolibre_departments():
    endpoint = "https://www.mercadolibre.com.ar/menu/departments"
    method = "GET"
    validation_key = "departments"
    api_request(endpoint, method, validation_key=validation_key)
