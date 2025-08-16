# Understanding Pods in Kubernetes
## Introduction to Pods
In this section, we will understand what exactly pods are, how to run them, and how to use them in Kubernetes.

A pod is the most basic unit in Kubernetes. It is the smallest unit and represents a process running in your cluster. The most common use case is running one container per pod. If you use multiple containers, the additional containers are typically helper containers. A pod acts as a wrapper or boundary around your containers.

Kubernetes manages pods rather than managing containers directly. We interact with pods using commands or execution instructions for the pod, not for the container directly. In a multi-container pod, the containers are coupled and share the same resources provided by the pod. There is one main container and other helper containers, such as sidecar or init containers.

If you are running Tomcat, you create one pod for it. If you are running MySQL, you create another pod. For RabbitMQ, another pod. For high availability, you need multiple pods horizontally scaled, not multiple containers in a pod, but multiple pods. For example, multiple Tomcat pods or multiple NGINX pods horizontally scaled. This can be managed easily in Kubernetes.

## Running Pods in Kubernetes
Previously, we ran containers with the docker run command and used Docker Compose for better management. Similarly, you can run a direct pod workload on the Kubernetes cluster or use a definition file. The definition file is the most suitable way because it enables infrastructure as code. You do not need to run long commands on your shell; instead, you put everything in the definition file and run it.

A definition file will have these entries: apiVersion, kind, metadata, and spec. Most definition files will have these four entries. For a pod definition file, the kind will be Pod, and the object is pod with apiVersion: v1, which is the stable version. Other objects like service, deployment, or ingress may have different versions. For example, service uses v1, deployment uses apps/v1, and new objects may have beta versions before reaching stable releases.

The metadata section contains information about the pod, such as the name and labels (key-value pairs, similar to tags in AWS). The spec section contains the technical details. Remember, this is a YAML file. The apiVersion value is a string, kind is a string, metadata is a dictionary, and spec contains the technical details.

In the spec section, you define containers. Since it is a pod definition file, it will have containers inside. The containers field is a list, allowing multiple containers. Each container has a name and an image. You can also specify ports, which is also a list. Each port has a name and a containerPort number.

Example Pod Definition File Structure
Below is a typical structure of a pod definition file in YAML format.
```
apiVersion: v1
kind: Pod
metadata:
  name: vproapp
  labels:
    app: vproapp
spec:
  containers:
    - name: appcontainer
      image: imranvisualpath/freshtomcatapp:V7
      ports:
        - name: vproapp-port
          containerPort: 8080
```
To create the pod, use the following command:
```
kubectl create -f vproapppod.yaml
```
To get information about the pod, use:
```
kubectl get pod
```
The status will change as the pod comes to the running state. For more detailed information, use the describe command:
```
kubectl describe pod <pod-name>
```
At the end of the describe output, you will see events, which are useful for troubleshooting. For example, the default-scheduler schedules the pod, and kubelet pulls the image.

You can also edit a pod, but most fields are non-editable. To get the pod's YAML output, use:
```
kubectl get pod <pod-name> -o yaml
```
To edit a pod, use:
```
kubectl edit pod <pod-name>
```
## Creating and Managing Pod Definition Files
Let us see how to create a pod definition file in real time. First, create a directory called definitions and navigate into it. Then, create your pod definition file. For example, to run a Tomcat pod from the vProfile project, use your Docker Hub image.
```
mkdir definitions
cd definitions
touch vproapppod.yaml
```
In your YAML file, use three hyphens at the start. Specify kind: Pod, apiVersion: v1, metadata with the pod name and labels, and spec with containers. For the container, specify the name, image, and ports. The port number specified is the container's exposed port, not port mapping. Port mapping is handled differently, through services, which will be discussed next.

# Running and Inspecting the Pod
After saving your YAML file, run the following command to create the pod:
```
kubectl create -f vproapppod.yaml
```
Check the pod's status:
```
kubectl get pod
```
If the pod is being created, you will see the status as 'ContainerCreating'. Use the describe command to see what is happening:
```
kubectl describe pod vproapp
```
You will see events such as the default-scheduler assigning the pod to a node, and kubelet pulling the image. Once the container starts, check the pod status again. The output will show the pod name and readiness, such as 1/1 ready, meaning one container specified and one running.

# Deleting and Inspecting Pod Details
To delete your pod, use:
```
kubectl delete pod vproapp
```
Before deleting, you can inspect the pod details using the describe command. The pod will have an IP address, and you can see the container running inside, its container ID, and the port it is running on. The events section is helpful for troubleshooting if the container is not running.

# Conclusion
This covers the basics of pods in Kubernetes. Next, we will discuss services and how to perform port mapping and load balancing to access pods from the outside world.

# Key Takeaways
A pod is the most basic and smallest unit in Kubernetes, representing a process running in the cluster.
Pods are defined and managed using YAML definition files, specifying apiVersion, kind, metadata, and spec.
Kubernetes manages pods, not containers directly, and uses commands like kubectl create, kubectl get, and kubectl describe for pod management.
Pod definition files allow for infrastructure as code, making deployment and management more efficient.