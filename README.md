# Proyecto de Pruebas Automatizadas con Playwright, Pytest y Allure

Este proyecto contiene un conjunto de pruebas automatizadas para validar funcionalidades de login, carrito de compras y la interacción con servicios web.

## Requisitos Previos

1. **Python 3.7+**: Asegúrate de tener instalado Python 3.7 o superior.
2. **Node.js**: Se necesita para instalar y utilizar Playwright.
3. **Allure**: Debes tener instalada la CLI de Allure para generar los reportes. Si no la tienes instalada, ejecuta el siguiente comando:
   ```bash
   npm install -g allure-commandline --save-dev

## Instanciar el proyecto

1. Clona este repositorio:

```bash
git clone https://github.com/tu_usuario/tu_proyecto.git
cd tu_proyecto
```
2. Crea un entorno virtual (opcional, pero recomendado):
```bash
python -m venv venv
source venv/bin/activate  # En Windows: venv\Scripts\activate
```
3. Instala las dependencias del proyecto 
```bash
pip install -r requirements.txt
```
4. Instala los navegadores necesarios para Playwright:
```bash
playwright install
```

## Ejecutar set

1. Ejecuta el set completo utilizando chrome y firefox
```bash
pytest
```
2. Ejecuta el set completo utilizando chrome 
```bash
pytest --browser-type chromium
```
3. Ejecuta el set completo utilizando firefox
```bash
pytest --browser-type firefox
```
4. Ejecuta el set en modo debug
```bash
PWDEBUG=1 pytest
```