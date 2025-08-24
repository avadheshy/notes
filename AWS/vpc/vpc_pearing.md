# VPC Peering in AWS: Connecting Multiple VPCs Across Regions

## Introduction to VPC Peering

VPC Peering is a critical component for connecting resources across multiple VPCs in large-scale AWS environments. While a single VPC provides security through private subnets and high availability through multiple zones, enterprise environments often require multiple VPCs for different purposes:

- **Web Infrastructure VPC**: Hosting web applications
- **API VPC**: Backend services and APIs  
- **Database VPC**: Database clusters and storage

VPC Peering enables secure communication between these isolated networks, allowing resources in different VPCs to communicate as if they were within the same network.

## Prerequisites

- Existing VPC (e.g., `vprofile-VPC` in North California region)
- Understanding of CIDR blocks and IP addressing
- AWS Console access with appropriate permissions
- Knowledge of route tables and security groups

## Step 1: Create a New VPC for Peering

### Choose Target Region
For this example, we'll create a second VPC in the **Oregon** region to demonstrate cross-region peering.

> **Note**: You can also create VPCs in the same region or even in different AWS accounts.

### Create the Database VPC

1. **Navigate to Oregon region** in AWS Console
2. **Identify default VPC** and rename it to `default` for clarity
3. **Create new VPC** with the following settings:
   - **Name**: `vpro-db`
   - **CIDR Block**: `172.21.0.0/16` or `172.22.0.0/16`
   - **Region**: Oregon

### CIDR Block Requirements

| VPC | Region | CIDR Block | Notes |
|-----|--------|------------|-------|
| vprofile-VPC | North California | 172.20.0.0/16 | Existing VPC |
| vpro-db | Oregon | 172.21.0.0/16 | New VPC - **Must not overlap** |

> **Important**: CIDR ranges must not overlap between peered VPCs.

### Route Table Creation
When creating the VPC, AWS automatically creates a route table. Rename it to `vprodb-rt` for identification.

## Step 2: Establish VPC Peering Connection

### Initiate Peering Request

1. **Navigate to North California region** (requester VPC location)
2. **Go to VPC Console** → **Peering Connections**
3. **Click "Create Peering Connection"**

### Peering Configuration

| Setting | Value | Description |
|---------|-------|-------------|
| **Name** | `vpro-NC` | Identifier for the peering connection |
| **Requester VPC** | `vprofile-VPC` | Source VPC in North California |
| **Account** | My account | Same account peering |
| **Region** | Oregon | Target region |
| **Accepter VPC ID** | `vpc-xxxxxxxx` | VPC ID from Oregon region |

### Create the Connection

1. **Copy VPC ID** from Oregon region console
2. **Paste VPC ID** in accepter VPC field  
3. **Click "Create Peering Connection"**
4. **Status**: Will show as "Pending Acceptance"

## Step 3: Accept the Peering Connection

### Switch to Accepter Region

1. **Navigate to Oregon region**
2. **Go to VPC Console** → **Peering Connections**
3. **Locate pending request**

### Verify and Accept

1. **Select the peering request**
2. **Verify requester details**:
   - VPC ID matches source VPC
   - Account ID is correct
   - CIDR ranges don't overlap
3. **Actions** → **Accept Request**
4. **Status**: Will change to "Active"

> **Status Check**: Connection is established but routing is not yet configured.

## Step 4: Configure Route Tables for Peering

### Understanding Current Routing

Before peering configuration:
- Local traffic: Routes within VPC CIDR automatically
- Internet traffic: Routes through Internet Gateway or NAT Gateway
- Cross-VPC traffic: **No route exists**

### Configure North California Routes

1. **Navigate to North California region**
2. **VPC Console** → **Route Tables**
3. **Select route table** (e.g., private route table)
4. **Actions** → **Edit Routes**

#### Add Peering Route

| Destination | Target | Description |
|-------------|--------|-------------|
| 172.21.0.0/16 | pcx-xxxxxxxx | Route to Oregon VPC via peering |

### Configure Oregon Routes

1. **Navigate to Oregon region**
2. **Select `vprodb-rt` route table**
3. **Actions** → **Edit Routes**

#### Add Peering Route

| Destination | Target | Description |
|-------------|--------|-------------|
| 172.20.0.0/16 | pcx-xxxxxxxx | Route to North California VPC via peering |

### Selective Routing Strategy

> **Best Practice**: Only add routes to subnets that need cross-VPC access.

- **Private subnets**: Add peering routes if cross-VPC communication needed
- **Public subnets**: Consider security implications before adding routes
- **Database subnets**: Typically need peering for application access

## Step 5: Security Group Configuration

### Limitation: Cross-VPC Security Group References

❌ **Cannot reference security group IDs** from peered VPCs  
✅ **Must use CIDR blocks** for cross-VPC access

### Security Group Rules for Peered VPCs

#### Example: Allow SSH Access

| Type | Protocol | Port | Source | Use Case |
|------|----------|------|--------|----------|
| SSH | TCP | 22 | 172.21.5.10/32 | Specific instance IP |
| SSH | TCP | 22 | 172.21.0.0/16 | Entire peered VPC |
| SSH | TCP | 22 | 172.21.1.0/24 | Specific subnet |

#### Example: Database Access

