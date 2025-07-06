from cx_Freeze import setup, Executable
import sys
import os
import subprocess

# Files to include in the build
includefiles = ['billing.ico']
excludes = []
packages = []
base = None

# Use GUI base if on Windows
if sys.platform == 'win32':
    base = "Win32GUI"

# MSI shortcut (creates desktop shortcut in installer)
shortcut_table = [
    ("DesktopShortcut",        # Shortcut
     "DesktopFolder",          # Directory_
     "Grocery Cart",           # Shortcut name
     "TARGETDIR",              # Component_
     "[TARGETDIR]main.exe",    # Target
     None,                     # Arguments
     None,                     # Description
     None,                     # Hotkey
     None,                     # Icon
     None,                     # IconIndex
     None,                     # ShowCmd
     "TARGETDIR"               # Working directory
     )
]

# MSI installer configuration
msi_data = {"Shortcut": shortcut_table}
bdist_msi_options = {'data': msi_data}

# Main setup call
setup(
    name="Grocery Cart",
    version="0.1",
    description="Grocery billing system for desktop",
    author="Bongumusa Gumede",
    options={
        'build_exe': {
            'include_files': includefiles,
            'packages': packages,
            'excludes': excludes
        },
        'bdist_msi': bdist_msi_options
    },
    executables=[
        Executable(
            script="main.py",
            base=base,
            icon="billing.ico"
        )
    ]
)

# 📂 Auto-open the output folder after build (optional for course demonstration)
if os.path.exists("build"):
    print("\n✅ Build complete! Opening build folder...\n")
    if sys.platform == "win32":
        subprocess.Popen(f'explorer "{os.path.abspath("build")}"')
    else:
        print("🟡 Auto-open only supported on Windows.")
else:
    print("⚠️ Build folder not found.")
