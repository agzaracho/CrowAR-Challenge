import os
import pytest
from playwright.sync_api import sync_playwright
import allure

def pytest_addoption(parser):
    parser.addoption(
        "--report", action="store", default="true", help="Genera el reporte html con Allure y lo abre al finalizar el set"
    )

@pytest.fixture(params=["chromium", "firefox"])
def browser_type_launch(request):
    with sync_playwright() as p:
        browser_type = request.param

        # Agregar el navegador como una etiqueta dinámica en Allure
        allure.dynamic.label("browser", browser_type)

        # Lanzar el navegador con slow_mo para todos los navegadores
        browser = p[browser_type].launch(slow_mo=500)
        yield browser
        browser.close()

@pytest.hookimpl(tryfirst=True)
def pytest_sessionfinish(session, exitstatus):
    report_option = session.config.getoption("--report")
    pwdebug = os.getenv('PWDEBUG')

    # No generar el reporte si PWDEBUG está activado o si --report=false
    if report_option == "true" and pwdebug != "1":
        # Generar el reporte de Allure al finalizar las pruebas
        os.system('allure generate --clean ./allure-results -o ./allure-report')
        
        # Abrir el reporte de Allure en español
        os.system('allure serve allure-results --lang es')
