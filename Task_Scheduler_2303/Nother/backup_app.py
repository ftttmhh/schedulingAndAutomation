import os
import shutil
import platform
import subprocess
import time

class BackupApp:
    def backup_files(self, source_dir, dest_dir):
        print("Backing up files from", source_dir, "to", dest_dir)
        try:
            # Copy files from source directory to destination directory
            for root, dirs, files in os.walk(source_dir):
                for file in files:
                    src_file = os.path.join(root, file)
                    dest_file = os.path.join(dest_dir, os.path.relpath(src_file, source_dir))
                    dest_path = os.path.dirname(dest_file)
                    if not os.path.exists(dest_path):
                        os.makedirs(dest_path)
                    shutil.copy2(src_file, dest_file)
            print("Backup completed.")
        except Exception as e:
            print("Error during backup:", str(e))

    def perform_maintenance(self):
        print("Performing system maintenance...")
        try:
            # Perform disk cleanup based on the operating system
            if platform.system() == "Windows":
                # On Windows, use the built-in cleanup tool (cleanmgr) via command line
                os.system("cleanmgr /sagerun:1")  # Run cleanup using saved settings (Sagerun 1)
            elif platform.system() == "Linux":
                # On Linux, clean up temporary files using commands (e.g., apt clean)
                os.system("sudo apt clean")  # Example: Clean package cache on Debian-based systems
            elif platform.system() == "Darwin":
                # On macOS, clean up temporary files using commands (e.g., brew cleanup)
                os.system("brew cleanup")  # Example: Clean up Homebrew packages and formulae
            else:
                print("Unsupported operating system.")
        except Exception as e:
            print("Error performing system maintenance:", str(e))

    def open_app_at_time(self, app_path, open_time):
        current_platform = platform.system()
        if current_platform == "Windows":
            subprocess.Popen(["start", app_path], shell=True)
        elif current_platform == "Darwin":
            subprocess.Popen(["open", "-a", app_path])
        elif current_platform == "Linux":
            subprocess.Popen(["xdg-open", app_path])
        else:
            print("Unsupported operating system.")

        current_time = time.localtime()
        open_hour, open_minute = map(int, open_time.split(':'))
        open_timestamp = time.mktime((current_time.tm_year, current_time.tm_mon, current_time.tm_mday,
                                       open_hour, open_minute, 0, current_time.tm_wday, current_time.tm_yday, current_time.tm_isdst))
        current_timestamp = time.mktime(current_time)
        time_diff_seconds = open_timestamp - current_timestamp
        if time_diff_seconds > 0:
            print(f"Application will be opened at {open_time}.")
            time.sleep(time_diff_seconds)
        else:
            print("Specified time is in the past. Application will be opened immediately.")

