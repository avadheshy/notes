# EC2 Logs Management on AWS

## Introduction to Log Management on AWS

This comprehensive guide covers log management strategies on AWS, including archiving, storage solutions, and real-time log streaming. We'll explore different solutions for effective log management using AWS services.

## Setting Up the Web Server and Locating Logs

### Initial Setup
- **AMI**: Amazon Linux 2 AMI (commands are specific to this distribution)
- **Web Service**: Wave Cafe application
- **Web Server**: HTTPd installation with template from tooplate.com

### Log Location
On CentOS 7, HTTPd logs are located at:
- **Access logs**: `/var/log/httpd/access_log`
- **Error logs**: `/var/log/httpd/error_log`

When users access the website through HTTPd service, access logs are automatically generated and recorded in these files.

## Observing Log Generation

Log generation is rapid and continuous. Even minimal website access generates significant log data. Key observations:

- Every user action generates log entries
- Using `tail -f` command shows real-time log generation
- With thousands or millions of users, log files grow rapidly
- Unmanaged logs can quickly consume available disk space

## Archiving and Cleaning Log Files

### Best Practices
Regular log rotation and archiving is essential for:
- Preventing disk space exhaustion
- Maintaining system performance
- Ensuring log data availability for analysis

### Strategy
1. Archive logs with timestamps
2. Transfer archives to external storage (S3)
3. Clean local log files to free disk space

## Creating S3 Bucket for Log Storage

Create an S3 bucket in the same region as your EC2 instance:
- **Bucket name**: Use unique naming (e.g., `wave-web-logs`)
- **Region**: Match your EC2 instance region
- **Purpose**: Store archived log files

## Archiving Log Files with tar

### Archive Creation
```bash
tar czvf wave-web01-httpdlogs-19122020.tar.gz *
```

### Moving Archives
```bash
mv wave-web01-httpdlogs-19122020.tar.gz /tmp/logs-wave/
```

## Cleaning Log Files

Clear log file contents by redirecting from `/dev/null`:

```bash
> /var/log/httpd/access_log
> /var/log/httpd/error_log
```

## Installing and Configuring AWS CLI

### Installation
```bash
yum install awscli
```

### Configuration
```bash
aws configure
```
Provide:
- Access key ID
- Secret access key
- Default region
- Output format (e.g., json)

## Setting Up IAM User for S3 Access

Create an IAM user with:
- **Access type**: Programmatic access
- **Permissions**: S3 full access
- **Configuration**: Use `aws configure` command

## S3 Operations

### Listing Buckets
```bash
aws s3 ls
```

### Copying Files to S3
```bash
aws s3 cp /tmp/logs-wave/wave-web01-httpdlogs-19122020.tar.gz s3://wave-web-logs/
```

### Directory Synchronization
```bash
aws s3 sync /tmp/logs-wave/ s3://wave-web-logs/
```
- Copies only differential data
- Ideal for regular backups
- More efficient than full copies

## Automating Log Backups

### Automation Options
- **Bash scripts**: Simple shell-based automation
- **Python scripts**: More complex logic and error handling
- **Ansible playbooks**: Infrastructure as code approach
- **Cron jobs**: Schedule automated execution

### Post-Backup Cleanup
After transferring logs to S3, remove local files to free disk space.

## Streaming Live Logs with CloudWatch Logs

### Benefits
- Real-time log monitoring
- Dashboard visualization
- Developer access without production system login
- Log analysis capabilities
- Metric creation from log data
- Automated alerting

### Use Cases
- Troubleshooting issues in real-time
- Monitoring application performance
- Security event detection
- Compliance and audit requirements

## Using IAM Roles for Secure Access

### Advantages Over Access Keys
- No key management required
- No key rotation needed
- Enhanced security
- Automatic credential management

### Implementation
Assign IAM roles to EC2 instances for:
- S3 access permissions
- CloudWatch Logs permissions

## Installing and Configuring CloudWatch Logs Agent

### Installation
```bash
yum install awslogs
```

### Configuration File
Edit `/etc/awslogs/awslogs.conf` to specify:
- Log files to stream
- CloudWatch log group names
- Log stream names

### HTTPd Access Log Configuration
```ini
[/var/log/httpd/access_log]
file = /var/log/httpd/access_log
log_group_name = wave-web
log_stream_name = web01-httpd-access
```

**Important**: Verify the file path exists before configuration.

## Service Management

### Restart and Enable awslogs Service
```bash
systemctl restart awslogsd
systemctl enable awslogsd
```

## Verifying Log Streaming in CloudWatch

After configuration:
1. Check CloudWatch Logs console
2. Verify log group and stream creation
3. Access web server to generate logs
4. Confirm real-time log streaming

## Creating Metric Filters and Alarms

### Metric Filters
- Monitor specific patterns in log files
- Track suspicious IP addresses
- Count error occurrences
- Measure response times

### Alarms
- Set notification thresholds
- Automated responses to conditions
- Integration with SNS for notifications

## Log Streaming for Other AWS Services

### AWS Service Integration
- **RDS**: Built-in CloudWatch Logs integration
- **EC2**: Requires CloudWatch Logs agent
- **Load Balancers**: Special handling required (no OS access)

### Service-Specific Considerations
Different AWS services have varying log streaming capabilities and requirements.

## Load Balancer Access Logs

### Setup Process
1. Create classic load balancer for web server
2. Enable access log generation
3. Configure S3 bucket destination
4. Set delivery interval (e.g., every 5 minutes)

### Configuration Requirements
- S3 bucket policy (roles not supported)
- No direct access key configuration
- JSON policy format

## S3 Bucket Policy for Load Balancer Logs

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Principal": {
        "AWS": "arn:aws:iam::elb-account-id:root"
      },
      "Action": "s3:PutObject",
      "Resource": "arn:aws:s3:::bucket-name/prefix/AWSLogs/aws-account-id/*"
    },
    {
      "Effect": "Allow",
      "Principal": {
        "Service": "delivery.logs.amazonaws.com"
      },
      "Action": "s3:PutObject",
      "Resource": "arn:aws:s3:::bucket-name/prefix/AWSLogs/aws-account-id/*"
    },
    {
      "Effect": "Allow",
      "Principal": {
        "Service": "delivery.logs.amazonaws.com"
      },
      "Action": "s3:GetBucketAcl",
      "Resource": "arn:aws:s3:::bucket-name"
    }
  ]
}
```

### Policy Components
- **ELB Account ID**: Allows load balancer to write logs
- **Delivery Service**: Enables log delivery to S3
- **Bucket ACL**: Grants necessary bucket permissions

## Verifying Load Balancer Log Delivery

### Verification Steps
1. Save and apply bucket policy
2. Wait for delivery interval
3. Check S3 bucket for log files
4. Verify logs appear in designated directory (e.g., `elb-wave/AWSLogs/`)

### Expected Behavior
Logs should appear in the specified S3 location after a short interval, typically matching the configured delivery frequency.

---

## Summary

Effective log management on AWS requires a comprehensive approach combining:
- Regular archiving and cleanup
- Strategic use of S3 for storage
- Real-time monitoring with CloudWatch Logs
- Proper IAM configuration for security
- Service-specific log handling strategies

This multi-layered approach ensures optimal system performance, security, and operational visibility across your AWS infrastructure.