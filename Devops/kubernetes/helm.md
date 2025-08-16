# Complete Helm Guide - Kubernetes Package Manager

## Introduction to Helm

Helm is the Kubernetes package manager that allows you to manage your application as a single package on a Kubernetes cluster.

### Why Use Helm?

To run a complete application, we use multiple Kubernetes objects like:
- Deployment
- Service
- Ingress
- Volumes
- Secrets
- Config Maps
- DaemonSets
- StatefulSets

Managing these objects in separate files can be overwhelming. Helm converts these definition files into a single **Helm chart**, making your application a bundle of different Kubernetes objects.

### Benefits of Helm

- **Single Suite Deployment**: Deploy your application as one unit
- **Simple Management**: Use simple commands like `helm install myapp`, `helm uninstall`
- **Version Control**: Version your application easily
- **Templating**: Use variables and templates for configuration
- **Easy Updates**: Make minor changes and upgrades seamlessly

## Helm Terminology

### Charts (Helm Charts)
Collections of your Kubernetes objects and resources like deployments, services, ingress, volumes, etc. Charts are pre-configured resource bundles.

### Repositories
Storage locations where you can store and download Helm charts. There are predefined repositories with ready-made applications.

### Release
An instance of a chart running in the Kubernetes cluster. When you deploy a Helm chart, it's called a release.

### Values
Variables or defined values of variables that configure your charts. These are typically stored in `values.yaml`.

## Helm Chart Structure

When you create a Helm chart using `helm create myapp`, it creates a directory structure:

```
myapp/
├── Chart.yaml          # Chart metadata (name, version)
├── values.yaml         # Default values for variables
└── templates/          # Kubernetes resource templates
    ├── deployment.yaml
    ├── service.yaml
    ├── ingress.yaml
    └── ...
```

### Key Components

- **Templates Folder**: Contains all resources with variable names instead of hard-coded values
- **values.yaml**: Defines the actual values for variables used in templates
- **Chart.yaml**: Contains chart name and version information

## Basic Helm Commands

### Installation and Management
```bash
# Install a chart
helm install <release-name> <chart-path>

# Upgrade a release
helm upgrade <release-name> <chart-path>

# Uninstall a release
helm uninstall <release-name>

# List releases
helm list
```

### Repository Management
```bash
# Add a repository
helm repo add <name> <URL>

# Update repositories
helm repo update

# Search for charts
helm search repo <keyword>
```

### Chart Development
```bash
# Create a new chart
helm create <chart-name>

# Lint a chart
helm lint <chart-path>

# Render templates (dry run)
helm template <chart-path>
```

## Hands-On Exercise: WordPress with MySQL

### Prerequisites

1. **Kubernetes Cluster**: Running cluster with nginx ingress controller
2. **kubectl**: Configured to access your cluster
3. **Helm**: Installed on your local machine

### Installation Commands

**Helm Installation:**
- **macOS**: `brew install helm`
- **Windows**: `choco install kubernetes-helm`

**Verify Installation:**
```bash
kubectl get nodes
helm version
```

### Setting Up the Environment

#### 1. Install Amazon Q Extension (VSCode)
- Open VSCode Extensions
- Search for "Amazon Q" and install
- Authenticate with AWS account
- Use for generating Kubernetes definitions

#### 2. Create Project Structure
```bash
mkdir wordpress-project
cd wordpress-project
```

### WordPress and MySQL Setup

#### Required Kubernetes Resources

**For MySQL:**
- Deployment (MySQL 8.0 image)
- Service (port 3306)
- Persistent Volume Claim (20GB)
- Secret (database credentials)

**For WordPress:**
- Deployment (WordPress image)
- Service (LoadBalancer type)
- Persistent Volume Claim (20GB)
- Ingress (for external access)

#### Using AI to Generate Kubernetes Files

**Amazon Q Prompt Example:**
```
Create separate Kubernetes definition files for:
1. WordPress application deployment and service
2. MySQL database deployment and service
3. Persistent Volume Claims for both (default storage class)
4. Secret file with database users and passwords
5. Ingress with hostname: wordpress.yourdomain.com

Use appropriate environment variables and mount points.
```

### Converting to Helm Charts

#### 1. Create Helm Chart
```bash
helm create wp-chart
```

#### 2. Customize Chart Structure

**Directory Structure:**
```
wp-chart/
├── Chart.yaml
├── values.yaml
└── templates/
    ├── mysql-deployment.yaml
    ├── mysql-service.yaml
    ├── mysql-pvc.yaml
    ├── wordpress-deployment.yaml
    ├── wordpress-service.yaml
    ├── wordpress-pvc.yaml
    ├── ingress.yaml
    └── secret.yaml
```

#### 3. Template Variables Example

**In deployment.yaml:**
```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: {{ include "wp-chart.fullname" . }}-mysql
spec:
  replicas: {{ .Values.mysql.replicaCount }}
  template:
    spec:
      containers:
      - name: mysql
        image: "{{ .Values.mysql.image.repository }}:{{ .Values.mysql.image.tag }}"
        ports:
        - containerPort: 3306
        env:
        - name: MYSQL_ROOT_PASSWORD
          valueFrom:
            secretKeyRef:
              name: {{ include "wp-chart.fullname" . }}-secret
              key: mysql-root-password
```

