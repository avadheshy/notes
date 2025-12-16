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

# CloudWatch Guide for Python Backend Developers

## Overview

Amazon CloudWatch is a monitoring and observability service for AWS resources and applications. This guide covers essential CloudWatch concepts and usage patterns for Python backend developers.

## Core Concepts

**Metrics**: Quantitative data about your systems (CPU usage, request count, error rates)

**Logs**: Text-based records of events from your applications and AWS services

**Alarms**: Automated notifications based on metric thresholds

**Dashboards**: Visual representations of metrics and logs

**Events/EventBridge**: Event-driven automation triggers

## Setting Up CloudWatch with Python

### Installation

```bash
pip install boto3
```

### Basic Configuration

```python
import boto3
from datetime import datetime, timedelta

# Initialize CloudWatch clients
cloudwatch = boto3.client('cloudwatch', region_name='us-east-1')
logs_client = boto3.client('logs', region_name='us-east-1')
```

## Working with CloudWatch Logs

### Creating Log Groups and Streams

```python
def create_log_group(log_group_name):
    try:
        logs_client.create_log_group(logGroupName=log_group_name)
        print(f"Log group '{log_group_name}' created")
    except logs_client.exceptions.ResourceAlreadyExistsException:
        print(f"Log group '{log_group_name}' already exists")

def create_log_stream(log_group_name, log_stream_name):
    try:
        logs_client.create_log_stream(
            logGroupName=log_group_name,
            logStreamName=log_stream_name
        )
        print(f"Log stream '{log_stream_name}' created")
    except logs_client.exceptions.ResourceAlreadyExistsException:
        print(f"Log stream '{log_stream_name}' already exists")
```

### Sending Logs to CloudWatch

```python
def send_log_event(log_group_name, log_stream_name, message):
    timestamp = int(datetime.now().timestamp() * 1000)
    
    response = logs_client.put_log_events(
        logGroupName=log_group_name,
        logStreamName=log_stream_name,
        logEvents=[
            {
                'timestamp': timestamp,
                'message': message
            }
        ]
    )
    return response

# Example usage
send_log_event(
    '/aws/lambda/my-function',
    '2024-12-17',
    'User authentication successful'
)
```

### Using CloudWatch Logs with Python Logging

```python
import logging
from watchtower import CloudWatchLogHandler

# Setup logger with CloudWatch handler
logger = logging.getLogger(__name__)
logger.setLevel(logging.INFO)

handler = CloudWatchLogHandler(
    log_group='/aws/application/backend',
    stream_name='api-server',
    use_queues=True
)
logger.addHandler(handler)

# Use it like standard Python logging
logger.info("Application started")
logger.error("Database connection failed", exc_info=True)
```

### Querying Logs with CloudWatch Insights

```python
def query_logs(log_group_name, query_string, start_time, end_time):
    """
    Query CloudWatch Logs using CloudWatch Insights
    """
    response = logs_client.start_query(
        logGroupName=log_group_name,
        startTime=int(start_time.timestamp()),
        endTime=int(end_time.timestamp()),
        queryString=query_string
    )
    
    query_id = response['queryId']
    
    # Wait for query to complete
    response = None
    while response is None or response['status'] == 'Running':
        response = logs_client.get_query_results(queryId=query_id)
    
    return response['results']

# Example: Find all errors in the last hour
end_time = datetime.now()
start_time = end_time - timedelta(hours=1)

query = """
fields @timestamp, @message
| filter @message like /ERROR/
| sort @timestamp desc
| limit 100
"""

results = query_logs('/aws/application/backend', query, start_time, end_time)
```

## Working with CloudWatch Metrics

### Publishing Custom Metrics

