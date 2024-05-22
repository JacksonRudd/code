## Azure Setup

- az deployment group create --resource-group chat --template-file ./aks.bicep
  - Same with acr and perms bicep files

## Getting Started

- kubectl config get-contexts
- az aks get-credentials --resource-group chat --name klab
- kubectl config use-context klab

## Deploy

- docker build -t genacr222.azurecr.io/chat:latest .
- docker push genacr222.azurecr.io/chat:latest
- kubectl apply -f deployment.yaml

## Check on deployment

- kubectl get deployments
- kubectl describe deployment chat-app
- az deployment group show --resource-group chat --name perms
- kubectl get pods -o wide --all-namespaces

# Change Perms

- az role definition list --query "[].{Name:roleName, Id:id}" --output table