**In values.yaml:**
```yaml
mysql:
  replicaCount: 1
  image:
    repository: mysql
    tag: "8.0"
  persistence:
    enabled: true
    size: 20Gi

wordpress:
  replicaCount: 1
  image:
    repository: wordpress
    tag: latest
  persistence:
    enabled: true
    size: 20Gi

ingress:
  enabled: true
  hostname: wordpress.yourdomain.com
```

### Deployment and Management

#### 1. Validate Chart
```bash
# Lint the chart
helm lint wp-chart

# Render templates (dry run)
helm template wp-chart
```

#### 2. Deploy Application
```bash
# Install with namespace creation
helm install wp wp-chart --namespace wp-ns --create-namespace

# Verify deployment
helm list -n wp-ns
kubectl get all -n wp-ns
```

#### 3. Update and Upgrade
```bash
# Edit values or templates
# Increment version in Chart.yaml (0.1.0 → 0.1.1)

# Upgrade release
helm upgrade wp wp-chart -n wp-ns
```

#### 4. Access Application

**DNS Configuration:**
- Add CNAME record in your domain registrar
- Map subdomain to load balancer endpoint
- Or edit local hosts file for testing

**Example hosts entry:**
```
<load-balancer-ip> wordpress.yourdomain.com
```

### Advanced Helm Features

#### Conditional Resource Creation
```yaml
{{- if .Values.mysql.persistence.enabled }}
apiVersion: v1
kind: PersistentVolumeClaim
metadata:
  name: {{ include "wp-chart.fullname" . }}-mysql-pvc
spec:
  accessModes:
    - ReadWriteOnce
  resources:
    requests:
      storage: {{ .Values.mysql.persistence.size }}
{{- end }}
```

#### Using Helm Functions
```yaml
metadata:
  name: {{ include "wp-chart.fullname" . }}-mysql
  labels:
    {{- include "wp-chart.labels" . | nindent 4 }}
```

## Best Practices

### Chart Development Best Practices

1. **Use Include Functions**: For consistent naming and labeling
2. **Proper Indentation**: Maintain YAML syntax correctness
3. **Variable Management**: Import blocks from values.yaml
4. **Security**: Don't store plaintext passwords
5. **Resource Limits**: Define appropriate resource constraints
6. **Conditional Logic**: Use if/else blocks for optional resources

### AI-Assisted Development

**Using Amazon Q Developer:**
- Generate initial Kubernetes definitions
- Convert definitions to Helm charts
- Improve charts with best practices
- Add advanced templating features

**Example AI Prompt for Improvements:**
```
Improve the existing Helm charts according to development best practices. 
Add proper naming conventions, resource limits, health checks, and 
security considerations.
```

### Security Considerations

1. **Secrets Management**: Use Kubernetes secrets, not plaintext
2. **RBAC**: Implement proper role-based access control
3. **Network Policies**: Restrict inter-pod communication
4. **Image Security**: Use specific image tags, not "latest"
5. **Resource Limits**: Set CPU and memory limits

### Maintenance and Cleanup

```bash
# Uninstall release
helm uninstall wp -n wp-ns

# Delete namespace
kubectl delete namespace wp-ns

# Clean up cluster resources
kubectl delete pv <persistent-volume-name>
```

## Troubleshooting Common Issues

### Chart Validation Errors
- Run `helm lint` to identify syntax issues
- Use `helm template` to render and review output
- Check indentation and YAML formatting

### Deployment Issues
- Verify cluster connectivity: `kubectl get nodes`
- Check namespace and release status: `helm list -A`
- Review pod logs: `kubectl logs -n <namespace> <pod-name>`

### Ingress Problems
- Ensure ingress controller is installed
- Check ingress class name configuration
- Verify DNS resolution and load balancer status

## Learning Resources

### Recommended Helm Documentation
- **Introduction**: Basic concepts and terminology
- **Quick Start Guide**: Get started with Helm
- **Chart Development**: Creating and customizing charts
- **Tips and Tricks**: Advanced techniques
- **Best Practices**: Industry standards and recommendations

### Continuous Learning
- Practice creating charts for different applications
- Explore public Helm repositories (Artifact Hub)
- Use AI code assistants for learning and improvement
- Join Helm community forums and discussions

## Summary

Helm significantly simplifies Kubernetes application management by:

- **Packaging**: Bundling multiple Kubernetes resources into single charts
- **Templating**: Using variables for flexible, reusable configurations
- **Versioning**: Managing application versions and rollbacks
- **Automation**: Streamlining deployment and upgrade processes

### Key Takeaways

- **Helm acts as a package manager** for Kubernetes applications, bundling multiple objects into deployable charts
- **Charts consist of templates** with variables defined in values.yaml for easy configuration
- **Simple commands** enable installation, upgrading, and uninstalling of applications
- **AI tools** like Amazon Q Developer can assist in generating and enhancing Helm charts
- **Best practices** include proper templating, security considerations, and resource management
- **Continuous practice** and leveraging documentation are essential for mastering Helm