```python
def put_metric(namespace, metric_name, value, unit='Count', dimensions=None):
    """
    Publish a custom metric to CloudWatch
    """
    metric_data = {
        'MetricName': metric_name,
        'Value': value,
        'Unit': unit,
        'Timestamp': datetime.utcnow()
    }
    
    if dimensions:
        metric_data['Dimensions'] = dimensions
    
    response = cloudwatch.put_metric_data(
        Namespace=namespace,
        MetricData=[metric_data]
    )
    return response

# Example: Track API response time
put_metric(
    namespace='MyApp/API',
    metric_name='ResponseTime',
    value=245.5,
    unit='Milliseconds',
    dimensions=[
        {'Name': 'Environment', 'Value': 'Production'},
        {'Name': 'Endpoint', 'Value': '/api/users'}
    ]
)
```

### Publishing Multiple Metrics Efficiently

```python
def put_multiple_metrics(namespace, metrics):
    """
    Publish multiple metrics in a single API call (max 1000 per call)
    """
    metric_data = []
    
    for metric in metrics:
        data = {
            'MetricName': metric['name'],
            'Value': metric['value'],
            'Unit': metric.get('unit', 'Count'),
            'Timestamp': datetime.utcnow()
        }
        
        if 'dimensions' in metric:
            data['Dimensions'] = metric['dimensions']
        
        metric_data.append(data)
    
    response = cloudwatch.put_metric_data(
        Namespace=namespace,
        MetricData=metric_data
    )
    return response

# Example usage
metrics = [
    {'name': 'RequestCount', 'value': 150, 'unit': 'Count'},
    {'name': 'ErrorCount', 'value': 3, 'unit': 'Count'},
    {'name': 'AverageResponseTime', 'value': 235.2, 'unit': 'Milliseconds'}
]

put_multiple_metrics('MyApp/API', metrics)
```

### Retrieving Metrics

```python
def get_metric_statistics(namespace, metric_name, start_time, end_time, 
                         period=300, statistics=None, dimensions=None):
    """
    Retrieve metric statistics from CloudWatch
    """
    if statistics is None:
        statistics = ['Average', 'Sum', 'Maximum', 'Minimum']
    
    params = {
        'Namespace': namespace,
        'MetricName': metric_name,
        'StartTime': start_time,
        'EndTime': end_time,
        'Period': period,
        'Statistics': statistics
    }
    
    if dimensions:
        params['Dimensions'] = dimensions
    
    response = cloudwatch.get_metric_statistics(**params)
    return response['Datapoints']

# Example: Get API request count for the last hour
end_time = datetime.utcnow()
start_time = end_time - timedelta(hours=1)

datapoints = get_metric_statistics(
    namespace='MyApp/API',
    metric_name='RequestCount',
    start_time=start_time,
    end_time=end_time,
    period=300,  # 5-minute intervals
    statistics=['Sum']
)

for point in sorted(datapoints, key=lambda x: x['Timestamp']):
    print(f"{point['Timestamp']}: {point['Sum']} requests")
```

## Creating CloudWatch Alarms

### Metric-Based Alarm

```python
def create_alarm(alarm_name, metric_name, namespace, threshold, 
                comparison_operator='GreaterThanThreshold'):
    """
    Create a CloudWatch alarm for a metric
    """
    response = cloudwatch.put_metric_alarm(
        AlarmName=alarm_name,
        ComparisonOperator=comparison_operator,
        EvaluationPeriods=2,
        MetricName=metric_name,
        Namespace=namespace,
        Period=300,
        Statistic='Average',
        Threshold=threshold,
        ActionsEnabled=True,
        AlarmActions=[
            'arn:aws:sns:us-east-1:123456789012:my-sns-topic'
        ],
        AlarmDescription=f'Alarm when {metric_name} exceeds {threshold}',
        Unit='Count'
    )
    return response

# Example: Alert when error rate is high
create_alarm(
    alarm_name='HighErrorRate',
    metric_name='ErrorCount',
    namespace='MyApp/API',
    threshold=10,
    comparison_operator='GreaterThanThreshold'
)
```

### Composite Alarm

