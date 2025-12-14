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

# Complete AWS S3 Bucket Guide

## Table of Contents
1. [Introduction](#introduction)
2. [Key Concepts](#key-concepts)
3. [Bucket Creation and Configuration](#bucket-creation-and-configuration)
4. [Storage Classes](#storage-classes)
5. [Security and Access Control](#security-and-access-control)
6. [Data Management Features](#data-management-features)
7. [Performance Optimization](#performance-optimization)
8. [Monitoring and Logging](#monitoring-and-logging)
9. [Pricing Structure](#pricing-structure)
10. [Best Practices](#best-practices)
11. [Common Use Cases](#common-use-cases)
12. [CLI and API Operations](#cli-and-api-operations)
13. [Troubleshooting](#troubleshooting)

## Introduction

Amazon Simple Storage Service (S3) is a highly scalable, durable, and secure object storage service provided by AWS. S3 buckets are containers that hold your data (objects) and provide various management, security, and access features.

### Key Benefits
- **Durability**: 99.999999999% (11 9's) durability
- **Availability**: 99.99% availability SLA
- **Scalability**: Virtually unlimited storage capacity
- **Security**: Multiple layers of security controls
- **Cost-effective**: Pay only for what you use
- **Performance**: High request rates and data transfer speeds

## Key Concepts

### Buckets
- **Definition**: A container for objects stored in S3
- **Global namespace**: Bucket names must be globally unique across all AWS accounts
- **Regional**: Buckets are created in specific AWS regions
- **Flat structure**: No hierarchical structure, but prefixes create folder-like organization

### Objects
- **Definition**: Files stored in S3 buckets
- **Components**: Object data, metadata, and unique key (name)
- **Size limits**: 0 bytes to 5 TB per object
- **Versioning**: Multiple versions of the same object can coexist

### Keys
- **Definition**: Unique identifier for objects within a bucket
- **Format**: String of Unicode characters up to 1,024 bytes
- **Prefixes**: Use forward slashes to create folder-like structure

## Bucket Creation and Configuration

### Naming Requirements
- 3-63 characters long
- Lowercase letters, numbers, hyphens, and periods only
- Must start and end with letter or number
- Cannot be formatted as IP address
- Cannot start with "xn--" or end with "-s3alias"

### Creation Process
```bash
# AWS CLI example
aws s3 mb s3://my-unique-bucket-name --region us-east-1
```

### Configuration Options
- **Region selection**: Choose based on latency, compliance, and cost
- **Versioning**: Enable to keep multiple versions of objects
- **Server-side encryption**: Automatic encryption of stored objects
- **Public access settings**: Block or allow public access
- **Logging**: Enable access logging for audit trails
- **Tags**: Key-value pairs for organization and cost allocation

## Storage Classes

### Standard
- **Use case**: Frequently accessed data
- **Durability**: 99.999999999% (11 9's)
- **Availability**: 99.99%
- **Retrieval time**: Immediate

### Standard-IA (Infrequent Access)
- **Use case**: Long-term storage with infrequent access
- **Cost**: Lower storage cost, retrieval charges apply
- **Minimum storage duration**: 30 days
- **Minimum object size**: 128 KB

### One Zone-IA
- **Use case**: Infrequently accessed, non-critical data
- **Availability**: 99.5% (single AZ)
- **Cost**: 20% less than Standard-IA

### Glacier Storage Classes

#### Glacier Instant Retrieval
- **Retrieval time**: Milliseconds
- **Use case**: Archive data accessed once per quarter
- **Minimum storage duration**: 90 days

#### Glacier Flexible Retrieval
- **Retrieval time**: 1-5 minutes to 3-5 hours
- **Use case**: Backup and disaster recovery
- **Minimum storage duration**: 90 days

#### Glacier Deep Archive
- **Retrieval time**: 12-48 hours
- **Use case**: Long-term retention (7-10 years)
- **Minimum storage duration**: 180 days

### Intelligent Tiering
- **Automatic optimization**: Moves objects between access tiers
- **Use case**: Unknown or changing access patterns
- **No retrieval charges**: For frequent and infrequent access tiers

## Security and Access Control

### Bucket Policies
- **JSON-based**: Define permissions using IAM policy language
- **Resource-based**: Applied to buckets and objects
- **Conditions**: Support for IP addresses, time, SSL, etc.

Example bucket policy:
```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Sid": "PublicReadGetObject",
      "Effect": "Allow",
      "Principal": "*",
      "Action": "s3:GetObject",
      "Resource": "arn:aws:s3:::my-bucket/*"
    }
  ]
}
```

### Access Control Lists (ACLs)
- **Legacy method**: Predates IAM
- **Limited granularity**: Basic read/write permissions
- **Recommendation**: Use bucket policies instead

### IAM Policies
- **User-based**: Attached to IAM users, groups, or roles
- **Fine-grained**: Specific actions and resources
- **Cross-service**: Can combine with other AWS services

### Block Public Access
- **Four settings**:
  1. Block public access via new ACLs
  2. Block public access via any ACLs
  3. Block public access via new bucket policies
  4. Block public access via any bucket policies

### Encryption

#### Server-Side Encryption (SSE)
- **SSE-S3**: Amazon-managed keys
- **SSE-KMS**: AWS KMS managed keys
- **SSE-C**: Customer-provided keys

#### Client-Side Encryption
- **Customer responsibility**: Encrypt data before upload
- **AWS SDK support**: Built-in encryption libraries

## Data Management Features

### Versioning
- **Purpose**: Protect against accidental deletion/modification
- **States**: Unversioned, enabled, suspended
- **Object versions**: Unique version ID for each version
- **Delete markers**: Special markers for deleted objects

### Lifecycle Management
- **Automatic transitions**: Move objects between storage classes
- **Expiration rules**: Delete objects after specified time
- **Rule components**: Filters, actions, and timing

Example lifecycle rule:
```json
{
  "Rules": [
    {
      "Status": "Enabled",
      "Filter": {"Prefix": "logs/"},
      "Transitions": [
        {
          "Days": 30,
          "StorageClass": "STANDARD_IA"
        },
        {
          "Days": 90,
          "StorageClass": "GLACIER"
        }
      ],
      "Expiration": {
        "Days": 2555
      }
    }
  ]
}
```

### Cross-Region Replication (CRR)
- **Purpose**: Disaster recovery, compliance, latency reduction
- **Requirements**: Versioning enabled, IAM role
- **Options**: Entire bucket or prefix-based
- **Storage class**: Can change during replication

### Same-Region Replication (SRR)
- **Use cases**: Log aggregation, compliance, dev/test environments
- **Benefits**: Lower latency than CRR
- **Configuration**: Similar to CRR but within same region

### Multipart Upload
- **Large objects**: Recommended for objects >100 MB
- **Required**: Objects >5 GB
- **Benefits**: Improved throughput, quick recovery from failures
- **Process**: Initiate → Upload parts → Complete

## Performance Optimization

### Request Rate Performance
- **Baseline**: 3,500 PUT/COPY/POST/DELETE per second per prefix
- **GET requests**: 5,500 per second per prefix
- **Scaling**: Automatically scales to higher rates

### Transfer Acceleration
- **CloudFront edge locations**: Route uploads through nearest edge
- **Use case**: Global users uploading to centralized bucket
- **Cost**: Additional charges apply

### Multipart Upload
- **Parallel uploads**: Upload parts simultaneously
- **Fault tolerance**: Restart failed parts only
- **Threshold**: Use for objects >100 MB

### Byte-Range Fetches
- **Partial retrieval**: Download specific byte ranges
- **Use case**: Large files, resumable downloads
- **Performance**: Faster retrieval of small portions

## Monitoring and Logging

### CloudWatch Metrics
- **Storage metrics**: BucketSizeBytes, NumberOfObjects
- **Request metrics**: AllRequests, GetRequests, PutRequests
- **Data retrieval**: Available in CloudWatch console

### Server Access Logging
- **Purpose**: Detailed records of requests
- **Log format**: Standard format with request details
- **Delivery**: Logs delivered to specified S3 bucket

### CloudTrail Integration
- **API calls**: Log all S3 API calls
- **Management events**: Bucket-level operations
- **Data events**: Object-level operations (optional)

### S3 Event Notifications
- **Trigger events**: Object creation, removal, restoration
- **Destinations**: Lambda, SQS, SNS
- **Filtering**: Prefix and suffix filters available

## Pricing Structure

### Storage Costs
- **Per GB per month**: Varies by storage class
- **Regional variations**: Prices differ by AWS region
- **Volume discounts**: Lower per-GB cost at higher tiers

### Request Costs
- **PUT/POST/COPY**: Higher cost operations
- **GET/SELECT**: Lower cost operations
- **DELETE/CANCEL**: No charge

### Data Transfer
- **Internet egress**: Charged per GB
- **Within AWS**: Different rates for same region, cross-region
- **CloudFront**: No charge for transfer to CloudFront

### Additional Features
- **Cross-Region Replication**: Replication and cross-region transfer charges
- **Transfer Acceleration**: Additional per-GB fee
- **Inventory**: Monthly charge per million objects

## Best Practices

### Security
- Enable versioning for important data
- Use least privilege access policies
- Enable MFA delete for critical buckets
- Regularly audit access permissions
- Use CloudTrail for API logging
- Encrypt sensitive data

### Performance
- Use appropriate storage classes
- Implement lifecycle policies
- Use multipart upload for large files
- Consider Transfer Acceleration for global users
- Optimize request patterns to avoid hotspotting

### Cost Optimization
- Regular lifecycle policy reviews
- Use S3 Storage Class Analysis
- Delete incomplete multipart uploads
- Consider Intelligent Tiering for unknown access patterns
- Monitor and analyze access patterns

### Operational
- Use descriptive, consistent naming conventions
- Implement proper tagging strategies
- Set up monitoring and alerting
- Regular backup and disaster recovery testing
- Document bucket purposes and retention policies

## Common Use Cases

### Static Website Hosting
- Host static websites directly from S3
- Configure index and error documents
- Use CloudFront for global distribution
- Custom domain with Route 53

### Data Backup and Archival
- Primary or secondary backup location
- Lifecycle policies for automatic archiving
- Cross-Region Replication for disaster recovery
- Integration with AWS Backup

### Content Distribution
- Store and distribute media files
- Integration with CloudFront CDN
- Global content delivery
- Streaming media support

### Data Lake Storage
- Central repository for structured and unstructured data
- Integration with analytics services (Athena, EMR, Glue)
- Partitioned data organization
- Cost-effective storage for big data

### Application Data Storage
- Store application assets and user-generated content
- API integration for applications
- Scalable storage backend
- Mobile and web application support

## CLI and API Operations

### AWS CLI Commands

#### Bucket Operations
```bash
# Create bucket
aws s3 mb s3://my-bucket

# List buckets
aws s3 ls

# Remove empty bucket
aws s3 rb s3://my-bucket

# Remove bucket and all contents
aws s3 rb s3://my-bucket --force
```

#### Object Operations
```bash
# Upload file
aws s3 cp file.txt s3://my-bucket/

# Download file
aws s3 cp s3://my-bucket/file.txt ./

# Sync directory
aws s3 sync ./local-folder s3://my-bucket/remote-folder

# List objects
aws s3 ls s3://my-bucket/ --recursive

# Delete object
aws s3 rm s3://my-bucket/file.txt
```

### SDK Examples (Python - Boto3)

#### Basic Operations
```python
import boto3

# Create S3 client
s3 = boto3.client('s3')

# Create bucket
s3.create_bucket(Bucket='my-bucket')

# Upload file
s3.upload_file('local-file.txt', 'my-bucket', 'remote-file.txt')

# Download file
s3.download_file('my-bucket', 'remote-file.txt', 'downloaded-file.txt')

# List objects
response = s3.list_objects_v2(Bucket='my-bucket')
for obj in response.get('Contents', []):
    print(obj['Key'])
```

## Troubleshooting

### Common Issues

#### Access Denied (403)
- **Causes**: IAM permissions, bucket policies, ACLs, block public access
- **Solutions**: Check IAM policies, verify bucket policy, review ACL settings

#### Bucket Name Already Exists
- **Cause**: Bucket names must be globally unique
- **Solution**: Choose a different name or check if you own the bucket

#### Slow Upload/Download
- **Causes**: Large files, network latency, single-threaded operations
- **Solutions**: Use multipart upload, Transfer Acceleration, parallel operations

#### Lifecycle Rules Not Working
- **Causes**: Incorrect configuration, timing, filters
- **Solutions**: Verify rule syntax, check object age, confirm filters match

#### High Costs
- **Causes**: Wrong storage class, frequent access patterns, data transfer
- **Solutions**: Analyze access patterns, implement lifecycle rules, use Storage Class Analysis

### Monitoring Tools
- CloudWatch dashboards
- S3 Storage Lens
- Cost and Usage Reports
- AWS Config rules

### Support Resources
- AWS documentation
- AWS Support cases
- AWS forums
- AWS re:Post community

---

## Conclusion

AWS S3 is a powerful and flexible storage service that forms the backbone of many cloud applications. Understanding its features, capabilities, and best practices is essential for building scalable, secure, and cost-effective solutions. Regular review of your S3 implementation ensures optimal performance and cost management as your requirements evolve.

For the most up-to-date information, always refer to the official AWS S3 documentation and consider your specific use case requirements when implementing S3 solutions.


# AWS S3 Guide for Python Developers: Beginner to Advanced

## Table of Contents
1. [Introduction](#introduction)
2. [Prerequisites & Setup](#prerequisites--setup)
3. [Beginner: Getting Started with Boto3](#beginner-getting-started-with-boto3)
4. [Intermediate: Working with S3 Features](#intermediate-working-with-s3-features)
5. [Advanced: Performance & Production Patterns](#advanced-performance--production-patterns)
6. [Real-World Projects](#real-world-projects)
7. [Best Practices & Security](#best-practices--security)
8. [Troubleshooting](#troubleshooting)

---

## Introduction

Amazon S3 (Simple Storage Service) is an object storage service that lets you store and retrieve any amount of data. For Python developers, **Boto3** is the official AWS SDK that makes working with S3 straightforward and pythonic.

### What You'll Learn
- Basic CRUD operations with S3 buckets and objects
- Uploading/downloading files efficiently
- Working with metadata, permissions, and storage classes
- Advanced features like presigned URLs, multipart uploads, and event notifications
- Production-ready patterns for error handling and performance optimization

---

## Prerequisites & Setup

### Required Knowledge
- Basic Python programming (functions, classes, error handling)
- Understanding of file I/O operations
- Basic command line usage

### Installation

```bash
# Install boto3
pip install boto3

# Install additional helpful libraries
pip install python-dotenv  # For environment variables
pip install tqdm           # For progress bars
```

### AWS Credentials Setup

**Option 1: AWS CLI Configuration (Recommended)**
```bash
# Install AWS CLI
pip install awscli

# Configure credentials
aws configure
# Enter your AWS Access Key ID
# Enter your AWS Secret Access Key
# Enter default region (e.g., us-east-1)
# Enter output format (json)
```

**Option 2: Environment Variables**
```python
import os

os.environ['AWS_ACCESS_KEY_ID'] = 'your_access_key'
os.environ['AWS_SECRET_ACCESS_KEY'] = 'your_secret_key'
os.environ['AWS_DEFAULT_REGION'] = 'us-east-1'
```

**Option 3: Python Code (Not Recommended for Production)**
```python
import boto3

s3 = boto3.client(
    's3',
    aws_access_key_id='your_access_key',
    aws_secret_access_key='your_secret_key',
    region_name='us-east-1'
)
```

### Understanding Boto3 Architecture

Boto3 provides two main ways to interact with S3:

1. **Client** (Low-level): Direct mapping to AWS API
2. **Resource** (High-level): Object-oriented interface

```python
import boto3

# Client - more control, verbose
s3_client = boto3.client('s3')

# Resource - more pythonic, easier to use
s3_resource = boto3.resource('s3')
```

---

## Beginner: Getting Started with Boto3

### 1. Creating Your First Bucket

```python
import boto3
from botocore.exceptions import ClientError

def create_bucket(bucket_name, region='us-east-1'):
    """Create an S3 bucket in a specified region."""
    try:
        s3_client = boto3.client('s3', region_name=region)
        
        if region == 'us-east-1':
            # us-east-1 doesn't need LocationConstraint
            s3_client.create_bucket(Bucket=bucket_name)
        else:
            location = {'LocationConstraint': region}
            s3_client.create_bucket(
                Bucket=bucket_name,
                CreateBucketConfiguration=location
            )
        
        print(f"Bucket '{bucket_name}' created successfully!")
        return True
        
    except ClientError as e:
        print(f"Error: {e}")
        return False

# Usage
create_bucket('my-python-app-bucket-12345')
```

**Key Concepts:**
- Bucket names must be globally unique across all AWS accounts
- Use lowercase letters, numbers, hyphens only
- Include error handling with `ClientError`

### 2. Listing Buckets

```python
def list_buckets():
    """List all S3 buckets in your account."""
    s3_client = boto3.client('s3')
    
    try:
        response = s3_client.list_buckets()
        
        print("Your S3 Buckets:")
        for bucket in response['Buckets']:
            print(f"  • {bucket['Name']} (Created: {bucket['CreationDate']})")
            
    except ClientError as e:
        print(f"Error: {e}")

# Usage
list_buckets()
```

### 3. Uploading Files

```python
def upload_file(file_path, bucket_name, object_name=None):
    """
    Upload a file to S3 bucket.
    
    Args:
        file_path: Path to file to upload
        bucket_name: Target bucket name
        object_name: S3 object name (defaults to file_path basename)
    """
    import os
    
    if object_name is None:
        object_name = os.path.basename(file_path)
    
    s3_client = boto3.client('s3')
    
    try:
        s3_client.upload_file(file_path, bucket_name, object_name)
        print(f"✓ Uploaded {file_path} to {bucket_name}/{object_name}")
        return True
        
    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found")
        return False
        
    except ClientError as e:
        print(f"Error: {e}")
        return False

# Usage
upload_file('data.csv', 'my-python-app-bucket-12345')
upload_file('report.pdf', 'my-python-app-bucket-12345', 'reports/2024/report.pdf')
```

### 4. Downloading Files

```python
def download_file(bucket_name, object_name, file_path):
    """Download a file from S3 bucket."""
    s3_client = boto3.client('s3')
    
    try:
        s3_client.download_file(bucket_name, object_name, file_path)
        print(f"✓ Downloaded {object_name} to {file_path}")
        return True
        
    except ClientError as e:
        if e.response['Error']['Code'] == '404':
            print(f"Error: Object '{object_name}' not found")
        else:
            print(f"Error: {e}")
        return False

# Usage
download_file('my-python-app-bucket-12345', 'data.csv', 'local_data.csv')
```

### 5. Listing Objects in a Bucket

```python
def list_objects(bucket_name, prefix=''):
    """
    List all objects in a bucket (or with a prefix).
    
    Args:
        bucket_name: Name of the bucket
        prefix: Only list objects starting with this prefix
    """
    s3_client = boto3.client('s3')
    
    try:
        response = s3_client.list_objects_v2(
            Bucket=bucket_name,
            Prefix=prefix
        )
        
        if 'Contents' not in response:
            print(f"No objects found in {bucket_name}/{prefix}")
            return []
        
        objects = []
        print(f"Objects in {bucket_name}/{prefix}:")
        
        for obj in response['Contents']:
            size_mb = obj['Size'] / (1024 * 1024)
            print(f"  • {obj['Key']} ({size_mb:.2f} MB)")
            objects.append(obj['Key'])
        
        return objects
        
    except ClientError as e:
        print(f"Error: {e}")
        return []

# Usage
list_objects('my-python-app-bucket-12345')
list_objects('my-python-app-bucket-12345', prefix='reports/')
```

### 6. Deleting Objects

```python
def delete_object(bucket_name, object_name):
    """Delete an object from S3 bucket."""
    s3_client = boto3.client('s3')
    
    try:
        s3_client.delete_object(Bucket=bucket_name, Key=object_name)
        print(f"✓ Deleted {object_name} from {bucket_name}")
        return True
        
    except ClientError as e:
        print(f"Error: {e}")
        return False

# Usage
delete_object('my-python-app-bucket-12345', 'old_data.csv')
```

### 7. Deleting a Bucket

```python
def delete_bucket(bucket_name):
    """Delete an S3 bucket (must be empty)."""
    s3_client = boto3.client('s3')
    
    try:
        # First, delete all objects
        response = s3_client.list_objects_v2(Bucket=bucket_name)
        
        if 'Contents' in response:
            print(f"Deleting {len(response['Contents'])} objects...")
            for obj in response['Contents']:
                s3_client.delete_object(Bucket=bucket_name, Key=obj['Key'])
        
        # Then delete the bucket
        s3_client.delete_bucket(Bucket=bucket_name)
        print(f"✓ Bucket '{bucket_name}' deleted successfully")
        return True
        
    except ClientError as e:
        print(f"Error: {e}")
        return False

# Usage
delete_bucket('my-python-app-bucket-12345')
```

---

## Intermediate: Working with S3 Features

### 1. Working with Metadata

```python
def upload_with_metadata(file_path, bucket_name, object_name, metadata):
    """Upload file with custom metadata."""
    s3_client = boto3.client('s3')
    
    try:
        s3_client.upload_file(
            file_path,
            bucket_name,
            object_name,
            ExtraArgs={
                'Metadata': metadata,
                'ContentType': 'application/pdf'  # Set content type
            }
        )
        print(f"✓ Uploaded with metadata: {metadata}")
        
    except ClientError as e:
        print(f"Error: {e}")

# Usage
upload_with_metadata(
    'report.pdf',
    'my-bucket',
    'reports/q4-2024.pdf',
    metadata={
        'author': 'John Doe',
        'department': 'Sales',
        'quarter': 'Q4-2024'
    }
)

def get_object_metadata(bucket_name, object_name):
    """Retrieve object metadata."""
    s3_client = boto3.client('s3')
    
    try:
        response = s3_client.head_object(Bucket=bucket_name, Key=object_name)
        print(f"Metadata for {object_name}:")
        print(f"  Size: {response['ContentLength']} bytes")
        print(f"  Last Modified: {response['LastModified']}")
        print(f"  Content Type: {response['ContentType']}")
        print(f"  Custom Metadata: {response.get('Metadata', {})}")
        
    except ClientError as e:
        print(f"Error: {e}")

# Usage
get_object_metadata('my-bucket', 'reports/q4-2024.pdf')
```

### 2. Working with Storage Classes

```python
def upload_with_storage_class(file_path, bucket_name, object_name, storage_class):
    """
    Upload file with specific storage class.
    
    Storage classes:
    - STANDARD (default)
    - INTELLIGENT_TIERING
    - STANDARD_IA (Infrequent Access)
    - ONEZONE_IA
    - GLACIER_IR (Instant Retrieval)
    - GLACIER
    - DEEP_ARCHIVE
    """
    s3_client = boto3.client('s3')
    
    try:
        s3_client.upload_file(
            file_path,
            bucket_name,
            object_name,
            ExtraArgs={'StorageClass': storage_class}
        )
        print(f"✓ Uploaded to {storage_class}")
        
    except ClientError as e:
        print(f"Error: {e}")

# Usage examples
upload_with_storage_class('archive.zip', 'my-bucket', 'archives/2023.zip', 'GLACIER')
upload_with_storage_class('backup.sql', 'my-bucket', 'backups/daily.sql', 'STANDARD_IA')

def change_storage_class(bucket_name, object_name, new_storage_class):
    """Change storage class of existing object."""
    s3_client = boto3.client('s3')
    
    try:
        # Copy object to itself with new storage class
        copy_source = {'Bucket': bucket_name, 'Key': object_name}
        
        s3_client.copy_object(
            CopySource=copy_source,
            Bucket=bucket_name,
            Key=object_name,
            StorageClass=new_storage_class,
            MetadataDirective='COPY'
        )
        print(f"✓ Changed storage class to {new_storage_class}")
        
    except ClientError as e:
        print(f"Error: {e}")

# Usage
change_storage_class('my-bucket', 'old-file.zip', 'GLACIER')
```

### 3. Generating Presigned URLs

```python
def generate_presigned_url(bucket_name, object_name, expiration=3600):
    """
    Generate a presigned URL for temporary access.
    
    Args:
        bucket_name: Name of the bucket
        object_name: Object key
        expiration: URL expiration time in seconds (default: 1 hour)
    """
    s3_client = boto3.client('s3')
    
    try:
        url = s3_client.generate_presigned_url(
            'get_object',
            Params={'Bucket': bucket_name, 'Key': object_name},
            ExpiresIn=expiration
        )
        print(f"Presigned URL (valid for {expiration}s):")
        print(url)
        return url
        
    except ClientError as e:
        print(f"Error: {e}")
        return None

# Usage
url = generate_presigned_url('my-bucket', 'confidential.pdf', expiration=300)  # 5 minutes

def generate_presigned_upload_url(bucket_name, object_name, expiration=3600):
    """Generate presigned URL for uploading."""
    s3_client = boto3.client('s3')
    
    try:
        url = s3_client.generate_presigned_url(
            'put_object',
            Params={'Bucket': bucket_name, 'Key': object_name},
            ExpiresIn=expiration
        )
        return url
        
    except ClientError as e:
        print(f"Error: {e}")
        return None

# Usage - client can upload to this URL
upload_url = generate_presigned_upload_url('my-bucket', 'uploads/user-file.jpg')
```

### 4. Working with Object Tags

```python
def add_tags_to_object(bucket_name, object_name, tags):
    """
    Add tags to an S3 object.
    
    Args:
        tags: Dictionary of tag key-value pairs
    """
    s3_client = boto3.client('s3')
    
    tag_set = [{'Key': k, 'Value': v} for k, v in tags.items()]
    
    try:
        s3_client.put_object_tagging(
            Bucket=bucket_name,
            Key=object_name,
            Tagging={'TagSet': tag_set}
        )
        print(f"✓ Added tags: {tags}")
        
    except ClientError as e:
        print(f"Error: {e}")

# Usage
add_tags_to_object(
    'my-bucket',
    'data/sales-2024.csv',
    tags={
        'Environment': 'Production',
        'Department': 'Sales',
        'Year': '2024'
    }
)

def get_object_tags(bucket_name, object_name):
    """Retrieve tags from an object."""
    s3_client = boto3.client('s3')
    
    try:
        response = s3_client.get_object_tagging(
            Bucket=bucket_name,
            Key=object_name
        )
        
        tags = {tag['Key']: tag['Value'] for tag in response['TagSet']}
        print(f"Tags for {object_name}: {tags}")
        return tags
        
    except ClientError as e:
        print(f"Error: {e}")
        return {}

# Usage
get_object_tags('my-bucket', 'data/sales-2024.csv')
```

### 5. Uploading from Memory (Without Files)

```python
import io

def upload_string(bucket_name, object_name, content):
    """Upload string content directly to S3."""
    s3_client = boto3.client('s3')
    
    try:
        s3_client.put_object(
            Bucket=bucket_name,
            Key=object_name,
            Body=content.encode('utf-8')
        )
        print(f"✓ Uploaded string content to {object_name}")
        
    except ClientError as e:
        print(f"Error: {e}")

# Usage
upload_string('my-bucket', 'logs/app.log', 'Application started\nUser logged in\n')

def upload_dataframe(bucket_name, object_name, df):
    """Upload pandas DataFrame as CSV to S3."""
    import pandas as pd
    
    s3_client = boto3.client('s3')
    csv_buffer = io.StringIO()
    df.to_csv(csv_buffer, index=False)
    
    try:
        s3_client.put_object(
            Bucket=bucket_name,
            Key=object_name,
            Body=csv_buffer.getvalue()
        )
        print(f"✓ Uploaded DataFrame to {object_name}")
        
    except ClientError as e:
        print(f"Error: {e}")

# Usage
import pandas as pd
df = pd.DataFrame({'col1': [1, 2, 3], 'col2': ['a', 'b', 'c']})
upload_dataframe('my-bucket', 'data/output.csv', df)

def download_to_dataframe(bucket_name, object_name):
    """Download CSV from S3 directly to pandas DataFrame."""
    import pandas as pd
    
    s3_client = boto3.client('s3')
    
    try:
        obj = s3_client.get_object(Bucket=bucket_name, Key=object_name)
        df = pd.read_csv(io.BytesIO(obj['Body'].read()))
        print(f"✓ Downloaded {object_name} to DataFrame")
        return df
        
    except ClientError as e:
        print(f"Error: {e}")
        return None

# Usage
df = download_to_dataframe('my-bucket', 'data/sales.csv')
```

### 6. Working with JSON Data

```python
import json

def upload_json(bucket_name, object_name, data):
    """Upload Python dict as JSON to S3."""
    s3_client = boto3.client('s3')
    
    try:
        s3_client.put_object(
            Bucket=bucket_name,
            Key=object_name,
            Body=json.dumps(data, indent=2),
            ContentType='application/json'
        )
        print(f"✓ Uploaded JSON to {object_name}")
        
    except ClientError as e:
        print(f"Error: {e}")

# Usage
data = {
    'users': [
        {'id': 1, 'name': 'Alice'},
        {'id': 2, 'name': 'Bob'}
    ]
}
upload_json('my-bucket', 'data/users.json', data)

def download_json(bucket_name, object_name):
    """Download JSON from S3 and parse to Python dict."""
    s3_client = boto3.client('s3')
    
    try:
        obj = s3_client.get_object(Bucket=bucket_name, Key=object_name)
        data = json.loads(obj['Body'].read())
        print(f"✓ Downloaded and parsed {object_name}")
        return data
        
    except ClientError as e:
        print(f"Error: {e}")
        return None

# Usage
users = download_json('my-bucket', 'data/users.json')
```

### 7. Using the Resource Interface

```python
def resource_interface_examples():
    """Examples using boto3 resource interface (more pythonic)."""
    s3 = boto3.resource('s3')
    
    # List all buckets
    print("Buckets:")
    for bucket in s3.buckets.all():
        print(f"  • {bucket.name}")
    
    # Access a specific bucket
    bucket = s3.Bucket('my-bucket')
    
    # Upload file
    bucket.upload_file('data.csv', 'uploads/data.csv')
    
    # List objects in bucket
    print("\nObjects:")
    for obj in bucket.objects.filter(Prefix='uploads/'):
        print(f"  • {obj.key} ({obj.size} bytes)")
    
    # Download object
    obj = s3.Object('my-bucket', 'uploads/data.csv')
    obj.download_file('local_data.csv')
    
    # Delete object
    obj.delete()
    
    # Get object metadata
    obj = s3.Object('my-bucket', 'file.txt')
    print(f"Last modified: {obj.last_modified}")
    print(f"Content type: {obj.content_type}")

# Usage
resource_interface_examples()
```

---

## Advanced: Performance & Production Patterns

### 1. Multipart Upload for Large Files

```python
from boto3.s3.transfer import TransferConfig

def multipart_upload(file_path, bucket_name, object_name):
    """
    Upload large files using multipart upload.
    Automatically splits files into chunks for parallel upload.
    """
    # Configure multipart upload
    config = TransferConfig(
        multipart_threshold=1024 * 25,  # 25 MB
        max_concurrency=10,
        multipart_chunksize=1024 * 25,
        use_threads=True
    )
    
    s3_client = boto3.client('s3')
    
    try:
        s3_client.upload_file(
            file_path,
            bucket_name,
            object_name,
            Config=config
        )
        print(f"✓ Uploaded {file_path} using multipart upload")
        
    except ClientError as e:
        print(f"Error: {e}")

# Usage
multipart_upload('large_video.mp4', 'my-bucket', 'videos/large_video.mp4')
```

### 2. Progress Bar for Uploads/Downloads

```python
import os
from tqdm import tqdm

class ProgressPercentage:
    """Callback class for tracking upload/download progress."""
    
    def __init__(self, filename):
        self._filename = filename
        self._size = float(os.path.getsize(filename))
        self._seen_so_far = 0
        self._lock = threading.Lock()
        
    def __call__(self, bytes_amount):
        with self._lock:
            self._seen_so_far += bytes_amount
            percentage = (self._seen_so_far / self._size) * 100
            print(f"\r{self._filename}: {self._seen_so_far}/{self._size} ({percentage:.2f}%)", end='')

def upload_with_progress(file_path, bucket_name, object_name):
    """Upload with progress tracking."""
    s3_client = boto3.client('s3')
    
    try:
        s3_client.upload_file(
            file_path,
            bucket_name,
            object_name,
            Callback=ProgressPercentage(file_path)
        )
        print(f"\n✓ Upload complete")
        
    except ClientError as e:
        print(f"\nError: {e}")

# Modern approach with tqdm
import threading

def upload_with_tqdm(file_path, bucket_name, object_name):
    """Upload with tqdm progress bar."""
    s3_client = boto3.client('s3')
    file_size = os.path.getsize(file_path)
    
    with tqdm(total=file_size, unit='B', unit_scale=True, desc=file_path) as pbar:
        s3_client.upload_file(
            file_path,
            bucket_name,
            object_name,
            Callback=lambda bytes_transferred: pbar.update(bytes_transferred)
        )
    
    print("✓ Upload complete")

# Usage
upload_with_tqdm('large_file.zip', 'my-bucket', 'archives/large_file.zip')
```

### 3. Batch Operations

```python
from concurrent.futures import ThreadPoolExecutor, as_completed

def batch_upload(files, bucket_name, prefix='', max_workers=10):
    """
    Upload multiple files in parallel.
    
    Args:
        files: List of file paths to upload
        bucket_name: Target bucket
        prefix: S3 prefix/folder
        max_workers: Number of parallel threads
    """
    s3_client = boto3.client('s3')
    
    def upload_file(file_path):
        object_name = prefix + os.path.basename(file_path)
        try:
            s3_client.upload_file(file_path, bucket_name, object_name)
            return f"✓ {file_path}"
        except Exception as e:
            return f"✗ {file_path}: {e}"
    
    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        futures = [executor.submit(upload_file, f) for f in files]
        
        for future in as_completed(futures):
            print(future.result())

# Usage
files = ['file1.txt', 'file2.txt', 'file3.txt']
batch_upload(files, 'my-bucket', prefix='uploads/')

def batch_download(bucket_name, object_keys, local_dir, max_workers=10):
    """Download multiple files in parallel."""
    s3_client = boto3.client('s3')
    
    os.makedirs(local_dir, exist_ok=True)
    
    def download_file(object_key):
        local_path = os.path.join(local_dir, os.path.basename(object_key))
        try:
            s3_client.download_file(bucket_name, object_key, local_path)
            return f"✓ {object_key}"
        except Exception as e:
            return f"✗ {object_key}: {e}"
    
    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        futures = [executor.submit(download_file, key) for key in object_keys]
        
        for future in as_completed(futures):
            print(future.result())

# Usage
keys = ['data/file1.csv', 'data/file2.csv', 'data/file3.csv']
batch_download('my-bucket', keys, './downloads')
```

### 4. Pagination for Large Result Sets

```python
def list_all_objects(bucket_name, prefix=''):
    """
    List all objects in bucket, handling pagination.
    S3 returns max 1000 objects per request.
    """
    s3_client = boto3.client('s3')
    paginator = s3_client.get_paginator('list_objects_v2')
    
    page_iterator = paginator.paginate(
        Bucket=bucket_name,
        Prefix=prefix
    )
    
    all_objects = []
    
    try:
        for page in page_iterator:
            if 'Contents' in page:
                for obj in page['Contents']:
                    all_objects.append({
                        'key': obj['Key'],
                        'size': obj['Size'],
                        'last_modified': obj['LastModified']
                    })
        
        print(f"Found {len(all_objects)} objects")
        return all_objects
        
    except ClientError as e:
        print(f"Error: {e}")
        return []

# Usage
objects = list_all_objects('my-bucket', prefix='logs/')

def search_objects(bucket_name, search_term):
    """Search for objects containing a term in their key."""
    all_objects = list_all_objects(bucket_name)
    
    matching = [obj for obj in all_objects if search_term in obj['key']]
    
    print(f"Found {len(matching)} objects matching '{search_term}':")
    for obj in matching:
        print(f"  • {obj['key']}")
    
    return matching

# Usage
search_objects('my-bucket', '2024')
```

### 5. Error Handling and Retry Logic

```python
from botocore.exceptions import ClientError, NoCredentialsError
import time

def robust_upload(file_path, bucket_name, object_name, max_retries=3):
    """Upload with retry logic and comprehensive error handling."""
    s3_client = boto3.client('s3')
    
    for attempt in range(max_retries):
        try:
            s3_client.upload_file(file_path, bucket_name, object_name)
            print(f"✓ Upload successful on attempt {attempt + 1}")
            return True
            
        except FileNotFoundError:
            print(f"Error: File '{file_path}' not found")
            return False
            
        except NoCredentialsError:
            print("Error: AWS credentials not found")
            return False
            
        except ClientError as e:
            error_code = e.response['Error']['Code']
            
            if error_code == 'NoSuchBucket':
                print(f"Error: Bucket '{bucket_name}' does not exist")
                return False
                
            elif error_code == 'AccessDenied':
                print("Error: Access denied. Check your IAM permissions")
                return False
                
            elif error_code in ['RequestTimeout', 'SlowDown']:
                if attempt < max_retries - 1:
                    wait_time = (2 ** attempt)  # Exponential backoff
                    print(f"Retry {attempt + 1}/{max_retries} after {wait_time}s...")
                    time.sleep(wait_time)
                else:
                    print("Error: Max retries exceeded")
                    return False
            else:
                print(f"Error: {e}")
                return False
                
        except Exception as e:
            print(f"Unexpected error: {e}")
            return False
    
    return False

# Usage
robust_upload('data.csv', 'my-bucket', 'data/data.csv')
```

### 6. Object Versioning

```python
def enable_versioning(bucket_name):
    """Enable versioning on a bucket."""
    s3_client = boto3.client('s3')
    
    try:
        s3_client.put_bucket_versioning(
            Bucket=bucket_name,
            VersioningConfiguration={'Status': 'Enabled'}
        )
        print(f"✓ Versioning enabled on {bucket_name}")
        
    except ClientError as e:
        print(f"Error: {e}")

# Usage
enable_versioning('my-bucket')

def list_object_versions(bucket_name, object_key):
    """List all versions of an object."""
    s3_client = boto3.client('s3')
    
    try:
        response = s3_client.list_object_versions(
            Bucket=bucket_name,
            Prefix=object_key
        )
        
        if 'Versions' in response:
            print(f"Versions of {object_key}:")
            for version in response['Versions']:
                print(f"  • Version ID: {version['VersionId']}")
                print(f"    Last Modified: {version['LastModified']}")
                print(f"    Size: {version['Size']} bytes")
                print(f"    Is Latest: {version['IsLatest']}")
                print()
        
    except ClientError as e:
        print(f"Error: {e}")

# Usage
list_object_versions('my-bucket', 'important-file.txt')

def download_specific_version(bucket_name, object_key, version_id, file_path):
    """Download a specific version of an object."""
    s3_client = boto3.client('s3')
    
    try:
        s3_client.download_file(
            bucket_name,
            object_key,
            file_path,
            ExtraArgs={'VersionId': version_id}
        )
        print(f"✓ Downloaded version {version_id}")
        
    except ClientError as e:
        print(f"Error: {e}")

# Usage
download_specific_version('my-bucket', 'file.txt', 'version-id-here', 'old-version.txt')
```

### 7. S3 Select - Query Data Without Downloading

```python
def query_csv_with_s3_select(bucket_name, object_key, sql_query):
    """
    Query CSV files using SQL without downloading entire file.
    Much faster and cheaper for large files!
    """
    s3_client = boto3.client('s3')
    
    try:
        response = s3_client.select_object_content(
            Bucket=bucket_name,
            Key=object_key,
            ExpressionType='SQL',
            Expression=sql_query,
            InputSerialization={
                'CSV': {
                    'FileHeaderInfo': 'USE',  # Use first row as headers
                    'FieldDelimiter': ','
                }
            },
            OutputSerialization={
                'CSV': {}
            }
        )
        
        # Process the streaming response
        results = []
        for event in response['Payload']:
            if 'Records' in event:
                records = event['Records']['Payload'].decode('utf-8')
                results.append(records)
        
        result_data = ''.join(results)
        print("Query results:")
        print(result_data)
        return result_data
        
    except ClientError as e:
        print(f"Error: {e}")
        return None

# Usage examples
# Query only specific columns
query_csv_with_s3_select(
    'my-bucket',
    'data/sales.csv',
    "SELECT customer_name, total_amount FROM S3Object WHERE total_amount > 1000"
)

# Count rows matching condition
query_csv_with_s3_select(
    'my-bucket',
    'data/sales.csv',
    "SELECT COUNT(*) FROM S3Object WHERE region = 'North'"
)
```

### 8. Transfer Acceleration

```python
def enable_transfer_acceleration(bucket_name):
    """Enable S3 Transfer Acceleration for faster uploads from distant locations."""
    s3_client = boto3.client('s3')
    
    try:
        s3_client.put_bucket_accelerate_configuration(
            Bucket=bucket_name,
            AccelerateConfiguration={'Status': 'Enabled'}
        )
        print(f"✓ Transfer Acceleration enabled on {bucket_name}")
        
    except ClientError as e:
        print(f"Error: {e}")

def upload_with_acceleration(file_path, bucket_name, object_name):
    """Upload using Transfer Acceleration."""
    # Use the accelerated endpoint
    s3_client = boto3.client(
        's3',
        config=boto3.session.Config(s3={'use_accelerate_endpoint': True})
    )
    
    try:
        s3_client.upload_file(file_path, bucket_name, object_name)
        print(f"✓ Uploaded via Transfer Acceleration")
        
    except ClientError as e:
        print(f"Error: {e}")

# Usage
enable_transfer_acceleration('my-bucket')
upload_with_acceleration('large-file.zip', 'my-bucket', 'uploads/large-file.zip')
```

---

## Real-World Projects

### Project 1: Automated Backup System

```python
import os
import datetime
from pathlib import Path

class S3BackupManager:
    """Automated backup system for local directories."""
    
    def __init__(self, bucket_name, backup_prefix='backups/'):
        self.s3_client = boto3.client('s3')
        self.bucket_name = bucket_name
        self.backup_prefix = backup_prefix
    
    def backup_directory(self, local_dir, include_subdirs=True):
        """Backup entire directory to S3."""
        timestamp = datetime.datetime.now().strftime('%Y%m%d_%H%M%S')
        backup_folder = f"{self.backup_prefix}{timestamp}/"
        
        files_uploaded = 0
        
        if include_subdirs:
            for root, dirs, files in os.walk(local_dir):
                for file in files:
                    local_path = os.path.join(root, file)
                    relative_path = os.path.relpath(local_path, local_dir)
                    s3_key = backup_folder + relative_path
                    
                    try:
                        self.s3_client.upload_file(local_path, self.bucket_name, s3_key)
                        files_uploaded += 1
                        print(f"✓ Backed up: {relative_path}")
                    except Exception as e:
                        print(f"✗ Failed to backup {relative_path}: {e}")
        else:
            for file in os.listdir(local_dir):
                local_path = os.path.join(local_dir, file)
                if os.path.isfile(local_path):
                    s3_key = backup_folder + file
                    
                    try:
                        self.s3_client.upload_file(local_path, self.bucket_name, s3_key)
                        files_uploaded += 1
                        print(f"✓ Backed up: {file}")
                    except Exception as e:
                        print(f"✗ Failed to backup {file}: {e}")
        
        print(f"\n✓ Backup complete! {files_uploaded} files uploaded to {backup_folder}")
        return backup_folder
    
    def list_backups(self):
        """List all available backups."""
        paginator = self.s3_client.get_paginator('list_objects_v2')
        
        backups = set()
        for page in paginator.paginate(Bucket=self.bucket_name, Prefix=self.backup_prefix):
            if 'Contents' in page:
                for obj in page['Contents']:
                    # Extract backup timestamp from path
                    parts = obj['Key'].split('/')
                    if len(parts) > 1:
                        backups.add(parts[1])
        
        print("Available backups:")
        for backup in sorted(backups, reverse=True):
            print(f"  • {backup}")
        
        return list(backups)
    
    def restore_backup(self, backup_id, restore_dir):
        """Restore a specific backup to local directory."""
        os.makedirs(restore_dir, exist_ok=True)
        
        backup_prefix = f"{self.backup_prefix}{backup_id}/"
        paginator = self.s3_client.get_paginator('list_objects_v2')
        
        files_restored = 0
        for page in paginator.paginate(Bucket=self.bucket_name, Prefix=backup_prefix):
            if 'Contents' in page:
                for obj in page['Contents']:
                    # Remove backup prefix to get relative path
                    relative_path = obj['Key'][len(backup_prefix):]
                    if relative_path:  # Skip directory markers
                        local_path = os.path.join(restore_dir, relative_path)
                        
                        # Create parent directories
                        os.makedirs(os.path.dirname(local_path), exist_ok=True)
                        
                        try:
                            self.s3_client.download_file(
                                self.bucket_name,
                                obj['Key'],
                                local_path
                            )
                            files_restored += 1
                            print(f"✓ Restored: {relative_path}")
                        except Exception as e:
                            print(f"✗ Failed to restore {relative_path}: {e}")
        
        print(f"\n✓ Restore complete! {files_restored} files restored to {restore_dir}")

# Usage
backup_manager = S3BackupManager('my-backup-bucket')

# Create backup
backup_manager.backup_directory('./my-project')

# List backups
backup_manager.list_backups()

# Restore backup
backup_manager.restore_backup('20241214_153045', './restored-project')
```

### Project 2: Image Processing Pipeline

```python
from PIL import Image
import io

class S3ImageProcessor:
    """Process images stored in S3 without downloading to disk."""
    
    def __init__(self, bucket_name):
        self.s3_client = boto3.client('s3')
        self.bucket_name = bucket_name
    
    def resize_image(self, source_key, dest_key, size=(800, 600)):
        """Resize image and save back to S3."""
        try:
            # Download image to memory
            response = self.s3_client.get_object(Bucket=self.bucket_name, Key=source_key)
            img_data = response['Body'].read()
            
            # Process image
            img = Image.open(io.BytesIO(img_data))
            img.thumbnail(size, Image.Resampling.LANCZOS)
            
            # Save to memory buffer
            buffer = io.BytesIO()
            img_format = img.format or 'JPEG'
            img.save(buffer, format=img_format)
            buffer.seek(0)
            
            # Upload back to S3
            self.s3_client.put_object(
                Bucket=self.bucket_name,
                Key=dest_key,
                Body=buffer,
                ContentType=f'image/{img_format.lower()}'
            )
            
            print(f"✓ Resized {source_key} -> {dest_key}")
            return True
            
        except Exception as e:
            print(f"Error: {e}")
            return False
    
    def create_thumbnail(self, source_key, size=(150, 150)):
        """Create thumbnail with consistent naming."""
        path_parts = source_key.rsplit('.', 1)
        dest_key = f"{path_parts[0]}_thumb.{path_parts[1]}"
        return self.resize_image(source_key, dest_key, size)
    
    def batch_process_images(self, prefix='images/', size=(800, 600)):
        """Process all images in a folder."""
        paginator = self.s3_client.get_paginator('list_objects_v2')
        
        for page in paginator.paginate(Bucket=self.bucket_name, Prefix=prefix):
            if 'Contents' in page:
                for obj in page['Contents']:
                    key = obj['Key']
                    if key.lower().endswith(('.jpg', '.jpeg', '.png', '.gif')):
                        # Create resized version in 'processed' folder
                        dest_key = key.replace(prefix, f'{prefix}processed/')
                        self.resize_image(key, dest_key, size)

# Usage
processor = S3ImageProcessor('my-images-bucket')

# Resize single image
processor.resize_image('photos/vacation.jpg', 'photos/vacation_resized.jpg', (1024, 768))

# Create thumbnail
processor.create_thumbnail('photos/vacation.jpg')

# Process all images in folder
processor.batch_process_images('uploads/', size=(800, 600))
```

### Project 3: Data Lake Manager

```python
import pandas as pd
from datetime import datetime

class S3DataLake:
    """Manage a data lake on S3 with partitioned data."""
    
    def __init__(self, bucket_name, base_prefix='datalake/'):
        self.s3_client = boto3.client('s3')
        self.bucket_name = bucket_name
        self.base_prefix = base_prefix
    
    def write_partitioned_data(self, df, table_name, partition_cols=None):
        """
        Write DataFrame to S3 with partitioning.
        
        Args:
            df: pandas DataFrame
            table_name: Name of the table/dataset
            partition_cols: List of columns to partition by (e.g., ['year', 'month'])
        """
        if partition_cols:
            # Group by partition columns
            for partition_values, group_df in df.groupby(partition_cols):
                # Build partition path
                if isinstance(partition_values, tuple):
                    partition_path = '/'.join([
                        f"{col}={val}" 
                        for col, val in zip(partition_cols, partition_values)
                    ])
                else:
                    partition_path = f"{partition_cols[0]}={partition_values}"
                
                # Create unique filename
                timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
                s3_key = f"{self.base_prefix}{table_name}/{partition_path}/data_{timestamp}.parquet"
                
                # Write partition to S3
                self._write_dataframe(group_df, s3_key)
                print(f"✓ Wrote partition: {partition_path}")
        else:
            # No partitioning - write entire dataframe
            timestamp = datetime.now().strftime('%Y%m%d_%H%M%S')
            s3_key = f"{self.base_prefix}{table_name}/data_{timestamp}.parquet"
            self._write_dataframe(df, s3_key)
            print(f"✓ Wrote data to {s3_key}")
    
    def _write_dataframe(self, df, s3_key):
        """Write DataFrame as Parquet to S3."""
        buffer = io.BytesIO()
        df.to_parquet(buffer, index=False)
        buffer.seek(0)
        
        self.s3_client.put_object(
            Bucket=self.bucket_name,
            Key=s3_key,
            Body=buffer
        )
    
    def read_partitioned_data(self, table_name, partition_filter=None):
        """
        Read data from S3 data lake with optional partition filtering.
        
        Args:
            table_name: Name of the table
            partition_filter: Dict of partition filters, e.g., {'year': '2024', 'month': '12'}
        """
        prefix = f"{self.base_prefix}{table_name}/"
        
        if partition_filter:
            for key, value in partition_filter.items():
                prefix += f"{key}={value}/"
        
        # List all parquet files
        paginator = self.s3_client.get_paginator('list_objects_v2')
        parquet_files = []
        
        for page in paginator.paginate(Bucket=self.bucket_name, Prefix=prefix):
            if 'Contents' in page:
                for obj in page['Contents']:
                    if obj['Key'].endswith('.parquet'):
                        parquet_files.append(obj['Key'])
        
        # Read and combine all parquet files
        dfs = []
        for s3_key in parquet_files:
            obj = self.s3_client.get_object(Bucket=self.bucket_name, Key=s3_key)
            df = pd.read_parquet(io.BytesIO(obj['Body'].read()))
            dfs.append(df)
            print(f"✓ Read: {s3_key}")
        
        if dfs:
            combined_df = pd.concat(dfs, ignore_index=True)
            print(f"\n✓ Loaded {len(combined_df)} rows")
            return combined_df
        else:
            print("No data found")
            return pd.DataFrame()
    
    def list_tables(self):
        """List all tables in the data lake."""
        prefix = self.base_prefix
        paginator = self.s3_client.get_paginator('list_objects_v2')
        
        tables = set()
        for page in paginator.paginate(Bucket=self.bucket_name, Prefix=prefix, Delimiter='/'):
            if 'CommonPrefixes' in page:
                for prefix_obj in page['CommonPrefixes']:
                    table_name = prefix_obj['Prefix'].replace(prefix, '').rstrip('/')
                    tables.add(table_name)
        
        print("Available tables:")
        for table in sorted(tables):
            print(f"  • {table}")
        
        return list(tables)

# Usage
datalake = S3DataLake('my-datalake-bucket')

# Create sample data
df = pd.DataFrame({
    'transaction_id': range(1000),
    'amount': [100.0 + i for i in range(1000)],
    'year': ['2024'] * 1000,
    'month': ['12'] * 500 + ['11'] * 500,
    'category': ['A'] * 500 + ['B'] * 500
})

# Write partitioned data
datalake.write_partitioned_data(df, 'transactions', partition_cols=['year', 'month'])

# Read specific partition
df_december = datalake.read_partitioned_data(
    'transactions',
    partition_filter={'year': '2024', 'month': '12'}
)

# List all tables
datalake.list_tables()
```

### Project 4: Log Aggregator

```python
import gzip
from datetime import datetime, timedelta

class S3LogAggregator:
    """Aggregate and analyze log files stored in S3."""
    
    def __init__(self, bucket_name, logs_prefix='logs/'):
        self.s3_client = boto3.client('s3')
        self.bucket_name = bucket_name
        self.logs_prefix = logs_prefix
    
    def upload_log(self, log_content, app_name, log_level='INFO'):
        """Upload log entry to S3 with automatic compression."""
        timestamp = datetime.now()
        
        # Organize by date and app
        s3_key = (
            f"{self.logs_prefix}"
            f"{app_name}/"
            f"year={timestamp.year}/"
            f"month={timestamp.month:02d}/"
            f"day={timestamp.day:02d}/"
            f"{timestamp.strftime('%Y%m%d_%H%M%S')}_{log_level}.log.gz"
        )
        
        # Compress log content
        compressed = gzip.compress(log_content.encode('utf-8'))
        
        try:
            self.s3_client.put_object(
                Bucket=self.bucket_name,
                Key=s3_key,
                Body=compressed,
                ContentType='application/gzip',
                Metadata={
                    'app': app_name,
                    'level': log_level,
                    'timestamp': timestamp.isoformat()
                }
            )
            print(f"✓ Uploaded log: {s3_key}")
            return s3_key
            
        except ClientError as e:
            print(f"Error: {e}")
            return None
    
    def read_logs(self, app_name, start_date, end_date=None, log_level=None):
        """Read and decompress logs for a date range."""
        if end_date is None:
            end_date = datetime.now()
        
        logs = []
        current_date = start_date
        
        while current_date <= end_date:
            prefix = (
                f"{self.logs_prefix}{app_name}/"
                f"year={current_date.year}/"
                f"month={current_date.month:02d}/"
                f"day={current_date.day:02d}/"
            )
            
            # List logs for this day
            response = self.s3_client.list_objects_v2(
                Bucket=self.bucket_name,
                Prefix=prefix
            )
            
            if 'Contents' in response:
                for obj in response['Contents']:
                    # Filter by log level if specified
                    if log_level and log_level not in obj['Key']:
                        continue
                    
                    # Download and decompress
                    try:
                        response = self.s3_client.get_object(
                            Bucket=self.bucket_name,
                            Key=obj['Key']
                        )
                        
                        compressed_data = response['Body'].read()
                        log_content = gzip.decompress(compressed_data).decode('utf-8')
                        
                        logs.append({
                            'key': obj['Key'],
                            'content': log_content,
                            'size': obj['Size'],
                            'timestamp': obj['LastModified']
                        })
                        
                    except Exception as e:
                        print(f"Error reading {obj['Key']}: {e}")
            
            current_date += timedelta(days=1)
        
        print(f"✓ Read {len(logs)} log files")
        return logs
    
    def search_logs(self, app_name, search_term, days_back=7):
        """Search logs for specific term."""
        end_date = datetime.now()
        start_date = end_date - timedelta(days=days_back)
        
        logs = self.read_logs(app_name, start_date, end_date)
        
        matches = []
        for log in logs:
            lines = log['content'].split('\n')
            for line_num, line in enumerate(lines, 1):
                if search_term in line:
                    matches.append({
                        'file': log['key'],
                        'line_number': line_num,
                        'content': line.strip()
                    })
        
        print(f"\nFound {len(matches)} matches for '{search_term}':")
        for match in matches[:10]:  # Show first 10
            print(f"  {match['file']}:{match['line_number']}")
            print(f"    {match['content'][:100]}...")
        
        return matches

# Usage
log_aggregator = S3LogAggregator('my-logs-bucket')

# Upload logs
log_aggregator.upload_log(
    "Application started successfully\nUser logged in: john@example.com",
    app_name='web-app',
    log_level='INFO'
)

log_aggregator.upload_log(
    "Database connection failed\nRetrying in 5 seconds",
    app_name='web-app',
    log_level='ERROR'
)

# Read logs from last 7 days
logs = log_aggregator.read_logs(
    'web-app',
    start_date=datetime.now() - timedelta(days=7)
)

# Search for errors
log_aggregator.search_logs('web-app', 'ERROR', days_back=30)
```

---

## Best Practices & Security

### 1. Secure Credential Management

```python
# ❌ NEVER DO THIS - Hardcoded credentials
s3 = boto3.client(
    's3',
    aws_access_key_id='AKIAIOSFODNN7EXAMPLE',
    aws_secret_access_key='wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY'
)

# ✅ USE THESE METHODS INSTEAD

# Method 1: Environment variables (best for local development)
import os
os.environ['AWS_ACCESS_KEY_ID'] = 'your_key'
os.environ['AWS_SECRET_ACCESS_KEY'] = 'your_secret'
s3 = boto3.client('s3')

# Method 2: AWS CLI configuration (recommended)
# Run: aws configure
s3 = boto3.client('s3')

# Method 3: IAM Roles (best for EC2/Lambda/ECS)
s3 = boto3.client('s3')  # Automatically uses IAM role

# Method 4: Using .env files with python-dotenv
from dotenv import load_dotenv
load_dotenv()  # Loads from .env file
s3 = boto3.client('s3')
```

### 2. Implementing Proper Access Control

```python
def set_bucket_policy_public_read(bucket_name, prefix='public/'):
    """Set bucket policy for public read access to specific prefix."""
    s3_client = boto3.client('s3')
    
    policy = {
        "Version": "2012-10-17",
        "Statement": [
            {
                "Sid": "PublicReadGetObject",
                "Effect": "Allow",
                "Principal": "*",
                "Action": "s3:GetObject",
                "Resource": f"arn:aws:s3:::{bucket_name}/{prefix}*"
            }
        ]
    }
    
    try:
        s3_client.put_bucket_policy(
            Bucket=bucket_name,
            Policy=json.dumps(policy)
        )
        print(f"✓ Public read policy applied to {prefix}")
        
    except ClientError as e:
        print(f"Error: {e}")

def set_bucket_policy_specific_user(bucket_name, user_arn):
    """Grant specific IAM user access to bucket."""
    s3_client = boto3.client('s3')
    
    policy = {
        "Version": "2012-10-17",
        "Statement": [
            {
                "Effect": "Allow",
                "Principal": {"AWS": user_arn},
                "Action": [
                    "s3:GetObject",
                    "s3:PutObject",
                    "s3:DeleteObject"
                ],
                "Resource": f"arn:aws:s3:::{bucket_name}/*"
            }
        ]
    }
    
    try:
        s3_client.put_bucket_policy(
            Bucket=bucket_name,
            Policy=json.dumps(policy)
        )
        print(f"✓ Access granted to {user_arn}")
        
    except ClientError as e:
        print(f"Error: {e}")
```

### 3. Enabling Encryption

```python
def enable_default_encryption(bucket_name, kms_key_id=None):
    """Enable default encryption for all new objects."""
    s3_client = boto3.client('s3')
    
    if kms_key_id:
        # Use KMS encryption
        encryption_config = {
            'Rules': [{
                'ApplyServerSideEncryptionByDefault': {
                    'SSEAlgorithm': 'aws:kms',
                    'KMSMasterKeyID': kms_key_id
                },
                'BucketKeyEnabled': True
            }]
        }
    else:
        # Use S3-managed encryption
        encryption_config = {
            'Rules': [{
                'ApplyServerSideEncryptionByDefault': {
                    'SSEAlgorithm': 'AES256'
                }
            }]
        }
    
    try:
        s3_client.put_bucket_encryption(
            Bucket=bucket_name,
            ServerSideEncryptionConfiguration=encryption_config
        )
        print(f"✓ Default encryption enabled")
        
    except ClientError as e:
        print(f"Error: {e}")

# Upload with explicit encryption
def upload_encrypted(file_path, bucket_name, object_name):
    """Upload file with server-side encryption."""
    s3_client = boto3.client('s3')
    
    try:
        s3_client.upload_file(
            file_path,
            bucket_name,
            object_name,
            ExtraArgs={'ServerSideEncryption': 'AES256'}
        )
        print(f"✓ Uploaded with encryption")
        
    except ClientError as e:
        print(f"Error: {e}")
```

### 4. Implementing Lifecycle Policies

```python
def set_lifecycle_policy(bucket_name):
    """Set lifecycle policy to automatically manage object lifecycle."""
    s3_client = boto3.client('s3')
    
    lifecycle_policy = {
        'Rules': [
            {
                'ID': 'Move to IA after 30 days',
                'Status': 'Enabled',
                'Filter': {'Prefix': 'documents/'},
                'Transitions': [
                    {
                        'Days': 30,
                        'StorageClass': 'STANDARD_IA'
                    },
                    {
                        'Days': 90,
                        'StorageClass': 'GLACIER'
                    }
                ]
            },
            {
                'ID': 'Delete old logs',
                'Status': 'Enabled',
                'Filter': {'Prefix': 'logs/'},
                'Expiration': {'Days': 90}
            },
            {
                'ID': 'Delete incomplete multipart uploads',
                'Status': 'Enabled',
                'Filter': {},
                'AbortIncompleteMultipartUpload': {'DaysAfterInitiation': 7}
            }
        ]
    }
    
    try:
        s3_client.put_bucket_lifecycle_configuration(
            Bucket=bucket_name,
            LifecycleConfiguration=lifecycle_policy
        )
        print(f"✓ Lifecycle policy applied")
        
    except ClientError as e:
        print(f"Error: {e}")
```

### 5. Monitoring and Logging

```python
def enable_server_access_logging(bucket_name, log_bucket_name, log_prefix='access-logs/'):
    """Enable S3 server access logging."""
    s3_client = boto3.client('s3')
    
    try:
        s3_client.put_bucket_logging(
            Bucket=bucket_name,
            BucketLoggingStatus={
                'LoggingEnabled': {
                    'TargetBucket': log_bucket_name,
                    'TargetPrefix': log_prefix
                }
            }
        )
        print(f"✓ Access logging enabled")
        
    except ClientError as e:
        print(f"Error: {e}")

def get_bucket_metrics(bucket_name):
    """Get CloudWatch metrics for bucket."""
    cloudwatch = boto3.client('cloudwatch')
    
    try:
        # Get number of objects
        response = cloudwatch.get_metric_statistics(
            Namespace='AWS/S3',
            MetricName='NumberOfObjects',
            Dimensions=[
                {'Name': 'BucketName', 'Value': bucket_name},
                {'Name': 'StorageType', 'Value': 'AllStorageTypes'}
            ],
            StartTime=datetime.now() - timedelta(days=1),
            EndTime=datetime.now(),
            Period=86400,
            Statistics=['Average']
        )
        
        if response['Datapoints']:
            num_objects = response['Datapoints'][0]['Average']
            print(f"Number of objects: {num_objects:,.0f}")
        
        # Get bucket size
        response = cloudwatch.get_metric_statistics(
            Namespace='AWS/S3',
            MetricName='BucketSizeBytes',
            Dimensions=[
                {'Name': 'BucketName', 'Value': bucket_name},
                {'Name': 'StorageType', 'Value': 'StandardStorage'}
            ],
            StartTime=datetime.now() - timedelta(days=1),
            EndTime=datetime.now(),
            Period=86400,
            Statistics=['Average']
        )
        
        if response['Datapoints']:
            size_bytes = response['Datapoints'][0]['Average']
            size_gb = size_bytes / (1024**3)
            print(f"Bucket size: {size_gb:.2f} GB")
        
    except ClientError as e:
        print(f"Error: {e}")
```

### 6. Cost Optimization

```python
class S3CostOptimizer:
    """Tools for optimizing S3 costs."""
    
    def __init__(self, bucket_name):
        self.s3_client = boto3.client('s3')
        self.bucket_name = bucket_name
    
    def find_large_objects(self, size_threshold_mb=100):
        """Find objects larger than threshold."""
        paginator = self.s3_client.get_paginator('list_objects_v2')
        
        large_objects = []
        total_size = 0
        
        for page in paginator.paginate(Bucket=self.bucket_name):
            if 'Contents' in page:
                for obj in page['Contents']:
                    size_mb = obj['Size'] / (1024 * 1024)
                    if size_mb > size_threshold_mb:
                        large_objects.append({
                            'key': obj['Key'],
                            'size_mb': size_mb,
                            'last_modified': obj['LastModified']
                        })
                        total_size += size_mb
        
        print(f"Found {len(large_objects)} objects > {size_threshold_mb}MB")
        print(f"Total size: {total_size:,.2f} MB")
        
        # Sort by size
        large_objects.sort(key=lambda x: x['size_mb'], reverse=True)
        
        print("\nTop 10 largest objects:")
        for obj in large_objects[:10]:
            print(f"  {obj['size_mb']:>10.2f} MB - {obj['key']}")
        
        return large_objects
    
    def find_old_objects(self, days_old=180):
        """Find objects not modified in X days."""
        paginator = self.s3_client.get_paginator('list_objects_v2')
        cutoff_date = datetime.now(datetime.timezone.utc) - timedelta(days=days_old)
        
        old_objects = []
        
        for page in paginator.paginate(Bucket=self.bucket_name):
            if 'Contents' in page:
                for obj in page['Contents']:
                    if obj['LastModified'] < cutoff_date:
                        days_since = (datetime.now(datetime.timezone.utc) - obj['LastModified']).days
                        old_objects.append({
                            'key': obj['Key'],
                            'size_mb': obj['Size'] / (1024 * 1024),
                            'days_old': days_since
                        })
        
        total_size = sum(obj['size_mb'] for obj in old_objects)
        
        print(f"Found {len(old_objects)} objects older than {days_old} days")
        print(f"Total size: {total_size:,.2f} MB")
        
        return old_objects
    
    def analyze_storage_classes(self):
        """Analyze distribution of storage classes."""
        paginator = self.s3_client.get_paginator('list_objects_v2')
        
        storage_stats = {}
        
        for page in paginator.paginate(Bucket=self.bucket_name):
            if 'Contents' in page:
                for obj in page['Contents']:
                    storage_class = obj.get('StorageClass', 'STANDARD')
                    
                    if storage_class not in storage_stats:
                        storage_stats[storage_class] = {
                            'count': 0,
                            'total_size_gb': 0
                        }
                    
                    storage_stats[storage_class]['count'] += 1
                    storage_stats[storage_class]['total_size_gb'] += obj['Size'] / (1024**3)
        
        print("Storage class distribution:")
        for storage_class, stats in storage_stats.items():
            print(f"  {storage_class}:")
            print(f"    Objects: {stats['count']:,}")
            print(f"    Size: {stats['total_size_gb']:.2f} GB")
        
        return storage_stats
    
    def find_incomplete_multipart_uploads(self):
        """Find incomplete multipart uploads (these cost money!)."""
        response = self.s3_client.list_multipart_uploads(Bucket=self.bucket_name)
        
        if 'Uploads' not in response:
            print("No incomplete multipart uploads found")
            return []
        
        uploads = response['Uploads']
        print(f"Found {len(uploads)} incomplete multipart uploads:")
        
        for upload in uploads:
            initiated = upload['Initiated']
            days_old = (datetime.now(datetime.timezone.utc) - initiated).days
            print(f"  {upload['Key']} - {days_old} days old")
        
        return uploads
    
    def cleanup_incomplete_multipart_uploads(self):
        """Clean up all incomplete multipart uploads."""
        uploads = self.find_incomplete_multipart_uploads()
        
        for upload in uploads:
            try:
                self.s3_client.abort_multipart_upload(
                    Bucket=self.bucket_name,
                    Key=upload['Key'],
                    UploadId=upload['UploadId']
                )
                print(f"✓ Aborted: {upload['Key']}")
            except ClientError as e:
                print(f"✗ Failed to abort {upload['Key']}: {e}")

# Usage
optimizer = S3CostOptimizer('my-bucket')

# Find large files
optimizer.find_large_objects(size_threshold_mb=500)

# Find old files that could be archived
old_files = optimizer.find_old_objects(days_old=365)

# Analyze storage distribution
optimizer.analyze_storage_classes()

# Clean up incomplete uploads
optimizer.cleanup_incomplete_multipart_uploads()
```

---

## Troubleshooting

### Common Errors and Solutions

```python
from botocore.exceptions import ClientError, NoCredentialsError, PartialCredentialsError

class S3Troubleshooter:
    """Helper class for diagnosing S3 issues."""
    
    @staticmethod
    def diagnose_connection():
        """Test AWS credentials and connectivity."""
        print("🔍 Diagnosing S3 connection...\n")
        
        # Test 1: Check credentials
        print("1. Checking AWS credentials...")
        try:
            s3_client = boto3.client('s3')
            print("   ✓ Credentials loaded")
        except NoCredentialsError:
            print("   ✗ No credentials found")
            print("   Fix: Run 'aws configure' or set environment variables")
            return False
        except PartialCredentialsError:
            print("   ✗ Incomplete credentials")
            print("   Fix: Ensure both access key and secret key are set")
            return False
        
        # Test 2: List buckets
        print("\n2. Testing API access...")
        try:
            response = s3_client.list_buckets()
            print(f"   ✓ Successfully connected. Found {len(response['Buckets'])} buckets")
        except ClientError as e:
            error_code = e.response['Error']['Code']
            if error_code == 'InvalidAccessKeyId':
                print("   ✗ Invalid access key")
            elif error_code == 'SignatureDoesNotMatch':
                print("   ✗ Invalid secret key")
            elif error_code == 'AccessDenied':
                print("   ✗ Access denied - check IAM permissions")
            else:
                print(f"   ✗ Error: {e}")
            return False
        
        print("\n✓ All checks passed!")
        return True
    
    @staticmethod
    def diagnose_bucket_access(bucket_name):
        """Test access to specific bucket."""
        s3_client = boto3.client('s3')
        
        print(f"🔍 Testing access to bucket: {bucket_name}\n")
        
        # Test 1: Check if bucket exists
        print("1. Checking if bucket exists...")
        try:
            s3_client.head_bucket(Bucket=bucket_name)
            print("   ✓ Bucket exists and is accessible")
        except ClientError as e:
            error_code = e.response['Error']['Code']
            if error_code == '404':
                print("   ✗ Bucket does not exist")
            elif error_code == '403':
                print("   ✗ Access denied - check bucket policy and IAM permissions")
            else:
                print(f"   ✗ Error: {e}")
            return False
        
        # Test 2: List objects
        print("\n2. Testing list objects...")
        try:
            response = s3_client.list_objects_v2(Bucket=bucket_name, MaxKeys=1)
            print("   ✓ Can list objects")
        except ClientError as e:
            print(f"   ✗ Cannot list objects: {e}")
            return False
        
        # Test 3: Test write access
        print("\n3. Testing write access...")
        test_key = '.test-access-file'
        try:
            s3_client.put_object(Bucket=bucket_name, Key=test_key, Body=b'test')
            print("   ✓ Can write objects")
            
            # Clean up test file
            s3_client.delete_object(Bucket=bucket_name, Key=test_key)
            print("   ✓ Can delete objects")
        except ClientError as e:
            print(f"   ✗ Cannot write/delete: {e}")
            return False
        
        print("\n✓ Full access confirmed!")
        return True
    
    @staticmethod
    def check_object_permissions(bucket_name, object_key):
        """Check permissions on specific object."""
        s3_client = boto3.client('s3')
        
        print(f"🔍 Checking permissions for: {bucket_name}/{object_key}\n")
        
        try:
            # Get object ACL
            acl = s3_client.get_object_acl(Bucket=bucket_name, Key=object_key)
            
            print("Object ACL:")
            for grant in acl['Grants']:
                grantee = grant['Grantee']
                permission = grant['Permission']
                
                if grantee['Type'] == 'CanonicalUser':
                    print(f"  User: {grantee.get('DisplayName', 'Unknown')} - {permission}")
                elif grantee['Type'] == 'Group':
                    print(f"  Group: {grantee['URI']} - {permission}")
            
            # Get object metadata
            metadata = s3_client.head_object(Bucket=bucket_name, Key=object_key)
            print(f"\nStorage class: {metadata.get('StorageClass', 'STANDARD')}")
            print(f"Encryption: {metadata.get('ServerSideEncryption', 'None')}")
            print(f"Size: {metadata['ContentLength']} bytes")
            
        except ClientError as e:
            print(f"✗ Error: {e}")

# Usage
troubleshooter = S3Troubleshooter()

# Diagnose connection
troubleshooter.diagnose_connection()

# Test bucket access
troubleshooter.diagnose_bucket_access('my-bucket')

# Check object permissions
troubleshooter.check_object_permissions('my-bucket', 'data/file.txt')
```

### Debug Mode and Logging

```python
import logging

def enable_boto3_logging():
    """Enable detailed logging for debugging."""
    # Set up logging
    boto3.set_stream_logger('boto3.resources', logging.DEBUG)
    
    # Or use standard logging
    logging.basicConfig(
        level=logging.DEBUG,
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
    )
    
    # Enable boto3 debug logging
    logger = logging.getLogger('boto3')
    logger.setLevel(logging.DEBUG)
    
    logger = logging.getLogger('botocore')
    logger.setLevel(logging.DEBUG)

# Usage
enable_boto3_logging()
s3_client = boto3.client('s3')
# Now all API calls will be logged in detail
```

### Performance Testing

```python
import time

class S3PerformanceTester:
    """Test S3 performance for your use case."""
    
    def __init__(self, bucket_name):
        self.s3_client = boto3.client('s3')
        self.bucket_name = bucket_name
    
    def test_upload_speed(self, file_size_mb=10):
        """Test upload speed."""
        # Create test file in memory
        test_data = b'x' * (file_size_mb * 1024 * 1024)
        test_key = f'performance-test/upload-test-{int(time.time())}.bin'
        
        print(f"Testing upload of {file_size_mb}MB file...")
        
        start_time = time.time()
        
        try:
            self.s3_client.put_object(
                Bucket=self.bucket_name,
                Key=test_key,
                Body=test_data
            )
            
            elapsed = time.time() - start_time
            speed_mbps = file_size_mb / elapsed
            
            print(f"✓ Upload completed in {elapsed:.2f} seconds")
            print(f"  Speed: {speed_mbps:.2f} MB/s")
            
            # Cleanup
            self.s3_client.delete_object(Bucket=self.bucket_name, Key=test_key)
            
            return speed_mbps
            
        except ClientError as e:
            print(f"✗ Upload failed: {e}")
            return None
    
    def test_download_speed(self, test_key):
        """Test download speed."""
        print(f"Testing download of {test_key}...")
        
        # Get file size first
        metadata = self.s3_client.head_object(Bucket=self.bucket_name, Key=test_key)
        size_mb = metadata['ContentLength'] / (1024 * 1024)
        
        start_time = time.time()
        
        try:
            response = self.s3_client.get_object(Bucket=self.bucket_name, Key=test_key)
            data = response['Body'].read()
            
            elapsed = time.time() - start_time
            speed_mbps = size_mb / elapsed
            
            print(f"✓ Download completed in {elapsed:.2f} seconds")
            print(f"  Speed: {speed_mbps:.2f} MB/s")
            
            return speed_mbps
            
        except ClientError as e:
            print(f"✗ Download failed: {e}")
            return None
    
    def test_list_performance(self, prefix=''):
        """Test object listing performance."""
        print(f"Testing list performance for prefix: {prefix or '(root)'}...")
        
        start_time = time.time()
        
        try:
            paginator = self.s3_client.get_paginator('list_objects_v2')
            
            object_count = 0
            for page in paginator.paginate(Bucket=self.bucket_name, Prefix=prefix):
                if 'Contents' in page:
                    object_count += len(page['Contents'])
            
            elapsed = time.time() - start_time
            
            print(f"✓ Listed {object_count} objects in {elapsed:.2f} seconds")
            print(f"  Rate: {object_count/elapsed:.0f} objects/second")
            
        except ClientError as e:
            print(f"✗ List failed: {e}")

# Usage
tester = S3PerformanceTester('my-bucket')

# Test upload speed
tester.test_upload_speed(file_size_mb=50)

# Test download speed
tester.test_download_speed('large-file.zip')

# Test list performance
tester.test_list_performance(prefix='data/')
```

---

## Advanced Topics

### 1. S3 Event Notifications with Lambda

```python
def setup_lambda_trigger(bucket_name, lambda_arn, events=None):
    """
    Configure S3 to trigger Lambda function on events.
    
    Common events:
    - s3:ObjectCreated:*
    - s3:ObjectRemoved:*
    - s3:ObjectRestore:*
    """
    if events is None:
        events = ['s3:ObjectCreated:*']
    
    s3_client = boto3.client('s3')
    
    notification_config = {
        'LambdaFunctionConfigurations': [
            {
                'LambdaFunctionArn': lambda_arn,
                'Events': events,
                'Filter': {
                    'Key': {
                        'FilterRules': [
                            {'Name': 'prefix', 'Value': 'uploads/'},
                            {'Name': 'suffix', 'Value': '.jpg'}
                        ]
                    }
                }
            }
        ]
    }
    
    try:
        s3_client.put_bucket_notification_configuration(
            Bucket=bucket_name,
            NotificationConfiguration=notification_config
        )
        print(f"✓ Lambda trigger configured")
        
    except ClientError as e:
        print(f"Error: {e}")
```

### 2. Cross-Region Replication

```python
def setup_cross_region_replication(source_bucket, dest_bucket, role_arn):
    """Set up cross-region replication."""
    s3_client = boto3.client('s3')
    
    # First, enable versioning on both buckets
    for bucket in [source_bucket, dest_bucket]:
        s3_client.put_bucket_versioning(
            Bucket=bucket,
            VersioningConfiguration={'Status': 'Enabled'}
        )
    
    # Configure replication
    replication_config = {
        'Role': role_arn,
        'Rules': [
            {
                'ID': 'ReplicateAll',
                'Status': 'Enabled',
                'Priority': 1,
                'Filter': {},
                'Destination': {
                    'Bucket': f'arn:aws:s3:::{dest_bucket}',
                    'ReplicationTime': {
                        'Status': 'Enabled',
                        'Time': {'Minutes': 15}
                    },
                    'Metrics': {
                        'Status': 'Enabled',
                        'EventThreshold': {'Minutes': 15}
                    }
                },
                'DeleteMarkerReplication': {'Status': 'Enabled'}
            }
        ]
    }
    
    try:
        s3_client.put_bucket_replication(
            Bucket=source_bucket,
            ReplicationConfiguration=replication_config
        )
        print(f"✓ Replication configured from {source_bucket} to {dest_bucket}")
        
    except ClientError as e:
        print(f"Error: {e}")
```

### 3. Static Website Hosting

```python
def setup_static_website(bucket_name, index_document='index.html', error_document='error.html'):
    """Configure bucket for static website hosting."""
    s3_client = boto3.client('s3')
    
    # Configure website hosting
    website_config = {
        'IndexDocument': {'Suffix': index_document},
        'ErrorDocument': {'Key': error_document}
    }
    
    try:
        # Set website configuration
        s3_client.put_bucket_website(
            Bucket=bucket_name,
            WebsiteConfiguration=website_config
        )
        
        # Make bucket public
        bucket_policy = {
            "Version": "2012-10-17",
            "Statement": [{
                "Sid": "PublicReadGetObject",
                "Effect": "Allow",
                "Principal": "*",
                "Action": "s3:GetObject",
                "Resource": f"arn:aws:s3:::{bucket_name}/*"
            }]
        }
        
        s3_client.put_bucket_policy(
            Bucket=bucket_name,
            Policy=json.dumps(bucket_policy)
        )
        
        # Get website URL
        region = s3_client.get_bucket_location(Bucket=bucket_name)['LocationConstraint']
        if region is None:
            region = 'us-east-1'
        
        website_url = f"http://{bucket_name}.s3-website-{region}.amazonaws.com"
        
        print(f"✓ Static website configured")
        print(f"  URL: {website_url}")
        
        return website_url
        
    except ClientError as e:
        print(f"Error: {e}")
        return None

# Usage
website_url = setup_static_website('my-website-bucket')
```

### 4. Working with Requester Pays

```python
def enable_requester_pays(bucket_name):
    """Enable requester pays (data transfer costs paid by downloader)."""
    s3_client = boto3.client('s3')
    
    try:
        s3_client.put_bucket_request_payment(
            Bucket=bucket_name,
            RequestPaymentConfiguration={'Payer': 'Requester'}
        )
        print(f"✓ Requester pays enabled")
        
    except ClientError as e:
        print(f"Error: {e}")

def download_from_requester_pays_bucket(bucket_name, object_key, file_path):
    """Download from requester pays bucket."""
    s3_client = boto3.client('s3')
    
    try:
        s3_client.download_file(
            bucket_name,
            object_key,
            file_path,
            ExtraArgs={'RequestPayer': 'requester'}
        )
        print(f"✓ Downloaded from requester pays bucket")
        
    except ClientError as e:
        print(f"Error: {e}")
```

---

## Quick Reference

### Essential Commands Cheat Sheet

```python
import boto3

# Initialize
s3_client = boto3.client('s3')
s3_resource = boto3.resource('s3')

# Buckets
s3_client.create_bucket(Bucket='name')
s3_client.list_buckets()
s3_client.delete_bucket(Bucket='name')

# Objects
s3_client.upload_file('local.txt', 'bucket', 'remote.txt')
s3_client.download_file('bucket', 'remote.txt', 'local.txt')
s3_client.list_objects_v2(Bucket='bucket', Prefix='folder/')
s3_client.delete_object(Bucket='bucket', Key='file.txt')

# Metadata
s3_client.head_object(Bucket='bucket', Key='file.txt')
s3_client.put_object_tagging(Bucket='bucket', Key='file.txt', Tagging={...})

# Presigned URLs
url = s3_client.generate_presigned_url('get_object', 
    Params={'Bucket': 'bucket', 'Key': 'file.txt'}, ExpiresIn=3600)

# Memory operations
s3_client.put_object(Bucket='bucket', Key='file.txt', Body=b'data')
obj = s3_client.get_object(Bucket='bucket', Key='file.txt')
data = obj['Body'].read()
```

### Common Patterns

```python
# Pattern 1: Safe file upload with retry
def safe_upload(file_path, bucket, key, max_retries=3):
    for attempt in range(max_retries):
        try:
            boto3.client('s3').upload_file(file_path, bucket, key)
            return True
        except Exception as e:
            if attempt == max_retries - 1:
                raise
            time.sleep(2 ** attempt)

# Pattern 2: Process all objects in bucket
def process_all_objects(bucket_name, processor_func):
    s3 = boto3.client('s3')
    paginator = s3.get_paginator('list_objects_v2')
    
    for page in paginator.paginate(Bucket=bucket_name):
        if 'Contents' in page:
            for obj in page['Contents']:
                processor_func(obj)

# Pattern 3: Conditional upload (only if newer)
def upload_if_newer(local_path, bucket, key):
    s3 = boto3.client('s3')
    local_mtime = os.path.getmtime(local_path)
    
    try:
        obj = s3.head_object(Bucket=bucket, Key=key)
        s3_mtime = obj['LastModified'].timestamp()
        
        if local_mtime > s3_mtime:
            s3.upload_file(local_path, bucket, key)
            return "uploaded"
        return "skipped"
    except ClientError:
        s3.upload_file(local_path, bucket, key)
        return "uploaded"
```

---

## Conclusion

This guide covered everything from basic S3 operations to advanced production patterns for Python developers. Key takeaways:

**Beginner:**
- Use boto3 client for most operations
- Always handle `ClientError` exceptions
- Start with simple CRUD operations

**Intermediate:**
- Leverage metadata and tags for organization
- Use presigned URLs for temporary access
- Work with different storage classes for cost optimization

**Advanced:**
- Implement multipart uploads for large files
- Use batch operations with threading for performance
- Build production-ready error handling and retry logic
- Optimize costs with lifecycle policies

**Best Practices:**
- Never hardcode credentials
- Enable encryption by default
- Use lifecycle policies to reduce costs
- Implement proper monitoring and logging
- Test thoroughly with error scenarios

### Next Steps

1. **Practice**: Build one of the real-world projects
2. **Explore**: Try S3 Select, event notifications, or Lambda integration
3. **Optimize**: Use the cost optimization tools on your buckets
4. **Scale**: Implement batch operations and multipart uploads
5. **Secure**: Review and implement security best practices

### Additional Resources

- [AWS S3 Documentation](https://docs.aws.amazon.com/s3/)
- [Boto3 Documentation](https://boto3.amazonaws.com/v1/documentation/api/latest/index.html)
- [AWS SDK for Python (Boto3) on GitHub](https://github.com/boto/boto3)
- [AWS re:Post Community](https://repost.aws/)

---

**Happy coding! **