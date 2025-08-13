# Complete Terraform Learning Guide

## Table of Contents
1. [What is Terraform?](#what-is-terraform)
2. [Installation](#installation)
3. [Basic Concepts](#basic-concepts)
4. [Configuration Syntax](#configuration-syntax)
5. [Core Commands](#core-commands)
6. [Providers](#providers)
7. [Resources](#resources)
8. [Variables](#variables)
9. [Outputs](#outputs)
10. [Data Sources](#data-sources)
11. [State Management](#state-management)
12. [Modules](#modules)
13. [Functions](#functions)
14. [Provisioners](#provisioners)
15. [Best Practices](#best-practices)
16. [Hands-on Examples](#hands-on-examples)
17. [Advanced Topics](#advanced-topics)
18. [Troubleshooting](#troubleshooting)

## What is Terraform?

Terraform is an open-source Infrastructure as Code (IaC) tool developed by HashiCorp. It allows you to define and provision infrastructure using a declarative configuration language called HashiCorp Configuration Language (HCL).

### Key Features:
- **Infrastructure as Code**: Define infrastructure in code files
- **Execution Plans**: Preview changes before applying them
- **Resource Graph**: Builds dependency graphs and parallelizes creation/modification
- **Change Automation**: Complex changesets can be applied with minimal human interaction
- **Multi-Cloud**: Works with AWS, Azure, GCP, and 100+ other providers

## Installation

### Using Package Managers

**macOS (Homebrew):**
```bash
brew install terraform
```

**Windows (Chocolatey):**
```bash
choco install terraform
```

**Ubuntu/Debian:**
```bash
wget -O- https://apt.releases.hashicorp.com/gpg | sudo gpg --dearmor -o /usr/share/keyrings/hashicorp-archive-keyring.gpg
echo "deb [signed-by=/usr/share/keyrings/hashicorp-archive-keyring.gpg] https://apt.releases.hashicorp.com $(lsb_release -cs) main" | sudo tee /etc/apt/sources.list.d/hashicorp.list
sudo apt update && sudo apt install terraform
```

### Manual Installation
1. Download from [terraform.io](https://www.terraform.io/downloads)
2. Unzip and add to PATH
3. Verify installation: `terraform version`

## Basic Concepts

### Infrastructure as Code (IaC)
- Define infrastructure using configuration files
- Version control your infrastructure
- Reproducible and consistent deployments

### Declarative vs Imperative
- **Declarative**: Describe the desired end state
- **Imperative**: Describe the steps to reach the end state
- Terraform uses declarative approach

### Terraform Workflow
1. **Write**: Author infrastructure as code
2. **Plan**: Preview changes before applying
3. **Apply**: Provision reproducible infrastructure

## Configuration Syntax

Terraform uses HashiCorp Configuration Language (HCL), which is designed to be human-readable and machine-friendly.

### Basic Syntax
```hcl
# This is a comment

# Block syntax
resource "resource_type" "resource_name" {
  argument1 = "value1"
  argument2 = "value2"
  
  # Nested block
  nested_block {
    nested_argument = "nested_value"
  }
}
```

### Data Types
```hcl
# String
variable "example_string" {
  type    = string
  default = "hello world"
}

# Number
variable "example_number" {
  type    = number
  default = 42
}

# Boolean
variable "example_bool" {
  type    = bool
  default = true
}

# List
variable "example_list" {
  type    = list(string)
  default = ["item1", "item2", "item3"]
}

# Map
variable "example_map" {
  type = map(string)
  default = {
    key1 = "value1"
    key2 = "value2"
  }
}

# Object
variable "example_object" {
  type = object({
    name = string
    age  = number
  })
  default = {
    name = "John"
    age  = 30
  }
}
```

## Core Commands

### Essential Commands
```bash
# Initialize a Terraform working directory
terraform init

# Create an execution plan
terraform plan

# Apply the changes required to reach the desired state
terraform apply

# Destroy the Terraform-managed infrastructure
terraform destroy

# Show current state
terraform show

# List resources in state
terraform state list

# Validate configuration
terraform validate

# Format configuration files
terraform fmt

# Show output values
terraform output
```

### Advanced Commands
```bash
# Import existing infrastructure
terraform import aws_instance.example i-1234567890abcdef0

# Refresh state
terraform refresh

# Force unlock state
terraform force-unlock LOCK_ID

# Generate graph
terraform graph | dot -Tpng > graph.png

# Show workspace
terraform workspace list
terraform workspace new production
terraform workspace select production
```

## Providers

Providers are plugins that interact with APIs of cloud providers, SaaS providers, and other services.

### Provider Configuration
```hcl
# Configure the AWS Provider
provider "aws" {
  region = "us-west-2"
}

# Configure Azure Provider
provider "azurerm" {
  features {}
}

# Configure Google Cloud Provider
provider "google" {
  project = "my-project-id"
  region  = "us-central1"
}
```

### Provider Versions
```hcl
terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 5.0"
    }
  }
  
  required_version = ">= 1.0"
}
```

## Resources

Resources are the most important element in Terraform. Each resource describes one or more infrastructure objects.

### Basic Resource Syntax
```hcl
resource "resource_type" "resource_name" {
  argument1 = "value1"
  argument2 = "value2"
}
```

### AWS Examples
```hcl
# EC2 Instance
resource "aws_instance" "web" {
  ami           = "ami-0c02fb55956c7d316"
  instance_type = "t3.micro"
  
  tags = {
    Name = "HelloWorld"
  }
}

# S3 Bucket
resource "aws_s3_bucket" "example" {
  bucket = "my-unique-bucket-name"
}

# VPC
resource "aws_vpc" "main" {
  cidr_block           = "10.0.0.0/16"
  enable_dns_hostnames = true
  enable_dns_support   = true
  
  tags = {
    Name = "main-vpc"
  }
}

# Security Group
resource "aws_security_group" "web" {
  name_prefix = "web-"
  vpc_id      = aws_vpc.main.id
  
  ingress {
    from_port   = 80
    to_port     = 80
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }
  
  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }
}
```

### Resource Dependencies
```hcl
# Implicit dependency (reference)
resource "aws_instance" "web" {
  ami           = "ami-0c02fb55956c7d316"
  instance_type = "t3.micro"
  subnet_id     = aws_subnet.main.id  # Implicit dependency
}

# Explicit dependency
resource "aws_instance" "web" {
  ami           = "ami-0c02fb55956c7d316"
  instance_type = "t3.micro"
  
  depends_on = [aws_security_group.web]  # Explicit dependency
}
```

## Variables

Variables make your Terraform configuration flexible and reusable.

### Variable Declaration
```hcl
# variables.tf
variable "instance_type" {
  description = "Type of EC2 instance"
  type        = string
  default     = "t3.micro"
}

variable "availability_zones" {
  description = "List of availability zones"
  type        = list(string)
  default     = ["us-west-2a", "us-west-2b"]
}

variable "tags" {
  description = "Common tags for resources"
  type        = map(string)
  default = {
    Environment = "development"
    Project     = "learning"
  }
}
```

### Using Variables
```hcl
resource "aws_instance" "web" {
  ami           = "ami-0c02fb55956c7d316"
  instance_type = var.instance_type
  
  tags = var.tags
}
```

### Variable Input Methods

**terraform.tfvars file:**
```hcl
instance_type = "t3.small"
tags = {
  Environment = "production"
  Project     = "web-app"
}
```

**Command line:**
```bash
terraform apply -var="instance_type=t3.small"
```

**Environment variables:**
```bash
export TF_VAR_instance_type=t3.small
terraform apply
```

### Variable Validation
```hcl
variable "instance_type" {
  description = "EC2 instance type"
  type        = string
  
  validation {
    condition = contains([
      "t3.micro", "t3.small", "t3.medium"
    ], var.instance_type)
    error_message = "Instance type must be t3.micro, t3.small, or t3.medium."
  }
}
```

## Outputs

Outputs are used to extract information about your infrastructure.

### Basic Outputs
```hcl
# outputs.tf
output "instance_id" {
  description = "ID of the EC2 instance"
  value       = aws_instance.web.id
}

output "instance_public_ip" {
  description = "Public IP address of the instance"
  value       = aws_instance.web.public_ip
}

output "vpc_id" {
  description = "ID of the VPC"
  value       = aws_vpc.main.id
  sensitive   = true  # Mark as sensitive
}
```

### Using Outputs
```bash
# Show all outputs
terraform output

# Show specific output
terraform output instance_id

# JSON format
terraform output -json
```

## Data Sources

Data sources allow you to fetch information about existing resources.

### Basic Data Sources
```hcl
# Get latest Amazon Linux AMI
data "aws_ami" "amazon_linux" {
  most_recent = true
  owners      = ["amazon"]
  
  filter {
    name   = "name"
    values = ["amzn2-ami-hvm-*-x86_64-gp2"]
  }
}

# Get current AWS region
data "aws_region" "current" {}

# Get availability zones
data "aws_availability_zones" "available" {
  state = "available"
}

# Use data source
resource "aws_instance" "web" {
  ami           = data.aws_ami.amazon_linux.id
  instance_type = "t3.micro"
}
```

## State Management

Terraform state tracks the mapping between your configuration and the real world.

### Local State
By default, state is stored locally in `terraform.tfstate`.

### Remote State
For team collaboration, use remote state backends.

**S3 Backend:**
```hcl
terraform {
  backend "s3" {
    bucket = "my-terraform-state"
    key    = "path/to/my/key"
    region = "us-west-2"
    
    # Optional: DynamoDB for state locking
    dynamodb_table = "terraform-locks"
    encrypt        = true
  }
}
```

### State Commands
```bash
# List resources in state
terraform state list

# Show a resource
terraform state show aws_instance.web

# Move a resource
terraform state mv aws_instance.old aws_instance.new

# Remove from state (doesn't destroy)
terraform state rm aws_instance.web

# Import existing resource
terraform import aws_instance.web i-1234567890abcdef0
```

## Modules

Modules are containers for multiple resources that are used together.

### Module Structure
```
modules/
  vpc/
    main.tf
    variables.tf
    outputs.tf
  ec2/
    main.tf
    variables.tf
    outputs.tf
```

### Creating a Module
```hcl
# modules/vpc/main.tf
resource "aws_vpc" "this" {
  cidr_block           = var.cidr_block
  enable_dns_hostnames = var.enable_dns_hostnames
  enable_dns_support   = var.enable_dns_support
  
  tags = merge(
    var.tags,
    {
      Name = var.name
    }
  )
}

resource "aws_subnet" "public" {
  count = length(var.public_subnets)
  
  vpc_id                  = aws_vpc.this.id
  cidr_block              = var.public_subnets[count.index]
  availability_zone       = var.availability_zones[count.index]
  map_public_ip_on_launch = true
  
  tags = merge(
    var.tags,
    {
      Name = "${var.name}-public-${count.index + 1}"
      Type = "Public"
    }
  )
}
```

```hcl
# modules/vpc/variables.tf
variable "name" {
  description = "Name to be used on all resources"
  type        = string
}

variable "cidr_block" {
  description = "CIDR block for VPC"
  type        = string
  default     = "10.0.0.0/16"
}

variable "public_subnets" {
  description = "List of public subnet CIDR blocks"
  type        = list(string)
  default     = []
}

variable "availability_zones" {
  description = "List of availability zones"
  type        = list(string)
}

variable "enable_dns_hostnames" {
  description = "Enable DNS hostnames"
  type        = bool
  default     = true
}

variable "enable_dns_support" {
  description = "Enable DNS support"
  type        = bool
  default     = true
}

variable "tags" {
  description = "Tags to apply to resources"
  type        = map(string)
  default     = {}
}
```

```hcl
# modules/vpc/outputs.tf
output "vpc_id" {
  description = "ID of the VPC"
  value       = aws_vpc.this.id
}

output "vpc_cidr_block" {
  description = "CIDR block of VPC"
  value       = aws_vpc.this.cidr_block
}

output "public_subnet_ids" {
  description = "IDs of public subnets"
  value       = aws_subnet.public[*].id
}
```

### Using a Module
```hcl
# main.tf
module "vpc" {
  source = "./modules/vpc"
  
  name               = "my-vpc"
  cidr_block         = "10.0.0.0/16"
  availability_zones = ["us-west-2a", "us-west-2b", "us-west-2c"]
  public_subnets     = ["10.0.1.0/24", "10.0.2.0/24", "10.0.3.0/24"]
  
  tags = {
    Environment = "production"
    Project     = "web-app"
  }
}

# Reference module outputs
resource "aws_instance" "web" {
  ami           = data.aws_ami.amazon_linux.id
  instance_type = "t3.micro"
  subnet_id     = module.vpc.public_subnet_ids[0]
}
```

### Module Sources
```hcl
# Local module
module "vpc" {
  source = "./modules/vpc"
}

# Git repository
module "vpc" {
  source = "git::https://github.com/user/terraform-aws-vpc.git"
}

# Terraform Registry
module "vpc" {
  source  = "terraform-aws-modules/vpc/aws"
  version = "3.0.0"
}

# S3 bucket
module "vpc" {
  source = "s3::https://s3-eu-west-1.amazonaws.com/examplecorp-terraform-modules/vpc.zip"
}
```

## Functions

Terraform includes many built-in functions for transforming and combining values.

### String Functions
```hcl
# String manipulation
locals {
  upper_name    = upper("hello world")           # "HELLO WORLD"
  lower_name    = lower("HELLO WORLD")           # "hello world"
  title_name    = title("hello world")           # "Hello World"
  trimmed       = trimspace("  hello world  ")  # "hello world"
  replaced      = replace("hello world", "world", "terraform") # "hello terraform"
  formatted     = format("Hello %s", "World")   # "Hello World"
  joined        = join("-", ["hello", "world"]) # "hello-world"
  split_result  = split("-", "hello-world")     # ["hello", "world"]
}
```

### Numeric Functions
```hcl
locals {
  absolute      = abs(-10)           # 10
  ceiling       = ceil(4.3)          # 5
  floor_value   = floor(4.7)         # 4
  maximum       = max(1, 2, 3)       # 3
  minimum       = min(1, 2, 3)       # 1
  parsed_int    = parseint("42", 10) # 42
}
```

### Collection Functions
```hcl
locals {
  list_length   = length(["a", "b", "c"])                    # 3
  concatenated  = concat(["a", "b"], ["c", "d"])             # ["a", "b", "c", "d"]
  contains_val  = contains(["a", "b", "c"], "b")             # true
  distinct_vals = distinct(["a", "b", "a", "c"])             # ["a", "b", "c"]
  element_val   = element(["a", "b", "c"], 1)                # "b"
  index_val     = index(["a", "b", "c"], "b")                # 1
  keys_result   = keys({a = 1, b = 2})                       # ["a", "b"]
  values_result = values({a = 1, b = 2})                     # [1, 2]
  lookup_val    = lookup({a = 1, b = 2}, "a", 0)             # 1
  merged        = merge({a = 1}, {b = 2})                    # {a = 1, b = 2}
  reversed      = reverse(["a", "b", "c"])                   # ["c", "b", "a"]
  sorted        = sort(["c", "a", "b"])                      # ["a", "b", "c"]
  sliced        = slice(["a", "b", "c", "d"], 1, 3)          # ["b", "c"]
}
```

### Conditional Functions
```hcl
locals {
  # Conditional expression
  instance_type = var.environment == "production" ? "t3.large" : "t3.micro"
  
  # Coalesce (return first non-null value)
  name = coalesce(var.custom_name, var.default_name, "fallback-name")
  
  # Try function (handle errors gracefully)
  parsed_number = try(tonumber(var.maybe_number), 0)
}
```

### Date/Time Functions
```hcl
locals {
  current_timestamp = timestamp()                    # Current time
  formatted_date    = formatdate("YYYY-MM-DD", timestamp())
  time_added        = timeadd(timestamp(), "24h")    # Add 24 hours
}
```

## Provisioners

Provisioners are used to execute scripts or commands on local or remote machines.

### Local Provisioner
```hcl
resource "aws_instance" "web" {
  ami           = data.aws_ami.amazon_linux.id
  instance_type = "t3.micro"
  
  provisioner "local-exec" {
    command = "echo 'Instance ${self.id} created'"
  }
  
  provisioner "local-exec" {
    when    = destroy
    command = "echo 'Instance ${self.id} destroyed'"
  }
}
```

### Remote Provisioner
```hcl
resource "aws_instance" "web" {
  ami           = data.aws_ami.amazon_linux.id
  instance_type = "t3.micro"
  key_name      = aws_key_pair.deployer.key_name
  
  connection {
    type        = "ssh"
    user        = "ec2-user"
    private_key = file("~/.ssh/id_rsa")
    host        = self.public_ip
  }
  
  provisioner "remote-exec" {
    inline = [
      "sudo yum update -y",
      "sudo yum install -y nginx",
      "sudo systemctl start nginx",
      "sudo systemctl enable nginx"
    ]
  }
  
  provisioner "file" {
    source      = "app.conf"
    destination = "/tmp/app.conf"
  }
}
```

## Best Practices

### Project Structure
```
terraform-project/
├── main.tf              # Main configuration
├── variables.tf         # Variable definitions
├── outputs.tf          # Output definitions
├── terraform.tfvars    # Variable values
├── versions.tf         # Provider versions
├── modules/            # Local modules
│   └── vpc/
│       ├── main.tf
│       ├── variables.tf
│       └── outputs.tf
└── environments/       # Environment-specific configs
    ├── dev/
    │   ├── main.tf
    │   └── terraform.tfvars
    └── prod/
        ├── main.tf
        └── terraform.tfvars
```

### Naming Conventions
```hcl
# Use descriptive names
resource "aws_instance" "web_server" {
  # Good: descriptive
}

resource "aws_instance" "i" {
  # Bad: not descriptive
}

# Use consistent naming
variable "vpc_cidr_block" {}
variable "subnet_cidr_blocks" {}
# Good: consistent pattern

variable "vpc_cidr" {}
variable "subnet_cidrs" {}
# Also good: consistent abbreviation
```

### Resource Organization
```hcl
# Group related resources
# networking.tf
resource "aws_vpc" "main" {}
resource "aws_subnet" "public" {}
resource "aws_internet_gateway" "main" {}

# compute.tf
resource "aws_instance" "web" {}
resource "aws_autoscaling_group" "web" {}

# security.tf
resource "aws_security_group" "web" {}
resource "aws_iam_role" "ec2_role" {}
```

### Use Local Values
```hcl
locals {
  common_tags = {
    Environment = var.environment
    Project     = var.project_name
    Owner       = var.owner
    CreatedBy   = "terraform"
  }
  
  name_prefix = "${var.project_name}-${var.environment}"
}

resource "aws_instance" "web" {
  ami           = data.aws_ami.amazon_linux.id
  instance_type = var.instance_type
  
  tags = merge(
    local.common_tags,
    {
      Name = "${local.name_prefix}-web-server"
    }
  )
}
```

### State Management Best Practices
- Always use remote state for team projects
- Enable state locking (DynamoDB for S3 backend)
- Use separate state files for different environments
- Never commit state files to version control
- Regularly backup state files

### Security Best Practices
```hcl
# Don't hardcode secrets
# Bad
resource "aws_db_instance" "bad" {
  password = "hardcoded_password"
}

# Good - use variables
resource "aws_db_instance" "good" {
  password = var.db_password
}

# Mark sensitive outputs
output "database_password" {
  value     = aws_db_instance.main.password
  sensitive = true
}

# Use data sources for secrets
data "aws_ssm_parameter" "db_password" {
  name            = "/myapp/database/password"
  with_decryption = true
}
```

## Hands-on Examples

### Example 1: Simple Web Server on AWS
```hcl
# main.tf
provider "aws" {
  region = var.aws_region
}

data "aws_ami" "amazon_linux" {
  most_recent = true
  owners      = ["amazon"]
  
  filter {
    name   = "name"
    values = ["amzn2-ami-hvm-*-x86_64-gp2"]
  }
}

resource "aws_vpc" "main" {
  cidr_block           = var.vpc_cidr
  enable_dns_hostnames = true
  enable_dns_support   = true
  
  tags = {
    Name = "${var.project_name}-vpc"
  }
}

resource "aws_subnet" "public" {
  vpc_id                  = aws_vpc.main.id
  cidr_block              = var.public_subnet_cidr
  availability_zone       = data.aws_availability_zones.available.names[0]
  map_public_ip_on_launch = true
  
  tags = {
    Name = "${var.project_name}-public-subnet"
  }
}

resource "aws_internet_gateway" "main" {
  vpc_id = aws_vpc.main.id
  
  tags = {
    Name = "${var.project_name}-igw"
  }
}

resource "aws_route_table" "public" {
  vpc_id = aws_vpc.main.id
  
  route {
    cidr_block = "0.0.0.0/0"
    gateway_id = aws_internet_gateway.main.id
  }
  
  tags = {
    Name = "${var.project_name}-public-rt"
  }
}

resource "aws_route_table_association" "public" {
  subnet_id      = aws_subnet.public.id
  route_table_id = aws_route_table.public.id
}

resource "aws_security_group" "web" {
  name_prefix = "${var.project_name}-web-"
  vpc_id      = aws_vpc.main.id
  
  ingress {
    from_port   = 80
    to_port     = 80
    protocol    = "tcp"
    cidr_blocks = ["0.0.0.0/0"]
  }
  
  ingress {
    from_port   = 22
    to_port     = 22
    protocol    = "tcp"
    cidr_blocks = [var.allowed_ssh_cidr]
  }
  
  egress {
    from_port   = 0
    to_port     = 0
    protocol    = "-1"
    cidr_blocks = ["0.0.0.0/0"]
  }
  
  tags = {
    Name = "${var.project_name}-web-sg"
  }
}

resource "aws_instance" "web" {
  ami                    = data.aws_ami.amazon_linux.id
  instance_type          = var.instance_type
  subnet_id              = aws_subnet.public.id
  vpc_security_group_ids = [aws_security_group.web.id]
  
  user_data = <<-EOF
              #!/bin/bash
              yum update -y
              yum install -y nginx
              systemctl start nginx
              systemctl enable nginx
              echo "<h1>Hello from Terraform!</h1>" > /var/www/html/index.html
              EOF
  
  tags = {
    Name = "${var.project_name}-web-server"
  }
}

data "aws_availability_zones" "available" {
  state = "available"
}
```

```hcl
# variables.tf
variable "aws_region" {
  description = "AWS region"
  type        = string
  default     = "us-west-2"
}

variable "project_name" {
  description = "Project name for resource naming"
  type        = string
  default     = "terraform-demo"
}

variable "vpc_cidr" {
  description = "CIDR block for VPC"
  type        = string
  default     = "10.0.0.0/16"
}

variable "public_subnet_cidr" {
  description = "CIDR block for public subnet"
  type        = string
  default     = "10.0.1.0/24"
}

variable "instance_type" {
  description = "EC2 instance type"
  type        = string
  default     = "t3.micro"
}

variable "allowed_ssh_cidr" {
  description = "CIDR block allowed for SSH access"
  type        = string
  default     = "0.0.0.0/0"  # Change this to your IP
}
```

```hcl
# outputs.tf
output "vpc_id" {
  description = "ID of the VPC"
  value       = aws_vpc.main.id
}

output "web_server_ip" {
  description = "Public IP of web server"
  value       = aws_instance.web.public_ip
}

output "web_server_url" {
  description = "URL of web server"
  value       = "http://${aws_instance.web.public_ip}"
}
```

### Example 2: Multi-Environment Setup
```hcl
# environments/dev/main.tf
module "infrastructure" {
  source = "../../modules/web-app"
  
  environment      = "dev"
  instance_type    = "t3.micro"
  min_size         = 1
  max_size         = 2
  desired_capacity = 1
  
  tags = {
    Environment = "development"
    Project     = "web-app"
    Owner       = "dev-team"
  }
}
```

```hcl
# environments/prod/main.tf
module "infrastructure" {
  source = "../../modules/web-app"
  
  environment      = "prod"
  instance_type    = "t3.medium"
  min_size         = 2
  max_size         = 10
  desired_capacity = 3
  
  tags = {
    Environment = "production"
    Project     = "web-app"
    Owner       = "ops-team"
  }
}
```

## Advanced Topics

### Dynamic Blocks
```hcl
resource "aws_security_group" "web" {
  name_prefix = "web-"
  
  dynamic "ingress" {
    for_each = var.ingress_ports
    content {
      from_port   = ingress.value.port
      to_port     = ingress.value.port
      protocol    = ingress.value.protocol
      cidr_blocks = ingress.value.cidr_blocks
    }
  }
}

variable "ingress_ports" {
  default = [
    {
      port        = 80
      protocol    = "tcp"
      cidr_blocks = ["0.0.0.0/0"]
    },
    {
      port        = 443
      protocol    = "tcp"
      cidr_blocks = ["0.0.0.0/0"]
    }
  ]
}
```

### For Expressions
```hcl
locals {
  # Create a map from a list
  instance_tags = {
    for instance in var.instances :
    instance.name => {
      type = instance.type
      zone = instance.zone
    }
  }
  
  # Filter and transform lists
  public_subnets = [
    for subnet in var.subnets :
    subnet.id if subnet.public == true
  ]
  
  # Create upper case list
  upper_names = [
    for name in var.names : upper(name)
  ]
  
  # Create map with index
  indexed_items = {
    for i, item in var.items :
    i => item
  }
}

# Example usage
variable "instances" {
  default = [
    { name = "web-1", type = "t3.micro", zone = "us-west-2a" },
    { name = "web-2", type = "t3.small", zone = "us-west-2b" },
    { name = "db-1", type = "t3.medium", zone = "us-west-2c" }
  ]
}
```

### Conditional Expressions and Logic
```hcl
locals {
  # Basic conditional
  instance_type = var.environment == "production" ? "t3.large" : "t3.micro"
  
  # Multiple conditions
  instance_count = (
    var.environment == "production" ? 3 :
    var.environment == "staging" ? 2 :
    1
  )
  
  # Complex conditions with logical operators
  create_backup = var.environment == "production" && var.backup_enabled
  
  # Null checks
  vpc_id = var.vpc_id != null ? var.vpc_id : aws_vpc.default.id
}
```

### Count and For_Each
```hcl
# Using count
resource "aws_instance" "web" {
  count = var.instance_count
  
  ami           = data.aws_ami.amazon_linux.id
  instance_type = var.instance_type
  
  tags = {
    Name = "web-${count.index + 1}"
  }
}

# Using for_each with set
resource "aws_instance" "web" {
  for_each = toset(var.availability_zones)
  
  ami               = data.aws_ami.amazon_linux.id
  instance_type     = var.instance_type
  availability_zone = each.key
  
  tags = {
    Name = "web-${each.key}"
  }
}

# Using for_each with map
resource "aws_s3_bucket" "buckets" {
  for_each = var.s3_buckets
  
  bucket = each.key
  
  tags = merge(
    var.common_tags,
    each.value,
    {
      Name = each.key
    }
  )
}

variable "s3_buckets" {
  default = {
    "my-app-logs" = {
      Environment = "production"
      Purpose     = "logging"
    }
    "my-app-backups" = {
      Environment = "production"
      Purpose     = "backup"
    }
  }
}
```

### Lifecycle Rules
```hcl
resource "aws_instance" "web" {
  ami           = data.aws_ami.amazon_linux.id
  instance_type = var.instance_type
  
  lifecycle {
    # Prevent accidental destruction
    prevent_destroy = true
    
    # Create before destroying (zero downtime)
    create_before_destroy = true
    
    # Ignore changes to specific attributes
    ignore_changes = [
      ami,
      user_data
    ]
  }
  
  tags = {
    Name = "web-server"
  }
}
```

### Workspace Management
```bash
# List workspaces
terraform workspace list

# Create workspace
terraform workspace new development
terraform workspace new staging
terraform workspace new production

# Switch workspace
terraform workspace select production

# Show current workspace
terraform workspace show

# Delete workspace
terraform workspace delete development
```

```hcl
# Use workspace in configuration
locals {
  workspace_configs = {
    development = {
      instance_type = "t3.micro"
      instance_count = 1
    }
    staging = {
      instance_type = "t3.small"
      instance_count = 2
    }
    production = {
      instance_type = "t3.large"
      instance_count = 3
    }
  }
  
  config = local.workspace_configs[terraform.workspace]
}

resource "aws_instance" "web" {
  count = local.config.instance_count
  
  ami           = data.aws_ami.amazon_linux.id
  instance_type = local.config.instance_type
  
  tags = {
    Name        = "web-${count.index + 1}"
    Environment = terraform.workspace
  }
}
```

### Custom Validation Rules
```hcl
variable "instance_type" {
  type        = string
  description = "EC2 instance type"
  
  validation {
    condition = can(regex("^t[23]\\.", var.instance_type))
    error_message = "Instance type must be from t2 or t3 family."
  }
}

variable "cidr_block" {
  type        = string
  description = "VPC CIDR block"
  
  validation {
    condition = can(cidrhost(var.cidr_block, 0))
    error_message = "Must be a valid IPv4 CIDR block address."
  }
}

variable "environment" {
  type        = string
  description = "Environment name"
  
  validation {
    condition = contains(["dev", "staging", "prod"], var.environment)
    error_message = "Environment must be dev, staging, or prod."
  }
}
```

### Sensitive Variables and Outputs
```hcl
variable "database_password" {
  type        = string
  description = "Database password"
  sensitive   = true
}

resource "aws_db_instance" "main" {
  allocated_storage = 20
  storage_type      = "gp2"
  engine            = "mysql"
  engine_version    = "8.0"
  instance_class    = "db.t3.micro"
  db_name           = "myapp"
  username          = "admin"
  password          = var.database_password
  
  skip_final_snapshot = true
}

output "database_endpoint" {
  value = aws_db_instance.main.endpoint
}

output "database_password" {
  value     = aws_db_instance.main.password
  sensitive = true
}
```

### Remote State Data Source
```hcl
# Reference remote state from another configuration
data "terraform_remote_state" "vpc" {
  backend = "s3"
  
  config = {
    bucket = "my-terraform-state"
    key    = "network/terraform.tfstate"
    region = "us-west-2"
  }
}

# Use outputs from remote state
resource "aws_instance" "web" {
  ami           = data.aws_ami.amazon_linux.id
  instance_type = "t3.micro"
  subnet_id     = data.terraform_remote_state.vpc.outputs.public_subnet_id
  
  vpc_security_group_ids = [
    data.terraform_remote_state.vpc.outputs.web_security_group_id
  ]
}
```

### Moved Blocks (Terraform 1.1+)
```hcl
# Handle resource moves/renames without recreating
moved {
  from = aws_instance.web
  to   = aws_instance.web_server
}

moved {
  from = aws_security_group.web
  to   = module.networking.aws_security_group.web
}
```

## Troubleshooting

### Common Issues and Solutions

#### 1. State Lock Issues
```bash
# Problem: State is locked
Error: Error acquiring the state lock

# Solution: Force unlock (use with caution)
terraform force-unlock <LOCK_ID>

# Better solution: Wait for lock to release or coordinate with team
```

#### 2. Resource Already Exists
```bash
# Problem: Resource already exists in AWS but not in state
Error: resource already exists

# Solution: Import the existing resource
terraform import aws_instance.web i-1234567890abcdef0
```

#### 3. Dependency Issues
```hcl
# Problem: Dependency cycle detected
# Solution: Remove unnecessary dependencies or restructure

# Bad - creates cycle
resource "aws_security_group" "web" {
  vpc_id = aws_vpc.main.id
}

resource "aws_vpc" "main" {
  # Don't reference security group here
  depends_on = [aws_security_group.web]  # This creates a cycle
}

# Good - proper dependency chain
resource "aws_vpc" "main" {
  cidr_block = "10.0.0.0/16"
}

resource "aws_security_group" "web" {
  vpc_id = aws_vpc.main.id
}
```

#### 4. Provider Configuration Issues
```hcl
# Problem: Provider not configured
# Solution: Add provider configuration

terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 5.0"
    }
  }
}

provider "aws" {
  region = var.aws_region
}
```

#### 5. Variable Validation Errors
```bash
# Problem: Variable validation failed
# Solution: Check variable values and validation rules

# Check current variable values
terraform plan -var-file="terraform.tfvars"

# Validate configuration
terraform validate
```

### Debugging Techniques

#### Enable Debug Logging
```bash
# Set log level
export TF_LOG=DEBUG
export TF_LOG_PATH=./terraform.log

# Run terraform command
terraform plan

# Different log levels: TRACE, DEBUG, INFO, WARN, ERROR
export TF_LOG=TRACE
```

#### Inspect State
```bash
# Show current state
terraform show

# List resources in state
terraform state list

# Show specific resource
terraform state show aws_instance.web

# Show state in JSON format
terraform show -json | jq '.'
```

#### Graph Visualization
```bash
# Generate dependency graph
terraform graph | dot -Tpng > graph.png

# For planning phase
terraform graph -type=plan | dot -Tpng > plan-graph.png
```

#### Console for Testing
```bash
# Start interactive console
terraform console

# Test expressions
> var.instance_type
> local.common_tags
> aws_instance.web.public_ip
```

### Performance Optimization

#### Parallel Execution
```bash
# Increase parallelism (default is 10)
terraform apply -parallelism=20

# Reduce for resource-constrained environments
terraform apply -parallelism=1
```

#### State Optimization
```bash
# Refresh state manually
terraform refresh

# Selective planning
terraform plan -target=aws_instance.web

# Selective apply
terraform apply -target=module.database
```

#### Provider Optimization
```hcl
provider "aws" {
  region = "us-west-2"
  
  # Skip some API calls for faster execution
  skip_credentials_validation = true
  skip_metadata_api_check     = true
  skip_region_validation      = true
}
```

## Additional Resources and Next Steps

### Official Documentation
- [Terraform Documentation](https://developer.hashicorp.com/terraform/docs)
- [Terraform Registry](https://registry.terraform.io/)
- [Terraform AWS Provider](https://registry.terraform.io/providers/hashicorp/aws/latest/docs)

### Learning Path
1. **Beginner**: Start with basic resources, understand state management
2. **Intermediate**: Learn modules, workspaces, and advanced functions
3. **Advanced**: Master complex expressions, custom providers, and CI/CD integration

### Recommended Practices for Teams
1. **Version Control**: Store all Terraform code in Git
2. **Code Review**: Require reviews for all infrastructure changes
3. **CI/CD Integration**: Automate terraform plan/apply in pipelines
4. **Documentation**: Document modules and maintain README files
5. **Testing**: Use tools like Terratest for infrastructure testing

### Tools and Extensions
- **IDE Extensions**: Terraform plugins for VS Code, IntelliJ
- **Linting**: TFLint for Terraform code analysis
- **Security Scanning**: Checkov, tfsec for security best practices
- **Cost Estimation**: Infracost for cost analysis
- **Testing**: Terratest, Terragrunt for testing and orchestration

### Example CI/CD Pipeline (GitHub Actions)
```yaml
name: Terraform

on:
  push:
    branches: [ main ]
  pull_request:
    branches: [ main ]

jobs:
  terraform:
    runs-on: ubuntu-latest
    
    steps:
    - uses: actions/checkout@v3
    
    - name: Setup Terraform
      uses: hashicorp/setup-terraform@v2
      with:
        terraform_version: 1.5.0
    
    - name: Terraform Init
      run: terraform init
    
    - name: Terraform Validate
      run: terraform validate
    
    - name: Terraform Plan
      run: terraform plan
      env:
        AWS_ACCESS_KEY_ID: ${{ secrets.AWS_ACCESS_KEY_ID }}
        AWS_SECRET_ACCESS_KEY: ${{ secrets.AWS_SECRET_ACCESS_KEY }}
    
    - name: Terraform Apply
      if: github.ref == 'refs/heads/main'
      run: terraform apply -auto-approve
      env:
        AWS_ACCESS_KEY_ID: ${{ secrets.AWS_ACCESS_KEY_ID }}
        AWS_SECRET_ACCESS_KEY: ${{ secrets.AWS_SECRET_ACCESS_KEY }}
```

This comprehensive guide covers the essential concepts and practical aspects of Terraform. Start with the basics, practice with the examples, and gradually move to more advanced topics as you become comfortable with the fundamentals. Remember to always test in a safe environment before applying changes to production infrastructure!