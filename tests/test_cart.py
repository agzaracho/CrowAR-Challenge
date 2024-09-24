import pytest
import allure

URL = "https://www.saucedemo.com/"

@pytest.mark.cart
@allure.title("Agregar producto al carrito")
@allure.description("Este test verifica que se pueda agregar un producto al carrito y valida que el producto agregado sea el correcto.")
@allure.tag("cart", "critical")
def test_add_product_to_cart(browser_type_launch):
    
    browser = browser_type_launch
    context = browser.new_context(record_video_dir="videos/")
    page = context.new_page()

    # Ir a la página e iniciar sesión
    page.goto(URL)
    page.fill("input[name='user-name']", "standard_user")
    page.fill("input[name='password']", "secret_sauce")
    page.click("input[name='login-button']")

    # Validar la cantidad de productos en el carrito antes de agregar
    initial_cart_count = page.locator(".shopping_cart_badge").inner_text() if page.locator(".shopping_cart_badge").count() > 0 else "0"
    assert initial_cart_count == "0", f"Se esperaba 0 productos en el carrito, pero se encontró {initial_cart_count}"

    # Agregar producto al carrito
    page.click("button[data-test='add-to-cart-sauce-labs-backpack']")

    # Validar la cantidad de productos en el carrito después de agregar
    updated_cart_count = page.locator(".shopping_cart_badge").inner_text()
    assert updated_cart_count == "1", f"Se esperaba 1 producto en el carrito, pero se encontró {updated_cart_count}"

    # Ingresar al carrito y validar que el producto agregado sea correcto
    page.click(".shopping_cart_link")
    product_in_cart = page.locator(".inventory_item_name").inner_text()
    assert product_in_cart == "Sauce Labs Backpack", f"Se esperaba 'Sauce Labs Backpack' en el carrito, pero se encontró {product_in_cart}"

    # Adjuntar el video al reporte de Allure
    video_path = page.video.path()
    page.close()
    context.close()

    allure.attach.file(video_path, name="Agregar producto al carrito", attachment_type=allure.attachment_type.MP4)


@pytest.mark.cart
@allure.title("Eliminar producto del carrito")
@allure.description("Este test verifica que se pueda eliminar un producto del carrito de compras.")
@allure.tag("cart", "medium")
def test_remove_product_from_cart(browser_type_launch):
    browser = browser_type_launch
    context = browser.new_context(record_video_dir="videos/")
    page = context.new_page()

    # Ejecutar la prueba
    page.goto(URL)
    page.fill("input[name='user-name']", "standard_user")
    page.fill("input[name='password']", "secret_sauce")
    page.click("input[name='login-button']")
    page.click("button[data-test='add-to-cart-sauce-labs-backpack']")
    page.click("button[data-test='remove-sauce-labs-backpack']")
    assert not page.locator(".shopping_cart_badge").is_visible()

    # Adjuntar el video al reporte de Allure
    video_path = page.video.path()
    page.close()
    context.close()

    allure.attach.file(video_path, name="Eliminar producto del carrito", attachment_type=allure.attachment_type.MP4)


@pytest.mark.cart
@allure.title("Agregar múltiples productos al carrito de compras")
@allure.description("Este test verifica que se puedan agregar múltiples productos al carrito de compras.")
@allure.tag("cart", "medium")
def test_add_multiple_products_to_cart(browser_type_launch):
    browser = browser_type_launch
    context = browser.new_context(record_video_dir="videos/")
    page = context.new_page()

    # Ejecutar la prueba
    page.goto(URL)
    page.fill("input[name='user-name']", "standard_user")
    page.fill("input[name='password']", "secret_sauce")
    page.click("input[name='login-button']")
    page.click("button[data-test='add-to-cart-sauce-labs-bike-light']")
    page.click("button[data-test='add-to-cart-sauce-labs-bolt-t-shirt']")
    
    # Verificar que se muestran dos productos en el carrito
    cart_badge = page.locator(".shopping_cart_badge")
    assert cart_badge.is_visible()
    assert cart_badge.inner_text() == "2"

    # Adjuntar el video al reporte de Allure
    video_path = page.video.path()
    page.close()
    context.close()

    allure.attach.file(video_path, name="Agregar múltiples productos al carrito de compras", attachment_type=allure.attachment_type.MP4)


@pytest.mark.cart
@allure.title("Agregar Sauce Labs Bolt T-Shirt al carrito")
@allure.description("Este test verifica que al agregar el producto Sauce Labs Bolt T-Shirt al carrito se obtiene un error.")
@allure.tag("cart", "critical")
def test_add_sauce_labs_bolt_tshirt_to_cart(browser_type_launch):
    browser = browser_type_launch
    context = browser.new_context(record_video_dir="videos/")
    page = context.new_page()

    # Ir a la página e intentar iniciar sesión con credenciales incorrectas
    page.goto(URL)
    page.fill("input[name='user-name']", "error_user")
    page.fill("input[name='password']", "secret_sauce")
    page.click("input[name='login-button']")

    # Verificar si el login fue exitoso
    login_error = page.locator("h3[data-test='error']").count()
    assert login_error == 0, "El usuario no pudo iniciar sesión correctamente."

    # Intentar agregar el producto Sauce Labs Bolt T-Shirt al carrito
    try:
        add_to_cart_button = page.locator("button[data-test='add-to-cart-sauce-labs-bolt-t-shirt']")
        assert add_to_cart_button.is_visible(), "El botón para agregar al carrito no está disponible."
        add_to_cart_button.click()

        updated_cart_count = page.locator(".shopping_cart_badge").inner_text() if page.locator(".shopping_cart_badge").count() > 0 else "0"
        assert updated_cart_count == "1", f"Se esperaba 1 producto en el carrito, pero se encontró {updated_cart_count}"

    except Exception as e:
        allure.attach(page.screenshot(), name="Error al agregar producto", attachment_type=allure.attachment_type.PNG)
        pytest.fail(f"No se pudo agregar el producto al carrito: {e}")

    finally:
        video_path = page.video.path()
        page.close()
        context.close()

        allure.attach.file(video_path, name="Agregar Sauce Labs Bolt T-Shirt al carrito", attachment_type=allure.attachment_type.MP4)
