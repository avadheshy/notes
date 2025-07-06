# Amazon CloudWatch

**Amazon CloudWatch** is a monitoring and observability service that acts as a **gatekeeper or watchman** for your AWS cloud environment. It provides **real-time metrics**, **logs**, **alerts**, and **automated actions** to help you monitor and operate your resources efficiently.

---

##  Key Features

- 📈 **Metrics Monitoring**
  - Tracks performance metrics like **CPU usage**, **memory**, **disk I/O**, **network traffic**, etc.
  - Supports both **default (EC2, RDS, etc.)** and **custom metrics** (e.g., memory usage via CloudWatch Agent)

- 📋 **Logging**
  - Collects logs from services like **EC2**, **Lambda**, **VPC Flow Logs**, **API Gateway**, etc.
  - Analyze logs using **CloudWatch Logs Insights**

- 🔔 **Alarms & Notifications**
  - Trigger alarms based on metric thresholds
  - Integrates with **SNS** to send notifications (email, SMS, Lambda, etc.)

- 🔄 **Events & Automation**
  - Detects state changes and triggers automated responses
  - Example: Auto-start/stop EC2, auto-scale, or Lambda function execution

- 💸 **Cost Optimization**
  - Monitor idle resources or under-utilized instances
  - Trigger **Lambda functions** to stop unused services to save costs

- 🚀 **Auto Scaling**
  - Alarms can trigger **Auto Scaling Groups** to add/remove EC2 instances automatically

---

## 🛠️ How to Create a CloudWatch Alarm

1. **Go to CloudWatch Console** → Alarms → `Create Alarm`
2. **Select a Metric**  
   - Choose metric from a resource like EC2 (e.g., `CPUUtilization`)
   - Scope: per-instance or aggregate
3. **Set the Condition**  
   - Example: `CPUUtilization > 60%` for 5 minutes
4. **Configure Actions**
   - Select/Create an **SNS Topic**
   - Subscribe with an email address or invoke a Lambda
5. **Name & Create Alarm**
   - CloudWatch will start monitoring and send alerts when the condition is met

---

## 📦 Integrations

| Service          | Role                                                                 |
|------------------|----------------------------------------------------------------------|
| **SNS**          | Sends notifications (email/SMS/HTTP/Lambda) when alarms trigger     |
| **Lambda**       | Run custom automation logic (e.g., shut down idle EC2)               |
| **Auto Scaling** | Add/remove instances based on demand                                 |
| **CloudTrail**   | Audit API calls and track changes to resources                       |
| **CloudWatch Agent** | Push custom metrics (e.g., memory, disk usage) from EC2           |

---

## 📝 Common Use Cases

- Monitor **EC2 CPU usage**, memory, and disk utilization
- Track **application logs** and errors from services
- Automatically scale **EC2 instances** up or down
- Notify admins via **email/SMS** when resource thresholds are breached
- Execute **Lambda scripts** to control costs or restart services

---

## 🔐 Security & Access

- IAM policies control access to CloudWatch features and resources.
- You can restrict alarm creation, log stream access, or metric viewing per user/group.

---

## ✅ Summary

| Capability       | Description                                       |
|------------------|---------------------------------------------------|
| Metrics          | Monitor resource health and performance           |
| Alarms           | Trigger alerts/actions based on conditions        |
| Logs             | Capture and analyze logs from AWS services        |
| Events           | Respond to changes with automation                |
| Custom Metrics   | Track app-level stats like memory or queue size   |
| Cost Control     | Automate resource management to reduce spending   |

