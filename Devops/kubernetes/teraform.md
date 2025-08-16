# Terraform for EKS Setup: Complete Guide

## Introduction to Amazon EKS and Terraform

Amazon EKS (Elastic Kubernetes Service) is a managed Kubernetes service that eliminates the complexity of manually managing Kubernetes clusters. Unlike self-managed clusters created with tools like kOps or Kubeadm, EKS handles the heavy lifting of cluster management, scaling, and maintenance.

### Why Use EKS?

| Traditional K8s Setup | Amazon EKS |
|----------------------|------------|
| Manual cluster creation with kOps/Kubeadm | Managed cluster provisioning |
| Complex system administration | AWS handles cluster management |
| Manual scaling and maintenance | Automated scaling and updates |
| Self-managed master nodes | Fully managed control plane |

### EKS Benefits
- **Managed Control Plane**: AWS manages the Kubernetes master nodes
- **Automatic Updates**: Regular security patches and updates
- **High Availability**: Multi-AZ control plane deployment
- **Integration**: Native AWS service integration
- **Simplified Operations**: Focus on applications, not infrastructure

> **Cost Warning**: EKS is an expensive service. Create clusters for learning/testing and destroy immediately to avoid unnecessary charges.

## EKS Architecture Overview

### Components Required
1. **EKS Cluster**: The managed control plane (master nodes)
2. **Worker Nodes**: EC2 instances running your workloads
3. **VPC**: Virtual Private Cloud for network isolation
4. **Subnets**: Public and private subnets across multiple AZs
5. **IAM Roles**: Proper permissions for EKS and worker nodes

### Pricing Structure
- **EKS Control Plane**: Charged per cluster per hour
- **Worker Nodes**: Standard EC2 pricing
- **Additional AWS Services**: VPC, NAT Gateway, EBS volumes

## Terraform Modules Overview

Terraform modules allow you to use pre-built, tested infrastructure code instead of writing everything from scratch.

### Key Modules Used
1. **VPC Module**: `terraform-aws-modules/vpc/aws`
2. **EKS Module**: `terraform-aws-modules/eks/aws`

### Module Benefits
- **Pre-tested Code**: Battle-tested by the community
- **Best Practices**: Follows AWS recommendations
- **Customizable**: Extensive variable options
- **Documentation**: Comprehensive usage examples

## Project Structure and Repository

### Repository Information
- **GitHub**: `github.com/hkhcoder/vprofile-project`
- **Branch**: `terraform-eks`
- **Clone Command**: 
```bash
git clone -b terraform-eks https://github.com/hkhcoder/vprofile-project.git
```

### File Structure
```
terraform-eks/
├── terraform.tf       # Provider and backend configuration
├── variables.tf       # Variable definitions
├── main.tf           # Main infrastructure code
└── outputs.tf        # Output definitions
```

## Configuration Files Breakdown

### 1. terraform.tf - Providers and Backend

```hcl
terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 5.0"
    }
    random = {
      source  = "hashicorp/random"
      version = "~> 3.1"
    }
    tls = {
      source  = "hashicorp/tls"
      version = "~> 4.0"
    }
    cloudinit = {
      source  = "hashicorp/cloudinit"
      version = "~> 2.2"
    }
    kubernetes = {
      source  = "hashicorp/kubernetes"
      version = "~> 2.16"
    }
  }
  
  backend "s3" {
    bucket = "your-terraform-state-bucket"
    key    = "eks/terraform.tfstate"
    region = "us-east-1"
  }
}
```

### 2. variables.tf - Variable Definitions

```hcl
variable "region" {
  description = "AWS region for the EKS cluster"
  type        = string
  default     = "us-east-1"
}

variable "cluster_name" {
  description = "Name of the EKS cluster"
  type        = string
  default     = "vprof-eks"
}
```

### 3. main.tf - Infrastructure Code

#### Provider Configuration
```hcl
provider "aws" {
  region = var.region
}

provider "kubernetes" {
  host                   = module.eks.cluster_endpoint
  cluster_ca_certificate = base64decode(module.eks.cluster_certificate_authority_data)
  
  exec {
    api_version = "client.authentication.k8s.io/v1beta1"
    command     = "aws"
    args        = ["eks", "get-token", "--cluster-name", module.eks.cluster_name]
  }
}
```

