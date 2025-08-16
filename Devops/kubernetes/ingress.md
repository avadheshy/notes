# Kubernetes Ingress Guide

## Introduction to Ingress

Ingress is an API object that manages external access to the services in a Kubernetes cluster, typically HTTP or HTTPS. It specifically handles external access coming from outside the cluster, such as from the Internet. For example, if you are running a web application inside a Pod in the Kubernetes cluster, ingress controls how users access it.

While services of type `NodePort` and `LoadBalancer` provide some external access, they are not sufficient when you have many applications or microservices. Ingress allows you to control different external access rules, such as routing based on URL paths or port numbers. It can also provide load balancing and SSL termination, so HTTPS connections can be terminated at the ingress, relieving internal Kubernetes components from handling SSL.

### How Ingress Works

Ingress exposes HTTP and HTTPS routes from outside the cluster to services within the cluster. Think of ingress as a load balancer where you can set various routing rules. For example, if someone accesses the path `/videos`, ingress can route that request to a specific service.

**Architecture Flow:**
1. User accesses ingress
2. Ingress routes the request to a service
3. Service routes it to the Pod
4. The service is typically of type `ClusterIP` (internal), and ingress exposes it externally

## Ingress Controller

To use ingress, you need an ingress controller. There are many types of ingress controllers available, and the market for them is growing rapidly.

### Popular Ingress Controllers

- **NGINX ingress controller** (most commonly used)
- **AKS Application Gateway Ingress Controller** (Azure)
- **Ambassador**
- **Apache**
- **BFE**
- **Contour**
- **Glue**
- **Skipper**
- **Traefik**

*This guide focuses on the NGINX ingress controller.*

## Installing NGINX Ingress Controller

The ingress controller is essentially an NGINX pod with a service of type `LoadBalancer` in front of it, typically a network load balancer.

### Installation Steps

1. Apply the manifest provided by the NGINX project:
   ```bash
   kubectl apply -f <nginx-ingress-manifest-url>
   ```

2. Verify the installation:
   ```bash
   kubectl get all -n ingress-nginx
   ```

### What Gets Created

- Namespace (`ingress-nginx`)
- Pods
- Services (LoadBalancer type)
- Deployments
- Replica sets
- Jobs
- Network load balancer in your cloud provider

## Application Deployment and Service

### Steps to Deploy Your Application

1. **Deploy your application** (e.g., Tomcat-based application pod)

2. **Create a ClusterIP service** that targets the pod's port (e.g., 8080)
   - This service is accessible only within the cluster
   - Cannot be accessed externally directly

## Ingress Resource and Rules

Ingress resources define rules that map external requests to internal services.

### Example Rule

Route requests to `vprofile.groophy.in/login` to your service:

**Request Flow:**
1. User accesses `http://vprofile.groophy.in/login`
2. Request goes to network load balancer
3. Load balancer forwards to ingress controller
4. Ingress controller routes to specified service on port 8080

### DNS Configuration Requirement

To use a custom domain like `vprofile.groophy.in`, you must create a DNS CNAME record pointing to the load balancer's DNS name.

## DNS Configuration

### Setting Up DNS

1. Go to your domain provider (e.g., GoDaddy)
2. Add a CNAME record
3. Map your desired subdomain (e.g., `vprofile`) to the load balancer's DNS name
4. Ensure no trailing dots or extra characters in the record

**Note:** DNS propagation may take some time, so plan accordingly.

## Creating and Verifying Ingress

### Steps

1. **Create the ingress resource:**
   ```bash
   kubectl apply -f ingress-manifest.yaml
   ```

2. **Verify the ingress resource:**
   ```bash
   kubectl get ingress
   ```

### Example

Accessing `http://vprofile.groophy.in/login` routes the request to the service named `myapp` on port 8080.

**Tip:** If your application internally handles routing, you may only need to specify the root path `/` in the ingress rule.

## Ingress Routing Examples

Ingress supports various routing rules for fine-grained control over how external traffic reaches your microservices.

### Path-based Routing

Routes requests based on URL paths:
- `/login` → routes to one service
- `/api` → routes to another service

### Host-based Routing

Routes requests based on the hostname:
- `vprofile.groophy.in` → routes to one service
- `api.groophy.in` → routes to another service

## Cleaning Up

After completing your experiments, remember to delete resources to avoid unnecessary charges, especially for cloud load balancers.

### Cleanup Methods

**Option 1: Delete entire namespace**
```bash
kubectl delete ns <namespace>
```
*Removes all associated resources*

**Option 2: Delete individual resources**
```bash
kubectl delete -f <manifest>
```

## Summary

Ingress is a powerful Kubernetes resource that manages external HTTP and HTTPS access to services inside the cluster. It provides:

- Advanced routing capabilities
- Load balancing
- SSL termination

### Setup Requirements

1. Install an ingress controller
2. Deploy your application and service
3. Configure DNS
4. Define ingress rules
5. Proper cleanup to avoid costs

## Key Takeaways

- **Ingress** is an API object that manages external HTTP and HTTPS access to services within a Kubernetes cluster
- **Advanced Features**: Provides routing rules, load balancing, and SSL termination for external traffic
- **Controller Required**: An ingress controller (such as NGINX) must be installed to implement ingress rules
- **DNS Configuration**: Proper DNS setup with CNAME records is essential to route external domain names to the ingress load balancer