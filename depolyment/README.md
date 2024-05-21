docker build -t genacr222.azurecr.io/chat:latest .
docker push genacr222.azurecr.io/chat:latest

az deployment group create --resource-group chat --template-file ./aks.bicep
az aks get-credentials --resource-group chat --name name

kubectl apply -f deployment.yaml
kubectl get deployments
kubectl describe deployment chat-app

az role definition list --query "[].{Name:roleName, Id:id}" --output table
az deployment group show --resource-group chat --name perms

kubectl get pods -o wide --all-namespaces
