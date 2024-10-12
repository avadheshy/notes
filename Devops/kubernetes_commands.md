# 1. Basic Cluster Information

## Get cluster status
    kubectl cluster-info


    This command shows general information about your Kubernetes cluster, such as the addresses of the Kubernetes master and services like the DNS.

## View node details:
    kubectl get nodes

    Displays a list of all nodes (machines) in your Kubernetes cluster, showing the status, roles, and other basic information.

#  2. Working with Pods

## List all pods

    kubectl get pods

    Shows the current pods running in your cluster. You can add -o  wide to get more detailed information about the pods like node  placement, IP, etc.

## Describe a specific pod:

    kubectl describe pod <pod-name>

    This provides detailed information about a specific pod, including its status, events, resource usage, and node assignment. Useful for debugging issues

## Get logs from a pod:

    kubectl logs <pod-name>

    Retrieves logs from a pod’s container, helpful for debugging issues with application deployment.

## Delete a pod:

    kubectl delete pod <pod-name>

    Deletes a specific pod. The pod is terminated and replaced automatically if it’s managed by a deployment or replica set.
## Execute a command in a running pod:

    kubectl exec -it <pod-name> -- /bin/bash

    Opens an interactive terminal to a running container within the pod. You can use this to access the container’s shell, run commands, or inspect the environment.

# 3. Deployments

## View deployments:
    kubectl get deployments

    Lists all the deployments running in your Kubernetes cluster, along with their status, number of desired pods, and ready pods.

## Create a new deployment

    kubectl create deployment <deployment-name> --image=<image>

    Creates a new deployment. A deployment is a higher-level Kubernetes object that manages pods and ensures they are running as expected. The --image flag specifies the container image for the deployment.

## Scale a deployment:
    kubectl scale deployment <deployment-name> --replicas=<number>

    Adjusts the number of replicas (pods) in a deployment. Kubernetes will add or remove pods to match the desired replica count.

## Update deployment image:
    kubectl set image deployment/<deployment-name> <container-name>=<new-image>

     Updates the container image used by a deployment. Kubernetes will update all running pods with the new image.

## Rollback to a previous deployment
    kubectl rollout undo deployment/<deployment-name>

    Rolls back a deployment to a previous version, which is useful if the current deployment has issues.

# 4. Services
# List services
    kubectl get svc

    Explanation: Lists all services in your Kubernetes cluster, showing how different applications inside and outside of the cluster can communicate with your pods.

## Expose a deployment as a service:

    kubectl expose deployment <deployment-name> --type=NodePort --port=<port>

    Creates a service for a deployment, allowing external traffic to access the application. --type=NodePort opens a port on each node in the cluster and routes traffic to the pods.

## Get service details:


    kubectl describe svc <service-name>

    Shows detailed information about a specific service, including its endpoints, ports, and configuration.

# 5. Namespaces

# List namespaces:

    kubectl get namespaces

    Lists all namespaces in the cluster. Namespaces allow for the logical partitioning of resources within a cluster.

# Create a namespace:


    kubectl create namespace <namespace-name>

    Creates a new namespace, which can be used to isolate resources like deployments, services, and pods.

# Delete a namespace:


    kubectl delete namespace <namespace-name>

    Deletes a specific namespace, which will also delete all resources within it.

# 6. ConfigMaps and Secrets
## Create a ConfigMap from a file:

    kubectl create configmap <config-name> --from-file=<file>

    Creates a ConfigMap from a file that can store non-sensitive configuration data and inject it into your pods as environment variables or volumes.

## Create a Secret:

    kubectl create secret generic <secret-name> --from-literal=<key>=<value>

    Creates a Kubernetes secret that stores sensitive information like passwords, tokens, or keys.

## View ConfigMap details:

kubectl get configmap <config-name> -o yaml

Displays detailed information about a ConfigMap in YAML format, which is useful for inspecting the configuration.

## View Secret details:

    kubectl get secret <secret-name> -o yaml
    Shows detailed information about a secret. The actual values are base64-encoded for security reasons.

# 7. Ingress
## List Ingress resources:

    kubectl get ingress

    Lists all Ingress resources. Ingress manages external HTTP(S) access to services within a cluster.

## Create an Ingress resource:

    kubectl apply -f <ingress.yaml>

    Applies an Ingress resource configuration from a YAML file, allowing external traffic to access services via routes defined in the Ingress.

## Describe an Ingress resource:

    kubectl describe ingress <ingress-name>
    Shows detailed information about an Ingress resource, including rules, hosts, and backend services.

# 8. Volumes and Persistent Volumes
## List Persistent Volume Claims (PVCs):

    kubectl get pvc


    Lists Persistent Volume Claims in the cluster. PVCs are requests for storage resources from Persistent Volumes.

## Describe a Persistent Volume Claim:

    kubectl describe pvc <pvc-name>
    Displays detailed information about a specific PVC, such as its status, capacity, and storage class.

# 9. Monitoring and Debugging
## Top nodes (view resource usage of nodes):

    kubectl top nodes
    Displays real-time resource usage (CPU, memory) for each node in your Kubernetes cluster.

## Top pods (view resource usage of pods):

    kubectl top pods
    Shows resource usage (CPU, memory) for each pod, useful for monitoring performance.

## View events in the cluster:


    kubectl get events
    Lists events across the cluster. This helps track lifecycle changes, errors, or other state transitions in resources.

# 10. Advanced Commands
## Port-forwarding to a pod:

    kubectl port-forward <pod-name> <local-port>:<pod-port>

    Forwards a local port to a port on a pod, which allows you to access the pod’s services locally without exposing it via a service.

# Apply resource configuration from a file:

    kubectl apply -f <file.yaml>
    Applies the configuration in a YAML file to the cluster, creating or updating resources like pods, services, deployments, etc.

## Delete resources from a file:

    kubectl delete -f <file.yaml>
    Deletes the resources defined in a YAML file from the cluster.

## View resource details in YAML/JSON format:

    kubectl get <resource> <name> -o yaml
    Retrieves the YAML/JSON representation of a resource, which can be useful for understanding how resources are configured in the cluster.