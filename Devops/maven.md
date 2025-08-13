# Maven Build Tool - Complete Guide

## Table of Contents
1. [What is Maven?](#what-is-maven)
2. [Build Process Overview](#build-process-overview)
3. [Maven Build Lifecycle](#maven-build-lifecycle)
4. [Installation Guide](#installation-guide)
5. [Maven Project Structure](#maven-project-structure)
6. [POM.xml Configuration](#pomxml-configuration)
7. [Common Maven Commands](#common-maven-commands)
8. [Best Practices](#best-practices)
9. [Troubleshooting](#troubleshooting)

## What is Maven?

**Apache Maven** is a powerful build automation and project management tool primarily used for Java projects. It simplifies and standardizes the build process by providing:

- **Dependency Management**: Automatically downloads and manages project dependencies
- **Build Automation**: Automates compilation, testing, packaging, and deployment
- **Project Standardization**: Enforces a standard project structure and naming conventions
- **Integration**: Works seamlessly with IDEs and CI/CD pipelines

### Why Use Maven?
- Simplifies dependency management
- Standardizes project structure
- Automates repetitive build tasks
- Integrates with popular IDEs
- Supports multi-module projects
- Extensive plugin ecosystem

## Build Process Overview

The typical build process involves these stages:

```
Source Code → Compile → Test → Package → Health Check → Deploy
```

### Build Tools Comparison
| Tool | Language | Description |
|------|----------|-------------|
| **Maven** | Java | Declarative, XML-based, dependency management |
| **Gradle** | Java/Groovy | Flexible, script-based, faster builds |
| **Ant** | Java | Procedural, XML-based, highly customizable |
| **Make** | C/C++ | Traditional Unix build tool |
| **MSBuild** | .NET | Microsoft's build platform |
| **NAnt** | .NET | .NET build tool similar to Ant |

## Maven Build Lifecycle

Maven follows a well-defined build lifecycle with the following **default phases**:

### 1. **validate**
- **Purpose**: Validates that the project is correct and all necessary information is available
- **Tasks**: 
  - Checks project structure
  - Validates POM.xml syntax
  - Ensures required properties are set

### 2. **compile**
- **Purpose**: Compiles the source code of the project
- **Tasks**:
  - Compiles Java source files from `src/main/java`
  - Processes resources from `src/main/resources`
  - Generates compiled classes in `target/classes`

### 3. **test**
- **Purpose**: Tests the compiled source code using suitable unit testing frameworks
- **Requirements**: Tests should not require the code to be packaged or deployed
- **Tasks**:
  - Compiles test sources from `src/test/java`
  - Runs unit tests (JUnit, TestNG, etc.)
  - Generates test reports

### 4. **package**
- **Purpose**: Takes the compiled code and packages it in distributable format
- **Common Formats**:
  - **JAR** (Java Archive) - for libraries and applications
  - **WAR** (Web Archive) - for web applications
  - **EAR** (Enterprise Archive) - for enterprise applications

### 5. **integration-test**
- **Purpose**: Processes and deploys the package for integration testing
- **Tasks**:
  - Deploys application to test environment
  - Runs integration tests
  - Tests interaction between components

### 6. **verify**
- **Purpose**: Runs checks on integration test results to ensure quality criteria are met
- **Tasks**:
  - Code coverage analysis
  - Static code analysis
  - Quality gate validation

### 7. **install**
- **Purpose**: Installs the package into local repository
- **Use Case**: Makes the artifact available as a dependency for other local projects
- **Location**: `~/.m2/repository`

### 8. **deploy**
- **Purpose**: Copies the final package to remote repository
- **Environment**: Typically done in build/CI environment
- **Use Case**: Shares artifacts with other developers and projects

## Installation Guide

### Prerequisites
- **JDK 8 or higher** (JDK 21 recommended for latest features)
- **Operating System**: Windows, macOS, or Linux

### Step 1: Install JDK 21

#### Windows
```powershell
# Using Chocolatey
choco install openjdk21

# Or download from Oracle/OpenJDK official website
```

#### macOS
```bash
# Using Homebrew
brew install openjdk@21

# Add to PATH
echo 'export PATH="/opt/homebrew/opt/openjdk@21/bin:$PATH"' >> ~/.zshrc
```

#### Linux (Ubuntu/Debian)
```bash
sudo apt update
sudo apt install openjdk-21-jdk

# Verify installation
java -version
javac -version
```

### Step 2: Install Maven

#### Windows
```powershell
# Using Chocolatey
choco install maven

# Or download from Apache Maven website
# Extract to C:\Program Files\Apache\maven
# Add to PATH: C:\Program Files\Apache\maven\bin
```

#### macOS
```bash
# Using Homebrew
brew install maven
```

#### Linux (Ubuntu/Debian)
```bash
sudo apt update
sudo apt install maven
```

### Step 3: Verify Installation
```bash
mvn -version
```

Expected output:
```
Apache Maven 3.9.x
Maven home: /usr/share/maven
Java version: 21.0.x
Java home: /usr/lib/jvm/java-21-openjdk
```

## Maven Project Structure

Maven enforces a standard directory structure:

```
my-project/
├── pom.xml                    # Project Object Model file
├── src/
│   ├── main/
│   │   ├── java/             # Main source code
│   │   └── resources/        # Main resources (config files, etc.)
│   └── test/
│       ├── java/             # Test source code
│       └── resources/        # Test resources
├── target/                   # Generated files (compiled classes, JARs, etc.)
├── .gitignore
└── README.md
```

### Key Directories
- **`src/main/java`**: Contains main application source code
- **`src/main/resources`**: Contains configuration files, properties, etc.
- **`src/test/java`**: Contains unit and integration test code
- **`src/test/resources`**: Contains test-specific resources
- **`target/`**: Contains all generated files (auto-created)

## POM.xml Configuration

The **Project Object Model (POM)** file is Maven's core configuration file:

```xml
<?xml version="1.0" encoding="UTF-8"?>
<project xmlns="http://maven.apache.org/POM/4.0.0"
         xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
         xsi:schemaLocation="http://maven.apache.org/POM/4.0.0 
         http://maven.apache.org/xsd/maven-4.0.0.xsd">
    
    <modelVersion>4.0.0</modelVersion>
    
    <!-- Project Coordinates -->
    <groupId>com.example</groupId>
    <artifactId>my-app</artifactId>
    <version>1.0.0-SNAPSHOT</version>
    <packaging>jar</packaging>
    
    <!-- Project Information -->
    <name>My Application</name>
    <description>A sample Maven project</description>
    <url>https://github.com/user/my-app</url>
    
    <!-- Properties -->
    <properties>
        <maven.compiler.source>21</maven.compiler.source>
        <maven.compiler.target>21</maven.compiler.target>
        <project.build.sourceEncoding>UTF-8</project.build.sourceEncoding>
        <junit.version>5.9.2</junit.version>
    </properties>
    
    <!-- Dependencies -->
    <dependencies>
        <!-- JUnit 5 for testing -->
        <dependency>
            <groupId>org.junit.jupiter</groupId>
            <artifactId>junit-jupiter</artifactId>
            <version>${junit.version}</version>
            <scope>test</scope>
        </dependency>
        
        <!-- Example: Spring Boot Starter -->
        <dependency>
            <groupId>org.springframework.boot</groupId>
            <artifactId>spring-boot-starter</artifactId>
            <version>3.1.0</version>
        </dependency>
    </dependencies>
    
    <!-- Build Configuration -->
    <build>
        <plugins>
            <!-- Maven Compiler Plugin -->
            <plugin>
                <groupId>org.apache.maven.plugins</groupId>
                <artifactId>maven-compiler-plugin</artifactId>
                <version>3.11.0</version>
                <configuration>
                    <source>21</source>
                    <target>21</target>
                </configuration>
            </plugin>
            
            <!-- Maven Surefire Plugin for testing -->
            <plugin>
                <groupId>org.apache.maven.plugins</groupId>
                <artifactId>maven-surefire-plugin</artifactId>
                <version>3.0.0</version>
            </plugin>
        </plugins>
    </build>
</project>
```

### Key POM Elements
- **`groupId`**: Organization or group identifier
- **`artifactId`**: Project name/identifier
- **`version`**: Project version
- **`packaging`**: Output format (jar, war, ear, pom)
- **`dependencies`**: External libraries required
- **`plugins`**: Build tools and their configurations

## Common Maven Commands

### Basic Commands

#### Build the Project
```bash
mvn clean compile
```
- `clean`: Removes the `target` directory
- `compile`: Compiles the main source code

#### Run Tests
```bash
mvn test
```
- Compiles and runs all unit tests
- Generates test reports in `target/surefire-reports`

#### Package the Application
```bash
mvn package
```
- Runs compile and test phases
- Creates JAR/WAR file in `target` directory

#### Install to Local Repository
```bash
mvn install
```
- Runs all phases up to install
- Copies artifact to local repository (`~/.m2/repository`)

#### Clean Build
```bash
mvn clean install
```
- Removes previous build artifacts
- Performs complete build and install

### Advanced Commands

#### Skip Tests
```bash
mvn install -DskipTests
mvn install -Dmaven.test.skip=true
```

#### Run Specific Test Class
```bash
mvn test -Dtest=MyTestClass
```

#### Generate Project from Archetype
```bash
mvn archetype:generate \
    -DgroupId=com.example \
    -DartifactId=my-app \
    -DarchetypeArtifactId=maven-archetype-quickstart \
    -DinteractiveMode=false
```

#### Dependency Analysis
```bash
mvn dependency:tree          # Show dependency tree
mvn dependency:analyze       # Analyze dependencies
mvn dependency:resolve       # Download dependencies
```

#### Run Application
```bash
mvn exec:java -Dexec.mainClass="com.example.Main"
```

### Lifecycle Commands
```bash
mvn validate        # Validate project
mvn compile         # Compile source code
mvn test           # Run tests
mvn package        # Create JAR/WAR
mvn verify         # Run integration tests
mvn install        # Install to local repo
mvn deploy         # Deploy to remote repo
```

## Best Practices

### 1. Project Structure
- Follow Maven's standard directory layout
- Keep source and test code separate
- Use meaningful package names

### 2. POM.xml Management
```xml
<!-- Use properties for version management -->
<properties>
    <spring.version>5.3.21</spring.version>
    <junit.version>5.9.2</junit.version>
</properties>

<!-- Use dependency management for multi-module projects -->
<dependencyManagement>
    <dependencies>
        <dependency>
            <groupId>org.springframework</groupId>
            <artifactId>spring-bom</artifactId>
            <version>${spring.version}</version>
            <type>pom</type>
            <scope>import</scope>
        </dependency>
    </dependencies>
</dependencyManagement>
```

### 3. Dependency Management
- Use specific versions instead of LATEST or RELEASE
- Regularly update dependencies for security patches
- Use `dependencyManagement` for version consistency
- Exclude transitive dependencies when needed

### 4. Testing
- Write unit tests for all business logic
- Use appropriate test scopes (`test`, `provided`)
- Configure test plugins properly
- Maintain good test coverage

### 5. Build Configuration
```xml
<build>
    <finalName>${project.artifactId}-${project.version}</finalName>
    
    <plugins>
        <!-- Ensure Java version consistency -->
        <plugin>
            <groupId>org.apache.maven.plugins</groupId>
            <artifactId>maven-compiler-plugin</artifactId>
            <version>3.11.0</version>
            <configuration>
                <source>21</source>
                <target>21</target>
                <encoding>UTF-8</encoding>
            </configuration>
        </plugin>
    </plugins>
</build>
```

## Troubleshooting

### Common Issues and Solutions

#### 1. Java Version Mismatch
**Problem**: "Unsupported class file major version"
**Solution**:
```bash
# Check Java version
java -version
javac -version

# Update POM.xml
<properties>
    <maven.compiler.source>21</maven.compiler.source>
    <maven.compiler.target>21</maven.compiler.target>
</properties>
```

#### 2. Dependency Resolution Failures
**Problem**: "Could not resolve dependencies"
**Solutions**:
```bash
# Clear local repository cache
rm -rf ~/.m2/repository

# Force update dependencies
mvn clean install -U

# Check dependency tree for conflicts
mvn dependency:tree
```

#### 3. Test Failures
**Problem**: Tests fail during build
**Solutions**:
```bash
# Run tests with detailed output
mvn test -X

# Skip tests temporarily
mvn install -DskipTests

# Run specific test
mvn test -Dtest=MyTestClass#myTestMethod
```

#### 4. Memory Issues
**Problem**: OutOfMemoryError during build
**Solution**:
```bash
# Set Maven options
export MAVEN_OPTS="-Xmx2048m -XX:MaxPermSize=256m"
```

#### 5. Plugin Version Conflicts
**Problem**: Plugin compatibility issues
**Solution**:
```xml
<pluginManagement>
    <plugins>
        <plugin>
            <groupId>org.apache.maven.plugins</groupId>
            <artifactId>maven-compiler-plugin</artifactId>
            <version>3.11.0</version>
        </plugin>
    </plugins>
</pluginManagement>
```

### Useful Debug Commands
```bash
mvn help:effective-pom      # Show effective POM
mvn help:active-profiles    # Show active profiles
mvn dependency:analyze      # Analyze dependencies
mvn versions:display-dependency-updates  # Check for updates
```

## Conclusion

Maven is an essential tool for Java development that standardizes project structure, automates builds, and simplifies dependency management. By following the lifecycle phases and best practices outlined in this guide, you can efficiently manage Java projects of any size.

For more advanced topics, explore:
- Multi-module projects
- Custom plugins
- Profiles for different environments
- Integration with CI/CD pipelines
- Maven repositories and artifact management

---

*This guide covers Maven fundamentals. For the latest features and updates, refer to the [official Apache Maven documentation](https://maven.apache.org/).*