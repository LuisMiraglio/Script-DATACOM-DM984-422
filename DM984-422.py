import sys
import os
import subprocess
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.edge.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException, NoSuchFrameException, ElementNotInteractableException
import time
import tempfile

from datetime import datetime

# Determinar la ruta base
if getattr(sys, 'frozen', False):
    base_path = sys._MEIPASS
else:
    base_path = os.path.dirname(__file__)

# Solicitar al usuario el nombre de red y la contraseña
user_ssid = input("Ingrese el SSID: ")
wpa_pass = input("Ingrese la contraseña: ")

# Obtiene la ruta del driver en base a la ruta determinada
driver_path = os.path.join(base_path, "msedgedriver.exe")
service = Service(driver_path)
options = webdriver.EdgeOptions()
driver = webdriver.Edge(service=service, options=options)

try:
    driver.get("http://support:support@192.168.0.1")

    # Esperar a que el frame "menufrm" esté presente
    try:
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.NAME, "menufrm"))
        )
        driver.switch_to.frame("menufrm")
    except TimeoutException:
        driver.quit()
        exit()

    # Buscar y hacer clic en "Advanced Setup"
    try:
        advanced_setup_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//a[contains(text(), 'Advanced Setup')]"))
        )
        advanced_setup_button.click()
    except TimeoutException:
        driver.quit()
        exit()
    
    driver.switch_to.default_content()  # Volver al contenido principal
    
    # Cambiar al frame que contiene el botón "Add"
    try:
        driver.switch_to.frame("basefrm")
    except NoSuchElementException:
        driver.quit()
        exit()

    # Esperar a que el botón "Add" esté presente y visible
    try:
        add_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//input[@type='button' and @value='Add']"))
        )
        add_button.click()
    except TimeoutException:
        driver.quit()
        exit()

    # Esperar a que el botón "Apply/Save" esté presente y visible
    try:
        apply_save_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//input[@type='button' and @value='Apply/Save']"))
        )
        apply_save_button.click()
    except TimeoutException:
        driver.quit()
        exit()

    # Cambiar al frame que contiene el menú
    try:
        driver.switch_to.default_content()  # Volver al contenido principal
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.NAME, "menufrm"))
        )
        driver.switch_to.frame("menufrm")
    except TimeoutException:
        driver.quit()
        exit()

    # Buscar y hacer clic en "WAN Service"
    try:
        wan_service_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//a[@class='menuLink' and @href='wancfg.cmd']"))
        )
        wan_service_button.click()
    except TimeoutException:
        driver.quit()
        exit()
    
    driver.switch_to.default_content()  # Volver al contenido principal

    # Cambiar al frame que contiene el botón "Add" en WAN Service
    try:
        driver.switch_to.frame("basefrm")
    except NoSuchFrameException:
        driver.quit()
        exit()

    # Esperar a que el botón "Add" esté presente y visible en WAN Service
    try:
        add_button_wan = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//input[@type='button' and @value='Add']"))
        )
        add_button_wan.click()
    except TimeoutException:
        driver.quit()
        exit()

    # Esperar a que la opción "IP over Ethernet" esté presente y visible
    try:
        ip_over_ethernet_option = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//input[@type='radio' and @name='ntwkPrtcl' and @onclick='prtclClick()'][following-sibling::text()[contains(., 'IP over Ethernet')]]"))
        )
        ip_over_ethernet_option.click()
    except TimeoutException:
        driver.quit()
        exit()

    # Ingresar el número 5 en el campo "Enter 802.1P Priority [0-7]"
    try:
        priority_field = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//input[@type='text' and @name='vlanMuxPr']"))
        )
        priority_field.clear()
        priority_field.send_keys("5")
    except TimeoutException:
        driver.quit()
        exit()

    # Ingresar el número 500 en el campo "Enter 802.1Q VLAN ID [0-4094]"
    try:
        vlan_id_field = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//input[@type='text' and @name='vlanMuxId']"))
        )
        vlan_id_field.clear()
        vlan_id_field.send_keys("500")
    except TimeoutException:
        driver.quit()
        exit()

    # Hacer clic en el botón "Next"
    try:
        next_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//input[@type='button' and @value='Next']"))
        )
        next_button.click()
    except TimeoutException:
        driver.quit()
        exit()
    time.sleep(5)

    # Hacer clic en el botón "Next" en la página "WAN IP Settings"
    try:
        next_button_wan_ip = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//input[@type='button' and @value='Next']"))
        )
        next_button_wan_ip.click()
    except TimeoutException:
        driver.quit()
        exit()

    # Seleccionar la casilla "Enable NAT"
    try:
        enable_nat_checkbox = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//input[@type='checkbox' and @name='enblNat' and @onclick='natClick(this)']"))
        )
        enable_nat_checkbox.click()
    except TimeoutException:
        driver.quit()
        exit()

    # Hacer clic en el botón "Next" en la página "Network Address Translation Settings"
    try:
        next_button_nat = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//input[@type='button' and @value='Next']"))
        )
        next_button_nat.click()
    except TimeoutException:
        driver.quit()
        exit()
    time.sleep(5)

    # Hacer clic en el botón "Next" en la página "Routing -- Default Gateway"
    try:
        next_button_routing = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//input[@type='button' and @value='Next']"))
        )
        next_button_routing.click()
    except TimeoutException:
        driver.quit()
        exit()
    time.sleep(5)

    # Hacer clic en el botón "Next" en la página "DNS Server Configuration"
    try:
        next_button_dns = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//input[@type='button' and @value='Next']"))
        )
        next_button_dns.click()
    except TimeoutException:
        driver.quit()
        exit()
    time.sleep(5)

    # Hacer clic en el botón "Apply/Save" en la página "WAN Setup - Summary"
    try:
        apply_save_button_summary = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//input[@type='button' and @name='btnSave' and @value='Apply/Save']"))
        )
        apply_save_button_summary.click()
    except TimeoutException:
        driver.quit()
        exit()
    time.sleep(5)

    # RECONEXIÓN A LA RED WIFI
    # Se utiliza siempre "WiFi_network" para reconectar, sin importar lo ingresado por el usuario
    wifi_reconnect = "WiFi_network"

    try:
        result = subprocess.run(
            ["netsh", "wlan", "connect", f"name={wifi_reconnect}"],
            capture_output=True, text=True, check=True
        )
    except subprocess.CalledProcessError as e:
        driver.quit()
        exit()

    # Esperar más tiempo para asegurarse de que la conexión se restablezca
    time.sleep(120)

    # Volver a ingresar a la IP con credenciales
    try:
        driver.get("http://support:support@192.168.0.1")

        # Esperar a que el frame "menufrm" esté presente
        WebDriverWait(driver, 30).until(
            EC.presence_of_element_located((By.NAME, "menufrm"))
        )
        driver.switch_to.frame("menufrm")
    except TimeoutException:
        driver.quit()
        exit()

    # Buscar y hacer clic en "Advanced Setup"
    try:
        advanced_setup_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//a[contains(text(), 'Advanced Setup')]"))
        )
        advanced_setup_button.click()
    except TimeoutException:
        driver.quit()
        exit()

    # Buscar y hacer clic en el enlace "Security"
    try:
        security_link = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//a[contains(text(), 'Security')]"))
        )
        security_link.click()
    except TimeoutException:
        driver.quit()
        exit()

    # Cambiar al frame que contiene el botón "Add" en la pantalla "Outgoing IP Filtering Setup"
    try:
        driver.switch_to.default_content()  # Volver al contenido principal
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.NAME, "basefrm"))
        )
        driver.switch_to.frame("basefrm")
    except TimeoutException:
        driver.quit()
        exit()

    # Esperar a que el botón "Add" esté presente y visible en la pantalla "Outgoing IP Filtering Setup"
    try:
        add_button_outgoing_ip = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//input[@type='button' and @value='Add']"))
        )
        add_button_outgoing_ip.click()
    except TimeoutException:
        driver.quit()
        exit()

    # Esperar a que el campo "Filter Name" esté presente y visible
    try:
        filter_name_field = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.NAME, "txtfltname"))
        )
        filter_name_field.clear()
        filter_name_field.send_keys("ping")
    except TimeoutException:
        driver.quit()
        exit()

    # Seleccionar la opción "ICMP" en el menú desplegable "Protocol"
    try:
        protocol_dropdown = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.NAME, "protocol"))
        )
        protocol_dropdown.click()
        protocol_option_icmp = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//select[@name='protocol']/option[@value='3']"))
        )
        protocol_option_icmp.click()
    except TimeoutException:
        driver.quit()
        exit()

    # Hacer clic en "Apply/Save"
    try:
        apply_save_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//input[@type='button' and @value='Apply/Save']"))
        )
        apply_save_button.click()
    except TimeoutException:
        driver.quit()
        exit()

    # Esperar a que el botón "Add" esté presente y visible en la pantalla "Outgoing IP Filtering Setup"
    try:
        add_button_outgoing_ip = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//input[@type='button' and @value='Add']"))
        )
        add_button_outgoing_ip.click()
    except TimeoutException:
        driver.quit()
        exit()

    # Esperar a que el campo "Filter Name" esté presente y visible
    try:
        filter_name_field = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.NAME, "txtfltname"))
        )
        filter_name_field.clear()
        filter_name_field.send_keys("web")
    except TimeoutException:
        driver.quit()
        exit()

    # Seleccionar la opción "TCP/UDP" en el menú desplegable "Protocol"
    try:
        protocol_dropdown = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.NAME, "protocol"))
        )
        protocol_dropdown.click()
        protocol_option_tcp_udp = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//select[@name='protocol']/option[@value='0']"))
        )
        protocol_option_tcp_udp.click()
    except TimeoutException:
        driver.quit()
        exit()

    # Ingresar "190.13.88.0/21" en el campo "Source IP address[/prefix length]"
    try:
        source_ip_field = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.NAME, "srcaddr"))
        )
        source_ip_field.clear()
        source_ip_field.send_keys("190.13.88.0/21")
    except TimeoutException:
        driver.quit()
        exit()

    # Ingresar "80" en el campo "Destination Port (port or port:port)"
    try:
        destination_port_field = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.NAME, "dstport"))
        )
        destination_port_field.clear()
        destination_port_field.send_keys("80")
    except TimeoutException:
        driver.quit()
        exit()

    # Hacer clic en "Apply/Save"
    try:
        apply_save_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//input[@type='button' and @value='Apply/Save']"))
        )
        apply_save_button.click()
    except TimeoutException:
        driver.quit()
        exit()

    # Cambiar al frame que contiene el menú
    try:
        driver.switch_to.default_content()  # Volver al contenido principal
        WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.NAME, "menufrm"))
        )
        driver.switch_to.frame("menufrm")
    except TimeoutException:
        driver.quit()
        exit()

    # Buscar y hacer clic en "Wireless"
    try:
        wireless_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//a[contains(text(), 'Wireless')]"))
        )
        wireless_button.click()
    except TimeoutException:
        driver.quit()
        exit()

    driver.switch_to.default_content()  # Volver al contenido principal

    # Cambiar al frame que contiene el campo "SSID"
    try:
        driver.switch_to.frame("basefrm")
    except NoSuchFrameException:
        driver.quit()
        exit()

    # Esperar a que el campo "SSID" esté presente y visible, e ingresar el valor ingresado por el usuario
    try:
        ssid_field = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//input[@type='text' and @name='wlSsid']"))
        )
        ssid_field.clear()
        ssid_field.send_keys(user_ssid)
        
        # Verificar que el valor ingresado en el campo SSID sea el mismo que user_ssid
        entered_value = ssid_field.get_attribute("value")
        if (entered_value == user_ssid):
            pass
        else:
            driver.quit()
            exit()
    except TimeoutException:
        driver.quit()
        exit()

    # Seleccionar el país "ARGENTINA" en el menú desplegable "Country"
    try:
        country_dropdown = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, "//select[@name='wlCountry']"))
        )
        country_dropdown.click()
        country_option_argentina = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//select[@name='wlCountry']/option[@value='AR']"))
        )
        country_option_argentina.click()
    except TimeoutException:
        driver.quit()
        exit()

    # Hacer clic en "Apply/Save"
    try:
        apply_save_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//input[@type='button' and @value='Apply/Save']"))
        )
        apply_save_button.click()
    except TimeoutException:
        driver.quit()
        exit()

    # **** NUEVO PASO: Reconectar a la nueva red ****
    # Generar dinámicamente un perfil para la red abierta con SSID igual a user_ssid
    profile_xml = f"""<?xml version="1.0"?>
<WLANProfile xmlns="http://www.microsoft.com/networking/WLAN/profile/v1">
    <name>{user_ssid}</name>
    <SSIDConfig>
        <SSID>
            <name>{user_ssid}</name>
        </SSID>
        <nonBroadcast>false</nonBroadcast>
    </SSIDConfig>
    <connectionType>ESS</connectionType>
    <connectionMode>auto</connectionMode>
    <MSM>
        <security>
            <authEncryption>
                <authentication>open</authentication>
                <encryption>none</encryption>
                <useOneX>false</useOneX>
            </authEncryption>
        </security>
    </MSM>
</WLANProfile>
"""
    # Guardar el perfil en un archivo temporal usando encoding UTF-8
    temp_dir = tempfile.gettempdir()
    profile_path = os.path.join(temp_dir, "temp_profile.xml")
    with open(profile_path, "w", encoding="utf-8") as f:
        f.write(profile_xml)

    # Agregar el perfil a Windows
    try:
        result_add = subprocess.run(
            ["netsh", "wlan", "add", "profile", f"filename={profile_path}"],
            capture_output=True, text=True, check=True
        )
    except subprocess.CalledProcessError as e:
        driver.quit()
        exit()
    time.sleep(30)

    # Conectar a la nueva red usando el perfil agregado
    try:
        result_connect = subprocess.run(
            ["netsh", "wlan", "connect", f"name={user_ssid}"],
            capture_output=True, text=True, check=True
        )
    except subprocess.CalledProcessError as e:
        driver.quit()
        exit()

    # Eliminar el archivo temporal del perfil
    os.remove(profile_path)

    # Esperar tiempo para que la nueva conexión se estabilice
    time.sleep(30)

    # Verificar la conexión actual usando netsh
    try:
        result_status = subprocess.run(
            ["netsh", "wlan", "show", "interfaces"],
            capture_output=True, text=True, check=True
        )
        if user_ssid in result_status.stdout:
            pass
        else:
            driver.quit()
            exit()
    except subprocess.CalledProcessError as e:
        driver.quit()
        exit()

    # --- NUEVO BLOQUE: Ir directo a Security en la nueva red ---
    # Esperar tiempo adicional para que la interfaz del módem se estabilice en la nueva red
    # Asumimos que la interfaz ya se cargó; forzamos el cambio al contenido principal y buscamos el frame 'menufrm'
    try:
        driver.switch_to.default_content()
        WebDriverWait(driver, 60).until(
            EC.presence_of_element_located((By.NAME, "menufrm"))
        )
        driver.switch_to.frame("menufrm")
    except TimeoutException:
        driver.quit()
        exit()

    # Buscar y hacer clic en el enlace "Security"
    try:
        # Usamos un XPATH basado en el href, ya que es estable:
        security_link = WebDriverWait(driver, 60).until(
            EC.element_to_be_clickable((By.XPATH, "//a[@href='wlsecurity.html']"))
        )
        security_link.click()
    except TimeoutException:
        driver.quit()
        exit()

    try:
        driver.switch_to.default_content()
        WebDriverWait(driver, 60).until(
            EC.presence_of_element_located((By.NAME, "basefrm"))
        )
        driver.switch_to.frame("basefrm")
    except TimeoutException:
        driver.quit()
        exit()

    # Seleccionar la opción "Mixed WPA2/WPA -PSK" en el menú desplegable "Network Authentication"
    try:
        auth_dropdown = WebDriverWait(driver, 60).until(
            EC.presence_of_element_located((By.XPATH, "//select[@name='wlAuthMode']"))
        )
        auth_dropdown.click()
        auth_option = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//select[@name='wlAuthMode']/option[@value='psk psk2']"))
        )
        auth_option.click()
    except TimeoutException:
        driver.quit()
        exit()

    # Esperar a que aparezca el campo de "WPA/WAPI passphrase" (que se hace visible tras seleccionar la opción)
    try:
        passphrase_field = WebDriverWait(driver, 60).until(
            EC.visibility_of_element_located((By.XPATH, "//input[@type='password' and @name='wlWpaPsk']"))
        )
        passphrase_field.clear()
        passphrase_field.send_keys(wpa_pass)
    except TimeoutException:
        driver.quit()
        exit()
    time.sleep(5)

    # Esperar a que el botón "Apply/Save" esté presente y visible
    try:
        apply_save_button = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//input[@type='button' and @value='Apply/Save']"))
        )
        apply_save_button.click()
    except TimeoutException:
        driver.quit()
        exit()
    time.sleep(5)

finally:
    # Mostrar mensaje de finalización mejorado con correo de contacto
    import ctypes
    ctypes.windll.user32.MessageBoxW(
        0, 
        "La configuración del módem y la red Wi-Fi se completó con éxito.\n\n"
        "Si necesitas soporte adicional, no dudes en contactarme:\n"
        "miraglioluis1@gmail.com\n\n"
        "Muchas gracias por utilizar mi Automatización.\n\n"
        "- Luis Miraglio -", 
        "Proceso de Configuración Finalizado", 
        0x40 | 0x1
    )
    time.sleep(15)
    driver.quit()
#Comando para compilar el script en un ejecutable con driver del navegador dentro de la carpeta del Script
#pyinstaller --onefile --add-binary "msedgedriver.exe;." "nombre del archivo.py"
