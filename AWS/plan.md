# 15-Day AWS Learning Roadmap

## Overview

This intensive 15-day roadmap will take you from AWS beginner to having practical knowledge of core AWS services. Each day includes theory, hands-on labs, and real-world scenarios. Plan to dedicate 3-4 hours daily for optimal results.

---

## Day 1: AWS Fundamentals & Account Setup

### Goals
- Understand cloud computing concepts
- Learn AWS global infrastructure
- Set up and secure your AWS account

### Topics to Cover
- What is cloud computing? (IaaS, PaaS, SaaS)
- AWS global infrastructure: Regions, Availability Zones, Edge Locations
- AWS service categories overview
- AWS pricing models and Free Tier

### Hands-On Practice
1. Create an AWS Free Tier account
2. Set up MFA (Multi-Factor Authentication) on root account
3. Create an IAM user with admin privileges
4. Set up billing alerts ($5, $10 thresholds)
5. Explore the AWS Management Console

### Resources
- AWS Free Tier: https://aws.amazon.com/free/
- AWS Global Infrastructure map
- AWS Pricing Calculator

### Key Takeaways
✓ Never use root account for daily operations  
✓ Always enable MFA  
✓ Monitor costs from day one  

---

## Day 2: Identity and Access Management (IAM)

### Goals
- Master AWS IAM concepts
- Implement security best practices
- Understand the shared responsibility model

### Topics to Cover
- IAM Users, Groups, Roles, and Policies
- Policy structure and evaluation logic
- AWS managed vs. customer managed policies
- IAM best practices
- AWS Shared Responsibility Model

### Hands-On Practice
1. Create multiple IAM users (developer, analyst)
2. Create IAM groups with different permissions
3. Attach policies to groups and add users
4. Create an IAM role for EC2 instances
5. Test permissions using the IAM Policy Simulator
6. Enable CloudTrail for audit logging

### Lab Exercise
Create a realistic scenario:
- Developers group: EC2, S3 read/write access
- Analysts group: S3 read-only, CloudWatch access
- Admin group: Full access

### Key Takeaways
✓ Use groups to manage permissions  
✓ Follow least privilege principle  
✓ Use roles for services, not access keys  

---

## Day 3: Amazon EC2 (Elastic Compute Cloud) - Basics

### Goals
- Launch and manage EC2 instances
- Understand instance types and pricing models
- Learn about security groups

### Topics to Cover
- EC2 instance types (General Purpose, Compute Optimized, Memory Optimized)
- AMIs (Amazon Machine Images)
- Pricing models: On-Demand, Reserved, Spot, Savings Plans
- Security Groups vs. NACLs
- Key Pairs for SSH access

### Hands-On Practice
1. Launch a t2.micro EC2 instance (Amazon Linux 2)
2. Connect via SSH (Linux/Mac) or PuTTY (Windows)
3. Install Apache web server and host a simple webpage
4. Create and attach security groups
5. Create a custom AMI from your instance
6. Stop, start, and terminate instances

### Lab Exercise
Deploy a simple web application:
```bash
sudo yum update -y
sudo yum install httpd -y
sudo systemctl start httpd
sudo systemctl enable httpd
echo "<h1>Hello from AWS!</h1>" | sudo tee /var/www/html/index.html
```

### Key Takeaways
✓ Always choose the right instance type for your workload  
✓ Stop instances when not in use to save costs  
✓ Security groups are stateful firewalls  

---

## Day 4: Amazon EC2 - Advanced Concepts

### Goals
- Learn about EBS volumes and snapshots
- Understand Auto Scaling and Load Balancing
- Explore EC2 placement groups

### Topics to Cover
- EBS volume types (gp3, io2, st1, sc1)
- EBS snapshots and lifecycle
- Elastic Load Balancers (ALB, NLB, GLB)
- Auto Scaling Groups (ASG)
- Launch Templates

### Hands-On Practice
1. Create and attach EBS volumes to EC2 instances
2. Take EBS snapshots and restore from snapshots
3. Create an Application Load Balancer
4. Set up an Auto Scaling Group (min: 2, desired: 2, max: 4)
5. Test auto-scaling by simulating load
6. Create a Launch Template

### Lab Exercise
Build a scalable web application:
- Launch Template with Apache installed
- Auto Scaling Group across 2 AZs
- Application Load Balancer distributing traffic
- Test by accessing the ALB DNS name

### Key Takeaways
✓ Use gp3 for most general-purpose workloads  
✓ ALB for HTTP/HTTPS, NLB for TCP/UDP  
✓ Auto Scaling provides high availability and cost optimization  

---

## Day 5: Amazon S3 (Simple Storage Service)

### Goals
- Master object storage concepts
- Implement S3 security and access controls
- Learn S3 storage classes

### Topics to Cover
- S3 buckets, objects, and keys
- S3 storage classes (Standard, IA, Glacier, etc.)
- S3 versioning and lifecycle policies
- S3 security: Bucket policies, ACLs, encryption
- S3 static website hosting
- Cross-Region Replication (CRR)

### Hands-On Practice
1. Create S3 buckets with different configurations
2. Upload files and organize with prefixes
3. Enable versioning on a bucket
4. Create lifecycle policies to transition objects to cheaper storage
5. Host a static website on S3
6. Implement bucket policies for public/private access
7. Enable server-side encryption (SSE-S3, SSE-KMS)

### Lab Exercise
Create a static portfolio website:
- Design simple HTML/CSS website
- Upload to S3 bucket
- Enable static website hosting
- Configure bucket policy for public read access
- Access via S3 website endpoint

### Key Takeaways
✓ S3 is object storage, not file storage  
✓ Use lifecycle policies to optimize costs  
✓ Enable versioning for important data  

---

## Day 6: AWS Networking - VPC (Virtual Private Cloud)

### Goals
- Design and implement custom VPCs
- Understand networking components
- Configure routing and connectivity

### Topics to Cover
- VPC, Subnets (public and private)
- Internet Gateway and NAT Gateway
- Route Tables and routing
- VPC Peering and Transit Gateway
- VPC Endpoints
- CIDR notation and IP addressing

### Hands-On Practice
1. Create a custom VPC (10.0.0.0/16)
2. Create public subnet (10.0.1.0/24) and private subnet (10.0.2.0/24)
3. Create and attach Internet Gateway
4. Configure route tables for public subnet
5. Launch EC2 in public subnet (web server)
6. Create NAT Gateway for private subnet
7. Launch EC2 in private subnet (database server)
8. Test connectivity between subnets

### Lab Exercise
Build a 3-tier architecture:
- Public subnet: Web tier (load balancer + web servers)
- Private subnet 1: Application tier
- Private subnet 2: Database tier
- Implement proper security groups and NACLs

### Key Takeaways
✓ Always plan IP addressing before creating VPC  
✓ Use NAT Gateway for private subnet internet access  
✓ One subnet = One Availability Zone  

---

## Day 7: Amazon RDS (Relational Database Service)

### Goals
- Deploy and manage relational databases
- Implement database high availability
- Understand RDS backup and recovery

### Topics to Cover
- RDS supported engines (MySQL, PostgreSQL, MariaDB, Oracle, SQL Server)
- RDS instance types and storage
- Multi-AZ deployments for HA
- Read Replicas for scaling reads
- Automated backups and snapshots
- RDS encryption and security

### Hands-On Practice
1. Launch RDS MySQL instance in private subnet
2. Configure security groups for database access
3. Connect from EC2 instance using MySQL client
4. Create database and tables
5. Enable automated backups
6. Create manual snapshot
7. Enable Multi-AZ deployment
8. Create Read Replica in different AZ

### Lab Exercise
Deploy a WordPress application:
- EC2 instances in public subnet running WordPress
- RDS MySQL in private subnet
- Configure WordPress to use RDS
- Test database connectivity
- Create backup and restore from snapshot

### Key Takeaways
✓ Use Multi-AZ for production databases  
✓ Read Replicas for read-heavy workloads  
✓ Never expose databases to the internet  

---

## Day 8: AWS Database Services & Caching

### Goals
- Learn about different database types
- Implement caching strategies
- Choose the right database for the use case

