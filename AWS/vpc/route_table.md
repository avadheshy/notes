# AWS VPC Route Tables Configuration Guide

## Introduction

This guide demonstrates how to create and configure route tables to connect Internet Gateway with public subnets, enabling internet connectivity. Route tables are the critical component that makes subnets "public" by directing traffic to the Internet Gateway.

## Current Architecture Status

Before starting:
```
✅ VPC Created (vprofile-VPC)
✅ Subnets Created (4 subnets: 2 public, 2 private)
✅ Internet Gateway Created and Attached
🔄 Route Tables Configuration (Current Step)
🔲 NAT Gateway (Next for private subnets)
🔲 Auto-assign Public IP Settings
```

## Understanding Route Tables

### What is a Route Table?
A route table contains a set of rules (routes) that determine where network traffic is directed. Each subnet must be associated with a route table, which controls the routing for the subnet.

### Default Route Table Behavior
- **Automatic Creation**: AWS automatically creates a route table when you create a VPC
- **Default Association**: All subnets are initially associated with the default route table
- **Local Routes**: Automatically includes routes for local VPC communication

## Step 1: Organize Existing Route Tables

### Current Route Tables Inventory
Navigate to **Route Tables** section to view existing tables:

1. **Default VPC Route Table**: Automatically created with default VPC
2. **vprofile-VPC Route Table**: Automatically created with custom VPC

### Rename for Organization
Rename existing route tables for easy identification:

| Original Name | New Name | Purpose |
|---------------|----------|---------|
| Default VPC RT | `Default-PubRT` | Default VPC public route table |
| vprofile-default-RT | `vprofile-default-RT` | Custom VPC default (unused) |

### Examining Default VPC Route Table
The default VPC's public route table contains:
```
Destination: 172.31.0.0/16    Target: Local
Destination: 0.0.0.0/0        Target: igw-xxxxxxxx (Internet Gateway)
```
This `0.0.0.0/0` route to Internet Gateway is what makes subnets "public."

## Step 2: Create Public Route Table

### Create New Route Table
1. Click **"Create Route Table"**
2. **Name**: `vpro-public-RT`
3. **Description**: Route table for public subnets of vprofile-VPC
4. **VPC**: Select `vprofile-VPC`
5. Click **"Create Route Table"**

### Initial Route Table State
After creation, the route table contains only local routes:
```
Destination: 172.20.0.0/16    Target: Local
```

## Step 3: Associate Route Table with Public Subnets

### Subnet Association Process
1. Select the newly created `vpro-public-RT`
2. Click on **"Subnet Associations"** tab
3. Click **"Edit Subnet Associations"**
4. Select both public subnets:
   - `vpro-pubsub-1`
   - `vpro-pubsub-2`
5. Click **"Save Associations"**

### Verification
After association, verify that both public subnets are listed under the route table's subnet associations.

## Step 4: Add Internet Gateway Route

### The Critical Route Entry
This step transforms private subnets into public subnets by adding internet connectivity.

#### Add Internet Route
1. Select `vpro-public-RT`
2. Click **"Routes"** tab
3. Click **"Edit Routes"**
4. Click **"Add Route"**
5. **Destination**: `0.0.0.0/0`
6. **Target**: Select Internet Gateway → `vprofile-IGW`
7. Click **"Save Changes"**

### Final Route Table Configuration
After adding the route, `vpro-public-RT` should contain:
```
Destination: 172.20.0.0/16    Target: Local
Destination: 0.0.0.0/0        Target: igw-xxxxxxxx (vprofile-IGW)
```

## Step 5: Enable Auto-Assign Public IP

### Current Limitation
Even with route table configured:
- Instances can access the internet (outbound)
- Instances **cannot** be accessed from internet (no public IP)
- Auto-assign public IP is disabled by default

### Enable Public IP Assignment

#### For First Public Subnet
1. Navigate to **Subnets**
2. Select `vpro-pubsub-1`
3. Click **"Actions"** → **"Edit Subnet Settings"**
4. Find **"Auto-assign IP Settings"**
5. **Enable**: "Auto-assign public IPv4 address"
6. Click **"Save"**

#### For Second Public Subnet
1. Select `vpro-pubsub-2`
2. Click **"Actions"** → **"Edit Subnet Settings"**
3. **Enable**: "Auto-assign public IPv4 address"
4. Click **"Save"**

### Impact of Auto-Assign Setting
| Setting | Instance Behavior |
|---------|-------------------|
| **Disabled** | Instances get private IP only, no direct internet access |
| **Enabled** | Instances automatically receive both private and public IP |

## Route Table Types and Purposes

### Public Route Table Configuration
```
Name: vpro-public-RT
Routes:
  - 172.20.0.0/16 → Local (VPC communication)
  - 0.0.0.0/0 → Internet Gateway (Internet access)
Associated Subnets: vpro-pubsub-1, vpro-pubsub-2
```

### Private Route Table Configuration (Future)
```
Name: vpro-private-RT (to be created)
Routes:
  - 172.20.0.0/16 → Local (VPC communication)
  - 0.0.0.0/0 → NAT Gateway (Internet access via NAT)
Associated Subnets: vpro-privsub-1, vpro-privsub-2
```

## Traffic Flow After Configuration

### Public Subnet Traffic Flow
```
Internet ↔ Internet Gateway ↔ Route Table (0.0.0.0/0 → IGW) ↔ Public Subnet ↔ EC2 Instance
```

### Instance Connectivity
After completing all steps:
- **Outbound Internet**: ✅ Instances can access internet
- **Inbound Internet**: ✅ Instances can be accessed from internet (with proper security groups)
- **Public IP**: ✅ Instances automatically receive public IP addresses
- **Private IP**: ✅ Instances retain private IP for VPC communication

