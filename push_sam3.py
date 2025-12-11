import argparse
from pydrive2.auth import GoogleAuth
from pydrive2.drive import GoogleDrive
import tarfile
import os

def auth_drive():
    """OAuth2 and return GoogleDrive"""
    gauth = GoogleAuth()
    gauth.LoadClientConfigFile("./client_secrets.json")
    # gauth.LocalWebserverAuth()
    gauth.CommandLineAuth()  
    return GoogleDrive(gauth)

def compress_folder(folder_path, output_filename):
    """Zip folder to tar.gz"""
    with tarfile.open(output_filename, "w:gz") as tar:
        tar.add(folder_path, arcname=os.path.basename(folder_path))
    print(f"📦 Zipped folder {folder_path} to {output_filename}")

def upload_file(drive, file_path, parent_id):
    """Upload file to Google Drive to folder have parent_id"""
    file_name = os.path.basename(file_path)
    gfile = drive.CreateFile({'title': file_name, 'parents': [{'id': parent_id}]})
    gfile.SetContentFile(file_path)
    gfile.Upload()
    print(f"✅ Uploaded {file_name} to Drive folder ID {parent_id}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Upload folder to Google Drive as a tar.gz file.")
    parser.add_argument("--folder", type=str, default="sam3")
    parser.add_argument("--tarfile", type=str, default="sam3.tar.gz")
    parser.add_argument("--drive_folder_id", type=str, default="1H_7q2hKzOwEj6wN7bu3aSUXZT23Ktjw_")
    args = parser.parse_args()

    drive = auth_drive()
    compress_folder(args.folder, args.tarfile)
    upload_file(drive, args.tarfile, args.drive_folder_id)