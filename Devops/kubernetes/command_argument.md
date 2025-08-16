# Kubernetes Commands and Arguments: Complete Guide

## Table of Contents
- [Introduction](#introduction)
- [Understanding Docker Commands](#understanding-docker-commands)
- [CMD vs ENTRYPOINT in Docker](#cmd-vs-entrypoint-in-docker)
- [Commands and Arguments in Kubernetes](#commands-and-arguments-in-kubernetes)
- [Practical Examples](#practical-examples)
- [Best Practices](#best-practices)
- [Common Use Cases](#common-use-cases)
- [Troubleshooting](#troubleshooting)
- [Key Takeaways](#key-takeaways)

## Introduction

When working with Kubernetes Pods, you often need to customize how containers execute commands or pass specific arguments to running applications. This guide covers how to effectively use commands and arguments in Kubernetes Pod specifications.

**Important Concept**: In Kubernetes, the **container** (not the Pod) executes commands. The Pod is merely a wrapper that provides shared resources like networking and storage to one or more containers.

## Understanding Docker Commands

Before diving into Kubernetes, let's understand how commands work in Docker, as Kubernetes builds upon these concepts.

### Basic Command Execution in Docker

When you build a Docker image, you specify commands that the container will execute using Dockerfile instructions:

```dockerfile
FROM ubuntu
CMD ["echo", "Hello from container!"]
```

When you run a container from this image:
```bash
docker run my-image
# Output: Hello from container!
```

The `CMD` instruction defines the default command that runs when the container starts.

## CMD vs ENTRYPOINT in Docker

Understanding the difference between `CMD` and `ENTRYPOINT` is crucial for working with Kubernetes commands and arguments.

### CMD Instruction

```dockerfile
FROM ubuntu
CMD ["echo", "Default message"]
```

- **Overridable**: Can be completely replaced when running the container
- **Default behavior**: Runs if no command is specified

```bash
# Uses default CMD
docker run my-image
# Output: Default message

# Overrides CMD completely
docker run my-image ls -la
# Output: (directory listing, not "Default message")
```

### ENTRYPOINT Instruction

```dockerfile
FROM ubuntu
ENTRYPOINT ["echo"]
```

- **Fixed command**: Cannot be overridden, only appended to
- **Higher priority**: Always executes first

```bash
# Fails - no arguments provided to echo
docker run my-image

# Provides argument to echo
docker run my-image "Hello World"
# Output: Hello World
```

### Combined CMD and ENTRYPOINT

```dockerfile
FROM ubuntu
ENTRYPOINT ["echo"]
CMD ["Default argument"]
```

This combination provides flexibility:

```bash
# Uses default argument from CMD
docker run my-image
# Output: Default argument

# Overrides CMD argument, keeps ENTRYPOINT
docker run my-image "Custom message"
# Output: Custom message
```

## Commands and Arguments in Kubernetes

Kubernetes provides two fields to control container execution:
- **`command`**: Corresponds to Docker's `ENTRYPOINT`
- **`args`**: Corresponds to Docker's `CMD`

### Kubernetes to Docker Mapping

| Kubernetes Field | Docker Equivalent | Purpose |
|------------------|-------------------|---------|
| `command` | `ENTRYPOINT` | The main executable |
| `args` | `CMD` | Arguments passed to the executable |

### Basic Pod Definition with Commands

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: command-demo
spec:
  containers:
  - name: command-demo-container
    image: debian
    command: ["printenv"]  # Override ENTRYPOINT
    args: ["HOSTNAME", "KUBERNETES_PORT"]  # Override CMD
```

## Practical Examples

### Example 1: Environment Variable Display

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: env-display-pod
spec:
  containers:
  - name: env-container
    image: debian
    command: ["printenv"]
    args: ["HOSTNAME", "KUBERNETES_PORT"]
```

**Create and test:**
```bash
# Create the pod
kubectl apply -f env-display-pod.yaml

# Check pod status
kubectl get pods

# View output (pod will show "Completed" status)
kubectl logs env-display-pod
```

**Expected output:**
```
command-demo-7f8b9c5d6-abc123
tcp://10.96.0.1:443
```

### Example 2: Using Environment Variables in Commands

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: echo-demo
spec:
  containers:
  - name: echo-container
    image: debian
    env:
    - name: MESSAGE
      value: "Hello from Kubernetes!"
    - name: USER_NAME
      value: "developer"
    command: ["sh", "-c"]
    args: ["echo 'Message: $MESSAGE' && echo 'User: $USER_NAME'"]
```

**Test the pod:**
```bash
kubectl apply -f echo-demo.yaml
kubectl logs echo-demo
```

**Output:**
```
Message: Hello from Kubernetes!
User: developer
```

### Example 3: Running a Script with Arguments

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: script-runner
spec:
  containers:
  - name: script-container
    image: python:3.9-alpine
    command: ["python3", "-c"]
    args: 
    - |
      import os
      import sys
      print(f"Arguments received: {sys.argv[1:]}")
      print(f"Pod name: {os.environ.get('POD_NAME', 'unknown')}")
      print(f"Namespace: {os.environ.get('POD_NAMESPACE', 'unknown')}")
    env:
    - name: POD_NAME
      valueFrom:
        fieldRef:
          fieldPath: metadata.name
    - name: POD_NAMESPACE
      valueFrom:
        fieldRef:
          fieldPath: metadata.namespace
```

### Example 4: Conditional Command Execution

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: conditional-pod
spec:
  containers:
  - name: conditional-container
    image: busybox
    env:
    - name: ENVIRONMENT
      value: "production"
    command: ["sh", "-c"]
    args:
    - |
      if [ "$ENVIRONMENT" = "production" ]; then
        echo "Running in production mode"
        echo "Performing production setup..."
      else
        echo "Running in development mode"
        echo "Performing development setup..."
      fi
```

## Best Practices

### 1. Use Appropriate Images

Choose images that contain the tools you need:

```yaml
# Good: Use specific images for specific tasks
containers:
- name: database-backup
  image: postgres:13-alpine
  command: ["pg_dump"]
  args: ["-h", "database-host", "-U", "user", "dbname"]

# Good: Use utility images for shell operations
- name: file-processor
  image: busybox
  command: ["sh", "-c"]
  args: ["find /data -name '*.txt' | wc -l"]
```

### 2. Handle Secrets Securely

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: secure-command-pod
spec:
  containers:
  - name: app-container
    image: alpine
    command: ["sh", "-c"]
    args: ["echo 'Connecting with user: $DB_USER'"]
    env:
    - name: DB_USER
      valueFrom:
        secretKeyRef:
          name: db-credentials
          key: username
    - name: DB_PASSWORD
      valueFrom:
        secretKeyRef:
          name: db-credentials
          key: password
```

### 3. Use Multi-line Scripts Properly

```yaml
# Good: Readable multi-line script
args:
- |
  #!/bin/bash
  set -e
  echo "Starting application setup..."
  
  # Configuration
  export CONFIG_FILE="/app/config.yaml"
  
  # Validation
  if [ ! -f "$CONFIG_FILE" ]; then
    echo "Error: Config file not found"
    exit 1
  fi
  
  # Start application
  exec /app/start.sh
```

### 4. Resource Management for Command Pods

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: resource-managed-pod
spec:
  containers:
  - name: worker-container
    image: python:3.9
    command: ["python3"]
    args: ["-c", "import time; print('Working...'); time.sleep(30); print('Done')"]
    resources:
      requests:
        memory: "64Mi"
        cpu: "100m"
      limits:
        memory: "128Mi"
        cpu: "200m"
```

## Common Use Cases

### 1. Data Processing Jobs

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: data-processor
spec:
  containers:
  - name: processor
    image: python:3.9
    command: ["python3"]
    args: ["/scripts/process_data.py", "--input", "/data/input.csv", "--output", "/data/output.csv"]
    volumeMounts:
    - name: data-volume
      mountPath: /data
    - name: script-volume
      mountPath: /scripts
  volumes:
  - name: data-volume
    persistentVolumeClaim:
      claimName: data-pvc
  - name: script-volume
    configMap:
      name: processing-scripts
```

### 2. Database Migration

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: db-migration
spec:
  containers:
  - name: migration-runner
    image: migrate/migrate
    command: ["migrate"]
    args: 
    - "-path"
    - "/migrations"
    - "-database"
    - "postgres://user:password@db:5432/mydb?sslmode=disable"
    - "up"
    volumeMounts:
    - name: migration-files
      mountPath: /migrations
  volumes:
  - name: migration-files
    configMap:
      name: db-migrations
```

### 3. Backup Operations

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: backup-pod
spec:
  containers:
  - name: backup-container
    image: alpine
    command: ["sh", "-c"]
    args:
    - |
      apk add --no-cache aws-cli
      DATE=$(date +%Y%m%d-%H%M%S)
      tar -czf /tmp/backup-$DATE.tar.gz /data
      aws s3 cp /tmp/backup-$DATE.tar.gz s3://my-backup-bucket/
    env:
    - name: AWS_ACCESS_KEY_ID
      valueFrom:
        secretKeyRef:
          name: aws-credentials
          key: access-key-id
    - name: AWS_SECRET_ACCESS_KEY
      valueFrom:
        secretKeyRef:
          name: aws-credentials
          key: secret-access-key
    volumeMounts:
    - name: data-volume
      mountPath: /data
      readOnly: true
```

## Troubleshooting

### Common Issues and Solutions

#### 1. Pod Stuck in "ContainerCreating"

```bash
# Check pod events
kubectl describe pod <pod-name>

# Common causes:
# - Image pull issues
# - Volume mount problems
# - Resource constraints
```

#### 2. Pod Status "CrashLoopBackOff"

```bash
# Check logs
kubectl logs <pod-name>

# Check previous container logs
kubectl logs <pod-name> --previous

# Common causes:
# - Command exits immediately
# - Command not found in container
# - Permissions issues
```

#### 3. Command Not Found

```bash
# Verify command exists in container
kubectl exec <pod-name> -- which <command>

# List available commands
kubectl exec <pod-name> -- ls /bin /usr/bin
```

#### 4. Environment Variables Not Expanding

```yaml
# Wrong: Variables won't expand in array format
args: ["echo", "$MESSAGE"]

# Correct: Use shell for variable expansion
command: ["sh", "-c"]
args: ["echo $MESSAGE"]
```

### Debugging Commands

```bash
# Interactive debugging
kubectl run debug-pod --image=busybox -it --rm -- sh

# Execute commands in running pods
kubectl exec <pod-name> -- <command>

# Check environment variables
kubectl exec <pod-name> -- env

# Verify file system
kubectl exec <pod-name> -- ls -la /

# Check processes
kubectl exec <pod-name> -- ps aux
```

## Key Takeaways

### Essential Concepts

1. **Container Execution**: Commands run in containers, not pods
2. **Kubernetes Mapping**: `command` maps to `ENTRYPOINT`, `args` maps to `CMD`
3. **Override Behavior**: Kubernetes fields override Dockerfile instructions
4. **Environment Variables**: Use shell execution for variable expansion

### Command Execution Flow

```
Kubernetes Pod Spec → Container Runtime → Docker Image → Command Execution
```

### When to Use Commands and Arguments

- **One-time Jobs**: Data processing, migrations, backups
- **Initialization**: Setup scripts, configuration tasks  
- **Debugging**: Troubleshooting and investigation
- **Custom Entrypoints**: Override default application behavior

### Best Practices Summary

- Use appropriate base images with required tools
- Handle secrets and sensitive data securely  
- Implement proper error handling in scripts
- Set resource limits for command pods
- Use descriptive pod and container names
- Implement logging for debugging purposes

This comprehensive approach to commands and arguments will help you effectively manage container execution in Kubernetes environments.