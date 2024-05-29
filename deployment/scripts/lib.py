import subprocess
import threading
def run_powershell_command(cmd):
    # Execute the PowerShell command
    completed_process = subprocess.run(["powershell", "-Command", cmd], capture_output=True, text=True)
    # Print the standard output and errors, if any
    if completed_process.stdout:
        print("Output:", completed_process.stdout)
    if completed_process.stderr:
        print("Error:", completed_process.stderr)


def run_powershell_new_thread(command):
    docker_thread = threading.Thread(target=lambda: run_powershell_command(command))
    docker_thread.start()
