import schedule
import time
from gui import BackupAppGUI
from backup_app import BackupApp

def main():
    app = BackupAppGUI(BackupApp())
    app.run()
    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()
