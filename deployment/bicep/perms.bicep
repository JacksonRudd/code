// resource myAKS 'Microsoft.ContainerService/managedClusters@2024-02-01' existing = {
//   name: 'name'
// }
// resource myACR 'Microsoft.ContainerRegistry/registries@2021-06-01-preview' existing = {
//   name: 'genacr222'
// }
// var aks_principal_id = myAKS.properties.identityProfile.kubeletidentity.objectId
// resource  AssignAcrPullToAks 'Microsoft.Authorization/roleAssignments@2020-04-01-preview' = {
//   name: guid(myAKS.id, myACR.id, 'ACSPullRoleAssignment')      
//   properties: {
//     description: 'Assign AcrPull role to AKS'
//     principalId: aks_principal_id
//     principalType: 'ServicePrincipal'
//     roleDefinitionId: '7f951dda-4ed3-4680-a7ca-43fe172d538d'
//     scope: myACR.id
//   }
// }

resource myAKS 'Microsoft.ContainerService/managedClusters@2024-02-01' existing = {
  name: 'klab'
}
resource myACR 'Microsoft.ContainerRegistry/registries@2021-06-01-preview' existing = {
  name: 'genacr222'
}

var aks_principal_id = myAKS.properties.identityProfile.kubeletidentity.objectId

resource AssignAcrPullToAks 'Microsoft.Authorization/roleAssignments@2020-04-01-preview' = {
  name: guid(myAKS.id, myACR.id, 'ACSPullRoleAssignment')      
  properties: {
    description: 'Assign AcrPull role to AKS'
    principalId: aks_principal_id
    principalType: 'ServicePrincipal'
    roleDefinitionId: resourceId('Microsoft.Authorization/roleDefinitions', '7f951dda-4ed3-4680-a7ca-43fe172d538d')
    scope:  resourceGroup().id
  }
}
