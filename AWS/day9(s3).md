#  Amazon S3 (Simple Storage Service)

Amazon S3 is a **fully managed object storage service** that provides industry-leading scalability, data availability, security, and performance. It allows you to store and retrieve any amount of data from anywhere on the web.

---

##  Key Features of Amazon S3

- **Object-based Storage**: Stores data as objects inside buckets
- **Globally Accessible**: Accessible via HTTP/HTTPS endpoints
- **High Durability**: "11 9s" (99.999999999%) durability
- **Highly Available & Scalable**
- **Security Controls**: IAM, Bucket Policies, ACLs, and Encryption
- **Flexible Storage Classes**
- **Lifecycle Management**
- **Static Website Hosting**
- **Versioning and Replication**
- **Cost Optimization**

---

##  Advantages of S3

1.  **High Availability and Durability**
2.  **Robust Security**
3.  **Scalability**
4.  **Cost-Effective**
5.  **High Performance**

---

##  Buckets and Objects

- A **bucket** is a container for storing objects (files + metadata).
- Each bucket name must be **globally unique**.
- Objects can be accessed via a unique URL (if public).
- Object ownership and permissions are managed per object/bucket.

---

##  Bucket Permissions

- You can edit **Bucket Policies** for fine-grained access control.
- You can allow **public access** (not recommended for sensitive data).
- Use **ACLs (Access Control Lists)** to manage object-level permissions.

---

##  S3 Storage Classes

| Class                     | Description                            | Cost       | Use Case                          |
|--------------------------|----------------------------------------|------------|-----------------------------------|
| S3 Standard              | Default, general-purpose               | 💰💰        | Frequent access                   |
| S3 Intelligent-Tiering   | Auto-moves objects between tiers       | 💰         | Unknown access patterns           |
| S3 Standard-IA           | Infrequent access, but fast retrieval  | 💰         | Backups, disaster recovery        |
| S3 One Zone-IA           | One AZ, lower cost                     | 💰         | Re-creatable, non-critical data   |
| S3 Glacier               | Archival, slow retrieval               | 💲          | Long-term backup                  |
| S3 Glacier Deep Archive  | Cheapest, very slow retrieval          | 💲          | Archival, regulatory compliance   |

---

##  Lifecycle Policies

Helps **automate transitions** between storage classes and **object expiration**:

Example Policy:
- Days 0–30: `S3 Standard`
- Day 31–60: `S3 Standard-IA`
- Day 61–90: `S3 One Zone-IA`
- After 90 Days: Move to `S3 Glacier`
- After 180 Days: **Delete object**

You can define:
- Filter rules (prefix/tags)
- Actions for current and previous versions
- Expiration/deletion policies

---

##  Versioning

- Keeps **multiple versions** of an object
- Stores even **deleted files** (you can restore them)
- Must be **explicitly enabled**
- Helps in **data recovery and audit trails**

---

##  Object Locking

- Prevents object deletion or overwrite for a defined time period
- Useful for **compliance and data retention policies**

---

## 🌐 Static Website Hosting on S3

Steps:
1. Create a **bucket** (must match domain name for custom domain hosting)
2. Upload your **HTML/CSS/JS** files
3. Enable **public access** to the bucket and objects
4. Enable **static website hosting** under bucket **Properties**
5. Set `index.html` as the default home page
6. (Optional) Enable **access logging** to monitor access

---

##  S3 Pricing Breakdown

1. **Storage Usage** (per GB/month)
2. **Request Costs** (PUT, GET, DELETE, etc.)
3. **Storage Class Tier** (Standard vs Glacier, etc.)
4. **Data Transfer** (IN is free, OUT is charged)
5. **Replication** (cross-region replication may incur charges)

---

##  Common S3 Use Cases

- Hosting **static websites**
- **Backup and archival** storage
- Serving files for **web/mobile applications**
- Storing **media files**, logs, and large datasets
- **Data lake** for analytics platforms (e.g., AWS Athena)

---

##  Cross-Region Replication (Disaster Recovery)

- Replicates objects across different AWS regions
- Must enable **versioning** in both source and destination buckets
- Set up a **replication rule**
- Optional: **Encrypt replicated objects**

---

##  Best Practices

- Use **tags** for cost allocation and resource management
- Enable **encryption** by default (SSE-S3 or SSE-KMS)
- Enable **MFA Delete** for added protection
- Use **CloudTrail** + **S3 Access Logs** for monitoring
- For data uploads: consider **multi-part uploads** for large files

---

##  Useful Links

- [S3 Documentation](https://docs.aws.amazon.com/s3/index.html)
- [Storage Class Comparison](https://aws.amazon.com/s3/storage-classes/)
- [S3 Pricing](https://aws.amazon.com/s3/pricing/)
- [Static Website Hosting Guide](https://docs.aws.amazon.com/AmazonS3/latest/userguide/WebsiteHosting.html)