#### VPC Module Configuration
```hcl
data "aws_availability_zones" "available" {
  filter {
    name   = "opt-in-status"
    values = ["opt-in-not-required"]
  }
}

module "vpc" {
  source = "terraform-aws-modules/vpc/aws"
  
  name = "${var.cluster_name}-vpc"
  cidr = "10.0.0.0/16"
  
  azs             = slice(data.aws_availability_zones.available.names, 0, 3)
  private_subnets = ["10.0.1.0/24", "10.0.2.0/24", "10.0.3.0/24"]
  public_subnets  = ["10.0.4.0/24", "10.0.5.0/24", "10.0.6.0/24"]
  
  enable_nat_gateway   = true
  single_nat_gateway   = true
  enable_dns_hostnames = true
  enable_dns_support   = true
  
  # EKS requires specific tags on public subnets
  public_subnet_tags = {
    "kubernetes.io/role/elb" = 1
  }
  
  private_subnet_tags = {
    "kubernetes.io/role/internal-elb" = 1
  }
}
```

#### EKS Module Configuration
```hcl
module "eks" {
  source = "terraform-aws-modules/eks/aws"
  
  cluster_name    = var.cluster_name
  cluster_version = "1.27"
  
  vpc_id                         = module.vpc.vpc_id
  subnet_ids                     = module.vpc.private_subnets
  cluster_endpoint_public_access = true
  
  # Managed Node Groups
  eks_managed_node_groups = {
    blue = {
      min_size     = 1
      max_size     = 3
      desired_size = 2
      
      instance_types = ["t3.small"]
      capacity_type  = "ON_DEMAND"
    }
    
    green = {
      min_size     = 1
      max_size     = 2
      desired_size = 1
      
      instance_types = ["t3.small"]
      capacity_type  = "ON_DEMAND"
    }
  }
}
```

## Prerequisites and Setup

### 1. Install Required Tools

#### Windows (using Chocolatey)
```bash
# Install Chocolatey first, then:
choco install terraform
choco install awscli
choco install kubernetes-cli
```

#### macOS (using Homebrew)
```bash
brew install terraform
brew install awscli
brew install kubernetes-cli
```

#### Linux (Ubuntu/Debian)
```bash
# Terraform
wget -O- https://apt.releases.hashicorp.com/gpg | sudo gpg --dearmor -o /usr/share/keyrings/hashicorp-archive-keyring.gpg
echo "deb [signed-by=/usr/share/keyrings/hashicorp-archive-keyring.gpg] https://apt.releases.hashicorp.com $(lsb_release -cs) main" | sudo tee /etc/apt/sources.list.d/hashicorp.list
sudo apt update && sudo apt install terraform

# AWS CLI
curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip"
unzip awscliv2.zip
sudo ./aws/install

# kubectl
curl -LO "https://dl.k8s.io/release/$(curl -L -s https://dl.k8s.io/release/stable.txt)/bin/linux/amd64/kubectl"
sudo install -o root -g root -m 0755 kubectl /usr/local/bin/kubectl
```

### 2. AWS CLI Configuration

#### Create IAM User
1. Go to AWS Console → IAM → Users
2. Create new user with programmatic access
3. Attach `AdministratorAccess` policy
4. Save Access Key ID and Secret Access Key

#### Configure AWS CLI
```bash
aws configure
# AWS Access Key ID: YOUR_ACCESS_KEY
# AWS Secret Access Key: YOUR_SECRET_KEY
# Default region name: us-east-1
# Default output format: json
```

#### Verify Configuration
```bash
aws sts get-caller-identity
```

### 3. S3 Backend Setup

#### Create S3 Bucket for Terraform State
```bash
aws s3 mb s3://your-terraform-state-bucket-unique-name
```

#### Update terraform.tf with your bucket name
```hcl
backend "s3" {
  bucket = "your-terraform-state-bucket-unique-name"
  key    = "eks/terraform.tfstate"
  region = "us-east-1"
}
```

