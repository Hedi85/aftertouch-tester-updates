import os
import sys
import shutil
import zipfile
import requests

from update_dialog import UpdateDialog
from PySide2.QtWidgets import QApplication
from PySide2.QtCore import QCoreApplication

# -----------------------------
# Your current application version
# -----------------------------
CURRENT_VERSION = "5.2.3"

# -----------------------------
# GitHub release endpoints
# -----------------------------
VERSION_URL = "https://github.com/Hedi85/aftertouch-tester-updates/releases/latest/download/version.txt"
UPDATE_URL  = "https://github.com/Hedi85/aftertouch-tester-updates/releases/latest/download/update.zip"


# ===================================================================
#  Find the real folder where the EXE lives
# ===================================================================
def get_app_folder():
    if getattr(sys, 'frozen', False):
        return os.path.dirname(os.path.abspath(sys.argv[0]))
    return os.path.dirname(os.path.abspath(__file__))



# ===================================================================
#  Create and run a .bat file to safely update the EXE
# ===================================================================
def run_batch_update(app_dir):
    exe_name = "Monophonic_AT_Arturia.exe"
    bat_path = os.path.join(app_dir, "run_update.bat")

    with open(bat_path, "w") as bat:
        bat.write(f'''
@echo off
echo Waiting for application to close...

:WAIT_APP
tasklist | find /I "{exe_name}" > nul
if not errorlevel 1 (
    timeout /T 1 > nul
    goto WAIT_APP
)

echo Removing PyInstaller temp folders...
for /D %%i in ("%temp%\\_MEI*") do rmdir /S /Q "%%i"

echo Installing new version...
xcopy "{app_dir}\\update_tmp\\*" "{app_dir}\\" /E /Y /Q

echo Cleaning up...
rmdir /S /Q "{app_dir}\\update_tmp"
del "{app_dir}\\update.zip"

echo Update completed successfully.
echo Please restart the application manually.
pause

del "%~f0"
''')

    os.startfile(bat_path)
    sys.exit(0)




# ===================================================================
#  Main update logic with progress window
# ===================================================================
def download_and_apply_update():
    app = QApplication.instance() or QApplication(sys.argv)

    dlg = UpdateDialog()
    dlg.show()
    QCoreApplication.processEvents()

    try:
        # ------------------------------------------------------------
        #  Step 1 — Download update.zip
        # ------------------------------------------------------------
        dlg.set_status("Downloading update…")
        QCoreApplication.processEvents()

        r = requests.get(UPDATE_URL, stream=True, timeout=10)
        r.raise_for_status()

        total = int(r.headers.get("content-length", 1))
        downloaded = 0

        app_dir = get_app_folder()
        update_path = os.path.join(app_dir, "update.zip")

        with open(update_path, "wb") as f:
            for chunk in r.iter_content(chunk_size=4096):
                if chunk:
                    f.write(chunk)
                    downloaded += len(chunk)
                    percent = int(downloaded * 100 / total)
                    dlg.set_progress(percent)
                    QCoreApplication.processEvents()

        # ------------------------------------------------------------
        #  Step 2 — Extract update.zip
        # ------------------------------------------------------------
        dlg.set_status("Extracting update…")
        dlg.set_progress(0)
        QCoreApplication.processEvents()

        temp_folder = os.path.join(app_dir, "update_tmp")

        with zipfile.ZipFile(update_path, "r") as z:
            files = z.namelist()
            total_files = len(files)

            for i, name in enumerate(files):
                z.extract(name, temp_folder)
                dlg.set_progress(int((i + 1) * 100 / total_files))
                QCoreApplication.processEvents()

        # ------------------------------------------------------------
        #  Step 3 — Run the batch updater
        # ------------------------------------------------------------
        dlg.set_status("Installing update…")
        dlg.set_progress(100)
        QCoreApplication.processEvents()

        run_batch_update(app_dir)

    except Exception as e:
        print("UPDATE FAILED:", e)
        dlg.set_status(f"Update failed: {e}")



# ===================================================================
#  Check for update on startup
# ===================================================================
def check_for_updates():
    try:
        print("Checking for updates...")
        response = requests.get(VERSION_URL, timeout=5)
        response.raise_for_status()
        online_version = response.text.strip()

        if online_version != CURRENT_VERSION:
            print(f"Update available: {online_version}")
            download_and_apply_update()
        else:
            print("Application is up to date.")

    except Exception as e:
        print("Could not check for updates:", e)
