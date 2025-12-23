# What is an EC2 Instance?
Amazon EC2 (Elastic Compute Cloud) is a virtual server in the AWS cloud that lets you run applications just like a physical machine — but scalable, on-demand, and with flexible pricing.
- In short: An EC2 instance is a virtual machine on AWS.
  
# Common Use Cases of EC2:
```
| Use Case                  | Description                                                  |
| ------------------------- | ------------------------------------------------------------ |
| **Web Hosting**           | Run websites or web apps (e.g., Django, Node.js, WordPress). |
| **Application Servers**   | Host backend logic, APIs, microservices.                     |
| **Batch Processing**      | Large-scale parallel jobs (e.g., image/video processing).    |
| **Machine Learning**      | Train models using GPU-based instances.                      |
| **Big Data & Analytics**  | Run Spark, Hadoop, or data analysis tools.                   |
| **Dev/Test Environments** | Quickly spin up test servers for QA or staging.              |
| **Gaming Servers**        | Run multiplayer game backend logic.                          |
| **VPN or Proxy Server**   | Set up a personal VPN or secure proxy.                       |

```
# EC2 Instance Types (Families)
AWS EC2 offers different instance families optimized for different use cases:
![Alt Text](./The-naming-principle-of-AWS-EC2-instance-types-1.png)

---

Instance families

```
    C – Compute

    D – Dense storage

    F – FPGA

    G – GPU

    Hpc – High performance computing

    I – I/O

    Inf – AWS Inferentia

    M – Most scenarios

    P – GPU

    R – Random access memory

    T – Turbo

    Trn – AWS Tranium

    U – Ultra-high memory

    VT – Video transcoding

    X – Extra-large memory
```
Additional capabilities
```
    a – AMD processors

    g – AWS Graviton processors

    i – Intel processors

    d – Instance store volumes

    n – Network and EBS optimized

    e – Extra storage or memory

    z – High performance
```

```
| Instance Type             | Purpose                           | Examples                 |
| ------------------------- | --------------------------------- | ------------------------ |
| **General Purpose**       | Balanced CPU, memory, networking  | `t3`, `t4g`, `m5`, `m6i` |
| **Compute Optimized**     | High-performance CPU workloads    | `c5`, `c6g`, `c7g`       |
| **Memory Optimized**      | Memory-intensive applications     | `r5`, `r6g`, `x2idn`     |
| **Storage Optimized**     | High IOPS or throughput workloads | `i3`, `i4i`, `d3en`      |
| **Accelerated Computing** | GPU or FPGA-based compute (AI/ML) | `p4`, `g5`, `inf2`, `f1` |
| **Burstable**             | Low-cost, burstable performance   | `t2`, `t3`, `t4g`        |

```
# EC2 Pricing Models:
- On-Demand – Pay by the hour/second, no commitment.

- Reserved – 1 or 3-year commitment, lower cost.

- Spot – Buy unused EC2 capacity at discount (can be interrupted).

- Savings Plans – Flexible pricing based on usage commitment.


# EC2 Instance Basics:
Understanding the concept of virtual servers and instances. Key components of an EC2 instance: AMI (Amazon Machine Image), instance types, and instance states. Differentiating between On-Demand, Reserved, and Spot instances.

# Requirements gathering for EC2
- OS which os to select
- Size Ram/CPU/Network
- Project Taging purpose
- Services/App Running(http,ssh,mysql)
- Environment Dev?prod/staging?Qa
- Loging User Owner

# Launching an EC2 Instance:
- Step-by-step guide on launching an EC2 instance using the AWS Management Console.
- Configuring instance details, such as instance type, network settings, and storage options.
- Understanding security groups and key pairs for securing instances.
  ```
  Names and tags->AMI->Instance Type->EBS(Elastic Block storage)->Tag (for filtering)-> Target Group->Keys
  ```
  - Create a Key pair for logging purpose(make it for every envirnment)
  - Make a security Group (That will be attach to ec2 Network Interface)
  - And name and tags to ec2 instance.
  - select AMI & select Instance type
  - select key pair and security Group
  - cofigure storge and launch instance
  # elastic ip
  it is a public ip
# What is Inbound and Outbound Rules ?
In network security (especially in cloud services like AWS EC2), Inbound and Outbound Rules control the flow of traffic to and from a resource, like a virtual server or security group.
- It is related to security group.
# Security Gooup
- Acts as a firewall for one or more instances
- You can add inbound and outbound rule to security groups that will be apply on ec2.
- They are statefull.
# Inbound Rules
- Control incoming traffic to your instance or server.

- Think of it as “Who is allowed to talk to me?”

Examples:

- Allow HTTP (port 80) from the internet.

- Allow SSH (port 22) from your IP only.
```
From: 0.0.0.0/0     Protocol: TCP     Port: 80     Action: Allow
```
# Outbound Rules
Control outgoing traffic from your instance to the outside world.

Think of it as “Who can I talk to?”

Examples:

- Allow all outbound internet traffic.

- Restrict to internal IP ranges only.


# Managing EC2 Instances:
- Starting, stopping, and terminating instances.
- Monitoring instance performance and utilization.
- Basic troubleshooting and accessing instances using SSH (Secure Shell).
In AWS, regions, availability zones, and data centers are distinct concepts that together form the backbone of AWS's infrastructure:
