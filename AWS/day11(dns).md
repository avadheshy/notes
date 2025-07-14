#  AWS Route 53 + Load Balancer (ALB) + Domain Setup Guide

This guide explains how to connect a domain (e.g., `crazycoder.shop` from Hostinger) to a dynamic website hosted on AWS using an EC2 instance behind an Application Load Balancer (ALB), with Route 53 handling DNS.

---

##  Prerequisites

- A registered domain (e.g., `crazycoder.shop`) — here, from Hostinger
- An EC2 instance running your dynamic web app (Node.js, Django, etc.)
- An ALB set up in front of your EC2 instance
- An AWS Route 53 hosted zone

---

## Step-by-Step Setup

###  1. Launch EC2 and Deploy App

- Launch an EC2 instance
- Install app stack (Node.js, Django, Apache, etc.)
- Test app via EC2 Public IP or via target group

---

###  2. Set Up Application Load Balancer (ALB)

- Go to EC2 → Load Balancers → Create Load Balancer → Application Load Balancer
- Add listeners:
  - HTTP (port 80)
  - Optional: HTTPS (port 443, see ACM setup below)
- Register your EC2 in a **Target Group**
- ALB is now accessible at:
```
my-alb-1234567890.us-east-1.elb.amazonaws.com
# this is load balancer dns name
```

---

###  3. Create Hosted Zone in Route 53

- Go to Route 53 → Hosted Zones → Create Hosted Zone
- Enter domain: `crazycoder.shop`
- AWS generates 4 **NS (nameserver) records**, e.g.:
```
ns-123.awsdns-45.com
ns-2345.awsdns-38.co.uk
..
```

---

###  4. Update Nameservers in Hostinger

- Log in to Hostinger dashboard
- Go to your domain → DNS/Nameserver settings
- Replace existing NS records with the 4 from Route 53
- Save and wait for DNS propagation (up to 24–48 hrs, usually faster)

---

###  5. Create Alias Record in Route 53

- In your hosted zone, click "Create Record"
- Type: `A`
- Name: (Leave blank for root domain or type `www`)
- Alias: `Yes`
- Target: Select your ALB DNS (it auto-populates)
- Save

Now, requests to `crazycoder.shop` will resolve to the Load Balancer.

---

##  Optional: Add HTTPS with ACM

1. Go to **ACM (AWS Certificate Manager)** → Request certificate
2. Add domain names:
 - `crazycoder.shop`
 - `www.crazycoder.shop`
3. Choose **DNS validation**
4. ACM provides a CNAME record → Add this in Route 53
5. Once validated, attach the cert to the HTTPS listener in your ALB

---

##  What Happens When a User Visits the Site?
```
User types: www.crazycoder.shop
↓
Browser sends DNS query
↓
DNS resolver checks .shop TLD server
↓
TLD server says: "Route 53 is authoritative"
↓
Route 53 finds A (Alias) record for www.crazycoder.shop
↓
Returns ALB DNS name (e.g., my-alb-1234.elb.amazonaws.com)
↓
Resolver asks AWS ELB DNS for IP of ALB
↓
ELB DNS returns IP addresses
↓
Browser connects to one of the IPs → Hits ALB
↓
ALB routes request to healthy EC2 instance in the target group
↓
Your web app responds 
```

---

##  Key Concepts

| Concept        | Explanation                                                                 |
|----------------|-----------------------------------------------------------------------------|
| **Route 53 Hosted Zone** | AWS's DNS service that maps your domain to AWS resources               |
| **Alias Record**         | Route 53-specific record that allows pointing root domain to ALB/S3/etc |
| **ALB DNS Name**         | A stable DNS entry managed by AWS ELB service                         |
| **No Static IP**         | ALBs don't use fixed IPs — DNS is used to load balance dynamically   |
| **Nameservers (NS)**     | Tell the world that Route 53 manages DNS for your domain             |

---

## 🔍 Testing Commands

```bash
# Check what DNS resolves for your domain
dig crazycoder.shop

# Check what IPs your ALB DNS returns
dig my-alb-1234.us-east-1.elb.amazonaws.com

# Trace DNS resolution
nslookup crazycoder.shop
#  Summary
Hostinger is only your domain registrar

Route 53 becomes the DNS provider after you change NS records

Route 53 points your domain to the ALB

ALB forwards traffic to your EC2 backend

(Optional) Use ACM + ALB to enable HTTPS

#
# Route 53: A vs Alias A Record

This guide explains the difference between **A** and **Alias A** records in AWS Route 53 and when to use each — especially for EC2 instances and Load Balancers (ALB).

---

##  What is an A Record?

- An **A Record** maps a domain name to a static IPv4 address.
- Commonly used when you want your domain (e.g., `crazycoder.shop`) to point directly to:
  - An EC2 instance (public IP)
  - An external server IP

###  Example: A Record for EC2
| Field         | Value              |
|---------------|--------------------|
| Record Type   | A                  |
| Name          | `crazycoder.shop` |
| Value (IP)    | `3.110.44.67`      |
| Alias         | No                 |

Use this when you are **not using a Load Balancer** and want to connect the domain directly to a **single EC2 instance**.

---

## What is an Alias A Record?

- **Alias A Records** are AWS-specific records that allow you to map your domain name to AWS services that do not have a static IP (like ALB, S3, CloudFront, etc.).
- You can use Alias A at the **root domain** (e.g., `crazycoder.shop`), which **CNAME records can't** do.

###  Example: Alias A Record for Load Balancer
| Field         | Value                                             |
|---------------|---------------------------------------------------|
| Record Type   | A                                                 |
| Name          | `crazycoder.shop`                                 |
| Alias         | Yes                                               |
| Alias Target  | `my-alb-1234567890.us-east-1.elb.amazonaws.com`   |

Use this when you are **using an ALB** or another AWS-managed service.

---

##  Key Differences

| Feature                  | A Record              | Alias A Record                          |
|--------------------------|-----------------------|------------------------------------------|
| Can point to IP          | ✅ Yes                | ❌ No                                     |
| Can point to ALB/S3/CF   | ❌ No                 | ✅ Yes                                    |
| Works at root domain     | ✅ Yes                | ✅ Yes                                    |
| Requires TTL             | ✅ Yes (customizable) | ❌ No (managed by AWS)                   |
| Cost                     | Standard query charge | **Free for AWS Alias lookups**          |
| Resolvable by external DNS | ✅ Yes              | ✅ Yes                                    |

---

##  When to Use What

| Use Case                           | Record Type   |
|------------------------------------|---------------|
| Point to EC2 public IP             | A             |
| Point to Load Balancer (ALB)       | Alias A       |
| Point to CloudFront/S3/API Gateway | Alias A       |
| Point to non-AWS static IP         | A             |

---

##  DNS Lookup Test

```bash
dig crazycoder.shop
dig my-alb-1234567890.us-east-1.elb.amazonaws.com
