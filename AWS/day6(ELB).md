#  What is ELB (Elastic Load Balancer)?

**Elastic Load Balancer (ELB)** is a fully managed service by AWS that automatically distributes incoming application traffic across multiple targets, such as EC2 instances, containers, and IP addresses.

It acts as a **proxy between users and backend servers**, improving availability and fault tolerance.

---

##  Types of Load Balancers

### 1. Classic Load Balancer (CLB)
- Works at **Layer 4 (Transport Layer)**
- Accepts traffic on port **443** (HTTPS)
- Forwards traffic to EC2 instances on port **80** (HTTP)
- Best suited for **simple, legacy applications**

### 2. Application Load Balancer (ALB)
- Operates at **Layer 7 (Application Layer)**
- Supports **intelligent routing** based on request content (e.g., path, host header)
- Best for **modern HTTP/HTTPS-based microservices and containers**

### 3. Network Load Balancer (NLB)
- Works at **Layer 4**
- Supports **static IP addresses**
- Handles **millions of requests per second** with ultra-low latency
- Ideal for **performance-critical applications**

### 4. Gateway Load Balancer (GLB)
- Operates at **Layer 3 (Network Layer)**
- Enables deployment of **third-party virtual appliances** such as:
  - Firewalls
  - Intrusion Detection/Prevention Systems (IDS/IPS)
  - Deep Packet Inspection (DPI)

---

##  Create an EC2 Image (AMI)

An **Amazon Machine Image (AMI)** allows you to create and launch EC2 instances with pre-configured operating systems and applications.

- Launch EC2 instance from an AMI **on-demand**
- Create a **Launch Template** using the AMI to automate instance creation in seconds

---

##  Create a Target Group for ELB

A **Target Group** is a group of EC2 instances or IP addresses that receive traffic from the ELB.

### Key Configuration Parameters:
- **Traffic Port** (e.g., 80, 443)
- **Healthy Threshold**: Number of successful health checks before marking target as healthy
- **Unhealthy Threshold**: Number of failed health checks before marking target as unhealthy
- **Timeout**: Time to wait for health check response
- **Interval**: Frequency of health checks
- **Success Status Codes**: HTTP codes considered healthy (e.g., 200)
- **Target Selection**: Attach EC2 instances or IPs to the target group

---

##  Create a Load Balancer

### Step-by-Step:
1. **Select the Load Balancer Type** (Application, Network, Classic, Gateway)
2. **Name the Load Balancer**
3. Choose **Internet-Facing** or **Internal**
4. **Select IP Address Type** (IPv4 or Dualstack)
5. Choose **Availability Zones** (at least 2 for redundancy)
6. **Select Security Groups**
7. Define **Listener Ports**:
   - Frontend (e.g., 443)
   - Backend (e.g., 80)
8. **Allow Traffic**:
   - From internet → Load Balancer
   - From Load Balancer → Target Group / EC2

---

##  Summary

| Type       | Layer | Key Feature                            | Best Use Case                        |
|------------|-------|-----------------------------------------|--------------------------------------|
| Classic LB | 4     | Basic HTTP/HTTPS forwarding             | Legacy/simple apps                   |
| ALB        | 7     | Intelligent content-based routing       | Microservices, modern web apps       |
| NLB        | 4     | Static IP, ultra-high performance       | Real-time, latency-sensitive apps    |
| GLB        | 3     | Appliance deployment, traffic mirroring | Security and traffic inspection use  |