```
Rule: MySQL/Aurora
Protocol: TCP
Port: 3306
Source: 172.20.0.0/16 (Web VPC CIDR)
Description: Allow web tier access to database
```

### CIDR Notation Guide

| Notation | Scope | Use Case |
|----------|-------|----------|
| `/32` | Single IP | Specific instance access |
| `/24` | Subnet (256 IPs) | Subnet-level access |
| `/16` | Large network (65,536 IPs) | VPC-level access |

## Step 6: Testing VPC Peering

### Verification Checklist

- [ ] Peering connection status is "Active"
- [ ] Route tables updated in both VPCs
- [ ] Security groups allow required traffic
- [ ] Network ACLs permit traffic (if custom NACLs used)

### Testing Connectivity

1. **Launch test instances** in both VPCs
2. **Attempt ping** between private IPs:
   ```bash
   ping <private_ip_of_peered_instance>
   ```
3. **Test specific services**:
   ```bash
   telnet <private_ip> <port>
   ```

## Step 7: Cleanup and Resource Management

### Deletion Order

⚠️ **Important**: Follow proper deletion sequence to avoid errors.

#### 1. Delete Route Table Entries
```
1. Navigate to route tables in both regions
2. Remove peering routes from all affected route tables
3. Save changes
```

#### 2. Delete Peering Connection
```
1. Go to Peering Connections in either region
2. Select the peering connection
3. Actions → Delete Peering Connection
4. Confirm deletion
```

#### 3. Delete VPC (if no longer needed)
```
1. Ensure no active peering connections
2. Delete associated resources:
   - NAT Gateways
   - Internet Gateways  
   - Elastic IPs
   - Instances
3. Delete the VPC
```

### Cost Considerations

- **Data transfer charges** apply for cross-region peering
- **NAT Gateway costs** if using NAT for internet access
- **Elastic IP charges** if not properly released

## Advanced Peering Scenarios

### Cross-Account VPC Peering

```
Requester: Account A, VPC in Region X
Accepter: Account B, VPC in Region Y

Additional Requirements:
- Account ID of accepter account
- Proper IAM permissions in both accounts
```

### Hub-and-Spoke Architecture

```
Central Hub VPC ←→ Production VPC
       ↕
Development VPC ←→ Staging VPC
```

### Peering Limitations

- **No transitive peering**: VPC A ←→ VPC B ←→ VPC C doesn't allow A ←→ C
- **Maximum 50 peering connections** per VPC
- **No overlapping CIDR blocks** between peered VPCs
- **Cross-region data transfer charges** apply

## Best Practices

### Security
- ✅ Use principle of least privilege in security groups
- ✅ Implement network segmentation
- ✅ Monitor cross-VPC traffic with VPC Flow Logs
- ✅ Use specific CIDR blocks rather than broad ranges

### Cost Optimization  
- ✅ Delete unused peering connections
- ✅ Monitor data transfer costs
- ✅ Consider AWS PrivateLink for service-to-service communication
- ✅ Release unused Elastic IPs

### Operational Excellence
- ✅ Document peering relationships
- ✅ Use consistent naming conventions
- ✅ Implement proper tagging strategy
- ✅ Regular review of peering connections

## Troubleshooting Common Issues

### Connection Issues

| Issue | Symptoms | Solution |
|-------|----------|----------|
| Peering Inactive | Status shows "Failed" | Check CIDR overlap, recreate connection |
| No Connectivity | Ping fails | Verify route tables and security groups |
| Partial Access | Some services work | Check port-specific security group rules |
| DNS Resolution | Can't resolve names | Enable DNS resolution in peering settings |

### Security Group Debugging

```bash
# Test connectivity
telnet <target_ip> <port>

# Check security group rules
aws ec2 describe-security-groups --group-ids sg-xxxxxxxx

# Verify route tables  
aws ec2 describe-route-tables --route-table-ids rtb-xxxxxxxx
```

## Learning Path and Next Steps

### Recommended Practice

1. **Repeat the setup** multiple times
2. **Try different scenarios**: same region, cross-account
3. **Experiment with security groups** and routing
4. **Monitor costs** during testing
5. **Document your architectures**

### Advanced Topics to Explore

- **AWS Transit Gateway**: Alternative to complex peering
- **AWS PrivateLink**: Service-to-service connectivity
- **VPN Connections**: Hybrid cloud scenarios  
- **Direct Connect**: Dedicated network connections

### Additional Resources

- [AWS VPC Peering Documentation](https://docs.aws.amazon.com/vpc/latest/peering/)
- [AWS Well-Architected Framework](https://aws.amazon.com/architecture/well-architected/)
- [VPC Best Practices](https://docs.aws.amazon.com/vpc/latest/userguide/vpc-security-best-practices.html)

## Conclusion

VPC Peering is an essential skill for DevOps engineers and cloud architects. Understanding how to securely connect multiple VPCs enables you to design scalable, secure, and efficient cloud architectures.

**Key Takeaways:**
- VPC Peering connects isolated networks securely
- Proper CIDR planning prevents connectivity issues  
- Security groups require CIDR notation for cross-VPC access
- Route table configuration is critical for traffic flow
- Practice and repetition solidify understanding

This knowledge forms the foundation for more advanced networking concepts and multi-VPC architectures in AWS.

---

> **Remember**: The best way to master VPC Peering is through hands-on practice. Set up, tear down, and repeat until the concepts become second nature.