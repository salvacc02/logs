import os
import datetime
from kubernetes import client
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive

# Función para obtener los logs de un pod en OpenShift
def get_pod_logs(namespace, pod_name, username, password, api_server):
    try:
        # Configurar manualmente la autenticación en Kubernetes
        configuration = client.Configuration()
        configuration.host = https://api.bsi-arrend-ocpd.jp58.p1.openshiftapps.com:6443
        configuration.username = arrendadoraclustadm
        configuration.password = iJK098H*m9qi2021
        configuration.verify_ssl = False  # Puede requerir configuración adicional para la verificación SSL

        # Crear un cliente de la API de Kubernetes con la configuración personalizada
        api_client = client.ApiClient(configuration)

        # Crear un cliente CoreV1Api con la configuración personalizada
        core_api = client.CoreV1Api(api_client)

        # Obtener los logs del pod
        logs = core_api.read_namespaced_pod_log(name=pod_name, namespace=namespace)

        return logs
    except Exception as e:
        print(f"Error: {e}")
        return None

# Función para subir un archivo a Google Drive
def upload_to_google_drive(file_name, folder_id, content):
    try:
        # Resto del código para subir a Google Drive (sin cambios)

    except Exception as e:
        print(f"Error al subir a Google Drive: {e}")
        return None

if __name__ == "__main__":
    namespace = "bsi-arren-service-prod"  # Reemplaza con el nombre de tu espacio de nombres
    pod_name = "msasr-o-b-listo-recovery-8-rnhrc"  # Reemplaza con el nombre de tu pod
    username = "tu_usuario"  # Reemplaza con tu nombre de usuario
    password = "tu_contraseña"  # Reemplaza con tu contraseña
    api_server = "https://tu.api.server.com"  # Reemplaza con la URL del servidor API de Kubernetes

    logs = get_pod_logs(namespace, pod_name, username, password, api_server)

    if logs:
        # Obtiene la fecha y la hora actual
        current_datetime = datetime.datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

        # Define el nombre del archivo de texto con la fecha y la hora
        txt_filename = f"logs_{current_datetime}.txt"

        # Subir el archivo de texto a Google Drive en la carpeta específica (reemplaza 'FOLDER_ID' con el ID de la carpeta de destino)
        folder_id = '1fKaIxie1-YhZYVH9nZVHRrX4ARg2RCc0'
        uploaded_file_id = upload_to_google_drive(txt_filename, folder_id, logs)

        if uploaded_file_id:
            print(f"ID del archivo subido a Google Drive: {uploaded_file_id}")

    else:
        print("No se pudieron obtener los logs del pod.")
