import subprocess
import sys
import tkinter as tk
from tkinter import messagebox
import os

# Create virtual environment
def create_virtualenv():
    # Check if the venv folder exists, if not create it
    if not os.path.exists('venv'):
        subprocess.check_call([sys.executable, '-m', 'venv', 'pcbuildxenv'])
        return "Virtual environment created successfully!"
    else:
        return "Virtual environment already exists."

class PipInstallerGUI:
    def __init__(self, root, package_list):
        self.root = root
        self.package_list = package_list
        
        # Setup window
        self.root.title("Install PCBuildX")
        self.root.geometry("400x300")

        # Create frames for better layout
        self.frame = tk.Frame(self.root)
        self.frame.pack(pady=20)

        # Add label
        self.label = tk.Label(self.frame, text="Select an action for pip packages", font=("Helvetica", 14))
        self.label.pack(pady=10)

        # Buttons for install, check, and uninstall
        self.install_button = tk.Button(self.frame, text="Install Packages", command=self.install_packages, width=20)
        self.install_button.pack(pady=5)

        self.check_button = tk.Button(self.frame, text="Check Installed Packages", command=self.check_installed, width=20)
        self.check_button.pack(pady=5)

        self.uninstall_button = tk.Button(self.frame, text="Uninstall Packages", command=self.uninstall_packages, width=20)
        self.uninstall_button.pack(pady=5)

        # Log output
        self.output_box = tk.Text(self.root, height=10, width=40)
        self.output_box.pack(pady=10)

        # Initialize virtual environment
        self.create_venv_message = create_virtualenv()
        self.write_output(self.create_venv_message)

    def run_subprocess(self, command):
        """Execute the given command and return output."""
        try:
            result = subprocess.check_output(command, stderr=subprocess.STDOUT)
            return result.decode()
        except subprocess.CalledProcessError as e:
            return e.output.decode()

    def install_packages(self):
        """Install the packages from the list."""
        self.clear_output()
        self.write_output("Installing packages...\n")
        for package in self.package_list:
            result = self.run_subprocess([sys.executable, "venv/bin/pip", "install", package])
            self.write_output(result)
        messagebox.showinfo("Installation Complete", "All packages installed successfully!")

    def check_installed(self):
        """Check if packages are installed."""
        self.clear_output()
        self.write_output("Checking installed packages...\n")
        for package in self.package_list:
            result = self.run_subprocess([sys.executable, "venv/bin/pip", "show", package])
            if "Name: " in result:
                self.write_output(f"{package} is installed.\n")
            else:
                self.write_output(f"{package} is NOT installed.\n")
        messagebox.showinfo("Check Complete", "Package check complete!")

    def uninstall_packages(self):
        """Uninstall the packages from the list."""
        self.clear_output()
        self.write_output("Uninstalling packages...\n")
        for package in self.package_list:
            result = self.run_subprocess([sys.executable, "venv/bin/pip", "uninstall", "-y", package])
            self.write_output(result)
        messagebox.showinfo("Uninstallation Complete", "All packages uninstalled successfully!")

    def write_output(self, output_text):
        """Write output to the Text widget."""
        self.output_box.insert(tk.END, output_text)
        self.output_box.yview(tk.END)  # Auto scroll to the end

    def clear_output(self):
        """Clear output box."""
        self.output_box.delete(1.0, tk.END)

if __name__ == "__main__":
    # List of packages you want to install, check, or uninstall
    packages = ["geopandas", "numpy", "functools", "multiprocessing", "rasterio", "matplotlib"]  # Example package list

    root = tk.Tk()
    installer_gui = PipInstallerGUI(root, packages)
    root.mainloop()