## What Makes a Subnet "Public"?

### Essential Requirements
1. **Route Table Association**: Subnet associated with route table
2. **Internet Gateway Route**: Route table has `0.0.0.0/0` → Internet Gateway
3. **Public IP Assignment**: Auto-assign public IP enabled
4. **Security Groups**: Allow inbound/outbound traffic as needed

### Common Misconceptions
- ❌ **Subnet CIDR Range**: CIDR block doesn't determine public/private
- ❌ **Subnet Name**: Naming convention doesn't affect functionality
- ❌ **Internet Gateway Attachment**: IGW alone doesn't make subnets public
- ✅ **Route Table Rules**: Only route table configuration determines subnet type

## Current Architecture Achievement

### Completed Components
```
VPC: vprofile-VPC (172.20.0.0/16)
├── Public Subnets (Internet Accessible)
│   ├── vpro-pubsub-1 (172.20.1.0/24, us-west-1a) ✅
│   └── vpro-pubsub-2 (172.20.2.0/24, us-west-1b) ✅
├── Private Subnets (No Internet Access Yet)
│   ├── vpro-privsub-1 (172.20.3.0/24, us-west-1a) 🔄
│   └── vpro-privsub-2 (172.20.4.0/24, us-west-1b) 🔄
├── Internet Gateway: vprofile-IGW ✅
└── Route Tables:
    ├── vpro-public-RT ✅
    └── vpro-private-RT (to be created) 🔄
```

## Next Steps for Private Subnets

### Required Components
1. **NAT Gateway**: Enable internet access for private subnets
2. **Elastic IP**: Required for NAT Gateway
3. **Private Route Table**: Route table for private subnets
4. **Route Configuration**: `0.0.0.0/0` → NAT Gateway

### Implementation Process
1. Create Elastic IP
2. Create NAT Gateway in public subnet
3. Create private route table
4. Add NAT Gateway route to private route table
5. Associate private subnets with private route table

## Troubleshooting

### Common Issues

#### Instances Can't Access Internet
**Symptoms**: No outbound internet connectivity
**Possible Causes**:
- Route table not associated with subnet
- Missing `0.0.0.0/0` route to Internet Gateway
- Security groups blocking traffic

**Solutions**:
- Verify subnet-route table associations
- Check route table entries
- Review security group rules

#### Can't SSH to Instances
**Symptoms**: Unable to connect from internet
**Possible Causes**:
- Auto-assign public IP disabled
- Security groups blocking SSH (port 22)
- Missing public IP address

**Solutions**:
- Enable auto-assign public IP on subnet
- Configure security groups to allow SSH
- Verify instance has public IP assigned

#### Wrong Route Table Association
**Symptoms**: Subnets not behaving as expected
**Possible Causes**:
- Subnets associated with default route table
- Wrong route table type associated

**Solutions**:
- Check subnet associations in route tables
- Move subnets to correct route table
- Verify route table configurations

### Validation Steps

#### Route Table Verification
1. **Check Associations**: Verify correct subnets are associated
2. **Verify Routes**: Confirm `0.0.0.0/0` points to Internet Gateway
3. **Test Connectivity**: Launch instance and test internet access

#### CLI Verification Commands
```bash
# List route tables
aws ec2 describe-route-tables --filters "Name=vpc-id,Values=vpc-xxxxxxxx"

# Check specific route table
aws ec2 describe-route-tables --route-table-ids rtb-xxxxxxxx
```

## Best Practices

### Naming Conventions
- Include VPC identifier in route table names
- Indicate subnet type (public/private) in names
- Use consistent naming across all resources
- Example: `projectname-public-RT`, `projectname-private-RT`

### Security Considerations
- Create separate route tables for public and private subnets
- Regularly audit route table entries
- Monitor unusual routing patterns
- Use least privilege principle for security groups

### Operational Excellence
- Document route table purposes and associations
- Tag route tables for cost tracking and management
- Monitor route table changes through CloudTrail
- Automate route table creation in infrastructure code

## Cost Implications

### Route Table Costs
- **Route Tables**: No direct charges
- **Data Transfer**: Charges apply for internet traffic
- **NAT Gateway**: Hourly charges for private subnet internet access

### Cost Optimization
- Monitor data transfer patterns
- Use VPC endpoints for AWS service access
- Implement data transfer monitoring
- Regular cost review and optimization

## Key Takeaways

- **Route tables created and properly named** for easy identification and management
- **Public subnets successfully associated** with public route table (`vpro-public-RT`)
- **Critical internet route added** (`0.0.0.0/0` → Internet Gateway) making subnets truly public
- **Auto-assign public IP enabled** on both public subnets for automatic public IP assignment
- **Public subnets now fully functional** - instances can access and be accessed from internet
- **Private subnets remain isolated** - will be configured in next phase with NAT Gateway
- **Foundation established** for complete VPC internet connectivity solution

## Interview Preparation

### Key Concepts to Remember
- Route tables control subnet traffic routing
- `0.0.0.0/0` route to IGW makes subnet public
- Subnet associations determine which route table controls traffic
- Auto-assign public IP is separate from route table configuration

### Common Interview Questions
- **Q**: What makes a subnet public vs private?
- **A**: Route table association - public subnets route `0.0.0.0/0` to Internet Gateway, private subnets route to NAT Gateway

- **Q**: Why do instances need public IPs if the subnet is public?
- **A**: Public subnet enables internet routing, but instances need public IPs for direct internet accessibility

- **Q**: Can you change a subnet from private to public?
- **A**: Yes, by associating it with a public route table (one that routes `0.0.0.0/0` to Internet Gateway)

- **Q**: What happens if you don't enable auto-assign public IP?
- **A**: Instances get private IPs only and cannot be directly accessed from internet, though they can still access internet outbound