# Kubernetes Pod Troubleshooting Guide

## Introduction to Troubleshooting Pods

In this lecture, we discuss how to find and fix issues with your pods. While we strive to create or manage everything perfectly, mistakes can still occur. The first step is to identify the mistake, and the second is to fix it.

## Setting Up a Local Environment

To minimize mistakes, it is recommended to run things first in your local environment. Whenever working on any project, always have a local environment set up. Test things in the following order:

1. **Local environment**
2. **Test or development environment**
3. **Production environment**

If you are working on any project, set up a local test environment for yourself, provided it is allowed in your project. You can do this on your VM instances or wherever you prefer, but having a local setup is important.

## Identifying Pod Issues

Even after taking precautions, mistakes can happen. For example, running the following command shows the status of your pods:

```bash
kubectl get pod
```

Suppose you see three pods:
- **NGINX one**: Running
- **NGINX twelve**: Shows `ImagePullBackOff` status
- **Web two**: Shows `CrashLoopBackOff` status

If you see `ImagePullBackOff`, it usually means you have provided the wrong image name.

## Investigating Pod Details

### Step 1: Get More Pod Information

To further investigate, you can use the following command to see more details, including the image name:

```bash
kubectl get pod -o wide
```

### Step 2: Check YAML Output

If the above doesn't reveal the issue, you can check the YAML output for more information:

```bash
kubectl get pod <pod-name> -o yaml
```

In the YAML output, you may see messages like 'Back-off pulling image ngnox', indicating a wrong image name was provided.

### Step 3: Describe the Pod

You can also use the JSON output or describe the pod for more details:

```bash
kubectl describe pod <pod-name>
```

In the events section, you can find errors such as:
- 'Failed to pull image'
- 'Repository does not exist'
- 'May require authorization'

If the image is in a private registry and credentials are not provided, similar errors may occur. Supplying credentials for private registries will be discussed in the secrets lecture.

## Fixing Common Issues

### Fixing Image Name Errors

Once you identify the mistake (e.g., using 'ngnox' instead of 'nginx'), you can fix it by editing your YAML file and reapplying the configuration.

1. **Delete the problematic pod:**
   ```bash
   kubectl delete pod <pod-name>
   ```

2. **Correct the image name in your YAML file and apply it again:**
   ```bash
   kubectl apply -f pod2.yaml
   ```

3. **Check the pod status to confirm the issue is resolved:**
   ```bash
   kubectl get pod
   ```

### Troubleshooting CrashLoopBackOff

For pods showing `CrashLoopBackOff`, follow these investigation steps:

1. **Get detailed pod information:**
   ```bash
   kubectl get pod web2 -o wide
   ```

2. **Check the YAML output:**
   ```bash
   kubectl get pod web2 -o yaml
   ```

3. **Check pod logs (often the most revealing):**
   ```bash
   kubectl logs web2
   ```

#### Example CrashLoopBackOff Issue

The logs might show that the container is trying to execute a command like 'test 47', which is not found. This error occurs because the command was appended at the end of the kubectl run command:

```bash
kubectl run web2 --image nginx test 47
```

Since 'test 47' is not a valid command, the container fails to start.

**Fix:**
1. Delete the pod:
   ```bash
   kubectl delete pod web2
   ```

2. Rerun the pod with the correct command and check the pod status:
   ```bash
   kubectl get pod
   ```

## Systematic Troubleshooting Approach

To summarize, the troubleshooting process involves:

1. **Check pod status** for errors
2. **Gather information** using:
   - `kubectl get pod -o wide`
   - `kubectl describe pod`
   - YAML/JSON outputs
3. **Examine pod logs** to identify issues not visible in events
4. **Fix the configuration** and redeploy the pod

Most of the time, the problem can be identified by checking the logs or events.

## Important Notes on Editing Pods and Deployments

Usually, pods are not edited directly. Instead, changes are made through:
- **Deployments**
- **DaemonSets** 
- **ReplicaSets**

These higher-level resources then manage the pods, deleting and recreating them as needed.

## Conclusion

By following these steps, you can gain experience and expertise in finding and fixing problems with your pods. Test these commands, intentionally break things, and practice fixing them to improve your troubleshooting skills.

## Key Troubleshooting Commands Reference

| Command | Purpose |
|---------|---------|
| `kubectl get pod` | Check pod status |
| `kubectl get pod -o wide` | Get detailed pod information |
| `kubectl get pod <name> -o yaml` | Get pod configuration in YAML |
| `kubectl describe pod <name>` | Get detailed pod description and events |
| `kubectl logs <pod-name>` | Check pod logs |
| `kubectl delete pod <name>` | Delete a problematic pod |

## Key Takeaways

- Always set up a local test environment to minimize and catch mistakes early
- Use `kubectl get pod`, `kubectl describe pod`, and `kubectl logs` to systematically diagnose pod issues
- Incorrect image names or commands can lead to common pod errors like `ImagePullBackOff` and `CrashLoopBackOff`
- Most problems can be identified by checking pod logs and events, and are fixed by correcting the configuration and redeploying
- Practice breaking things intentionally to improve troubleshooting skills