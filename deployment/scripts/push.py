import subprocess

from scripts.lib import run_powershell_command

def main():
    # Change the directory to the location of the Dockerfile if needed
    # subprocess.run(["cd", "/path/to/dockerfile"], shell=True)
    
    # Login to Azure Container Registry
    
    run_powershell_command('az acr login --name genacr222')
    
    # Build the Docker image
    run_powershell_command('docker build -t genacr222.azurecr.io/chat:latest ./basic_chat_app')
    
    # Push the Docker image
    run_powershell_command('docker push genacr222.azurecr.io/chat:latest')
    
    # Restart Kubernetes deployment
    run_powershell_command('kubectl rollout restart deployment/chat-app')

if __name__ == '__main__':
    main()