### Topics to Cover
- DynamoDB (NoSQL)
- Amazon Aurora (high-performance MySQL/PostgreSQL)
- Amazon ElastiCache (Redis and Memcached)
- Database selection criteria
- DAX (DynamoDB Accelerator)

### Hands-On Practice
1. Create DynamoDB table with partition key
2. Add items to DynamoDB table
3. Query and scan DynamoDB data
4. Create Global Secondary Index (GSI)
5. Set up ElastiCache Redis cluster
6. Connect application to Redis for caching
7. Test cache hit/miss scenarios

### Lab Exercise
Build a serverless application:
- DynamoDB table for storing user data
- Lambda function for CRUD operations
- ElastiCache for frequently accessed data
- Compare response times with and without caching

### Key Takeaways
✓ DynamoDB for NoSQL, key-value workloads  
✓ Aurora for high-performance relational databases  
✓ Use caching to reduce database load  

---

## Day 9: AWS Lambda & Serverless

### Goals
- Build serverless applications
- Understand event-driven architecture
- Implement serverless patterns

### Topics to Cover
- AWS Lambda fundamentals
- Lambda triggers and event sources
- Lambda layers and runtime environments
- Cold starts and warm starts
- Lambda pricing model
- Best practices for Lambda functions

### Hands-On Practice
1. Create simple Lambda function (Python/Node.js)
2. Configure Lambda triggers (S3, API Gateway, EventBridge)
3. Set up environment variables
4. Configure Lambda layers for shared code
5. Implement error handling and retries
6. Monitor Lambda with CloudWatch Logs
7. Create Lambda function with VPC access

### Lab Exercise
Build an image processing pipeline:
- S3 bucket for uploading images
- Lambda function triggered on image upload
- Resize image and save to different S3 bucket
- Send notification via SNS
- Use Lambda layers for image processing library

### Key Takeaways
✓ Lambda is ideal for event-driven workloads  
✓ Keep functions small and single-purpose  
✓ Optimize memory allocation for best price/performance  

---

## Day 10: Amazon API Gateway & Application Integration

### Goals
- Create RESTful APIs
- Integrate API Gateway with backend services
- Implement application messaging patterns

### Topics to Cover
- API Gateway types (REST, HTTP, WebSocket)
- API Gateway stages and deployment
- API authentication and authorization
- Amazon SQS (Simple Queue Service)
- Amazon SNS (Simple Notification Service)
- Amazon EventBridge

### Hands-On Practice
1. Create REST API with API Gateway
2. Integrate API with Lambda backend
3. Implement CORS configuration
4. Set up API Gateway stages (dev, prod)
5. Create SQS queue (Standard and FIFO)
6. Configure SNS topic with email subscription
7. Create Lambda function to process SQS messages
8. Set up EventBridge rule for scheduled events

### Lab Exercise
Build a serverless TODO API:
- API Gateway for REST endpoints (GET, POST, PUT, DELETE)
- Lambda functions for business logic
- DynamoDB for data storage
- SNS for notifications
- SQS for async processing
- Test with Postman or curl

### Key Takeaways
✓ API Gateway handles throttling and caching  
✓ SQS for decoupling components  
✓ SNS for pub/sub messaging patterns  

---

## Day 11: Containers - ECS & ECR

### Goals
- Understand container orchestration
- Deploy containerized applications
- Learn Docker basics for AWS

### Topics to Cover
- Container concepts and Docker basics
- Amazon ECS (Elastic Container Service)
- ECS Task Definitions and Services
- Fargate vs. EC2 launch types
- Amazon ECR (Elastic Container Registry)
- ECS Service Auto Scaling

### Hands-On Practice
1. Install Docker locally and build simple container
2. Create ECR repository
3. Push Docker image to ECR
4. Create ECS cluster (Fargate launch type)
5. Define ECS task definition
6. Create ECS service with load balancer
7. Scale ECS service
8. Update application with new image version

### Lab Exercise
Deploy containerized web application:
```dockerfile
FROM nginx:alpine
COPY index.html /usr/share/nginx/html/
EXPOSE 80
```
- Build and tag image
- Push to ECR
- Deploy on ECS Fargate
- Configure Application Load Balancer
- Implement rolling updates

