import tkinter as tk
from backup_app import BackupApp

class BackupAppGUI:
    def __init__(self, backup_app):
        self.backup_app = backup_app

        self.root = tk.Tk()
        self.root.title("Backup Application")
        self.root.geometry("400x300")
        self.root.configure(bg="#2C3E50")  # Set background color

        # Initialize frames
        self.home_frame = tk.Frame(self.root, bg="#2C3E50")
        self.backup_frame = tk.Frame(self.root, bg="#2C3E50")
        self.maintenance_frame = tk.Frame(self.root, bg="#2C3E50")
        self.app_opener_frame = tk.Frame(self.root, bg="#2C3E50")

        # Pack frames initially
        self.home_frame.pack(fill=tk.BOTH, expand=True)
        self.backup_frame.pack(fill=tk.BOTH, expand=True)
        self.maintenance_frame.pack(fill=tk.BOTH, expand=True)
        self.app_opener_frame.pack(fill=tk.BOTH, expand=True)

        # Show home frame initially
        self.show_frame(self.home_frame)

        # Create widgets for each frame
        self.create_home_widgets()
        self.create_backup_widgets()
        self.create_maintenance_widgets()
        self.create_app_opener_widgets()

    def show_frame(self, frame):
        # Hide all frames and then show the specified frame
        for f in [self.home_frame, self.backup_frame, self.maintenance_frame, self.app_opener_frame]:
            f.pack_forget()
        frame.pack(fill=tk.BOTH, expand=True)

    def create_home_widgets(self):
        # Home frame widgets
        # Welcome message
        welcome_label = tk.Label(self.home_frame, text="Welcome to Backup Application", font=("Helvetica", 18, "bold"), fg="white", bg="#2C3E50")
        welcome_label.pack(pady=10)

        # Buttons to navigate to other frames
        backup_button = tk.Button(self.home_frame, text="Backup Files", font=("Helvetica", 12), bg="#3498DB", fg="white", command=lambda: self.show_frame(self.backup_frame))
        backup_button.pack(pady=5)

        maintenance_button = tk.Button(self.home_frame, text="Perform Maintenance", font=("Helvetica", 12), bg="#3498DB", fg="white", command=lambda: self.show_frame(self.maintenance_frame))
        maintenance_button.pack(pady=5)

        app_opener_button = tk.Button(self.home_frame, text="Open App", font=("Helvetica", 12), bg="#3498DB", fg="white", command=lambda: self.show_frame(self.app_opener_frame))
        app_opener_button.pack(pady=5)

    def create_backup_widgets(self):
        # Backup frame widgets
        self.backup_frame_label = tk.Label(self.backup_frame, text="Backup Files", font=("Helvetica", 18, "bold"), fg="white", bg="#2C3E50")
        self.backup_frame_label.pack(pady=10)

        # Source directory input
        self.source_label = tk.Label(self.backup_frame, text="Source Directory:", font=("Helvetica", 12), fg="white", bg="#2C3E50")
        self.source_label.pack()
        self.source_entry = tk.Entry(self.backup_frame, font=("Helvetica", 12))
        self.source_entry.pack()

        # Backup directory input
        self.backup_label = tk.Label(self.backup_frame, text="Backup Directory:", font=("Helvetica", 12), fg="white", bg="#2C3E50")
        self.backup_label.pack()
        self.backup_entry = tk.Entry(self.backup_frame, font=("Helvetica", 12))
        self.backup_entry.pack()

        # Backup time input
        self.time_label = tk.Label(self.backup_frame, text="Backup Time (HH:MM):", font=("Helvetica", 12), fg="white", bg="#2C3E50")
        self.time_label.pack()
        self.time_entry = tk.Entry(self.backup_frame, font=("Helvetica", 12))
        self.time_entry.pack()

        # Button to run backup
        self.backup_button = tk.Button(self.backup_frame, text="Run Backup", font=("Helvetica", 12), bg="#3498DB", fg="white", command=self.run_backup)
        self.backup_button.pack(pady=5)

        # Button to go back to home page
        self.back_to_home_button = tk.Button(self.backup_frame, text="Back to Home", font=("Helvetica", 12), bg="#3498DB", fg="white", command=lambda: self.show_frame(self.home_frame))
        self.back_to_home_button.pack(pady=5)

    def create_maintenance_widgets(self):
        # Maintenance frame widgets
        self.maintenance_frame_label = tk.Label(self.maintenance_frame, text="Perform Maintenance", font=("Helvetica", 18, "bold"), fg="white", bg="#2C3E50")
        self.maintenance_frame_label.pack(pady=10)

        # Button to perform maintenance
        self.maintenance_button = tk.Button(self.maintenance_frame, text="Run Maintenance", font=("Helvetica", 12), bg="#3498DB", fg="white", command=self.run_maintenance)
        self.maintenance_button.pack(pady=5)

        # Button to go back to home page
        self.back_to_home_button = tk.Button(self.maintenance_frame, text="Back to Home", font=("Helvetica", 12), bg="#3498DB", fg="white", command=lambda: self.show_frame(self.home_frame))
        self.back_to_home_button.pack(pady=5)

    def create_app_opener_widgets(self):
        # App opener frame widgets
        self.app_opener_frame_label = tk.Label(self.app_opener_frame, text="Open App", font=("Helvetica", 18, "bold"), fg="white", bg="#2C3E50")
        self.app_opener_frame_label.pack(pady=10)

        # App directory input
        self.app_directory_label = tk.Label(self.app_opener_frame, text="App Directory:", font=("Helvetica", 12), fg="white", bg="#2C3E50")
        self.app_directory_label.pack()
        self.app_directory_entry = tk.Entry(self.app_opener_frame, font=("Helvetica", 12))
        self.app_directory_entry.pack()

        # Time to open app input
        self.app_time_label = tk.Label(self.app_opener_frame, text="Open Time (HH:MM):", font=("Helvetica", 12), fg="white", bg="#2C3E50")
        self.app_time_label.pack()
        self.app_time_entry = tk.Entry(self.app_opener_frame, font=("Helvetica", 12))
        self.app_time_entry.pack()

        # Button to open app
        self.open_app_button = tk.Button(self.app_opener_frame, text="Open App Now", font=("Helvetica", 12), bg="#3498DB", fg="white", command=self.open_app)
        self.open_app_button.pack(pady=5)

        # Button to go back to home page
        self.back_to_home_button = tk.Button(self.app_opener_frame, text="Back to Home", font=("Helvetica", 12), bg="#3498DB", fg="white", command=lambda: self.show_frame(self.home_frame))
        self.back_to_home_button.pack(pady=5)

    def run_backup(self):
        source_dir = self.source_entry.get()
        dest_dir = self.backup_entry.get()
        backup_time = self.time_entry.get()

        # Call the backup method of BackupApp with provided inputs
        self.backup_app.backup_files(source_dir, dest_dir)
        print("Backup scheduled for", backup_time)

    def run_maintenance(self):
        # Placeholder function for performing maintenance
        self.backup_app.perform_maintenance()
        print("Maintenance performed.")

    def open_app(self):
        app_directory = self.app_directory_entry.get()
        open_time = self.app_time_entry.get()

        # Call the method to open app with provided inputs
        self.backup_app.open_app_at_time(app_directory, open_time)
        print("App opening scheduled for", open_time)

    def run(self):
        self.root.mainloop()




