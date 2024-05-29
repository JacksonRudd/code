## Azure Setup

- az deployment group create --resource-group chat --template-file ./aks.bicep
- Same with acr and perms bicep files

## Getting Started

- kubectl config get-contexts
- az aks get-credentials --resource-group chat --name klab
- kubectl config use-context klab

## Deploy Code

- az acr login --name genacr222
- docker build -t genacr222.azurecr.io/chat:latest .
- docker push genacr222.azurecr.io/chat:latest
- kubectl rollout restart deployment/chat-app

## Deploy K8

- kubectl apply -f deployment.yaml

## Check on deployment

- kubectl get deployments
- kubectl describe deployment chat-app
- az deployment group show --resource-group chat --name perms
- kubectl get pods -o wide --all-namespaces
- kubectl get deployment chat-app -o yaml

## Debugging

- kubectl logs PODNAME
- kubectl describe pod PODNAME
- kubectl exec -it PODNAME -- /bin/bash

## Change Perms

- az role definition list --query "[].{Name:roleName, Id:id}" --output table

## Questions

- Why am i not able to connect to my backend from my client?
- Why am I getting traffic from 10.244.0.1 on my pods
- Now that I've ignored that why am I not getting traffic at all?
