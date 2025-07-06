# 🗄️ EBS (Elastic Block Store) – AWS Persistent Storage

Amazon EBS (Elastic Block Store) provides **block-level storage** volumes for use with Amazon EC2 instances. These volumes behave like hard drives and are used to **run operating systems, store databases, application data, or files**.

---

## 🔧 Key Features

- **Block-based storage** (similar to traditional hard disks)
- Used to **run EC2 OS**, store **database data**, file storage, etc.
- **Located in the same Availability Zone (AZ)** as the attached EC2 instance
- **Snapshots** can be taken to **back up** the volume or migrate to other regions/accounts

---

## 📦 EBS Volume Types

| Type                     | Description                                | Best For                          |
|--------------------------|--------------------------------------------|-----------------------------------|
| **General Purpose SSD (gp2/gp3)** | Balanced price/performance               | Most workloads                    |
| **Provisioned IOPS SSD (io1/io2)** | High-performance IOPS                    | Large databases, latency-sensitive apps |
| **Throughput Optimized HDD (st1)** | High throughput, low-cost HDD            | Big Data, Data Warehousing       |
| **Cold HDD (sc1)**       | Low-cost, infrequent access                 | File servers                      |
| **Magnetic (Standard)**  | Previous-gen, low-cost                      | Backups, archives (legacy use)    |

---

## Working with EBS Volumes on Linux

### Check Disks and Partitions

```bash
sudo fdisk -l        # Lists all disks and partitions
df -h                # Shows mounted filesystems and usage

# Connect EBS Volume to a Directory
Step 1: Partition the Volume
sudo fdisk /dev/xvdf    # Replace xvdf with your volume name
# Press 'n' to create new partition, 'w' to write
Step 2: Format the Partition
sudo mkfs -t ext4 /dev/xvdf1
Step 3: Mount the Volume Temporarily
sudo mkdir /mnt/data
sudo mount /dev/xvdf1 /mnt/data
Step 4: Mount the Volume Permanently
#Edit the /etc/fstab file:

sudo nano /etc/fstab
# Add the line:
/dev/xvdf1   /mnt/data   ext4   defaults,nofail   0   2
#Then test:

sudo mount -a   # Verifies all entries in fstab
```
# EBS Encryption
Can encrypt at the time of volume creation

Choose default AWS-managed key or a custom KMS key

KMS keys may incur extra cost

Encryption ensures data at rest, in transit, and snapshots are secure

# EBS Snapshots
Backup of the volume stored in Amazon S3

Can be used to:

Recover data

Change volume type

Change region (copy snapshot to another region)

Share with another AWS account

# Notes
EBS volumes must be in the same AZ as the EC2 instance to attach

Snapshots are incremental, meaning only changed blocks are saved after the first full snapshot

Use Amazon Data Lifecycle Manager (DLM) to automate snapshot creation and retention

🧪 Useful Commands Recap

| Task           | Command Example                                 |
| -------------- | ----------------------------------------------- |
| List disks     | `sudo fdisk -l`                                 |
| Format volume  | `sudo mkfs -t ext4 /dev/xvdf1`                  |
| Mount volume   | `sudo mount /dev/xvdf1 /mnt/data`               |
| Make directory | `sudo mkdir /mnt/data`                          |
| Update fstab   | `/dev/xvdf1 /mnt/data ext4 defaults,nofail 0 2` |
| Reload mount   | `sudo mount -a`                                 |