### Key Takeaways
✓ Fargate for serverless containers  
✓ ECR for private Docker registry  
✓ ECS manages container orchestration  

---

## Day 12: Monitoring & Logging - CloudWatch

### Goals
- Implement comprehensive monitoring
- Set up alerts and notifications
- Analyze logs and metrics

### Topics to Cover
- CloudWatch Metrics (standard and custom)
- CloudWatch Logs and Log Groups
- CloudWatch Alarms
- CloudWatch Dashboards
- CloudWatch Events/EventBridge
- CloudWatch Insights

### Hands-On Practice
1. View EC2 metrics in CloudWatch
2. Create custom metrics from application
3. Set up CloudWatch Logs agent on EC2
4. Create log groups and streams
5. Create CloudWatch Alarms (CPU > 80%)
6. Configure SNS for alarm notifications
7. Build CloudWatch Dashboard
8. Use CloudWatch Logs Insights for queries

### Lab Exercise
Implement complete monitoring solution:
- EC2 instances with CloudWatch agent
- Application logs sent to CloudWatch Logs
- Alarms for CPU, memory, disk usage
- Dashboard showing all key metrics
- SNS notifications for critical alarms
- Log analysis with Insights queries

### Key Takeaways
✓ CloudWatch is central to AWS monitoring  
✓ Set alarms before issues occur  
✓ Use dashboards for real-time visibility  

---

## Day 13: Security Services & Best Practices

### Goals
- Implement security layers
- Learn AWS security services
- Apply security best practices

### Topics to Cover
- AWS WAF (Web Application Firewall)
- AWS Shield (DDoS protection)
- AWS KMS (Key Management Service)
- AWS Secrets Manager
- AWS Systems Manager Parameter Store
- AWS GuardDuty
- AWS Security Hub
- AWS Config

### Hands-On Practice
1. Create KMS customer managed key
2. Encrypt S3 bucket with KMS
3. Store secrets in Secrets Manager
4. Store parameters in Parameter Store
5. Access secrets from Lambda function
6. Enable GuardDuty for threat detection
7. Set up AWS WAF rules for ALB
8. Configure AWS Config rules

### Lab Exercise
Secure a web application:
- WAF protecting ALB with rate limiting
- Secrets Manager for database credentials
- KMS encryption for data at rest
- CloudTrail for audit logging
- GuardDuty for threat detection
- Security Hub for compliance checking

### Key Takeaways
✓ Never hardcode credentials  
✓ Encrypt sensitive data at rest and in transit  
✓ Use WAF to protect web applications  

---

## Day 14: DevOps & CI/CD on AWS

### Goals
- Implement CI/CD pipelines
- Automate deployments
- Use Infrastructure as Code

### Topics to Cover
- AWS CodeCommit, CodeBuild, CodeDeploy, CodePipeline
- Infrastructure as Code with CloudFormation
- AWS CDK (Cloud Development Kit)
- Elastic Beanstalk
- AWS Systems Manager

### Hands-On Practice
1. Create CodeCommit repository
2. Push application code
3. Create CodeBuild project
4. Set up CodeDeploy application
5. Create CodePipeline for automated deployment
6. Write CloudFormation template for infrastructure
7. Deploy stack with CloudFormation
8. Use Elastic Beanstalk for quick deployment

### Lab Exercise
Build complete CI/CD pipeline:
```yaml
# buildspec.yml
version: 0.2
phases:
  build:
    commands:
      - npm install
      - npm test
      - npm run build
artifacts:
  files:
    - '**/*'
```
- Source: CodeCommit
- Build: CodeBuild
- Deploy: CodeDeploy or ECS
- Pipeline: CodePipeline automating everything

### Key Takeaways
✓ Automate everything possible  
✓ Use IaC for reproducible infrastructure  
✓ Implement proper testing in pipeline  

---

## Day 15: Advanced Topics & Real-World Project

### Goals
- Explore advanced AWS services
- Build comprehensive project
- Prepare for AWS certification

### Topics to Cover
- AWS Organizations and Control Tower
- AWS Cost Management and Optimization
- AWS Well-Architected Framework
- Route 53 (DNS service)
- CloudFront (CDN)
- AWS Backup and disaster recovery
- Certification paths (Cloud Practitioner, Solutions Architect)

