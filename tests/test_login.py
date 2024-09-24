import pytest
import allure

# URL de la aplicación
URL = "https://www.saucedemo.com/"

@pytest.mark.login
@allure.title("Inicio de sesión válido")
@allure.description("Este test verifica que un usuario válido puede iniciar sesión correctamente.")
@allure.tag("login", "critical")
def test_valid_login(browser_type_launch):
    
    browser = browser_type_launch
    context = browser.new_context(record_video_dir="videos/")
    page = context.new_page()

    # Ejecutar la prueba
    page.goto(URL)
    page.fill("input[name='user-name']", "standard_user")
    page.fill("input[name='password']", "secret_sauce")
    page.click("input[name='login-button']")
    assert page.url == "https://www.saucedemo.com/inventory.html"

    # Cerrar página y contexto
    video_path = page.video.path()
    page.close()
    context.close()

    # Adjuntar el video al reporte Allure
    allure.attach.file(video_path, name="Inicio de sesión válido", attachment_type=allure.attachment_type.MP4)


@pytest.mark.login
@allure.title("Inicio de sesión inválido")
@allure.description("Este test verifica que un intento de inicio de sesión con credenciales incorrectas muestra el mensaje de error adecuado.")
@allure.tag("login", "medium")
def test_invalid_login(browser_type_launch):
    
    browser = browser_type_launch
    context = browser.new_context(record_video_dir="videos/")
    page = context.new_page()

    # Ejecutar la prueba
    page.goto(URL)
    page.fill("input[name='user-name']", "invalid_user")
    page.fill("input[name='password']", "wrong_password")
    page.click("input[name='login-button']")
    error_message = page.locator("h3[data-test='error']").inner_text()
    assert "Username and password do not match" in error_message

    # Cerrar página y contexto
    video_path = page.video.path()
    page.close()
    context.close()

    # Adjuntar el video al reporte Allure
    allure.attach.file(video_path, name="Inicio de sesión con credenciales incorrectas", attachment_type=allure.attachment_type.MP4)


@pytest.mark.login
@allure.title("Inicio de sesión sin credenciales")
@allure.description("Este test verifica que el sistema muestra un mensaje de error cuando se intenta iniciar sesión sin ingresar credenciales.")
@allure.tag("login", "low")
def test_empty_login(browser_type_launch):
    
    browser = browser_type_launch
    context = browser.new_context(record_video_dir="videos/")
    page = context.new_page()

    # Ejecutar la prueba
    page.goto(URL)
    page.click("input[name='login-button']")
    error_message = page.locator("h3[data-test='error']").inner_text()
    assert "Username is required" in error_message

    # Cerrar página y contexto
    video_path = page.video.path()
    page.close()
    context.close()

    # Adjuntar el video al reporte Allure
    allure.attach.file(video_path, name="Inicio de sesión sin credenciales", attachment_type=allure.attachment_type.MP4)
