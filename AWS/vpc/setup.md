# VPC Setup Guide

## Overview

This guide outlines the complete setup of a Virtual Private Cloud (VPC) in AWS, designed for high availability and security. The architecture includes public and private subnets, NAT Gateway, Bastion host, and VPC peering configuration.

## VPC Network Design

### Main VPC Configuration
- **CIDR Block**: `172.20.0.0/16`
- **IP Address Capacity**: 65,536 addresses
- **Region**: US West (Northern California) - `us-west-1`
- **Availability Zones**: 
  - `us-west-1a`
  - `us-west-1b`

### Subnet Architecture

The VPC will be divided into four subnets for optimal resource distribution and high availability:

| Subnet Type | CIDR Block | Availability Zone | Purpose |
|-------------|------------|-------------------|---------|
| Public Subnet 1 | `172.20.1.0/24` | us-west-1a | Internet-facing resources |
| Public Subnet 2 | `172.20.2.0/24` | us-west-1b | Internet-facing resources |
| Private Subnet 1 | `172.20.3.0/24` | us-west-1a | Internal resources |
| Private Subnet 2 | `172.20.4.0/24` | us-west-1b | Internal resources |

## Required Components

### Core Infrastructure
- **Internet Gateway**: 1 (for internet access to public subnets)
- **NAT Gateway**: 1 (cost-optimized configuration)
- **Elastic IP**: 1 (assigned to NAT Gateway)
- **Route Tables**: 2 (separate for public and private subnets)

### Security Components
- **Bastion Host**: Jump server in public subnet for secure private subnet access
- **Network Access Control List (NACL)**: Subnet-level firewall for public subnets

### Additional Features
- **VPC Peering**: Connection to secondary VPC for inter-VPC communication

## Architecture Details

### High Availability Considerations
- Resources distributed across two availability zones
- Redundant subnets in each zone (public and private)
- For production environments, consider multiple NAT Gateways for true high availability

### Routing Configuration

#### Public Subnet Route Table
- **Destination**: `0.0.0.0/0`
- **Target**: Internet Gateway
- **Purpose**: Direct internet access for public subnet resources

#### Private Subnet Route Table
- **Destination**: `0.0.0.0/0`
- **Target**: NAT Gateway
- **Purpose**: Outbound internet access through NAT Gateway

### Security Architecture

#### Network Access Control Lists (NACLs)
- **Level**: Subnet-level firewall
- **Rules**: Both allow and deny rules supported
- **Scope**: Applied to public subnets initially
- **Advantage**: More granular control compared to Security Groups

#### Bastion Host Configuration
- **Location**: Public subnet
- **Purpose**: Secure access point to private subnet resources
- **Function**: Jump server for administrative access

## Implementation Phases

### Phase 1: VPC Foundation
1. Create main VPC with `172.20.0.0/16` CIDR
2. Create four subnets across two availability zones
3. Configure Internet Gateway

### Phase 2: NAT and Routing
1. Create Elastic IP
2. Deploy NAT Gateway
3. Configure route tables for public and private subnets
4. Associate route tables with respective subnets

### Phase 3: Security and Access
1. Deploy Bastion host in public subnet
2. Configure NACLs for public subnets
3. Set up security groups as needed

### Phase 4: VPC Peering
1. Create secondary VPC
2. Establish VPC peering connection
3. Configure routing for inter-VPC communication

## Cost Optimization Notes

- **Single NAT Gateway**: Implemented for cost savings
- **Production Recommendation**: Deploy NAT Gateways in both availability zones for high availability
- **Trade-off**: Cost vs. availability - single point of failure with one NAT Gateway

## Best Practices

### Security
- Use Bastion host for secure access to private resources
- Implement both NACLs and Security Groups for defense in depth
- Regularly review and update access rules

### High Availability
- Distribute resources across multiple availability zones
- Consider multiple NAT Gateways for production workloads
- Plan for subnet capacity growth

### Monitoring
- Enable VPC Flow Logs for traffic analysis
- Monitor NAT Gateway usage and costs
- Track inter-VPC communication patterns

## Next Steps

After completing this VPC setup:
1. Deploy application resources in appropriate subnets
2. Configure monitoring and logging
3. Implement backup and disaster recovery procedures
4. Review and optimize security configurations
5. Plan for scaling and future requirements

## Key Benefits

- **High Availability**: Multi-AZ deployment
- **Security**: Layered security with public/private separation
- **Scalability**: Large IP address space for growth
- **Cost-Effective**: Optimized NAT Gateway configuration
- **Flexibility**: VPC peering enables multi-VPC architectures