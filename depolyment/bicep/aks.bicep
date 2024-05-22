@description('The Kubernetes cluster for running several of my applications')
resource aksCluster 'Microsoft.ContainerService/managedClusters@2024-02-01' = {
  name: 'klab'
  location: resourceGroup().location
  identity: {
    type: 'SystemAssigned'
  }
  properties: {
    dnsPrefix: 'dnsprefix'
    enableRBAC: true
    agentPoolProfiles: [
      {
        name: 'small'
        count: 1 // Start with a single node
        vmSize: 'Standard_B2s' // Use a cheaper VM size
        osType: 'Linux'
        mode: 'System'
        enableAutoScaling: true
        minCount: 1
        maxCount: 3
      }
    ]
  }
}
