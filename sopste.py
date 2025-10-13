import time
import getpass
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

URL_INICIO = "https://bapro.sopste.org.ar/area_empresas/index.php"
EXCEL_PATH = "panaderos.xlsx"  # Cambiar si está en otra carpeta

def main():
    usuario = "30712543945"
    password = "custode"

    # Configurar Chrome
    options = webdriver.ChromeOptions()
    options.add_argument("--start-maximized")

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)

    try:
        driver.get(URL_INICIO)
        time.sleep(2)

        # Ir al login
        link_login = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, "//a[contains(@href,'login.php')]"))
        )
        
        link_login.click()
        time.sleep(2)

        # Completar login
        campo_usuario = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.NAME, "usuario"))
        )
        campo_password = driver.find_element(By.NAME, "password")
        campo_usuario.send_keys(usuario)
        time.sleep(1)
        campo_password.send_keys(password)
        time.sleep(1)

        boton_ingresar = driver.find_element(By.XPATH, "//input[@type='submit' and @value='Ingresar']")
        boton_ingresar.click()
        time.sleep(2)

        # Esperar página principal
        WebDriverWait(driver, 15).until(
            EC.presence_of_element_located((By.XPATH, "//a[contains(.,'Ver / Modificar listado de empleados activos')]"))
        )

        # Leer Excel
        df = pd.read_excel(EXCEL_PATH)

        # Formatear CUIL (XX-XXXXXXXX-X)
        df["CUIL_fmt"] = df["CUIL"].astype(str).str.replace(".", "").str.zfill(11)
        df["CUIL_fmt"] = df["CUIL_fmt"].apply(lambda x: f"{x[:2]}-{x[2:10]}-{x[10:]}")

        # Loop sobre los empleados
        for _, row in df.iterrows():
            
            # Entrar a empleados activos
            print("👥 Entrando a 'Ver / Modificar listado de empleados activos'...")
            link_empleados = driver.find_element(By.XPATH, "//a[contains(.,'Ver / Modificar listado de empleados activos')]")
            link_empleados.click()
            time.sleep(2)

            cuil = row["CUIL_fmt"]
            sueldo = str(row["Remuneración 8"])
            entero, decimal = sueldo.split(".")
            if len(decimal) == 1: decimal += "0"
            print(f"\n➡️ Procesando {cuil} (sueldo: {entero},{decimal})")

            try:
                # Buscar fila por CUIL
                fila = WebDriverWait(driver, 10).until(
                    EC.presence_of_element_located((By.XPATH, f"//td[contains(.,'{cuil}')]/.."))
                )

                # Hacer clic en "Editar"
                link_editar = fila.find_element(By.XPATH, ".//a[contains(text(),'Editar')]")
                link_editar.click()
                print(f"✏️ Entrando a editar {cuil}...")

                # --- Completar los campos de remuneración ---
                print("💰 Completando campos de remuneración...")

                # Campo principal de sueldo (parte entera)
                campo_entero = driver.find_element(By.ID, "sueldo_empl")
                campo_entero.clear()
                time.sleep(1)  # espera para evitar problemas de carga
                campo_entero.send_keys(entero)

                # Campo de centavos
                campo_centavos = driver.find_element(By.ID, "sueldo_cent_empl")
                campo_centavos.clear()
                time.sleep(1)  # espera para evitar problemas de carga
                campo_centavos.send_keys(decimal)  # rellena con 0 si es un solo dígito

                print("💰 Sueldo actualizado. Esperando 2 segundos antes de guardar...")
                time.sleep(2)

                # --- Guardar los datos ---
                boton_guardar = driver.find_element(By.XPATH, "//input[@type='submit' and contains(@value,'Guardar Datos de Empleado')]")
                boton_guardar.click()

                # Esperar a que vuelva o confirmar guardado
                time.sleep(2)

                
                boton_volver = WebDriverWait(driver, 10).until(
                    EC.element_to_be_clickable((By.XPATH, "//a[@href='admin.php']"))
                )
                boton_volver.click()
                time.sleep(2)

            except Exception as e:
                print(f"❌ No se pudo procesar {cuil}: {e}")

        print("\n✅ Proceso completado correctamente.")

    except Exception as e:
        print("❌ Error durante el proceso:", e)
        input("Presioná ENTER para cerrar...")
    finally:
        driver.quit()

if __name__ == "__main__":
    main()
