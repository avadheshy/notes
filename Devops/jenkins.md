
how to make variable name of the file base on each build like $build_id $version
you can add variable name with  timestamp pulgin >manage jenkins>set timestamp
- publish artifact to s3 bucket
# CI/CD with Jenkins - Django & Java Complete Guide

## Table of Contents
1. [Prerequisites](#prerequisites)
2. [Jenkins Installation and Setup](#jenkins-installation-and-setup)
3. [Jenkins Configuration](#jenkins-configuration)
4. [Django CI/CD Pipeline](#django-cicd-pipeline)
5. [Java CI/CD Pipeline](#java-cicd-pipeline)
6. [Advanced Pipeline Features](#advanced-pipeline-features)
7. [Monitoring and Notifications](#monitoring-and-notifications)
8. [Best Practices](#best-practices)
9. [Troubleshooting](#troubleshooting)

## Prerequisites

### System Requirements
- Linux/macOS/Windows server
- Minimum 2GB RAM (4GB recommended)
- Java 11 or later
- Docker (optional but recommended)
- Git

### Tools and Technologies
- **Django**: Python 3.8+, pip, virtualenv
- **Java**: Maven/Gradle, JDK 11+
- **Testing**: pytest (Django), JUnit (Java)
- **Code Quality**: SonarQube, pylint, checkstyle
- **Deployment**: Docker, Kubernetes, AWS/Azure/GCP

## Jenkins Installation and Setup

### 1. Install Jenkins on Ubuntu/Debian

```bash
# Update system
sudo apt update

# Install Java
sudo apt install openjdk-11-jdk

# Add Jenkins repository
wget -q -O - https://pkg.jenkins.io/debian-stable/jenkins.io.key | sudo apt-key add -
sudo sh -c 'echo deb https://pkg.jenkins.io/debian-stable binary/ > /etc/apt/sources.list.d/jenkins.list'

# Install Jenkins
sudo apt update
sudo apt install jenkins

# Start Jenkins
sudo systemctl start jenkins
sudo systemctl enable jenkins

# Check status
sudo systemctl status jenkins
```

### 2. Initial Jenkins Setup

1. Access Jenkins at `http://your-server:8080`
2. Retrieve initial admin password:
   ```bash
   sudo cat /var/lib/jenkins/secrets/initialAdminPassword
   ```
3. Install suggested plugins
4. Create admin user
5. Configure Jenkins URL

### 3. Install Additional Plugins

Navigate to **Manage Jenkins > Manage Plugins** and install:

**Essential Plugins:**
- Pipeline
- Git
- GitHub Integration
- Docker Pipeline
- Blue Ocean
- SonarQube Scanner

**Django-specific:**
- Python Plugin
- Cobertura Plugin
- Warnings Next Generation

**Java-specific:**
- Maven Integration
- Gradle Plugin
- JUnit Plugin
- Jacoco Plugin

## Jenkins Configuration

### 1. Global Tool Configuration

Go to **Manage Jenkins > Global Tool Configuration**:

**JDK Configuration:**
```
Name: JDK-11
JAVA_HOME: /usr/lib/jvm/java-11-openjdk-amd64
```

**Git Configuration:**
```
Name: Default
Path to Git executable: /usr/bin/git
```

**Maven Configuration:**
```
Name: Maven-3.8.4
Install automatically: ✓
Version: 3.8.4
```

**Python Configuration:**
```
Name: Python-3.9
Install automatically: ✓
Version: 3.9.7
```

### 2. Credentials Setup

Go to **Manage Jenkins > Manage Credentials**:

- **GitHub Token**: For repository access
- **DockerHub**: For container registry
- **AWS/Azure/GCP**: For cloud deployment
- **Database**: For application configuration

### 3. System Configuration

**Environment Variables:**
```
DJANGO_SETTINGS_MODULE=myproject.settings.production
DATABASE_URL=postgresql://user:pass@localhost/dbname
JAVA_OPTS=-Xmx2048m -XX:MaxPermSize=512m
```

## Django CI/CD Pipeline

### 1. Django Project Structure
```
django-project/
├── manage.py
├── requirements.txt
├── requirements-dev.txt
├── Dockerfile
├── docker-compose.yml
├── Jenkinsfile
├── pytest.ini
├── .pylintrc
├── myproject/
│   ├── settings/
│   │   ├── __init__.py
│   │   ├── base.py
│   │   ├── development.py
│   │   ├── production.py
│   │   └── testing.py
│   └── ...
└── tests/
```

### 2. Django Jenkinsfile

```groovy
pipeline {
    agent any
    
    environment {
        DJANGO_SETTINGS_MODULE = 'myproject.settings.testing'
        DATABASE_URL = 'sqlite:///test.db'
        PYTHONPATH = "${WORKSPACE}"
    }
    
    stages {
        stage('Checkout') {
            steps {
                checkout scm
                echo 'Code checked out successfully'
            }
        }
        
        stage('Setup Environment') {
            steps {
                sh '''
                    python3 -m venv venv
                    . venv/bin/activate
                    pip install --upgrade pip
                    pip install -r requirements-dev.txt
                '''
            }
        }
        
        stage('Code Quality Analysis') {
            parallel {
                stage('Linting') {
                    steps {
                        sh '''
                            . venv/bin/activate
                            pylint --output-format=parseable myproject/ > pylint-report.txt || true
                            flake8 myproject/ --output-file=flake8-report.txt || true
                        '''
                        recordIssues enabledForFailure: true, tools: [pyLint(pattern: 'pylint-report.txt'), flake8(pattern: 'flake8-report.txt')]
                    }
                }
                
                stage('Security Scan') {
                    steps {
                        sh '''
                            . venv/bin/activate
                            bandit -r myproject/ -f json -o bandit-report.json || true
                        '''
                        recordIssues enabledForFailure: true, tools: [pyDocStyle(pattern: 'bandit-report.json')]
                    }
                }
            }
        }
        
        stage('Database Migration') {
            steps {
                sh '''
                    . venv/bin/activate
                    python manage.py migrate --settings=myproject.settings.testing
                '''
            }
        }
        
        stage('Unit Tests') {
            steps {
                sh '''
                    . venv/bin/activate
                    pytest --junitxml=test-results.xml --cov=myproject --cov-report=xml --cov-report=html
                '''
            }
            post {
                always {
                    junit 'test-results.xml'
                    publishCoverage adapters: [coberturaAdapter('coverage.xml')], sourceFileResolver: sourceFiles('STORE_ALL_BUILD')
                    publishHTML([
                        allowMissing: false,
                        alwaysLinkToLastBuild: true,
                        keepAll: true,
                        reportDir: 'htmlcov',
                        reportFiles: 'index.html',
                        reportName: 'Coverage Report'
                    ])
                }
            }
        }
        
        stage('Integration Tests') {
            steps {
                sh '''
                    . venv/bin/activate
                    python manage.py test tests.integration --settings=myproject.settings.testing
                '''
            }
        }
        
        stage('Build Docker Image') {
            steps {
                script {
                    def image = docker.build("myproject:${BUILD_NUMBER}")
                    docker.withRegistry('https://registry.hub.docker.com', 'dockerhub-credentials') {
                        image.push()
                        image.push("latest")
                    }
                }
            }
        }
        
        stage('Deploy to Staging') {
            when {
                branch 'develop'
            }
            steps {
                sh '''
                    docker-compose -f docker-compose.staging.yml down
                    docker-compose -f docker-compose.staging.yml up -d
                '''
            }
        }
        
        stage('Deploy to Production') {
            when {
                branch 'main'
            }
            steps {
                input message: 'Deploy to production?', ok: 'Deploy'
                sh '''
                    # Production deployment commands
                    kubectl set image deployment/django-app django-app=myproject:${BUILD_NUMBER}
                    kubectl rollout status deployment/django-app
                '''
            }
        }
    }
    
    post {
        always {
            cleanWs()
        }
        success {
            emailext (
                subject: "SUCCESS: Job '${env.JOB_NAME} [${env.BUILD_NUMBER}]'",
                body: "Good news! The build ${env.BUILD_URL} was successful.",
                to: "${env.CHANGE_AUTHOR_EMAIL}"
            )
        }
        failure {
            emailext (
                subject: "FAILURE: Job '${env.JOB_NAME} [${env.BUILD_NUMBER}]'",
                body: "Bad news! The build ${env.BUILD_URL} failed.",
                to: "${env.CHANGE_AUTHOR_EMAIL}"
            )
        }
    }
}
```

### 3. Django Dockerfile

```dockerfile
FROM python:3.9-slim

WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    gcc \
    postgresql-client \
    && rm -rf /var/lib/apt/lists/*

# Install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy project
COPY . .

# Collect static files
RUN python manage.py collectstatic --noinput --settings=myproject.settings.production

# Create non-root user
RUN useradd --create-home --shell /bin/bash app
RUN chown -R app:app /app
USER app

EXPOSE 8000

CMD ["gunicorn", "--bind", "0.0.0.0:8000", "myproject.wsgi:application"]
```

### 4. Django Testing Configuration

**pytest.ini:**
```ini
[tool:pytest]
DJANGO_SETTINGS_MODULE = myproject.settings.testing
python_files = tests.py test_*.py *_tests.py
addopts = --tb=short --strict-markers
markers =
    slow: marks tests as slow
    integration: marks tests as integration tests
    unit: marks tests as unit tests
```

**requirements-dev.txt:**
```
Django>=4.0.0
pytest-django
pytest-cov
pylint
flake8
bandit
black
isort
factory-boy
```

## Java CI/CD Pipeline

### 1. Java Project Structure (Maven)
```
java-project/
├── pom.xml
├── Dockerfile
├── Jenkinsfile
├── sonar-project.properties
├── src/
│   ├── main/
│   │   └── java/
│   │       └── com/example/
│   └── test/
│       └── java/
│           └── com/example/
└── target/
```

### 2. Java Jenkinsfile (Maven)

```groovy
pipeline {
    agent any
    
    tools {
        maven 'Maven-3.8.4'
        jdk 'JDK-11'
    }
    
    environment {
        SONAR_TOKEN = credentials('sonar-token')
        DOCKER_REGISTRY = 'your-registry.com'
    }
    
    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }
        
        stage('Build') {
            steps {
                sh 'mvn clean compile'
            }
        }
        
        stage('Unit Tests') {
            steps {
                sh 'mvn test'
            }
            post {
                always {
                    junit 'target/surefire-reports/*.xml'
                    publishCoverage adapters: [jacocoAdapter('target/site/jacoco/jacoco.xml')], sourceFileResolver: sourceFiles('STORE_ALL_BUILD')
                }
            }
        }
        
        stage('Code Quality Analysis') {
            parallel {
                stage('SonarQube Analysis') {
                    steps {
                        withSonarQubeEnv('SonarQube') {
                            sh '''
                                mvn sonar:sonar \
                                  -Dsonar.projectKey=java-project \
                                  -Dsonar.host.url=${SONAR_HOST_URL} \
                                  -Dsonar.login=${SONAR_TOKEN}
                            '''
                        }
                    }
                }
                
                stage('Checkstyle') {
                    steps {
                        sh 'mvn checkstyle:checkstyle'
                        recordIssues enabledForFailure: true, tools: [checkStyle(pattern: 'target/checkstyle-result.xml')]
                    }
                }
                
                stage('SpotBugs') {
                    steps {
                        sh 'mvn spotbugs:spotbugs'
                        recordIssues enabledForFailure: true, tools: [spotBugs(pattern: 'target/spotbugsXml.xml')]
                    }
                }
            }
        }
        
        stage('Quality Gate') {
            steps {
                timeout(time: 1, unit: 'HOURS') {
                    waitForQualityGate abortPipeline: true
                }
            }
        }
        
        stage('Integration Tests') {
            steps {
                sh 'mvn failsafe:integration-test failsafe:verify'
            }
            post {
                always {
                    junit 'target/failsafe-reports/*.xml'
                }
            }
        }
        
        stage('Package') {
            steps {
                sh 'mvn package -DskipTests'
                archiveArtifacts artifacts: 'target/*.jar', fingerprint: true
            }
        }
        
        stage('Build Docker Image') {
            steps {
                script {
                    def image = docker.build("java-app:${BUILD_NUMBER}")
                    docker.withRegistry("https://${DOCKER_REGISTRY}", 'docker-registry-credentials') {
                        image.push()
                        image.push("latest")
                    }
                }
            }
        }
        
        stage('Deploy to Staging') {
            when {
                branch 'develop'
            }
            steps {
                sh '''
                    kubectl set image deployment/java-app java-app=java-app:${BUILD_NUMBER} -n staging
                    kubectl rollout status deployment/java-app -n staging
                '''
            }
        }
        
        stage('Deploy to Production') {
            when {
                branch 'main'
            }
            steps {
                input message: 'Deploy to production?', ok: 'Deploy'
                sh '''
                    kubectl set image deployment/java-app java-app=java-app:${BUILD_NUMBER} -n production
                    kubectl rollout status deployment/java-app -n production
                '''
            }
        }
    }
    
    post {
        always {
            cleanWs()
        }
    }
}
```

### 3. Java pom.xml Configuration

```xml
<?xml version="1.0" encoding="UTF-8"?>
<project xmlns="http://maven.apache.org/POM/4.0.0"
         xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
         xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 
         http://maven.apache.org/xsd/maven-4.0.0.xsd">
    <modelVersion>4.0.0</modelVersion>

    <groupId>com.example</groupId>
    <artifactId>java-app</artifactId>
    <version>1.0.0</version>
    <packaging>jar</packaging>

    <properties>
        <maven.compiler.source>11</maven.compiler.source>
        <maven.compiler.target>11</maven.compiler.target>
        <junit.version>5.8.2</junit.version>
        <jacoco.version>0.8.7</jacoco.version>
        <sonar.java.coveragePlugin>jacoco</sonar.java.coveragePlugin>
        <sonar.dynamicAnalysis>reuseReports</sonar.dynamicAnalysis>
        <sonar.jacoco.reportPath>${project.basedir}/../target/jacoco.exec</sonar.jacoco.reportPath>
        <sonar.language>java</sonar.language>
    </properties>

    <dependencies>
        <!-- Spring Boot -->
        <dependency>
            <groupId>org.springframework.boot</groupId>
            <artifactId>spring-boot-starter-web</artifactId>
            <version>2.7.0</version>
        </dependency>
        
        <!-- Testing -->
        <dependency>
            <groupId>org.junit.jupiter</groupId>
            <artifactId>junit-jupiter</artifactId>
            <version>${junit.version}</version>
            <scope>test</scope>
        </dependency>
        
        <dependency>
            <groupId>org.springframework.boot</groupId>
            <artifactId>spring-boot-starter-test</artifactId>
            <version>2.7.0</version>
            <scope>test</scope>
        </dependency>
    </dependencies>

    <build>
        <plugins>
            <!-- Surefire Plugin for Unit Tests -->
            <plugin>
                <groupId>org.apache.maven.plugins</groupId>
                <artifactId>maven-surefire-plugin</artifactId>
                <version>3.0.0-M7</version>
                <configuration>
                    <includes>
                        <include>**/*Test.java</include>
                        <include>**/*Tests.java</include>
                    </includes>
                </configuration>
            </plugin>
            
            <!-- Failsafe Plugin for Integration Tests -->
            <plugin>
                <groupId>org.apache.maven.plugins</groupId>
                <artifactId>maven-failsafe-plugin</artifactId>
                <version>3.0.0-M7</version>
                <configuration>
                    <includes>
                        <include>**/*IT.java</include>
                        <include>**/*IntegrationTest.java</include>
                    </includes>
                </configuration>
                <executions>
                    <execution>
                        <goals>
                            <goal>integration-test</goal>
                            <goal>verify</goal>
                        </goals>
                    </execution>
                </executions>
            </plugin>
            
            <!-- JaCoCo Plugin for Code Coverage -->
            <plugin>
                <groupId>org.jacoco</groupId>
                <artifactId>jacoco-maven-plugin</artifactId>
                <version>${jacoco.version}</version>
                <executions>
                    <execution>
                        <goals>
                            <goal>prepare-agent</goal>
                        </goals>
                    </execution>
                    <execution>
                        <id>report</id>
                        <phase>test</phase>
                        <goals>
                            <goal>report</goal>
                        </goals>
                    </execution>
                </executions>
            </plugin>
            
            <!-- Checkstyle Plugin -->
            <plugin>
                <groupId>org.apache.maven.plugins</groupId>
                <artifactId>maven-checkstyle-plugin</artifactId>
                <version>3.1.2</version>
                <configuration>
                    <configLocation>checkstyle.xml</configLocation>
                    <encoding>UTF-8</encoding>
                    <consoleOutput>true</consoleOutput>
                    <failsOnError>false</failsOnError>
                </configuration>
                <executions>
                    <execution>
                        <id>validate</id>
                        <phase>validate</phase>
                        <goals>
                            <goal>check</goal>
                        </goals>
                    </execution>
                </executions>
            </plugin>
            
            <!-- SpotBugs Plugin -->
            <plugin>
                <groupId>com.github.spotbugs</groupId>
                <artifactId>spotbugs-maven-plugin</artifactId>
                <version>4.7.1.1</version>
                <configuration>
                    <effort>Max</effort>
                    <threshold>Low</threshold>
                    <xmlOutput>true</xmlOutput>
                </configuration>
            </plugin>
        </plugins>
    </build>
</project>
```

### 4. Java Dockerfile

```dockerfile
FROM openjdk:11-jre-slim

WORKDIR /app

# Create app user
RUN groupadd -r app && useradd -r -g app app

# Copy JAR file
COPY target/*.jar app.jar

# Change ownership
RUN chown -R app:app /app

# Switch to app user
USER app

EXPOSE 8080

HEALTHCHECK --interval=30s --timeout=3s --start-period=5s --retries=3 \
    CMD curl -f http://localhost:8080/health || exit 1

CMD ["java", "-jar", "app.jar"]
```

## Advanced Pipeline Features

### 1. Multi-Branch Pipeline Setup

Create a **Multibranch Pipeline** job in Jenkins:

1. **Branch Sources**: Configure GitHub/GitLab
2. **Build Configuration**: Mode: by Jenkinsfile
3. **Scan Repository Triggers**: Periodically scan for changes

### 2. Shared Library for Common Functions

**vars/deployToKubernetes.groovy:**
```groovy
def call(Map config) {
    sh """
        kubectl set image deployment/${config.app} ${config.app}=${config.image} -n ${config.namespace}
        kubectl rollout status deployment/${config.app} -n ${config.namespace}
    """
}
```

**Usage in Jenkinsfile:**
```groovy
deployToKubernetes([
    app: 'my-app',
    image: "my-app:${BUILD_NUMBER}",
    namespace: 'production'
])
```

### 3. Parallel Execution Matrix

```groovy
stage('Cross-Platform Testing') {
    matrix {
        axes {
            axis {
                name 'PLATFORM'
                values 'linux', 'windows', 'macos'
            }
            axis {
                name 'BROWSER'
                values 'chrome', 'firefox', 'safari'
            }
        }
        stages {
            stage('Test') {
                steps {
                    sh "run-tests --platform=${PLATFORM} --browser=${BROWSER}"
                }
            }
        }
    }
}
```

### 4. Blue-Green Deployment Strategy

```groovy
stage('Blue-Green Deployment') {
    steps {
        script {
            def newVersion = "v${BUILD_NUMBER}"
            def oldVersion = sh(script: "kubectl get service myapp -o jsonpath='{.spec.selector.version}'", returnStdout: true).trim()
            
            // Deploy new version
            sh "kubectl set image deployment/myapp-green myapp=myapp:${newVersion}"
            sh "kubectl rollout status deployment/myapp-green"
            
            // Health check
            sh "kubectl exec deployment/myapp-green -- curl -f http://localhost:8080/health"
            
            // Switch traffic
            sh "kubectl patch service myapp -p '{\"spec\":{\"selector\":{\"version\":\"${newVersion}\"}}}'"
            
            // Clean up old version
            sleep 60
            sh "kubectl delete deployment myapp-blue || true"
            sh "kubectl patch deployment myapp-green -p '{\"metadata\":{\"name\":\"myapp-blue\"}}'"
        }
    }
}
```

## Monitoring and Notifications

### 1. Slack Integration

Install **Slack Notification Plugin** and configure:

```groovy
post {
    always {
        slackSend(
            channel: '#ci-cd',
            color: currentBuild.result == 'SUCCESS' ? 'good' : 'danger',
            message: """
                Job: ${env.JOB_NAME}
                Build: ${env.BUILD_NUMBER}
                Status: ${currentBuild.result}
                Duration: ${currentBuild.durationString}
                URL: ${env.BUILD_URL}
            """
        )
    }
}
```

### 2. Email Notifications

```groovy
post {
    failure {
        emailext (
            subject: "FAILED: Job '${env.JOB_NAME} [${env.BUILD_NUMBER}]'",
            body: """
                <h2>Build Failed</h2>
                <p><strong>Job:</strong> ${env.JOB_NAME}</p>
                <p><strong>Build Number:</strong> ${env.BUILD_NUMBER}</p>
                <p><strong>Build URL:</strong> <a href="${env.BUILD_URL}">${env.BUILD_URL}</a></p>
                <p><strong>Console Output:</strong> <a href="${env.BUILD_URL}console">${env.BUILD_URL}console</a></p>
            """,
            mimeType: 'text/html',
            to: "${env.CHANGE_AUTHOR_EMAIL}",
            cc: "devops@company.com"
        )
    }
}
```

### 3. Prometheus Metrics

Install **Prometheus Plugin** for Jenkins metrics:

```groovy
pipeline {
    agent any
    
    stages {
        stage('Metrics') {
            steps {
                script {
                    // Custom metrics
                    publishMetrics([
                        metric('build_duration_seconds', currentBuild.duration / 1000),
                        metric('test_count', env.TEST_COUNT as Integer),
                        metric('coverage_percentage', env.COVERAGE as Float)
                    ])
                }
            }
        }
    }
}
```

## Best Practices

### 1. Security Best Practices

- **Credentials Management**: Use Jenkins credentials store
- **Least Privilege**: Limit Jenkins user permissions
- **Secrets Scanning**: Use tools like GitLeaks, TruffleHog
- **Container Security**: Scan images with tools like Trivy, Clair
- **Network Security**: Use VPNs, private networks for deployment

### 2. Performance Optimization

- **Parallel Execution**: Run independent stages in parallel
- **Agent Distribution**: Use multiple Jenkins agents
- **Caching**: Cache dependencies (Maven repo, pip cache)
- **Incremental Builds**: Build only changed modules
- **Resource Limits**: Set appropriate CPU/memory limits

### 3. Code Quality Gates

```groovy
stage('Quality Gate') {
    steps {
        script {
            def qualityGate = [
                'coverage': 80,
                'duplicated_lines_density': 5,
                'bugs': 0,
                'vulnerabilities': 0,
                'security_hotspots': 0
            ]
            
            qualityGate.each { metric, threshold ->
                def value = getMetricValue(metric)
                if (metric == 'coverage' && value < threshold) {
                    error("Code coverage ${value}% is below threshold ${threshold}%")
                }
                if (metric != 'coverage' && value > threshold) {
                    error("${metric} count ${value} exceeds threshold ${threshold}")
                }
            }
        }
    }
}
```

### 4. Environment Management

```groovy
pipeline {
    agent any
    
    parameters {
        choice(
            name: 'ENVIRONMENT',
            choices: ['development', 'staging', 'production'],
            description: 'Select deployment environment'
        )
        booleanParam(
            name: 'SKIP_TESTS',
            defaultValue: false,
            description: 'Skip test execution'
        )
    }
    
    environment {
        DATABASE_URL = credentials("db-url-${params.ENVIRONMENT}")
        API_KEY = credentials("api-key-${params.ENVIRONMENT}")
    }
}
```

### 5. Artifact Management

```groovy
stage('Artifact Management') {
    steps {
        // Version artifacts
        sh "cp target/app.jar target/app-${BUILD_NUMBER}.jar"
        
        // Upload to artifact repository
        nexusArtifactUploader(
            nexusVersion: 'nexus3',
            protocol: 'http',
            nexusUrl: 'nexus.company.com:8081',
            groupId: 'com.company',
            version: "${BUILD_NUMBER}",
            repository: 'maven-releases',
            credentialsId: 'nexus-credentials',
            artifacts: [
                [artifactId: 'myapp',
                 classifier: '',
                 file: "target/app-${BUILD_NUMBER}.jar",
                 type: 'jar']
            ]
        )
    }
}
```

## Troubleshooting

### 1. Common Issues

**Issue: Out of Memory Errors**
```bash
# Solution: Increase Jenkins heap size
sudo systemctl edit jenkins

[Service]
Environment="JAVA_OPTS=-Xms512m -Xmx2048m"
```

**Issue: Permission Denied**
```bash
# Solution: Add Jenkins user to docker group
sudo usermod -aG docker jenkins
sudo systemctl restart jenkins
```

**Issue: Build Fails on Agent**
```groovy
// Solution: Specify node requirements
pipeline {
    agent {
        label 'linux && docker'
    }
}
```

### 2. Debug Techniques

```groovy
stage('Debug') {
    steps {
        sh 'env | sort'  // Print all environment variables
        sh 'pwd && ls -la'  // Show current directory
        sh 'docker ps'  // Show running containers
        sh 'kubectl get pods -n ${NAMESPACE}'  // Show Kubernetes pods
    }
}
```

### 3. Pipeline Optimization

```groovy
// Use stash/unstash for file transfer between agents
stage('Build') {
    agent { label 'build-agent' }
    steps {
        sh 'mvn package'
        stash includes: 'target/*.jar', name: 'app-jar'
    }
}

stage('Deploy') {
    agent { label 'deploy-agent' }
    steps {
        unstash 'app-jar'
        sh 'docker build -t myapp .'
    }
}
```

### 4. Monitoring Pipeline Health

```groovy
pipeline {
    agent any
    
    options {
        timeout(time: 1, unit: 'HOURS')
        retry(3)
        timestamps()
    }
    
    stages {
        stage('Health Check') {
            steps {
                script {
                    try {
                        sh 'curl -f http://localhost:8080/health'
                    } catch (Exception e) {
                        currentBuild.result = 'UNSTABLE'
                        error("Health check failed: ${e.getMessage()}")
                    }
                }
            }
        }
    }
}
```

---

This comprehensive guide covers CI/CD implementation with Jenkins for both Django and Java projects. Customize the configurations based on your specific requirements and infrastructure setup.

# Jenkins ↔ SonarQube Integration (Different Servers)

## 1️⃣ Prerequisites
- **Jenkins Server**
  - Jenkins installed and running.
  - SonarQube Scanner plugin installed.
- **SonarQube Server**
  - SonarQube installed and running.
  - Accessible from the Jenkins server (network connectivity open on port 9000 or custom port).

---

## 2️⃣ SonarQube Server Setup

### Step 1: Install & Start SonarQube
1. Download from: [SonarQube Downloads](https://www.sonarsource.com/products/sonarqube/downloads/)
2. Extract and start:
   ```bash
   cd sonarqube-x.x.x/bin/linux-x86-64
   ./sonar.sh start
Access in browser:

cpp
Copy
Edit
http://<SONARQUBE_SERVER_IP>:9000
Default login:

pgsql
Copy
Edit
Username: admin
Password: admin
Step 2: Generate Authentication Token
Login to SonarQube.

Navigate: My Account → Security.

Generate a token (e.g., jenkins-token).

Save this token — will be added in Jenkins.

3️⃣ Jenkins Server Setup
Step 1: Install SonarQube Scanner Plugin
Go to Manage Jenkins → Plugins → Available.

Search for SonarQube Scanner → Install.

Step 2: Configure SonarQube Server in Jenkins
Go to Manage Jenkins → System.

Find SonarQube servers → Add SonarQube:

Name: SonarQubeServer

Server URL: http://<SONARQUBE_SERVER_IP>:9000

Server authentication token:

Add Credential → Type: Secret text → Value: <Generated Token>

Select this credential.

Save.

Step 3: Configure SonarQube Scanner in Jenkins
Go to Manage Jenkins → Tools → SonarQube Scanner.

Click Add SonarQube Scanner:

Name: SonarScanner

Install automatically OR provide a local installation path.

Save.

4️⃣ Jenkins Pipeline Example
groovy
Copy
Edit
pipeline {
    agent any
    tools {
        sonarQubeScanner 'SonarScanner' // Name from Tools config
    }
    environment {
        SONAR_AUTH_TOKEN = credentials('sonarqube-token-id') // ID from Jenkins credentials
    }
    stages {
        stage('Checkout') {
            steps {
                git url: 'https://github.com/your/repo.git', branch: 'main'
            }
        }
        stage('SonarQube Analysis') {
            steps {
                withSonarQubeEnv('SonarQubeServer') { // Name from System config
                    sh """
                        sonar-scanner \
                        -Dsonar.projectKey=MyProjectKey \
                        -Dsonar.sources=. \
                        -Dsonar.host.url=http://<SONARQUBE_SERVER_IP>:9000 \
                        -Dsonar.login=$SONAR_AUTH_TOKEN
                    """
                }
            }
        }
        stage('Quality Gate') {
            steps {
                timeout(time: 1, unit: 'HOURS') {
                    waitForQualityGate abortPipeline: true
                }
            }
        }
    }
}
5️⃣ Quality Gate Webhook (Optional)
To allow Jenkins to get instant Quality Gate results:

In SonarQube:

Go to Administration → Configuration → Webhooks → Create.

Name: Jenkins

URL:

arduino
Copy
Edit
http://<JENKINS_SERVER_IP>:8080/sonarqube-webhook/
Save.

6️⃣ Network Notes
Ensure SonarQube’s port (9000 by default) is open for inbound traffic from the Jenkins server.

Ensure Jenkins’s port (8080 default) is open for inbound traffic from the SonarQube server (if using webhooks).