```python
def create_composite_alarm(alarm_name, alarm_rule):
    """
    Create a composite alarm based on multiple alarms
    """
    response = cloudwatch.put_composite_alarm(
        AlarmName=alarm_name,
        AlarmRule=alarm_rule,
        ActionsEnabled=True,
        AlarmActions=[
            'arn:aws:sns:us-east-1:123456789012:my-sns-topic'
        ],
        AlarmDescription='Composite alarm for system health'
    )
    return response

# Example: Alert when both CPU and error rate are high
alarm_rule = "ALARM(HighCPUAlarm) AND ALARM(HighErrorRate)"
create_composite_alarm('SystemUnhealthy', alarm_rule)
```

## Structured Logging Best Practices

### Using JSON for Structured Logs

```python
import json
import logging

class JSONFormatter(logging.Formatter):
    def format(self, record):
        log_data = {
            'timestamp': datetime.utcnow().isoformat(),
            'level': record.levelname,
            'message': record.getMessage(),
            'module': record.module,
            'function': record.funcName,
            'line': record.lineno
        }
        
        # Add extra fields if they exist
        if hasattr(record, 'user_id'):
            log_data['user_id'] = record.user_id
        if hasattr(record, 'request_id'):
            log_data['request_id'] = record.request_id
        
        return json.dumps(log_data)

# Setup logger with JSON formatter
logger = logging.getLogger(__name__)
handler = logging.StreamHandler()
handler.setFormatter(JSONFormatter())
logger.addHandler(handler)
logger.setLevel(logging.INFO)

# Log with extra context
logger.info('User logged in', extra={'user_id': 'user123', 'request_id': 'req456'})
```

### Decorator for Function Timing

```python
import functools
import time

def log_execution_time(metric_name):
    """
    Decorator to log function execution time to CloudWatch
    """
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            start_time = time.time()
            try:
                result = func(*args, **kwargs)
                return result
            finally:
                execution_time = (time.time() - start_time) * 1000
                put_metric(
                    namespace='MyApp/Performance',
                    metric_name=metric_name,
                    value=execution_time,
                    unit='Milliseconds'
                )
                logger.info(f"{func.__name__} executed in {execution_time:.2f}ms")
        return wrapper
    return decorator

@log_execution_time('DatabaseQueryTime')
def fetch_user_data(user_id):
    # Your database query here
    pass
```

## Context Manager for Metric Tracking

```python
from contextlib import contextmanager

@contextmanager
def track_operation(operation_name):
    """
    Context manager to track operation success/failure and duration
    """
    start_time = time.time()
    success = False
    
    try:
        yield
        success = True
    finally:
        duration = (time.time() - start_time) * 1000
        
        metrics = [
            {
                'name': f'{operation_name}Duration',
                'value': duration,
                'unit': 'Milliseconds'
            },
            {
                'name': f'{operation_name}Success' if success else f'{operation_name}Failure',
                'value': 1,
                'unit': 'Count'
            }
        ]
        
        put_multiple_metrics('MyApp/Operations', metrics)

# Usage
with track_operation('DatabaseWrite'):
    # Your database write operation
    db.save(data)
```

## Integration with Flask/FastAPI

### Flask Middleware Example

```python
from flask import Flask, request, g
import time
import uuid

app = Flask(__name__)

@app.before_request
def before_request():
    g.start_time = time.time()
    g.request_id = str(uuid.uuid4())

@app.after_request
def after_request(response):
    duration = (time.time() - g.start_time) * 1000
    
    # Log request
    logger.info(
        'HTTP request',
        extra={
            'request_id': g.request_id,
            'method': request.method,
            'path': request.path,
            'status_code': response.status_code,
            'duration_ms': duration
        }
    )
    
    # Send metrics
    metrics = [
        {
            'name': 'RequestCount',
            'value': 1,
            'unit': 'Count',
            'dimensions': [
                {'Name': 'Method', 'Value': request.method},
                {'Name': 'Endpoint', 'Value': request.path},
                {'Name': 'StatusCode', 'Value': str(response.status_code)}
            ]
        },
        {
            'name': 'ResponseTime',
            'value': duration,
            'unit': 'Milliseconds',
            'dimensions': [
                {'Name': 'Endpoint', 'Value': request.path}
            ]
        }
    ]
    
    put_multiple_metrics('MyApp/API', metrics)
    
    return response
```