### Hands-On Practice
1. Configure Route 53 hosted zone
2. Set up CloudFront distribution for S3 website
3. Implement custom domain with SSL/TLS
4. Review AWS Well-Architected Framework
5. Use Cost Explorer and Budget alerts
6. Create AWS Backup plan

### Capstone Project
Build a complete 3-tier web application:

**Architecture:**
- Route 53 for DNS
- CloudFront for content delivery
- S3 for static assets
- ALB for load balancing
- EC2 Auto Scaling for web tier
- Lambda for serverless functions
- RDS Multi-AZ for database
- ElastiCache for caching
- CloudWatch for monitoring
- IAM for security
- VPC with public/private subnets

**Requirements:**
- High availability across multiple AZs
- Auto-scaling based on demand
- Secure communication (HTTPS)
- Database backups
- Monitoring and alerting
- Cost optimization

### Project Checklist
□ Infrastructure deployed across 2+ AZs  
□ Auto Scaling configured and tested  
□ Database with automated backups  
□ CloudWatch monitoring and alarms  
□ Proper IAM roles and policies  
□ Cost under $20 with Free Tier  
□ Documentation of architecture  

---

## Post-Roadmap: Next Steps

### Continue Learning
1. **Get Certified**: AWS Certified Cloud Practitioner or Solutions Architect Associate
2. **Explore Specializations**: Machine Learning, Big Data, Security
3. **Advanced Services**: EKS, Step Functions, AppSync, Amplify
4. **Real-World Experience**: Build more projects, contribute to open source

### Study Resources
- AWS Free Digital Training
- AWS Well-Architected Labs
- AWS Workshops (workshops.aws)
- A Cloud Guru / Linux Academy courses
- AWS re:Invent and re:Inforce videos
- AWS Skill Builder

### Practice Platforms
- AWS Free Tier (12 months)
- CloudAcademy Labs
- Qwiklabs
- AWS Workshop Studio

### Community
- AWS Community Builders
- AWS User Groups
- Reddit: r/aws, r/AWSCertifications
- AWS Discord communities
- LinkedIn AWS groups

---

## Cost Management Tips

### Staying Within Free Tier
- Stop EC2 instances when not in use
- Delete unused resources (EBS volumes, snapshots)
- Use t2.micro/t3.micro instances only
- Monitor billing daily
- Set billing alerts at $5, $10, $20
- Clean up resources after each lab

### Monthly Free Tier Limits
- EC2: 750 hours of t2.micro/t3.micro
- S3: 5GB storage, 20,000 GET requests
- RDS: 750 hours of db.t2.micro/db.t3.micro
- Lambda: 1M requests, 400,000 GB-seconds
- CloudWatch: 10 custom metrics, 10 alarms

### Resource Cleanup Checklist
□ Terminate all EC2 instances  
□ Delete EBS volumes and snapshots  
□ Remove RDS instances  
□ Empty and delete S3 buckets  
□ Delete NAT Gateways  
□ Remove Elastic IPs  
□ Delete Load Balancers  
□ Clean up CloudFormation stacks  

---

## Success Metrics

By the end of 15 days, you should be able to:

✓ Design and deploy scalable web applications on AWS  
✓ Implement security best practices  
✓ Set up monitoring and alerting  
✓ Automate deployments with CI/CD  
✓ Optimize costs and resource usage  
✓ Troubleshoot common AWS issues  
✓ Speak confidently about AWS services  
✓ Be ready for AWS certification exams  

---

## Final Tips

1. **Hands-on is crucial**: Don't just read, build things
2. **Document everything**: Keep notes of commands and configurations
3. **Break things**: Learn from failures
4. **Join communities**: Learn from others' experiences
5. **Stay updated**: AWS releases new features constantly
6. **Think architecture**: Always consider availability, scalability, security
7. **Practice cost optimization**: Treat Free Tier budget like production budget

**Remember**: AWS is vast. This roadmap covers core services, but continuous learning is essential. Focus on understanding fundamentals deeply rather than memorizing services superficially.

Good luck on your AWS journey! 🚀