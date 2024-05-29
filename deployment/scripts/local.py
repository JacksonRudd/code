# scripts/local.py
from scripts.lib import run_powershell_command, run_powershell_new_thread, subprocess

def main():
    # Stop all running Docker containers
    run_powershell_command('docker ps -q | ForEach-Object {docker stop $_}')
    run_powershell_command('docker ps -aq | ForEach-Object {docker rm $_}')
    
    # Build the Docker image
    run_powershell_command('docker build -t local .\\basic_chat_app\\')
    
    # Run the Docker container
    run_powershell_new_thread('docker run -it -p 5000:5000 local')
    
    # Start the client script in a new command prompt
    subprocess.run('start cmd /c python .\\basic_chat_app\\client.py', shell=True)

if __name__ == "__main__":
    main()
