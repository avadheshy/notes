# Difference between cluster, node and pod
1. Cluster
   
   __A cluster is the highest-level container in Kubernetes. It consists of a group of nodes (which can be physical or virtual machines) that work together to run containerized applications.__

    __The cluster contains the control plane (e.g., the API server, controller manager, etcd) and worker nodes, which together orchestrate the deployment and scaling of applications.__
2.  Node
   
    __A node is a machine (physical or virtual) within the Kubernetes cluster. It provides the computational resources needed to run pods__

    __Each node runs:__

> kubelet, which is the primary agent that communicates with the control plane.

> Container runtime (e.g., Docker or containerd), responsible for running containers.

>kube-proxy, which manages networking for services on the node.

__There are typically two types of nodes:__

__Master Node:__ Responsible for managing the Kubernetes cluster (API server, scheduling, etc.).

__Worker Node__: Executes the containers inside pods.

3. Pod

        A pod is the smallest deployable unit in Kubernetes. It represents one or more tightly coupled containers that share the same network namespace and storage.

        Pods are the entities where your application’s containerized workloads are run. Each pod can contain one or multiple containers (usually one) that work together.

        Pods are created and scheduled to run on nodes within the cluster. Each pod gets its own unique IP address, and containers inside a pod can communicate with each other directly using localhost.


## component of Controle Plane
1. API Server:

    It is used for communication perpos.

2.  Scheduler :

        It is used for assign node to newly created pod.

3.  ETCD

I       t is used to store current state of cluster in the form of key-pair.

4. Controller Mannager
 
        Responsible for managing state of clusetr

 ## Component of Data Plane

 1. Kubelate 

            It is responsible for communication with controlle plain and make sures every containe is running in pods.

 2. POD
 
        It is smallest unite in Kubernetes

 3. Kube Proxy :
 
        Is responsible for network communication

 4. Container runtime: 
 
        tool responsible for running container.