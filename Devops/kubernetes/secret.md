# Kubernetes Secrets: Managing Sensitive Data Securely

## Introduction to Kubernetes Secrets

Kubernetes Secrets provide a way to store and manage sensitive information such as passwords, OAuth tokens, SSH keys, and Docker registry credentials. Unlike ConfigMaps, which store data in plain text, Secrets store data in an encoded format to prevent accidental exposure.

### The Problem with Plain Text Storage

When using ConfigMaps for sensitive data:
- Passwords and credentials are stored in clear text
- Definition files are typically stored in git repositories
- Anyone with repository access can see sensitive information
- Security risks increase with plain text exposure

### The Solution with Secrets

Secrets provide:
- Encoded storage of sensitive data
- Safe injection into pod definitions
- Multiple types for different use cases
- Better security practices for credential management

> **Important**: Secrets use base64 encoding, not encryption. This is encoding for obfuscation, not a security measure.

## Creating Secrets

### Imperative Method

```bash
kubectl create secret generic <secret-name> --from-literal=<key>=<value>
```

**Example:**
```bash
kubectl create secret generic mysecret --from-literal=username=admin --from-literal=password=mysecretpass
```

### Understanding Base64 Encoding

Secrets encode values using base64. You can manually encode/decode values:

#### Encoding
```bash
echo -n 'secret pass' | base64
# Output: c2VjcmV0IHBhc3M=
```

#### Decoding
```bash
echo 'c2VjcmV0IHBhc3M=' | base64 -d
# Output: secret pass
```

> **Security Note**: Base64 is encoding, not encryption. Anyone with access to the Kubernetes control plane can retrieve and decode values.

### Declarative Method

For declarative creation, you must first encode your data:

1. **Encode your values:**
```bash
echo -n 'admin' | base64          # Output: YWRtaW4=
echo -n 'mysecretpass' | base64   # Output: bXlzZWNyZXRwYXNz
```

2. **Create the Secret definition file (mysecret.yaml):**
```yaml
apiVersion: v1
kind: Secret
metadata:
  name: mysecret
type: Opaque
data:
  username: YWRtaW4=           # base64 encoded 'admin'
  password: bXlzZWNyZXRwYXNz   # base64 encoded 'mysecretpass'
```

3. **Apply the Secret:**
```bash
kubectl create -f mysecret.yaml
```

## Types of Secrets

Kubernetes supports several Secret types:

| Type | Description | Use Case |
|------|-------------|----------|
| `Opaque` | Default type for arbitrary user-defined data | General passwords, API keys |
| `kubernetes.io/service-account-token` | Service account token | Kubernetes authentication |
| `kubernetes.io/dockercfg` | Docker configuration | Docker registry authentication |
| `kubernetes.io/dockerconfigjson` | Docker configuration JSON | Modern Docker registry auth |
| `kubernetes.io/ssh-auth` | SSH authentication | SSH keys |
| `kubernetes.io/tls` | TLS certificates | SSL/TLS certificates |

## Using Secrets in Pod Definitions

### Method 1: Import All Keys with envFrom

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: secret-pod
spec:
  containers:
  - name: mycontainer
    image: nginx
    envFrom:
    - secretRef:
        name: mysecret
```

### Method 2: Selective Import with valueFrom

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: secret-pod
spec:
  containers:
  - name: mycontainer
    image: nginx
    env:
    - name: SECRET_USERNAME
      valueFrom:
        secretKeyRef:
          name: mysecret
          key: username
    - name: SECRET_PASSWORD
      valueFrom:
        secretKeyRef:
          name: mysecret
          key: password
```

## Docker Registry Secrets

### Creating Docker Registry Secrets

For private Docker registries, use the `docker-registry` type:

```bash
kubectl create secret docker-registry <secret-name> \
  --docker-username=<username> \
  --docker-password=<password> \
  --docker-email=<email> \
  --docker-server=<server>
```

**Example:**
```bash
kubectl create secret docker-registry myregistry-secret \
  --docker-username=myuser \
  --docker-password=mypassword \
  --docker-email=myuser@example.com \
  --docker-server=myregistry.com:5000
```

### Using Docker Registry Secrets

