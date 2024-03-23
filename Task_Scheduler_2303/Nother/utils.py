import os
import shutil
import platform
import subprocess
import time

def backup_files(source_dir, dest_dir):
    """Backup files from source directory to destination directory."""
    if not os.path.exists(dest_dir):
        os.makedirs(dest_dir)
    for root, dirs, files in os.walk(source_dir):
        for file in files:
            src_file = os.path.join(root, file)
            dest_file = os.path.join(dest_dir, os.path.relpath(src_file, source_dir))
            dest_path = os.path.dirname(dest_file)
            if not os.path.exists(dest_path):
                os.makedirs(dest_path)
            shutil.copy2(src_file, dest_file)

def open_app_at_time(app_path, open_time):
    """Open an application at a specified time."""
    current_platform = platform.system()
    if current_platform == "Windows":
        # On Windows, use 'start' command to open the application
        subprocess.Popen(["start", app_path], shell=True)
    elif current_platform == "Darwin":  # macOS
        # On macOS, use 'open' command to open the application
        subprocess.Popen(["open", "-a", app_path])
    elif current_platform == "Linux":
        # On Linux, use 'xdg-open' command to open the application
        subprocess.Popen(["xdg-open", app_path])
    else:
        print("Unsupported operating system.")

    # Calculate the time difference between the current time and the open time
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
