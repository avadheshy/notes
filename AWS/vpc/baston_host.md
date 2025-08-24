# AWS Bastion Host Setup Guide

## Introduction

This guide demonstrates how to create and configure a Bastion Host (Jump Server) in AWS VPC. A Bastion Host provides secure access to resources in private subnets, serving as the single, controlled entry point for administrative access to your private infrastructure.

## Understanding Bastion Host

### What is a Bastion Host?
A **Bastion Host** (also called **Jump Server**) is a secure network host that acts as an entry point to access resources in private subnets. It's not a VPC-specific term but a general networking security concept.

### Purpose and Function
- **Secure Access Point**: Single controlled entry to private subnet resources
- **SSH Gateway**: Enables SSH access to private instances
- **Security Chokepoint**: Centralizes and controls access to sensitive resources
- **Audit Trail**: Provides single point for logging and monitoring access

### Fort Analogy
> Think of a Bastion Host as the **heavily guarded entrance to a fort**:
> - Everything valuable is safely inside the fort (private subnet)
> - Multiple resources exist inside, but access requires passing through the gate
> - If the gate is weak or poorly guarded, the entire fort is compromised
> - The stronger the gate, the more secure everything inside remains

## Network Access Flow

### Direct Access (Not Possible)
```
❌ Internet → Private Instance (No Public IP, Cannot Access)
```

### Bastion Host Access (Secure Method)
```
✅ Internet → Bastion Host (Public Subnet) → Private Instance (Private Subnet)
```

### Access Limitations for Private Instances
- **No Public IP**: Private instances never receive public IP addresses
- **No Direct Internet Access**: Cannot be reached directly from internet
- **Route Table Restrictions**: Even with public IP, private subnet routing prevents direct access
- **Administrative Access**: SSH/RDP must go through Bastion Host

## Prerequisites

Before creating a Bastion Host:
- VPC with public and private subnets configured
- Internet Gateway attached and routing configured
- Understanding of security group concepts
- SSH key pair management knowledge

## Step 1: Create Security Group for Bastion Host

### Security Group Requirements
The Bastion Host security group should be **highly restrictive** since it's the gateway to your private infrastructure.

### Create Bastion Security Group
1. Navigate to **EC2 Dashboard** → **Security Groups**
2. Click **"Create Security Group"**
3. **Configuration**:
   - **Name**: `vpro-bastion-sg`
   - **Description**: `Security group for bastion host - SSH access only`
   - **VPC**: Select `vprofile-VPC` ⚠️ **Critical**: Must match target VPC

### Security Group Rules

#### Inbound Rules (Restrictive)
| Type | Protocol | Port Range | Source | Description |
|------|----------|------------|--------|-------------|
| SSH | TCP | 22 | My IP | SSH access from your IP only |

#### Outbound Rules (Default)
- **All Traffic**: Allowed (for system updates and accessing private instances)

### Security Best Practices

#### Production Environment
- **Source IP**: Corporate/Office network IP range only
- **Time-based Access**: Consider time restrictions if supported
- **Multi-factor Authentication**: Implement where possible
- **Regular Review**: Audit and update IP restrictions regularly

#### Development/Learning Environment
- **Temporary Flexibility**: If "My IP" causes issues, temporarily use `0.0.0.0/0`
- **Quick Rollback**: Change back to specific IP once connectivity is confirmed
- **⚠️ Never use `0.0.0.0/0` in production**

## Step 2: Create SSH Key Pair

### Key Pair Security Importance
> The private key is **the key to your fort's gate** - treat it with extreme care.

### Create Key Pair
1. Navigate to **EC2** → **Key Pairs**
2. Click **"Create Key Pair"**
3. **Configuration**:
   - **Name**: `vpro-bastion-key`
   - **Key Pair Type**: RSA (default)
   - **Private Key File Format**: `.pem`
4. Click **"Create Key Pair"**

### Key Management Best Practices
- **Secure Storage**: Store private key in secure, encrypted location
- **Access Control**: Limit who can access the private key
- **Backup Strategy**: Secure backup of private key
- **Regular Rotation**: Plan for periodic key rotation
- **Never Share**: Private key should never be shared or transmitted insecurely

### File Permissions (Linux/macOS)
```bash
chmod 400 vpro-bastion-key.pem
```

## Step 3: Choose Secure AMI

### AMI Security Considerations
Standard AWS AMIs are functional but may not be hardened for security-critical roles like Bastion Hosts.

### AMI Options