Reference the Secret in your pod definition:

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: private-reg-pod
spec:
  containers:
  - name: private-reg-container
    image: myregistry.com:5000/my-app:latest
  imagePullSecrets:
  - name: myregistry-secret
```

## Complete Example: Creating and Using a Secret

### Step 1: Create the Secret

**Create mysecret.yaml:**
```yaml
apiVersion: v1
kind: Secret
metadata:
  name: mysecret
type: Opaque
data:
  username: YWRtaW4=           # 'admin' in base64
  password: bXlzZWNyZXRwYXNz   # 'mysecretpass' in base64
```

**Apply the Secret:**
```bash
kubectl create -f mysecret.yaml
```

### Step 2: Create a Pod Using the Secret

**Create readsecret.yaml:**
```yaml
apiVersion: v1
kind: Pod
metadata:
  name: secret-test-pod
spec:
  containers:
  - name: test-container
    image: nginx
    env:
    - name: SECRET_USERNAME
      valueFrom:
        secretKeyRef:
          name: mysecret
          key: username
    - name: SECRET_PASSWORD
      valueFrom:
        secretKeyRef:
          name: mysecret
          key: password
```

**Create the pod:**
```bash
kubectl create -f readsecret.yaml
```

### Step 3: Verify Secret Injection

**Connect to the pod:**
```bash
kubectl exec --stdin --tty secret-test-pod -- /bin/bash
```

**Check environment variables:**
```bash
echo $SECRET_USERNAME  # Output: admin
echo $SECRET_PASSWORD  # Output: mysecretpass
```

## Common Commands

| Operation | Command |
|-----------|---------|
| Create Secret (imperative) | `kubectl create secret generic <name> --from-literal=<key>=<value>` |
| Create Secret (declarative) | `kubectl create -f secret.yaml` |
| List Secrets | `kubectl get secrets` |
| Describe Secret | `kubectl describe secret <name>` |
| View Secret data (base64) | `kubectl get secret <name> -o yaml` |
| Delete Secret | `kubectl delete secret <name>` |
| Create Docker registry Secret | `kubectl create secret docker-registry <name> --docker-*` |

## Best Practices

### Security Considerations
1. **Use RBAC**: Limit access to Secrets using Role-Based Access Control
2. **Enable Encryption at Rest**: Configure etcd encryption for stored Secrets
3. **Rotate Secrets**: Regularly update and rotate sensitive credentials
4. **Limit Exposure**: Use specific key selection rather than importing all keys
5. **Audit Access**: Monitor who accesses Secrets in your cluster

### Operational Best Practices
1. **Naming Convention**: Use descriptive names for Secrets
2. **Documentation**: Document what each Secret contains and its purpose
3. **Environment Separation**: Use different Secrets for different environments
4. **Backup Strategy**: Include Secrets in your backup and disaster recovery plans

## Troubleshooting

### Common Issues

1. **Pod fails to start**: Check if Secret exists and keys are correct
```bash
kubectl describe pod <pod-name>
kubectl get secret <secret-name>
```

2. **Wrong values in container**: Verify base64 encoding
```bash
kubectl get secret <secret-name> -o yaml
echo '<base64-value>' | base64 -d
```

3. **ImagePullBackOff with private registry**: Verify docker-registry Secret
```bash
kubectl describe secret <registry-secret-name>
```

## Key Takeaways

- **Secrets vs ConfigMaps**: Use Secrets for sensitive data, ConfigMaps for non-sensitive configuration
- **Encoding vs Encryption**: Secrets use base64 encoding, which is easily reversible
- **Multiple Types**: Different Secret types serve different purposes (generic, docker-registry, TLS, etc.)
- **Injection Methods**: Use `envFrom` for all keys or `valueFrom` for specific keys
- **Docker Integration**: `docker-registry` type Secrets enable private registry access
- **Security**: Implement proper RBAC and encryption for production environments

## Next Steps

After mastering Secrets, consider exploring:
- **RBAC**: Role-Based Access Control for Secret permissions
- **Pod Security Policies**: Additional security layers
- **External Secret Management**: Tools like Vault, AWS Secrets Manager
- **Encryption at Rest**: Securing Secret storage in etcd
- **Secret Rotation**: Automated credential rotation strategies