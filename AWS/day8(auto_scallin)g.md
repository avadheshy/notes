#  Auto Scaling Group (ASG) – AWS

**Auto Scaling** is a service in AWS that **automatically monitors** and **adjusts compute capacity** to maintain application performance and reduce cost. It helps ensure that you have the right number of Amazon EC2 instances running to handle the load of your application.

---

##  Key Concepts

- **Launch Template**: Blueprint used to launch new EC2 instances.
- **Auto Scaling Group (ASG)**: A group of EC2 instances managed by Auto Scaling.
- **Scaling Policies**: Rules that define when and how to scale up/down.
- **Health Checks**: Ensure only healthy instances stay in service.
- **CloudWatch Alarms**: Used to trigger scaling actions based on metrics (e.g., CPU usage).

---

##  How Auto Scaling Works

1. **Monitors CloudWatch Metrics** like `CPUUtilization`, `NetworkIn`, `DiskReadOps`, etc.
2. When a metric exceeds the defined threshold:
   - **Scale-out**: Launch new EC2 instances
   - **Scale-in**: Terminate EC2 instances
3. Uses **Launch Templates** to create new instances
4. Maintains desired instance count as per capacity settings

---

##  Steps to Create an Auto Scaling Group (ASG)

### 1.  Create a Target Group
- This is used for routing traffic to instances (via Load Balancer)

### 2.  Create a Load Balancer
- Select ALB/NLB
- Attach to Target Group
- Allow traffic to/from target group

### 3.  Create a Security Group
- Allow required ports (e.g., 80, 443, 22)

### 4.  Create a Launch Template
- Define:
  - AMI ID
  - Instance Type
  - Key Pair
  - Security Group
  - User Data Script
- Save versioned launch template

### 5.  Create the Auto Scaling Group
- **Name** the ASG
- Select **Launch Template**
- Choose **VPC** and **at least 2 Availability Zones**
- Configure **Health Checks** (EC2 or ELB)
- Set **Capacity**:
  - Minimum
  - Desired
  - Maximum
- Add **Scaling Policies**:
  - Target tracking (e.g., CPU > 60%)
  - Step scaling
  - Scheduled scaling
- Add **Notification Settings**
  - SNS for scaling events
- **Add Tags** (for billing, organization)

---

##  Modifying Instances in an ASG

You **cannot directly modify** instances in an Auto Scaling Group manually. Instead:

- **Update the Launch Template**
- **Create a new version** of the template
- **Update ASG to use the new version**
- Optionally, **manually trigger instance refresh** or **replace instances**

---

##  Important Best Practices

- **Avoid storing dynamic data** (e.g., logs, user uploads) inside EC2
- Use **EFS, NFS, or S3** for persistent storage
- Store logs centrally (e.g., **EFS**, **CloudWatch Logs**)
- Make instances **stateless** so they can be terminated or replaced at any time

---

##  Summary

| Component         | Description                                                  |
|-------------------|--------------------------------------------------------------|
| Launch Template   | Blueprint for EC2 instance creation                          |
| Target Group      | Routing unit used by ELB                                     |
| Load Balancer     | Distributes traffic to ASG instances                         |
| ASG Policies      | Controls scale-in and scale-out behavior                     |
| Monitoring        | Done via CloudWatch alarms                                   |
| Instance Storage  | Should use shared/centralized storage (e.g., EFS/S3)         |
| Notifications     | Send alerts via SNS when scaling happens                     |

---
For creating auto scaling we need 3 things
- AMI
- Launch template
- Auto calling group
---

##  Useful Resources

- [AWS Auto Scaling Documentation](https://docs.aws.amazon.com/autoscaling/)
- [Launch Template Guide](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/ec2-launch-templates.html)
- [CloudWatch Metrics for Auto Scaling](https://docs.aws.amazon.com/autoscaling/ec2/userguide/as-instance-monitoring.html)