### FastAPI Middleware Example

```python
from fastapi import FastAPI, Request
from starlette.middleware.base import BaseHTTPMiddleware
import time

app = FastAPI()

class CloudWatchMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        start_time = time.time()
        request_id = str(uuid.uuid4())
        
        response = await call_next(request)
        
        duration = (time.time() - start_time) * 1000
        
        # Log and send metrics (async)
        logger.info(
            'HTTP request',
            extra={
                'request_id': request_id,
                'method': request.method,
                'path': request.url.path,
                'status_code': response.status_code,
                'duration_ms': duration
            }
        )
        
        return response

app.add_middleware(CloudWatchMiddleware)
```

## Common CloudWatch Insights Queries

### Error Analysis
```
fields @timestamp, @message
| filter @message like /ERROR|Exception/
| stats count() by bin(5m)
```

### Top Endpoints by Request Count
```
fields @timestamp, endpoint, status_code
| stats count() as request_count by endpoint
| sort request_count desc
| limit 10
```

### Average Response Time by Endpoint
```
fields @timestamp, endpoint, duration_ms
| stats avg(duration_ms) as avg_duration by endpoint
| sort avg_duration desc
```

### Requests with High Latency
```
fields @timestamp, endpoint, duration_ms, user_id
| filter duration_ms > 1000
| sort @timestamp desc
```

## Cost Optimization Tips

1. **Set Log Retention Periods**: Don't keep logs indefinitely
   ```python
   logs_client.put_retention_policy(
       logGroupName='/aws/application/backend',
       retentionInDays=7  # Options: 1, 3, 5, 7, 14, 30, 60, 90, etc.
   )
   ```

2. **Use Metric Filters**: Convert logs to metrics instead of querying logs repeatedly

3. **Batch Metric Publishing**: Send multiple metrics in single API calls

4. **Sample High-Volume Logs**: For very high traffic, consider sampling non-critical logs

5. **Use CloudWatch Insights Efficiently**: Be specific with time ranges and filters

## IAM Permissions Required

```json
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": [
                "logs:CreateLogGroup",
                "logs:CreateLogStream",
                "logs:PutLogEvents",
                "logs:DescribeLogStreams",
                "logs:StartQuery",
                "logs:GetQueryResults"
            ],
            "Resource": "arn:aws:logs:*:*:*"
        },
        {
            "Effect": "Allow",
            "Action": [
                "cloudwatch:PutMetricData",
                "cloudwatch:GetMetricStatistics",
                "cloudwatch:PutMetricAlarm",
                "cloudwatch:DescribeAlarms"
            ],
            "Resource": "*"
        }
    ]
}
```

## Troubleshooting

**Issue**: Logs not appearing in CloudWatch
- Verify IAM permissions
- Check log group and stream names are correct
- Ensure timestamp is in milliseconds since epoch

**Issue**: Metrics not showing up
- Namespace and metric names are case-sensitive
- Metrics can take up to 2 minutes to appear
- Check for throttling errors in responses

**Issue**: High CloudWatch costs
- Review log retention policies
- Implement log sampling for high-volume applications
- Use metric filters instead of Insights queries where possible

## Additional Resources

- [AWS CloudWatch Documentation](https://docs.aws.amazon.com/cloudwatch/)
- [Boto3 CloudWatch Reference](https://boto3.amazonaws.com/v1/documentation/api/latest/reference/services/cloudwatch.html)
- [CloudWatch Logs Insights Query Syntax](https://docs.aws.amazon.com/AmazonCloudWatch/latest/logs/CWL_QuerySyntax.html)
- [Watchtower Library](https://github.com/kislyuk/watchtower) - Python CloudWatch logging handler