#### Option 1: Standard AWS AMIs (Learning/Development)
- **Ubuntu Server 22.04 LTS**: Free tier eligible
- **Amazon Linux 2**: AWS optimized
- **Cost**: Free
- **Security**: Basic OS security

#### Option 2: Hardened AMIs (Production Recommended)
**Center for Internet Security (CIS) AMIs:**
- **CIS Amazon Linux 2**: Hardened Amazon Linux
- **CIS Ubuntu**: Security-tested Ubuntu
- **CIS CentOS**: Hardened CentOS
- **Cost**: ~$130/year per instance
- **Security**: Vulnerability tested and hardened

#### Option 3: Third-party Security AMIs
- Multiple providers available in AWS Marketplace
- Pre-configured with security tools
- Regular security updates and patches
- Varying costs and features

### Production vs Learning Trade-off
| Environment | Recommended AMI | Cost | Security Level |
|-------------|----------------|------|----------------|
| **Learning** | Standard Ubuntu/Amazon Linux | Free | Basic |
| **Development** | CIS AMIs or Standard | Low | Medium |
| **Production** | CIS AMIs or Enterprise Security | Medium | High |

## Step 4: Launch Bastion Host Instance

### Instance Configuration
1. Navigate to **EC2** → **Instances** → **"Launch Instance"**
2. **AMI Selection**: Ubuntu Server 22.04 LTS (Free Tier)
3. **Instance Details**:
   - **Name**: `bastion`
   - **Instance Type**: `t2.micro` (free tier eligible)
   - **Key Pair**: Select `vpro-bastion-key`

### Network Configuration (Critical)
1. Click **"Edit"** in Network Settings
2. **VPC**: Select `vprofile-VPC` ⚠️ **Must match security group VPC**
3. **Subnet**: Select public subnet (`vpro-pubsub-1` or `vpro-pubsub-2`)
4. **Auto-assign Public IP**: Enabled (should be automatic)
5. **Security Group**: Select `vpro-bastion-sg`

### VPC-Specific Resource Binding
> ⚠️ **Critical Concept**: Security groups are VPC-specific. You can only attach security groups created in the same VPC as your instance.

### Launch Verification Checklist
- [ ] **VPC**: Correct custom VPC selected
- [ ] **Subnet**: Public subnet selected
- [ ] **Security Group**: Bastion security group from correct VPC
- [ ] **Key Pair**: Bastion-specific key pair selected
- [ ] **Auto-assign Public IP**: Enabled

## Step 5: Test Bastion Host Connectivity

### Wait for Instance Launch
Monitor instance state until:
- **Instance State**: Running
- **Status Check**: 2/2 checks passed
- **Public IP**: Assigned and visible

### SSH Connection Test

#### Connection Details
- **Public IP**: Copy from EC2 instance details
- **Username**: `ubuntu` (for Ubuntu AMI)
- **Private Key**: `vpro-bastion-key.pem`
- **Port**: 22 (default SSH)

#### SSH Command (Linux/macOS)
```bash
ssh -i vpro-bastion-key.pem ubuntu@<BASTION-PUBLIC-IP>
```

#### SSH Command (Windows - Git Bash)
```bash
ssh -i vpro-bastion-key.pem ubuntu@<BASTION-PUBLIC-IP>
```

### Successful Connection Indicators
1. **Connection Established**: No timeout or connection refused errors
2. **Host Verification**: Accept host key fingerprint
3. **Login Prompt**: Ubuntu command prompt appears
4. **System Access**: Can execute basic commands

### Connection Success Validation
```bash
# Check system information
uname -a

# Check network configuration
ip addr show

# Verify internet connectivity
ping -c 3 google.com
```

## Bastion Host Architecture

### Current Network Topology
```
Internet
    │
    └── Internet Gateway
            │
            └── Public Subnet (vpro-pubsub-1)
                    │
                    └── Bastion Host [Public IP + Private IP]
                            │
                            └── (Future) SSH to Private Subnet Instances
```

### Security Boundaries
```
┌─ Public Subnet (DMZ) ──────────────────┐
│  ┌── Bastion Host ──┐                   │
│  │ • Public IP      │                   │
│  │ • SSH Access     │ ←── Internet      │
│  │ • Security Hardened │                │
│  └──────────────────┘                   │
└─────────────────────────────────────────┘
           │ SSH Connection
           ↓
┌─ Private Subnet (Secure Zone) ──────────┐
│  ┌── Application Servers ──┐             │
│  │ • Private IP Only       │             │
│  │ • No Direct Internet    │             │
│  │ • Access via Bastion    │             │
│  └─────────────────────────┘             │
└─────────────────────────────────────────┘
```

