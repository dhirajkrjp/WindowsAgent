import subprocess
from pywinauto import Application, Desktop
import time

def open_application(app_name, exe_path=None):
    """Focuses an application if running, or launches it."""
    print(f"--> [Windows] Attempting to open/focus {app_name}")
    
    try:
        # Try to find an existing window first
        windows = Desktop(backend="uia").windows(title_re=f".*{app_name}.*", visible_only=True)
        if windows:
            windows[0].set_focus()
            print(f"--> [Windows] Focused existing {app_name} window.")
            return True
            
        # If not running and path is provided, launch it
        if exe_path:
            subprocess.Popen(exe_path)
            time.sleep(2) # Wait for it to open
            print(f"--> [Windows] Launched new {app_name} instance.")
            return True
            
    except Exception as e:
        print(f"--> [Windows] Error managing {app_name}: {e}")
    
    return False