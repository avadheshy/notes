# Amazon EFS (Elastic File System)

**Amazon EFS** is a scalable, fully managed, elastic **network file system** that can be **mounted by multiple EC2 instances** (and other AWS services) at the same time. It's ideal for **shared file storage**, such as content management systems, analytics, and home directories.

---

## Key Features

- **Fully Managed**: No provisioning or managing storage
- **Shared Access**: Can be accessed by **multiple instances across AZs**
- **Elastic**: Scales automatically as you add/remove files
- **POSIX-Compliant**: Works like a Linux file system
- **Supports NFS (v4.1 or v4.0)**: Standard protocol for file systems
- **Secure**: Uses IAM, VPC, and Security Groups for control
- **Cost-effective**: Pay for what you use (GB stored/month)

---

## Steps to Create an EFS

1. **Go to the Amazon EFS console**
2. **Click "Create file system"**
3. **Name your EFS**
4. **Choose Performance Mode**:
   - General Purpose (default, good for latency-sensitive workloads)
   - Max I/O (good for highly parallel applications)
5. **Choose Throughput Mode**:
   - Bursting or Provisioned
6. **Add Tags** (optional but helpful for billing and organization)
7. **Configure Network Access**:
   - Select VPC and Subnets
   - Ensure **Security Group allows NFS (port 2049)** inbound

---

## Create an Access Point (Optional but Recommended)

Access points simplify managing access permissions:

1. Navigate to **Access Points** tab
2. Click **Create Access Point**
3. Choose the **file system**
4. Configure **path, POSIX user, and permissions**
5. Create the access point — now use this to mount EFS securely

---

##  Mounting EFS on EC2

###  Install Amazon EFS Utils

```bash
sudo yum install -y amazon-efs-utils   # For Amazon Linux
# OR
sudo apt install -y amazon-efs-utils   # For Ubuntu
```

Ensure Inbound Rules for NFS
Security group must allow inbound TCP traffic on port 2049

Mount Command (Using Access Point)
```
sudo mkdir /mnt/efs
sudo mount -t efs -o tls,accesspoint=fsap-xxxxxxxx fs-xxxxxxxx:/ /mnt/efs
```
Mount Without Access Point (Direct)
```
sudo mount -t efs fs-xxxxxxxx:/ /mnt/efs
```
Optional: Add to /etc/fstab for auto-mount on reboot
```
fs-xxxxxxxx:/ /mnt/efs efs _netdev,tls 0 0
```

# Use Cases
```
| Use Case                    | Description                               |
| --------------------------- | ----------------------------------------- |
| Web servers                 | Share static files between EC2s           |
| Content Management Systems  | Shared access to media/content            |
| Analytics & Big Data        | Store intermediate or shared results      |
| Home Directories            | Provide user-specific persistent storage  |
| Container Storage (EKS/ECS) | Mount persistent volume inside containers |

```
# Summary
```
| Feature           | Details                                       |
| ----------------- | --------------------------------------------- |
| Protocol          | NFSv4.1, NFSv4.0                              |
| Mount Target      | One per AZ                                    |
| Access            | Multiple EC2s, containers, Lambda             |
| Performance Modes | General Purpose, Max I/O                      |
| Security          | IAM + Security Groups (NFS port 2049)         |
| Access Points     | Scoped access with POSIX user and permissions |

```
