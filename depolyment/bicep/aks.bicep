@description('The kubernetes cluster for running several of my applications')
resource aksCluster 'Microsoft.ContainerService/managedClusters@2024-02-01' = {
  name: 'name'
  location: resourceGroup().location
  identity: {
    type: 'SystemAssigned'
  }
  properties: {
   dnsPrefix: 'dnsprefix'
    enableRBAC: true
    // not sure if I need this yet.
    // servicePrincipalProfile: {
    //   clientId:'msi'
    // }
    agentPoolProfiles: [
      {
        name: 'agentpool'
        count: 3
        vmSize: 'Standard_DS2_v2'
        osType: 'Linux'
        mode: 'System'
      }
    ]
  }
}
