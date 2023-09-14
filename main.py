import os
import datetime
from kubernetes import config as k8s_config
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive

# Función para obtener los logs de un pod en OpenShift
def get_pod_logs(namespace, pod_name):
    try:
        # Carga la configuración de OpenShift desde el archivo kubeconfig
        k8s_config.load_kube_config()

        # Obtiene los logs del pod
        from kubernetes import client
        core_api = client.CoreV1Api()
        logs = core_api.read_namespaced_pod_log(name=pod_name, namespace=namespace)

        return logs
    except Exception as e:
        print(f"Error: {e}")
        return None

# Función para subir un archivo a Google Drive
def upload_to_google_drive(file_name, folder_id, content):
    try:
        # Crear una instancia de GoogleAuth sin autenticación web
        gauth = GoogleAuth(settings_file="settings.yaml")

        # Intentar cargar las credenciales existentes o crear nuevas
        gauth.LocalWebserverAuth()

        # Guardar las credenciales en un archivo para futuros usos
        gauth.SaveCredentialsFile("mycreds.txt")

        drive = GoogleDrive(gauth)

        # Subir el archivo de texto a Google Drive en la carpeta específica
        file = drive.CreateFile({'title': file_name, 'parents': [{'kind': 'drive#folderLink', 'id': folder_id}]})
        file.SetContentString(content)  # Usamos SetContentString para establecer el contenido

        file.Upload()

        print(f"Archivo '{file_name}' subido a Google Drive con éxito.")

        return file['id']
    except Exception as e:
        print(f"Error al subir a Google Drive: {e}")
        return None

if __name__ == "__main__":
    namespace = "bsi-arren-service-prod"  # Reemplaza con el nombre de tu espacio de nombres
    pod_name = "msasr-o-b-listo-recovery-8-rnhrc"  # Reemplaza con el nombre de tu pod

    logs = get_pod_logs(namespace, pod_name)

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