## Deployment Steps

### Step 1: Initialize Terraform
```bash
cd terraform-eks-project
terraform init
```

Expected output:
```
Initializing modules...
Downloading terraform-aws-modules/vpc/aws...
Downloading terraform-aws-modules/eks/aws...

Initializing the backend...
Successfully configured the backend "s3"!

Terraform has been successfully initialized!
```

### Step 2: Plan the Deployment
```bash
terraform plan
```

This will show you all the resources that will be created (approximately 53 resources).

### Step 3: Apply the Configuration
```bash
terraform apply
```

Type `yes` when prompted. The deployment will take 10-15 minutes.

### Step 4: Verify Deployment

#### Check AWS Console
1. **EKS Console**: Verify cluster creation
2. **EC2 Console**: Check worker nodes
3. **VPC Console**: Verify VPC and subnets

#### Generate kubeconfig
```bash
aws eks update-kubeconfig --name vprof-eks --region us-east-1
```

#### Test kubectl access
```bash
kubectl get nodes
kubectl get pods --all-namespaces
```

Expected output:
```
NAME                                       STATUS   ROLES    AGE   VERSION
ip-10-0-1-xxx.us-east-1.compute.internal   Ready    <none>   5m    v1.27.x
ip-10-0-2-xxx.us-east-1.compute.internal   Ready    <none>   5m    v1.27.x
ip-10-0-3-xxx.us-east-1.compute.internal   Ready    <none>   5m    v1.27.x
```

## Managing the EKS Cluster

### Scaling Node Groups

#### Update main.tf
```hcl
eks_managed_node_groups = {
  blue = {
    min_size     = 2
    max_size     = 5
    desired_size = 4  # Increased from 2
    
    instance_types = ["t3.medium"]  # Changed instance type
  }
}
```

#### Apply changes
```bash
terraform plan
terraform apply
```

### Adding New Node Groups
```hcl
eks_managed_node_groups = {
  # Existing node groups...
  
  spot_nodes = {
    min_size     = 0
    max_size     = 5
    desired_size = 2
    
    instance_types = ["t3.medium", "t3.large"]
    capacity_type  = "SPOT"
  }
}
```

## Troubleshooting Common Issues

### Issue 1: Terraform Version Conflicts
**Error**: Provider version requirements not met

**Solution**:
```bash
# Uninstall current Terraform
choco uninstall terraform  # Windows
brew uninstall terraform   # macOS

# Install latest version
choco install terraform
brew install terraform

# Reinitialize
terraform init -upgrade
```

### Issue 2: AWS Authentication Errors
**Error**: `unable to load aws credentials`

**Solutions**:
```bash
# Check AWS configuration
aws configure list

# Test AWS access
aws sts get-caller-identity

# Reconfigure if needed
aws configure
```

### Issue 3: kubectl Connection Issues
**Error**: `unable to connect to server`

**Solution**:
```bash
# Update kubeconfig
aws eks update-kubeconfig --name your-cluster-name --region your-region

# Verify kubeconfig
cat ~/.kube/config

# Test connection
kubectl cluster-info
```

### Issue 4: Node Groups Not Ready
**Error**: Nodes stuck in `NotReady` state

**Check**:
```bash
# Describe nodes for more information
kubectl describe nodes

# Check system pods
kubectl get pods -n kube-system

# Check EKS cluster status in AWS Console
```

## Cost Management

### Understanding EKS Costs

| Component | Cost (Approximate) |
|-----------|-------------------|
| EKS Control Plane | $0.10/hour (~$73/month) |
| t3.small worker nodes | $0.0208/hour per node |
| NAT Gateway | $0.045/hour (~$32/month) |
| EBS volumes | $0.10/GB/month |

### Cost Optimization Tips

1. **Use Spot Instances**: Up to 90% savings on worker nodes
2. **Right-size instances**: Start small and scale as needed
3. **Single NAT Gateway**: Use one NAT gateway instead of multiple
4. **Delete unused resources**: Regularly clean up test clusters

## Cleanup and Resource Destruction

