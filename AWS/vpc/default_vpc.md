# AWS Default VPC Guide

## Introduction

This guide provides a comprehensive overview of the Default Virtual Private Cloud (VPC) in AWS, focusing on understanding its structure, components, and characteristics. The examples and demonstrations are based on the North California region (US West 1), which is ideal for learning due to its simplified two-availability-zone setup.

## Getting Started

### Accessing VPC Dashboard
1. Search for "VPC" in the AWS Management Console
2. Open the VPC service
3. Navigate to the VPC Dashboard

The dashboard displays various VPC configurations including:
- VPCs
- NAT Gateways
- Subnets
- Route Tables
- Internet Gateways

## Default VPC Overview

### Key Characteristics
- **Automatic Creation**: AWS automatically creates a default VPC in every region
- **Manual Creation**: Cannot be created manually by users
- **Restoration**: If deleted, must be restored by AWS Support
- **Identification**: Can be renamed to "DEFAULT VPC" for easy identification

### Default VPC Specifications
- **CIDR Block**: `172.31.0.0/16`
- **IP Address Capacity**: ~65,000 addresses
- **Availability**: Present in every AWS region
- **Subnet Mask**: `/16`

## Default Subnets

### Subnet Configuration
Each default VPC contains **two public subnets** with the following characteristics:

| Property | Details |
|----------|---------|
| **Number of Subnets** | 2 |
| **Type** | Public |
| **CIDR Block** | `/20` each |
| **IP Addresses per Subnet** | ~4,096 |
| **Reserved IPs** | 5 per subnet (AWS internal use) |
| **IP Range** | 172.31.16.x |

### Subnet Naming Convention
For better organization and identification:
- **Subnet 1**: `Default-pubsub1`
- **Subnet 2**: `Default-pubsub2`

### Availability Zone Distribution
- Each subnet is associated with a different availability zone
- Example: `us-west-1a` and `us-west-1b`

## Identifying Public vs Private Subnets

### Route Table Analysis
The key to determining whether a subnet is public or private lies in examining its **route table entries**:

#### Public Subnet Route Table
- **Local Traffic**: `172.31.0.0/16` → Routes locally within VPC
- **Internet Traffic**: `0.0.0.0/0` → Routes to Internet Gateway

#### Private Subnet Route Table
- **Local Traffic**: VPC CIDR → Routes locally within VPC
- **Internet Traffic**: `0.0.0.0/0` → Routes to NAT Gateway

### Critical Rule to Remember
> **Public Subnets**: Traffic routed to Internet Gateway  
> **Private Subnets**: Traffic routed to NAT Gateway

This distinction is fundamental for AWS networking and commonly appears in technical interviews.

## Route Tables Deep Dive

### Route Table Components
1. **Destination**: IP address range
2. **Target**: Where traffic is directed
3. **Associated Subnets**: Which subnets use this route table

### Default Route Table Entries
```
Destination: 172.31.0.0/16    Target: Local
Destination: 0.0.0.0/0        Target: igw-xxxxxxxxx
```

### Route Table Verification Steps
1. Select a subnet
2. View associated route table
3. Examine route entries
4. Identify target for `0.0.0.0/0` route
5. Confirm Internet Gateway ID

## Internet Gateway

### Characteristics
- **Attachment**: Connected to default VPC
- **Function**: Enables internet access for public subnets
- **Identification**: Visible in route tables as target
- **Management**: View details in "Internet Gateways" section

### Best Practices
- Never delete the default Internet Gateway
- Can be inspected but should not be modified
- Essential for public subnet functionality

## IP Address Management

### IP Address Allocation
- **Instance IPs**: Assigned from subnet's CIDR range
- **Format**: 172.31.16.x (for default subnets)
- **Identification**: Private IP reveals subnet membership
- **Exclusions**: Not from 10.x.x.x or 20.x.x.x ranges

### Reserved IP Addresses
AWS reserves **5 IP addresses** per subnet:
1. Network address
2. VPC router
3. DNS server
4. Future use
5. Broadcast address

## Advanced VPC Components

The VPC dashboard includes additional components for advanced use cases:
- **Egress-only Internet Gateways**
- **DHCP Option Sets**
- **VPC Endpoints**
- **Endpoint Services**
- **Network ACLs**
- **NAT Gateways**
- **Elastic IPs**

*Note: These advanced topics are beyond the scope of basic VPC understanding.*

## Critical Best Practices

### ⚠️ Important Warnings
1. **Never delete the default VPC**
2. **Never delete the default Internet Gateway**
3. **Never delete default route tables**
4. **Always contact AWS Support** if default VPC is accidentally deleted

### Naming Conventions
- Rename default VPC to "DEFAULT VPC" (uppercase)
- Use descriptive names for subnets: "Default-pubsub1", "Default-pubsub2"
- Maintain consistent naming across all VPC components

## Troubleshooting and Identification

### Verifying Default VPC
1. Navigate to "Your VPCs"
2. Look for VPC with "default VPC" designation
3. Check CIDR block: `172.31.0.0/16`
4. Compare VPC ID with subnet VPC associations

### Common Issues
- **Missing Default VPC**: Contact AWS Support
- **Connectivity Problems**: Check route tables
- **IP Assignment**: Verify subnet CIDR ranges
- **Internet Access**: Confirm Internet Gateway attachment

## Next Steps

After understanding the default VPC:
1. Learn to create custom VPCs
2. Practice adding subnets to custom VPCs
3. Explore NAT Gateways for private subnets
4. Study Network ACLs and security groups
5. Implement VPC peering and endpoints

## Key Takeaways

- **Default VPC exists in every AWS region** and cannot be manually created
- **Default VPC uses CIDR block 172.31.0.0/16** providing ~65,000 IP addresses
- **Public subnets route to Internet Gateway**, private subnets route to NAT Gateway
- **Route table analysis is essential** for understanding subnet types
- **Never delete default VPC components** - restoration requires AWS Support
- **Understanding route tables and subnet associations** is crucial for VPC management

## Interview Preparation

Key concepts frequently asked in AWS interviews:
- Difference between public and private subnets
- Route table configuration and analysis
- Default VPC characteristics and limitations
- IP address ranges and subnet identification
- Internet Gateway vs NAT Gateway routing