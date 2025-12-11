from pydrive2.auth import GoogleAuth
from pydrive2.drive import GoogleDrive
import tarfile
import os

def auth_drive():
    """OAuth2 and return GoogleDrive"""
    gauth = GoogleAuth()
    gauth.LoadClientConfigFile("/root/VLM-high-resolution/client_secret.json")
    gauth.LocalWebserverAuth()
    return GoogleDrive(gauth)

def download_file(drive, file_id, output_path):
    """Download file as file_id"""
    print(f"⬇️ Downloading file ID: {file_id}")
    file = drive.CreateFile({'id': file_id})
    file.GetContentFile(output_path)
    print(f"✅ Downloaded: {output_path}")

def extract_tar_gz(filepath, extract_to):
    """Unzip .tar.gz"""
    os.makedirs(extract_to, exist_ok=True)
    with tarfile.open(filepath, 'r:gz') as tar_ref:
        tar_ref.extractall(extract_to)
    print(f"📦 Unzipped to: {extract_to}")

if __name__ == "__main__":
    file_id = ""
    output_file = "sam3.tar.gz"
    extract_folder = "./"

    drive = auth_drive()
    download_file(drive, file_id, output_file)
    extract_tar_gz(output_file, extract_folder)