### Immediate Cleanup (Recommended)
```bash
terraform destroy
```

Type `yes` when prompted. This process takes 5-10 minutes.

### Verify Cleanup
Check AWS Console to ensure all resources are deleted:
- EKS cluster
- EC2 instances (worker nodes)
- VPC and associated resources
- Load balancers (if any were created)

### Manual Cleanup (if needed)
If terraform destroy fails:
```bash
# Delete any remaining resources manually in AWS Console
# Then retry terraform destroy
terraform destroy -auto-approve
```

## Advanced Configuration

### Custom VPC CIDR
```hcl
module "vpc" {
  source = "terraform-aws-modules/vpc/aws"
  
  cidr = "172.16.0.0/16"  # Custom CIDR
  
  private_subnets = ["172.16.1.0/24", "172.16.2.0/24", "172.16.3.0/24"]
  public_subnets  = ["172.16.4.0/24", "172.16.5.0/24", "172.16.6.0/24"]
}
```

### Different Instance Types
```hcl
eks_managed_node_groups = {
  general = {
    instance_types = ["t3.medium", "t3.large"]
  }
  
  compute_optimized = {
    instance_types = ["c5.large", "c5.xlarge"]
  }
  
  memory_optimized = {
    instance_types = ["r5.large", "r5.xlarge"]
  }
}
```

### Enable Private Cluster
```hcl
module "eks" {
  # ... other configuration
  
  cluster_endpoint_private_access = true
  cluster_endpoint_public_access  = false
  
  cluster_endpoint_public_access_cidrs = ["10.0.0.0/16"]  # Restrict access
}
```

## Outputs and References

### Useful Outputs
```hcl
# outputs.tf
output "cluster_endpoint" {
  description = "Endpoint for EKS control plane"
  value       = module.eks.cluster_endpoint
}

output "cluster_name" {
  description = "Kubernetes Cluster Name"
  value       = module.eks.cluster_name
}

output "vpc_id" {
  description = "ID of the VPC"
  value       = module.vpc.vpc_id
}

output "private_subnets" {
  description = "List of IDs of private subnets"
  value       = module.vpc.private_subnets
}
```

## Next Steps and Best Practices

### Production Readiness Checklist
- [ ] Enable cluster logging
- [ ] Configure RBAC (Role-Based Access Control)
- [ ] Set up monitoring (CloudWatch, Prometheus)
- [ ] Implement security policies
- [ ] Configure backup strategies
- [ ] Set up CI/CD pipelines
- [ ] Enable cluster autoscaling

### Learning Resources
1. **AWS EKS Documentation**: Deep dive into EKS features
2. **Terraform AWS Provider Docs**: Advanced configuration options
3. **Kubernetes Official Docs**: Core Kubernetes concepts
4. **AWS Well-Architected Framework**: Best practices for AWS

### Interview Preparation Topics
- EKS vs self-managed Kubernetes
- Node group types and scaling strategies
- VPC and networking requirements for EKS
- IAM roles and permissions for EKS
- Cost optimization strategies
- Disaster recovery and backup procedures

## Key Takeaways

- **EKS Simplifies Kubernetes**: Managed control plane reduces operational overhead
- **Terraform Modules**: Leverage community modules for rapid deployment
- **Cost Awareness**: EKS is expensive; clean up resources promptly
- **Proper Setup**: Correct AWS CLI and Terraform configuration is crucial
- **Modular Architecture**: VPC and EKS modules provide flexibility and best practices
- **Production Considerations**: Additional setup required for production workloads

## Commands Reference

| Operation | Command |
|-----------|---------|
| Initialize Terraform | `terraform init` |
| Plan deployment | `terraform plan` |
| Apply configuration | `terraform apply` |
| Destroy resources | `terraform destroy` |
| Update kubeconfig | `aws eks update-kubeconfig --name <cluster> --region <region>` |
| Check nodes | `kubectl get nodes` |
| Check AWS identity | `aws sts get-caller-identity` |
| View kubeconfig | `cat ~/.kube/config` |

Remember to always destroy your test clusters to avoid unnecessary AWS charges!