## Security Best Practices

### Access Control
- **IP Restrictions**: Limit SSH access to known IP ranges
- **Key Management**: Secure storage and rotation of SSH keys
- **Session Monitoring**: Log and monitor all SSH sessions
- **Time-based Access**: Implement session timeout policies

### System Hardening
- **Regular Updates**: Keep OS and software packages updated
- **Minimal Services**: Run only necessary services
- **Firewall Configuration**: Host-based firewall rules
- **Log Monitoring**: Centralized logging and alerting

### Operational Security
- **Regular Audits**: Periodic security assessments
- **Change Management**: Controlled changes to configuration
- **Backup Strategy**: Secure configuration backups
- **Incident Response**: Plan for security incidents

## Next Steps

### Immediate Next Actions
1. **Launch Private Instance**: Create instance in private subnet
2. **Configure Private Access**: SSH from Bastion to private instance
3. **Set Up Application**: Deploy services in private subnet
4. **Load Balancer Integration**: Configure external access to private services

### Advanced Configurations
1. **Multiple Bastion Hosts**: High availability setup
2. **Session Recording**: Implement session logging
3. **Multi-factor Authentication**: Additional security layers
4. **Automated Hardening**: Configuration management tools

## Troubleshooting

### Common Connection Issues

#### Cannot SSH to Bastion Host
**Symptoms**: Connection timeout or refused
**Possible Causes**:
- Security group not allowing your IP
- Instance not in public subnet
- Public IP not assigned
- Wrong key pair or permissions

**Solutions**:
- Verify security group allows your current IP
- Confirm instance is in public subnet
- Check auto-assign public IP setting
- Verify key pair permissions (chmod 400)

#### Security Group Not Available During Launch
**Symptoms**: Cannot find security group when launching instance
**Cause**: Security group created in different VPC
**Solution**: Recreate security group in correct VPC

#### SSH Key Permission Errors (Linux/macOS)
**Symptoms**: "Bad permissions" error when using SSH key
**Solution**: 
```bash
chmod 400 vpro-bastion-key.pem
```

### Validation Commands

#### Test SSH Connectivity
```bash
# Test connection without logging in
ssh -i vpro-bastion-key.pem -o ConnectTimeout=10 ubuntu@<IP> "echo Connection successful"
```

#### Check Security Groups
```bash
# AWS CLI - Check security group rules
aws ec2 describe-security-groups --group-names vpro-bastion-sg
```

## Cost Considerations

### Bastion Host Costs
- **EC2 Instance**: t2.micro (~$8.50/month if not free tier)
- **Data Transfer**: Minimal for SSH sessions
- **Elastic IP**: Free while attached to running instance
- **Security AMIs**: Additional ~$130/year for hardened AMIs

### Cost Optimization
- **Instance Scheduling**: Stop/start bastion during non-business hours
- **Right-sizing**: Use smallest instance type sufficient for access needs
- **Monitoring**: Track usage and optimize accordingly

## Key Takeaways

- **Bastion Host serves as secure gateway** to private subnet resources
- **Single point of entry** enables centralized access control and monitoring
- **Security is paramount** - restrictive security groups, secure AMIs, and proper key management
- **VPC-specific resources** must be created in the same VPC as target instances
- **Public subnet placement** is required for internet accessibility
- **Connection validation confirms** that public subnet configuration is working correctly
- **Foundation established** for secure private subnet access and management
- **Security best practices** include IP restrictions, hardened AMIs, and proper key management

## Interview Preparation

### Key Concepts to Remember
- Purpose and function of Bastion Hosts in network security
- Difference between public and private subnet access patterns
- Security group and VPC resource relationships
- SSH key management and security considerations

### Common Interview Questions

**Q**: Why do you need a Bastion Host instead of direct access to private instances?
**A**: Private instances have no public IPs and are in subnets that don't route to Internet Gateway, requiring controlled access through public subnet gateway.

**Q**: Where should a Bastion Host be placed and why?
**A**: In a public subnet, because it needs internet connectivity to serve as entry point while private instances remain isolated.

**Q**: What security measures should be implemented for Bastion Hosts?
**A**: Restrictive security groups (IP whitelisting), hardened AMIs, secure key management, regular patching, and session monitoring.

**Q**: Can you use the same security group for instances in different VPCs?
**A**: No, security groups are VPC-specific and cannot be shared across VPCs.

**Q**: What happens if a Bastion Host is compromised?
**A**: It provides potential access to all private subnet resources, which is why security hardening and monitoring are critical.