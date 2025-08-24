# Website Deployment in a VPC with Bastion Host and Load Balancer

## Overview

This guide walks through setting up a website in a private subnet within a VPC, accessible through a load balancer in the public subnet. The architecture includes a bastion host for secure SSH access to the private instance.

## Architecture Components

- **VPC**: Named `vprofile VPC`
- **Bastion Host**: For secure SSH access to private instances
- **Private Instance**: Hosts the website in a private subnet
- **Application Load Balancer**: Routes traffic from internet to private instance
- **Security Groups**: Control traffic flow between components

## Prerequisites

- AWS Account with appropriate permissions
- Working bastion host in public subnet
- VPC with public and private subnets configured
- NAT Gateway for private subnet internet access

## Step 1: Create SSH Key Pair for Private Instance

1. Navigate to **EC2 Console** → **Key Pairs**
2. Create a new key pair named `web-key` (or your preferred name)
3. Download the `.pem` file to your local machine

## Step 2: Copy SSH Key to Bastion Host

Transfer the private key to the bastion host using SCP:

```bash
scp -i <path_to_bastion_key> <path_to_web_key.pem> ubuntu@<bastion_host_public_IP>:/home/ubuntu
```

Verify the key is copied by SSH into bastion host and running:

```bash
ls -la ~/web-key.pem
```

## Step 3: Launch Private Instance

### Instance Configuration
- **Name**: `web01-priv`
- **AMI**: Amazon Linux 2 (or preferred OS)
- **Instance Type**: t2.micro
- **Key Pair**: `web-key`
- **Network**: `vprofile VPC`
- **Subnet**: Private subnet (1 or 2)
- **Auto-assign Public IP**: Disabled

### Security Group Configuration
Create security group `web01-sg` with the following inbound rules:

| Type | Protocol | Port | Source |
|------|----------|------|--------|
| SSH | TCP | 22 | Bastion Host Security Group |
| HTTP | TCP | 80 | Load Balancer Security Group (create later) |

## Step 4: SSH Access to Private Instance

1. **SSH into bastion host first**:
   ```bash
   ssh -i <bastion_key> ubuntu@<bastion_public_IP>
   ```

2. **Set proper permissions on web key**:
   ```bash
   chmod 400 web-key.pem
   ```

3. **SSH into private instance**:
   ```bash
   ssh -i web-key.pem ec2-user@<private_IP_of_instance>
   ```

## Step 5: Website Setup on Private Instance

### Install Required Packages

```bash
sudo yum install httpd wget unzip -y
```

### Download Website Template

1. Visit [Tooplate.com](https://www.tooplate.com) or another template site
2. Copy the download URL of your chosen template
3. Download the template:
   ```bash
   wget <template_download_URL>
   ```

### Deploy Website

1. **Unzip the template**:
   ```bash
   unzip <template_file.zip>
   ```

2. **Copy files to web directory**:
   ```bash
   sudo cp -r <unzipped_folder>/* /var/www/html/
   ```

3. **Start and enable Apache**:
   ```bash
   sudo systemctl start httpd
   sudo systemctl enable httpd
   ```

## Step 6: Create Load Balancer Components

### Create Target Group

1. Navigate to **EC2 Console** → **Target Groups**
2. Create target group with these settings:
   - **Name**: `web-tg`
   - **Target Type**: Instances
   - **Protocol**: HTTP
   - **Port**: 80
   - **VPC**: `vprofile VPC`
3. **Register targets**: Add the `web01-priv` instance

### Create Load Balancer Security Group

Create security group `web-elb-sg` in `vprofile VPC`:

| Type | Protocol | Port | Source |
|------|----------|------|--------|
| HTTP | TCP | 80 | 0.0.0.0/0 (IPv4) |
| HTTP | TCP | 80 | ::/0 (IPv6) |

### Create Application Load Balancer

1. Navigate to **EC2 Console** → **Load Balancers**
2. Create Application Load Balancer with:
   - **Name**: Choose appropriate name
   - **Scheme**: Internet-facing
   - **VPC**: `vprofile VPC`
   - **Subnets**: Select both public subnets
   - **Security Groups**: `web-elb-sg`
   - **Listeners**: Port 80 → `web-tg` target group

## Step 7: Update Security Groups

### Update Private Instance Security Group

Modify `web01-sg` to allow HTTP traffic from load balancer:

| Type | Protocol | Port | Source |
|------|----------|------|--------|
| SSH | TCP | 22 | Bastion Host Security Group |
| HTTP | TCP | 80 | `web-elb-sg` Security Group |

## Step 8: Verify and Access Website

### Health Check Verification

1. Wait for load balancer to become **Active**
2. Check target group health - instance should show as **Healthy**
3. If unhealthy, verify security group rules allow port 80 from load balancer

### Access Website

1. Copy the **DNS name** of the load balancer from AWS Console
2. Open the DNS name in a web browser
3. Your website should be accessible from the internet

## Architecture Benefits

- **Security**: Website instance has no public IP and is isolated in private subnet
- **Scalability**: Load balancer can distribute traffic to multiple instances
- **High Availability**: Load balancer spans multiple availability zones
- **Controlled Access**: Bastion host provides secure administrative access

## Troubleshooting Tips

- **Instance showing unhealthy**: Check security group rules for port 80
- **Cannot SSH to private instance**: Verify bastion host connectivity and key permissions
- **Website not loading**: Ensure Apache is running and load balancer is in public subnets
- **Permission denied errors**: Check SSH key file permissions (should be 400)

## Security Best Practices

- Keep private keys secure and use appropriate file permissions
- Regularly update security group rules to follow principle of least privilege
- Monitor access logs and enable CloudTrail for audit purposes
- Consider using AWS Systems Manager Session Manager for bastion-less access

## Conclusion

This architecture provides a secure, scalable way to host websites in AWS while maintaining security through network isolation and controlled access patterns. The load balancer enables high availability and the bastion host ensures secure administrative access to private resources.