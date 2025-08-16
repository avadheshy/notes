# Kubernetes ConfigMaps: Complete Configuration Management Guide

## Table of Contents
- [Introduction](#introduction)
- [Understanding ConfigMaps](#understanding-configmaps)
- [Creating ConfigMaps](#creating-configmaps)
- [Consuming ConfigMaps in Pods](#consuming-configmaps-in-pods)
- [Advanced ConfigMap Usage](#advanced-configmap-usage)
- [Best Practices](#best-practices)
- [Troubleshooting](#troubleshooting)
- [Real-World Examples](#real-world-examples)
- [Key Takeaways](#key-takeaways)

## Introduction

In Kubernetes, applications often require configuration data such as environment variables, configuration files, and other settings. ConfigMaps provide a way to decouple configuration artifacts from image content, making your applications more portable and easier to manage.

**Core Concept**: ConfigMaps store non-confidential data in key-value pairs and can be consumed by Pods as environment variables, command-line arguments, or as configuration files in volumes.

## Understanding ConfigMaps

### What are ConfigMaps?

ConfigMaps are Kubernetes objects that allow you to:
- Store configuration data separately from application code
- Inject configuration into Pods at runtime
- Update configuration without rebuilding container images
- Share configuration across multiple Pods

### ConfigMap vs Environment Variables

| Method | Scope | Flexibility | Management |
|--------|-------|-------------|------------|
| **Direct env vars** | Pod-specific | Limited | Scattered |
| **ConfigMaps** | Cluster-wide | High | Centralized |

### ConfigMap Data Types

ConfigMaps can store:
- **Simple key-value pairs**: Environment variables
- **Multi-line data**: Configuration files
- **Binary data**: Small files (though Secrets are preferred for sensitive data)

## Creating ConfigMaps

### Method 1: Imperative Creation (Command Line)

#### From Literal Values
```bash
# Create ConfigMap with literal key-value pairs
kubectl create configmap app-config \
  --from-literal=DATABASE_HOST=mysql.example.com \
  --from-literal=DATABASE_PORT=3306 \
  --from-literal=LOG_LEVEL=info

# View the created ConfigMap
kubectl get configmap app-config -o yaml
```

#### From Files
```bash
# Create from a single file
kubectl create configmap nginx-config --from-file=nginx.conf

# Create from multiple files
kubectl create configmap app-configs \
  --from-file=app.properties \
  --from-file=database.yaml

# Create from directory
kubectl create configmap web-config --from-file=./config-directory/
```

#### From Environment File
```bash
# Create .env file
cat > app.env << EOF
DATABASE_HOST=mysql.example.com
DATABASE_PORT=3306
CACHE_ENABLED=true
LOG_LEVEL=debug
EOF

# Create ConfigMap from env file
kubectl create configmap app-env-config --from-env-file=app.env
```

### Method 2: Declarative Creation (YAML)

#### Basic ConfigMap Example
```yaml
apiVersion: v1
kind: ConfigMap
metadata:
  name: database-config
  namespace: default
  labels:
    app: myapp
    component: database
data:
  # Simple key-value pairs
  MYSQL_DATABASE: "ecommerce"
  MYSQL_USER: "webapp"
  MYSQL_ROOT_PASSWORD: "rootpassword"
  DATABASE_PORT: "3306"
  MAX_CONNECTIONS: "100"
```

#### Advanced ConfigMap with Files
```yaml
apiVersion: v1
kind: ConfigMap
metadata:
  name: application-config
data:
  # Simple configuration values
  log_level: "info"
  debug_mode: "false"
  max_connections: "100"
  
  # Application properties file
  app.properties: |
    # Application Configuration
    server.port=8080
    spring.datasource.url=jdbc:mysql://db:3306/myapp
    spring.datasource.username=user
    spring.datasource.password=password
    
    # Logging configuration
    logging.level.com.myapp=DEBUG
    logging.pattern.console=%d{HH:mm:ss.SSS} [%thread] %-5level %logger{36} - %msg%n
    
  # Nginx configuration
  nginx.conf: |
    server {
        listen 80;
        server_name localhost;
        
        location / {
            proxy_pass http://backend:8080;
            proxy_set_header Host $host;
            proxy_set_header X-Real-IP $remote_addr;
        }
        
        location /health {
            access_log off;
            return 200 "healthy\n";
        }
    }
    
  # JSON configuration
  config.json: |
    {
      "database": {
        "host": "mysql.default.svc.cluster.local",
        "port": 3306,
        "name": "myapp"
      },
      "redis": {
        "host": "redis.default.svc.cluster.local",
        "port": 6379
      },
      "features": {
        "enable_caching": true,
        "enable_analytics": false
      }
    }
```

### Creating ConfigMaps
```bash
# Apply YAML file
kubectl apply -f configmap.yaml

# Verify creation
kubectl get configmaps
kubectl describe configmap application-config
```

## Consuming ConfigMaps in Pods

### Method 1: Environment Variables

#### Import All Keys as Environment Variables
```yaml
apiVersion: v1
kind: Pod
metadata:
  name: app-pod-envfrom
spec:
  containers:
  - name: app-container
    image: nginx:alpine
    envFrom:
    - configMapRef:
        name: database-config
    # All keys from database-config will be available as env vars
```

#### Import Specific Keys as Environment Variables
```yaml
apiVersion: v1
kind: Pod
metadata:
  name: app-pod-selective
spec:
  containers:
  - name: app-container
    image: nginx:alpine
    env:
    - name: DB_HOST
      valueFrom:
        configMapKeyRef:
          name: database-config
          key: MYSQL_DATABASE
    - name: DB_USER
      valueFrom:
        configMapKeyRef:
          name: database-config
          key: MYSQL_USER
    - name: LOG_LEVEL
      value: "info"  # Direct value
```

#### Mixed Environment Variables
```yaml
apiVersion: v1
kind: Pod
metadata:
  name: mixed-env-pod
spec:
  containers:
  - name: app-container
    image: myapp:latest
    env:
    # Direct environment variables
    - name: APP_NAME
      value: "my-application"
    - name: APP_VERSION
      value: "1.0.0"
    # From ConfigMap
    - name: DATABASE_URL
      valueFrom:
        configMapKeyRef:
          name: database-config
          key: MYSQL_DATABASE
    # From Secret
    - name: API_KEY
      valueFrom:
        secretKeyRef:
          name: api-credentials
          key: api-key
    envFrom:
    # Import all from ConfigMap
    - configMapRef:
        name: application-config
    # Import all from another ConfigMap
    - configMapRef:
        name: feature-flags
```

### Method 2: Volume Mounts (Configuration Files)

#### Mount Entire ConfigMap as Files
```yaml
apiVersion: v1
kind: Pod
metadata:
  name: config-files-pod
spec:
  containers:
  - name: app-container
    image: nginx:alpine
    volumeMounts:
    - name: config-volume
      mountPath: /etc/config
      readOnly: true
    command: ["/bin/sh"]
    args: ["-c", "while true; do sleep 30; done"]
  volumes:
  - name: config-volume
    configMap:
      name: application-config
```

#### Mount Specific Keys as Files
```yaml
apiVersion: v1
kind: Pod
metadata:
  name: selective-config-pod
spec:
  containers:
  - name: nginx-container
    image: nginx:alpine
    volumeMounts:
    - name: nginx-config
      mountPath: /etc/nginx/conf.d
      readOnly: true
    - name: app-config
      mountPath: /etc/app
      readOnly: true
  volumes:
  - name: nginx-config
    configMap:
      name: application-config
      items:
      - key: nginx.conf
        path: default.conf
  - name: app-config
    configMap:
      name: application-config
      items:
      - key: app.properties
        path: application.properties
      - key: config.json
        path: config.json
```

#### Mount with Custom File Permissions
```yaml
apiVersion: v1
kind: Pod
metadata:
  name: permissions-pod
spec:
  containers:
  - name: app-container
    image: alpine:latest
    volumeMounts:
    - name: config-volume
      mountPath: /etc/myapp
    command: ["/bin/sh", "-c", "ls -la /etc/myapp && sleep 3600"]
  volumes:
  - name: config-volume
    configMap:
      name: application-config
      defaultMode: 0644
      items:
      - key: app.properties
        path: app.properties
        mode: 0600  # Only owner can read/write
```

### Method 3: Command Line Arguments

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: args-pod
spec:
  containers:
  - name: app-container
    image: busybox
    command: ["/bin/sh"]
    args: ["-c", "echo Database: $(DATABASE_HOST):$(DATABASE_PORT)"]
    envFrom:
    - configMapRef:
        name: database-config
```

## Advanced ConfigMap Usage

### Automatic ConfigMap Updates

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: auto-update-pod
spec:
  containers:
  - name: app-container
    image: nginx:alpine
    volumeMounts:
    - name: config-volume
      mountPath: /etc/config
    # Application should watch for file changes
  volumes:
  - name: config-volume
    configMap:
      name: application-config
      # Files will be updated when ConfigMap changes (may take up to 60 seconds)
```

### ConfigMap with SubPath

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: subpath-pod
spec:
  containers:
  - name: nginx-container
    image: nginx:alpine
    volumeMounts:
    - name: nginx-config
      mountPath: /etc/nginx/nginx.conf
      subPath: nginx.conf  # Mount only this file, not entire directory
      readOnly: true
  volumes:
  - name: nginx-config
    configMap:
      name: application-config
```

## Best Practices

### 1. Naming Conventions

```yaml
# Good: Descriptive names
apiVersion: v1
kind: ConfigMap
metadata:
  name: webapp-database-config
  labels:
    app: webapp
    component: database
    environment: production

# Good: Environment-specific naming
metadata:
  name: webapp-config-prod
  name: webapp-config-dev
  name: webapp-config-test
```

### 2. Organization and Structure

```yaml
# Organize by application component
apiVersion: v1
kind: ConfigMap
metadata:
  name: webapp-frontend-config
data:
  API_URL: "https://api.example.com"
  ENABLE_ANALYTICS: "true"
  
---
apiVersion: v1
kind: ConfigMap
metadata:
  name: webapp-backend-config
data:
  DATABASE_HOST: "postgres.example.com"
  CACHE_TTL: "3600"
```

### 3. Environment Management

```bash
# Use overlays for different environments
kubectl apply -f base/
kubectl apply -f overlays/development/
kubectl apply -f overlays/production/
```

### 4. Configuration Validation

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: validation-pod
spec:
  initContainers:
  - name: config-validator
    image: busybox
    command: ["/bin/sh", "-c"]
    args:
    - |
      echo "Validating configuration..."
      if [ -z "$DATABASE_HOST" ]; then
        echo "ERROR: DATABASE_HOST not set"
        exit 1
      fi
      if [ -z "$API_KEY" ]; then
        echo "ERROR: API_KEY not set"  
        exit 1
      fi
      echo "Configuration validation passed"
    envFrom:
    - configMapRef:
        name: application-config
  containers:
  - name: app-container
    image: myapp:latest
    envFrom:
    - configMapRef:
        name: application-config
```

### 5. Size Limitations

```yaml
# ConfigMaps have a 1MB size limit
# For large configurations, consider:
# 1. Multiple ConfigMaps
# 2. External configuration management
# 3. Init containers to fetch config

apiVersion: v1
kind: ConfigMap
metadata:
  name: large-config-part1
data:
  config-section-1: |
    # Large configuration part 1
    
---
apiVersion: v1
kind: ConfigMap  
metadata:
  name: large-config-part2
data:
  config-section-2: |
    # Large configuration part 2
```

## Troubleshooting

### Common Issues and Solutions

#### 1. ConfigMap Not Found
```bash
# Check if ConfigMap exists
kubectl get configmap
kubectl get configmap <name> -o yaml

# Check namespace
kubectl get configmap -n <namespace>

# Describe pod for error details
kubectl describe pod <pod-name>
```

#### 2. Environment Variables Not Available
```bash
# Check pod environment
kubectl exec <pod-name> -- env | grep <VARIABLE>

# Verify ConfigMap keys
kubectl get configmap <name> -o yaml

# Check pod logs
kubectl logs <pod-name>
```

#### 3. Configuration Files Not Mounted
```bash
# Check mount points
kubectl exec <pod-name> -- ls -la /etc/config

# Verify volume mounts
kubectl describe pod <pod-name>

# Check file contents
kubectl exec <pod-name> -- cat /etc/config/<filename>
```

#### 4. Permission Issues
```bash
# Check file permissions
kubectl exec <pod-name> -- ls -la /etc/config

# Update ConfigMap with proper modes
kubectl patch configmap <name> -p '{"data":{"file":"content"}}'
```

### Debugging Commands

```bash
# View ConfigMap contents
kubectl get configmap <name> -o yaml
kubectl describe configmap <name>

# Test ConfigMap in temporary pod
kubectl run test-pod --image=busybox -it --rm \
  --env="TEST_VAR=value" \
  -- /bin/sh

# Check environment variables in pod
kubectl exec <pod-name> -- printenv

# View mounted files
kubectl exec <pod-name> -- find /etc/config -type f -exec cat {} \;

# Monitor ConfigMap changes
kubectl get configmap <name> -w
```

## Real-World Examples

### Example 1: Web Application with Database

```yaml
# Database ConfigMap
apiVersion: v1
kind: ConfigMap
metadata:
  name: webapp-db-config
data:
  DATABASE_HOST: "postgresql.default.svc.cluster.local"
  DATABASE_PORT: "5432"
  DATABASE_NAME: "webapp_production"
  CONNECTION_POOL_SIZE: "20"
  CONNECTION_TIMEOUT: "30"

---
# Application ConfigMap  
apiVersion: v1
kind: ConfigMap
metadata:
  name: webapp-app-config
data:
  LOG_LEVEL: "info"
  ENABLE_DEBUG: "false"
  SESSION_TIMEOUT: "3600"
  
  # Application properties file
  application.yaml: |
    server:
      port: 8080
      servlet:
        context-path: /api
    
    logging:
      level:
        com.webapp: INFO
        org.springframework: WARN
    
    management:
      endpoints:
        web:
          exposure:
            include: health,info,metrics

---
# Web Application Pod
apiVersion: v1
kind: Pod
metadata:
  name: webapp-pod
spec:
  containers:
  - name: webapp
    image: webapp:1.0.0
    ports:
    - containerPort: 8080
    envFrom:
    - configMapRef:
        name: webapp-db-config
    - configMapRef:
        name: webapp-app-config
    volumeMounts:
    - name: app-config
      mountPath: /etc/webapp
      readOnly: true
  volumes:
  - name: app-config
    configMap:
      name: webapp-app-config
```

### Example 2: Multi-Container Pod with Shared Configuration

```yaml
apiVersion: v1
kind: ConfigMap
metadata:
  name: shared-config
data:
  REDIS_HOST: "redis.default.svc.cluster.local"
  REDIS_PORT: "6379"
  LOG_LEVEL: "info"
  
  nginx.conf: |
    upstream backend {
        server localhost:8080;
    }
    
    server {
        listen 80;
        location / {
            proxy_pass http://backend;
        }
    }

---
apiVersion: v1
kind: Pod
metadata:
  name: multi-container-pod
spec:
  containers:
  # Frontend container
  - name: nginx
    image: nginx:alpine
    ports:
    - containerPort: 80
    volumeMounts:
    - name: nginx-config
      mountPath: /etc/nginx/conf.d
      readOnly: true
      
  # Backend container  
  - name: app
    image: myapp:latest
    ports:
    - containerPort: 8080
    envFrom:
    - configMapRef:
        name: shared-config
        
  volumes:
  - name: nginx-config
    configMap:
      name: shared-config
      items:
      - key: nginx.conf
        path: default.conf
```

### Example 3: ConfigMap with Secrets Integration

```yaml
# ConfigMap for non-sensitive data
apiVersion: v1
kind: ConfigMap
metadata:
  name: app-config
data:
  DATABASE_HOST: "postgres.example.com"
  DATABASE_PORT: "5432"
  LOG_LEVEL: "info"
  FEATURE_FLAG_ANALYTICS: "true"

---
# Secret for sensitive data
apiVersion: v1
kind: Secret
metadata:
  name: app-secrets
type: Opaque
stringData:
  DATABASE_PASSWORD: "super-secret-password"
  API_KEY: "secret-api-key"

---
# Pod using both ConfigMap and Secret
apiVersion: v1
kind: Pod
metadata:
  name: secure-app-pod
spec:
  containers:
  - name: app
    image: myapp:latest
    env:
    # From ConfigMap
    - name: DB_HOST
      valueFrom:
        configMapKeyRef:
          name: app-config
          key: DATABASE_HOST
    # From Secret
    - name: DB_PASSWORD
      valueFrom:
        secretKeyRef:
          name: app-secrets
          key: DATABASE_PASSWORD
    envFrom:
    # All non-sensitive config
    - configMapRef:
        name: app-config
    # All sensitive config  
    - secretRef:
        name: app-secrets
```

## Key Takeaways

### Essential Concepts

1. **Separation of Concerns**: ConfigMaps separate configuration from application code
2. **Runtime Injection**: Configuration is injected at Pod creation time
3. **Multiple Consumption Methods**: Environment variables, files, or command arguments
4. **Cluster-Wide Resource**: ConfigMaps can be shared across multiple Pods

### Configuration Management Flow

```
ConfigMap Creation → Pod Reference → Runtime Injection → Container Access
```

### When to Use ConfigMaps

- **Application Settings**: Database connections, API endpoints, feature flags
- **Configuration Files**: Application config files, web server configurations
- **Environment-Specific Values**: Different values for dev/staging/production
- **Shared Configuration**: Common settings across multiple applications

### ConfigMap vs Secrets

| Use Case | ConfigMap | Secret |
|----------|-----------|---------|
| **Non-sensitive data** | ✅ Yes | ❌ No |
| **Sensitive data** | ❌ No | ✅ Yes |
| **Configuration files** | ✅ Yes | ✅ Yes |
| **Environment variables** | ✅ Yes | ✅ Yes |
| **Base64 encoding** | ❌ No | ✅ Yes |

### Best Practices Summary

- Use descriptive names for ConfigMaps and keys
- Organize ConfigMaps by application or component
- Validate configuration before application startup
- Use appropriate consumption method for your use case
- Keep ConfigMaps under the 1MB size limit
- Consider using Secrets for sensitive data
- Implement proper RBAC for ConfigMap access
- Document your configuration structure and usage

ConfigMaps are fundamental to modern Kubernetes application deployment, providing flexible and maintainable configuration management that scales with your applications.