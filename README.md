# Script DATACOM DM984-422

## 🖥️ Ejecutable incluido

Este proyecto contiene un ejecutable `.exe` llamado **DATACOM DM984-422**, ubicado en la carpeta `dist/`.

> ⚠️ **Ejecutá este archivo para configurar tu módem DATACOM DM984-422 de forma automática.**

---

## 🌐 Compatibilidad con Microsoft Edge

Este ejecutable funciona específicamente con la versión **135.0.3179.85** del navegador **Microsoft Edge**.

> ❌ Si tu versión de Edge es diferente, el programa **no funcionará correctamente**.

---

## ✅ ¿Qué hacer si no tenés esa versión?

Tenés **dos opciones** para usar el programa:

### Opción 1: Instalar la versión compatible de Edge

Podés buscar e instalar manualmente la versión **135.0.3179.85** de Microsoft Edge para asegurar el correcto funcionamiento del ejecutable.

### Opción 2: Reemplazar el driver y recompilar el ejecutable

Si preferís usar tu versión actual de Edge, podés reemplazar el driver incluido y volver a compilar el ejecutable. Seguí estos pasos:

1. **Eliminar los archivos anteriores**:
   - Borrá `msedgedriver.exe`.
   - Eliminá las carpetas `build/`, `dist/` y el archivo `.spec`.

2. **Descargar el driver correcto**:
   - Abrí Edge y accedé a `edge://settings/help` para ver tu versión exacta.
   - Ingresá a la [página oficial de WebDriver](https://developer.microsoft.com/en-us/microsoft-edge/tools/webdriver/).
   - Descargá el `.zip` correspondiente a tu versión.

3. **Agregar el nuevo driver al proyecto**:
   - Extraé el `.zip` y copiá `msedgedriver.exe` a la raíz del proyecto (junto al archivo `.py`).

4. **Recompilar el ejecutable**:
   - Abrí Visual Studio Code.
   - Abrí una terminal (`Ctrl + ñ` o desde el menú `Terminal > Nueva terminal`).
   - Ejecutá el siguiente comando:
     ```bash
     pyinstaller --onefile --add-binary "msedgedriver.exe;." "NOMBRE_DEL_SCRIPT.py"
     ```
     > Reemplazá `NOMBRE_DEL_SCRIPT.py` por el nombre real del archivo, por ejemplo: `DM984-422.py`.

5. **Ubicar el nuevo ejecutable**:
   - Se generarán nuevamente las carpetas `build/`, `dist/` y un archivo `.spec`.
   - Dentro de `dist/` encontrarás el nuevo ejecutable listo para usar.

> 💬 Si necesitás ayuda para actualizar el driver o compilar el ejecutable, no dudes en contactarme.

---

## ⬇️ Cómo descargar el proyecto

1. Hacé clic acá 👉 [Descargar ZIP](https://github.com/LuisMiraglio/Script-DATACOM-DM984-422/archive/refs/heads/main.zip)
2. Extraé el archivo ZIP en tu computadora.
3. Ingresá a la carpeta `dist/` y ejecutá **DATACOM_DM984-422.exe**.

> No es necesario instalar nada adicional. Solo asegurate de tener la versión correcta de Edge.

---

## 🛠️ Requisitos

- Sistema operativo: **Windows 10 o superior**
- Microsoft Edge versión **135.0.3179.85** (o compatible con el driver incluido)
- **Permisos de administrador** para aplicar la configuración del módem

---

## 🧰 Tecnologías utilizadas

- **Python 3**
- **Selenium**
- **PyInstaller**
