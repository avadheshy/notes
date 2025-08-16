# Kubernetes Namespaces

## Introduction to Namespaces

In this lecture, we will discuss namespaces and how you can group or isolate your resources within a Kubernetes cluster.

A Kubernetes cluster can have multiple namespaces. These namespaces are used to set various kinds of security policies, quotas, and other configurations for your resources.

When you create a cluster, some namespaces are created automatically, such as:
- `default`
- `kube-system` 
- `kube-public`

However, you can add more namespaces and specify in which namespace your resources get created.

If you run the command `kubectl get namespaces`, you can see the existing namespaces. You can also create additional namespaces, for example, one for your development environment and another for production. This allows you to isolate your environments effectively. You can also create different namespaces for different projects.

## What Are Namespaces?

According to the documentation, namespaces provide a mechanism for isolating groups of resources within a single cluster. The names of resources need to be unique within a namespace. For example, if you have a pod named `nginx1` in one namespace, you cannot have another pod with the same name in that namespace. However, you can have pods with the same name in different namespaces.

**Important:** Resource names must be unique within a namespace but not across namespaces.

## When to Use Multiple Namespaces

In small environments, people often do not use namespaces and create most resources in the default namespace. However, when you have many users, multiple projects, or multiple environments to manage, it is better to create namespaces and group your resources accordingly.

From experience, when you create your own namespace, it is very easy to delete the entire namespace. Deleting the namespace removes all resources within it with a single command. While this can be dangerous, it is also useful for cleanup.

## Viewing Namespaces and Resources

### Basic Commands

- **View namespaces:** `kubectl get ns`
  - Shows namespaces such as `default`, `node-lease`, `kube-system`, and `kube-public`

- **View all objects in default namespace:** `kubectl get all`
  - Shows all objects in the default namespace by default

- **View resources across all namespaces:** `kubectl get all --all-namespaces`
  - Displays information including ReplicaSets, Deployments, DaemonSets, Services, and Pods in different namespaces

### Namespace-Specific Views

In the `kube-system` namespace, you will find all your control plane resources running as pods, such as:
- etcd manager
- controller
- proxy
- scheduler pods

To look at resources in a specific namespace, use the `-n` flag:
```bash
kubectl get svc -n kube-system
```

## Creating and Using Namespaces

### Creating a Namespace

Create your own namespace:
```bash
kubectl create ns kubekart
```

### Running Resources in a Specific Namespace

Run a pod in a specific namespace:
```bash
kubectl run nginx --namespace=kubekart
```

You can have pods with the same name in different namespaces. If you try to create a pod with the same name in the same namespace, it will fail because the resource already exists.

## Specifying Namespace in Definition Files

In your pod definition file, you can specify the namespace in the metadata section:

```yaml
metadata:
  name: nginx12
  namespace: kubekart
```

Apply the configuration:
```bash
kubectl apply -f <file>
```

Verify pods running in a specific namespace:
```bash
kubectl get pod -n kubekart
```

## Deleting a Namespace

You can delete an entire namespace and all its resources:
```bash
kubectl delete ns kubekart
```

⚠️ **Warning:** This is a powerful command that removes everything within the namespace and the namespace itself. Use it with caution.

## Additional Notes

- Take your time to go through the documentation on namespaces
- You can specify the namespace in the kubeconfig file so that every time you use the kubectl command, it uses that namespace by default unless you specify otherwise
- Please test the commands and review the documentation

## Key Takeaways

- Kubernetes clusters can have multiple namespaces to group or isolate resources
- Namespaces help set security policies, quotas, and manage resource isolation
- Resource names must be unique within a namespace but can be duplicated across namespaces
- Deleting a namespace removes all resources within it, which is a powerful but potentially dangerous operation