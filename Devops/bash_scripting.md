# Bash Scripting - Complete Guide

## Table of Contents
1. [Introduction to Bash Scripting](#introduction-to-bash-scripting)
2. [Basic Syntax](#basic-syntax)
3. [Variables](#variables)
4. [Command Line Arguments](#command-line-arguments)
5. [System Variables](#system-variables)
6. [Quotes and Special Characters](#quotes-and-special-characters)
7. [Command Substitution](#command-substitution)
8. [Variable Export and Environment](#variable-export-and-environment)
9. [User Input](#user-input)
10. [Decision Making](#decision-making)
11. [Loops](#loops)
12. [Functions](#functions)
13. [File Operations](#file-operations)
14. [String Operations](#string-operations)
15. [Arrays](#arrays)
16. [Error Handling](#error-handling)
17. [Process Management](#process-management)
18. [Monitoring and Automation](#monitoring-and-automation)
19. [Remote Execution](#remote-execution)
20. [Best Practices](#best-practices)
21. [Common Use Cases](#common-use-cases)

## Introduction to Bash Scripting

**Bash** (Bourne Again Shell) is a command-line interpreter and scripting language for Unix/Linux systems. It allows you to automate tasks, manage systems, and create powerful scripts for various purposes.

### Why Use Bash Scripts?
- Automate repetitive tasks
- System administration and monitoring
- Deployment automation
- Log processing and analysis
- File management operations
- System configuration

## Basic Syntax

### Shebang (#!)
```bash
#!/bin/bash
```
- The **shebang** (`#!`) tells the system which interpreter to use
- Must be the first line of the script
- Makes the script executable directly

### Comments
```bash
# This is a single-line comment

: '
This is a 
multi-line comment
block
'
```

### Basic Output
```bash
#!/bin/bash
echo "Hello, World!"
echo "Current date: $(date)"
printf "Formatted output: %s\n" "Hello"
```

### Making Scripts Executable
```bash
chmod +x script.sh
./script.sh
```

## Variables

### Variable Declaration and Usage
```bash
#!/bin/bash

# Variable assignment (no spaces around =)
name="John"
age=25
pi=3.14159

# Accessing variables
echo "Name: $name"
echo "Age: ${age}"
echo "Pi value: $pi"

# Read-only variables
readonly DATABASE_URL="localhost:5432"
```

### Variable Naming Rules
- Must start with letter or underscore
- Can contain letters, numbers, and underscores
- Case-sensitive
- No spaces around the `=` operator

### Local vs Global Variables
```bash
#!/bin/bash

global_var="I'm global"

function my_function() {
    local local_var="I'm local"
    echo "Inside function: $local_var"
    echo "Inside function: $global_var"
}

my_function
echo "Outside function: $global_var"
# echo "Outside function: $local_var"  # This would cause an error
```

## Command Line Arguments

```bash
#!/bin/bash

echo "Script name: $0"
echo "First argument: $1"
echo "Second argument: $2"
echo "All arguments: $@"
echo "Number of arguments: $#"
echo "Process ID: $$"

# Check if arguments are provided
if [ $# -eq 0 ]; then
    echo "Usage: $0 <arg1> <arg2> ..."
    exit 1
fi
```

### Special Parameters
| Parameter | Description |
|-----------|-------------|
| `$0` | Script name |
| `$1-$9` | Command line arguments |
| `$#` | Number of arguments |
| `$@` | All arguments as separate strings |
| `$*` | All arguments as single string |
| `$$` | Process ID of current shell |
| `$!` | Process ID of last background command |

## System Variables

```bash
#!/bin/bash

# Exit code of last command
echo "Exit code: $?"

# Current user
echo "Current user: $USER"

# Hostname
echo "Hostname: $HOSTNAME"

# Home directory
echo "Home directory: $HOME"

# Current working directory
echo "Current directory: $PWD"

# Random number (0-32767)
echo "Random number: $RANDOM"

# Path variable
echo "PATH: $PATH"

# Shell being used
echo "Shell: $SHELL"
```

### Important Environment Variables
| Variable | Description |
|----------|-------------|
| `$HOME` | User's home directory |
| `$PATH` | Executable search path |
| `$PWD` | Present working directory |
| `$USER` | Current username |
| `$SHELL` | Current shell |
| `$HOSTNAME` | System hostname |
| `$RANDOM` | Random number generator |
| `$LINENO` | Current line number in script |

## Quotes and Special Characters

### Single Quotes (')
```bash
#!/bin/bash
name="World"
echo 'Hello $name'  # Output: Hello $name (literal)
```

### Double Quotes (")
```bash
#!/bin/bash
name="World"
echo "Hello $name"  # Output: Hello World (variable expanded)
echo "Today is $(date)"  # Command substitution works
echo "Random: $RANDOM"
```

### Escaping Special Characters
```bash
#!/bin/bash
echo "Price: \$100"  # Output: Price: $100
echo "Quote: \"Hello\""  # Output: Quote: "Hello"
echo "Backslash: \\"  # Output: Backslash: \
```

## Command Substitution

```bash
#!/bin/bash

# Using backticks (older syntax)
current_date=`date`
echo "Date: $current_date"

# Using $() (preferred syntax)
current_user=$(whoami)
echo "Current user: $current_user"

# More complex examples
file_count=$(ls -1 | wc -l)
echo "Files in current directory: $file_count"

# Nested command substitution
today=$(date +%Y-%m-%d)
backup_file="backup_${today}.tar.gz"
echo "Backup file: $backup_file"
```

## Variable Export and Environment

### Exporting Variables
```bash
#!/bin/bash

# Local variable (only in current shell)
local_var="I'm local"

# Export variable to child processes
export GLOBAL_VAR="I'm exported"

# Alternative syntax
declare -x ANOTHER_VAR="Also exported"

# Run a child script that can access GLOBAL_VAR
bash child_script.sh
```

### Configuration Files

#### User-specific: ~/.bashrc
```bash
# Add to ~/.bashrc for user-specific variables
export MY_APP_PATH="/opt/myapp"
export DATABASE_URL="localhost:5432"

# Custom aliases
alias ll='ls -la'
alias grep='grep --color=auto'

# Custom functions
mkcd() {
    mkdir -p "$1" && cd "$1"
}
```

#### System-wide: /etc/profile
```bash
# Add to /etc/profile for all users
export JAVA_HOME="/usr/lib/jvm/java-11-openjdk"
export PATH="$PATH:$JAVA_HOME/bin"
```

### Loading Configuration
```bash
# Reload .bashrc
source ~/.bashrc
# or
. ~/.bashrc
```

## User Input

```bash
#!/bin/bash

# Basic input
echo "Enter your name:"
read name
echo "Hello, $name!"

# Input with prompt
read -p "Enter your age: " age
echo "You are $age years old"

# Silent input (for passwords)
read -sp "Enter password: " password
echo
echo "Password length: ${#password}"

# Input with timeout
if read -t 5 -p "Enter something (5 seconds): " input; then
    echo "You entered: $input"
else
    echo "Timeout!"
fi

# Reading multiple values
read -p "Enter first and last name: " first last
echo "First: $first, Last: $last"
```

## Decision Making

### if-elif-else
```bash
#!/bin/bash

read -p "Enter a number: " num

if [ $num -gt 10 ]; then
    echo "Number is greater than 10"
elif [ $num -eq 10 ]; then
    echo "Number is exactly 10"
elif [ $num -eq 0 ]; then
    echo "Number is zero"
else
    echo "Number is less than 10"
fi
```

### Comparison Operators

#### Numeric Comparisons
| Operator | Description |
|----------|-------------|
| `-eq` | Equal to |
| `-ne` | Not equal to |
| `-gt` | Greater than |
| `-ge` | Greater than or equal |
| `-lt` | Less than |
| `-le` | Less than or equal |

#### String Comparisons
```bash
#!/bin/bash

string1="hello"
string2="world"

if [ "$string1" = "$string2" ]; then
    echo "Strings are equal"
elif [ "$string1" != "$string2" ]; then
    echo "Strings are not equal"
fi

# Check if string is empty
if [ -z "$string1" ]; then
    echo "String is empty"
fi

# Check if string is not empty
if [ -n "$string1" ]; then
    echo "String is not empty"
fi
```

#### File Test Operators
```bash
#!/bin/bash

file="example.txt"

if [ -f "$file" ]; then
    echo "$file is a regular file"
fi

if [ -d "$file" ]; then
    echo "$file is a directory"
fi

if [ -r "$file" ]; then
    echo "$file is readable"
fi

if [ -w "$file" ]; then
    echo "$file is writable"
fi

if [ -x "$file" ]; then
    echo "$file is executable"
fi
```

### case Statement
```bash
#!/bin/bash

read -p "Enter your choice (1-3): " choice

case $choice in
    1)
        echo "You chose option 1"
        ;;
    2)
        echo "You chose option 2"
        ;;
    3)
        echo "You chose option 3"
        ;;
    *)
        echo "Invalid choice"
        ;;
esac
```

## Loops

### for Loop
```bash
#!/bin/bash

# Loop through list of items
for lang in java python php dotnet c cpp; do
    echo "Learning $lang"
done

# Loop through range
for i in {1..5}; do
    echo "Iteration: $i"
done

# C-style for loop
for ((i=1; i<=10; i++)); do
    echo "Counter: $i"
done

# Loop through files
for file in *.txt; do
    if [ -f "$file" ]; then
        echo "Processing: $file"
    fi
done

# Loop through command output
for user in $(cat /etc/passwd | cut -d: -f1); do
    echo "User: $user"
done
```

### while Loop
```bash
#!/bin/bash

counter=0
while [ $counter -lt 5 ]; do
    echo "Counter value: $counter"
    counter=$((counter + 1))
done

# Reading file line by line
while IFS= read -r line; do
    echo "Line: $line"
done < "input.txt"

# Infinite loop with break
while true; do
    read -p "Enter 'quit' to exit: " input
    if [ "$input" = "quit" ]; then
        break
    fi
    echo "You entered: $input"
done
```

### until Loop
```bash
#!/bin/bash

counter=0
until [ $counter -ge 5 ]; do
    echo "Counter: $counter"
    counter=$((counter + 1))
done
```

## Functions

```bash
#!/bin/bash

# Simple function
greet() {
    echo "Hello, World!"
}

# Function with parameters
greet_user() {
    local name=$1
    local age=$2
    echo "Hello, $name! You are $age years old."
}

# Function with return value
add_numbers() {
    local num1=$1
    local num2=$2
    local result=$((num1 + num2))
    echo $result  # Return via echo
}

# Function that returns exit code
check_file() {
    local filename=$1
    if [ -f "$filename" ]; then
        return 0  # Success
    else
        return 1  # Failure
    fi
}

# Using functions
greet
greet_user "Alice" 25

sum=$(add_numbers 10 20)
echo "Sum: $sum"

if check_file "example.txt"; then
    echo "File exists"
else
    echo "File not found"
fi
```

## File Operations

```bash
#!/bin/bash

# Create file
touch newfile.txt
echo "Content" > newfile.txt

# Append to file
echo "More content" >> newfile.txt

# Read file
while IFS= read -r line; do
    echo "Line: $line"
done < newfile.txt

# Copy file
cp source.txt destination.txt

# Move/rename file
mv oldname.txt newname.txt

# Delete file
rm unwanted.txt

# Create directory
mkdir -p /path/to/directory

# Check file properties
file="example.txt"
if [ -f "$file" ]; then
    echo "File size: $(stat -c%s "$file") bytes"
    echo "Last modified: $(stat -c%y "$file")"
fi

# Find files
find . -name "*.txt" -type f
find . -mtime -1  # Files modified in last 24 hours
```

## String Operations

```bash
#!/bin/bash

text="Hello World"

# String length
echo "Length: ${#text}"

# Substring
echo "Substring: ${text:6:5}"  # Starting at position 6, length 5

# Replace
echo "Replace: ${text/World/Universe}"  # Replace first occurrence
echo "Replace all: ${text//o/0}"        # Replace all occurrences

# Case conversion
echo "Uppercase: ${text^^}"
echo "Lowercase: ${text,,}"

# Remove prefix/suffix
filename="document.pdf"
echo "Without extension: ${filename%.pdf}"

path="/home/user/documents/file.txt"
echo "Filename only: ${path##*/}"
echo "Directory only: ${path%/*}"
```

## Arrays

```bash
#!/bin/bash

# Declare array
languages=("bash" "python" "java" "javascript")

# Add element
languages+=("go")

# Access elements
echo "First language: ${languages[0]}"
echo "All languages: ${languages[@]}"
echo "Array length: ${#languages[@]}"

# Loop through array
for lang in "${languages[@]}"; do
    echo "Language: $lang"
done

# Associative arrays (Bash 4+)
declare -A person
person[name]="John"
person[age]=30
person[city]="New York"

echo "Name: ${person[name]}"
echo "All keys: ${!person[@]}"
echo "All values: ${person[@]}"
```

## Error Handling

```bash
#!/bin/bash

# Exit on any error
set -e

# Exit on undefined variables
set -u

# Show commands being executed
set -x

# Custom error handling
handle_error() {
    echo "Error occurred in script at line $1"
    exit 1
}

# Trap errors
trap 'handle_error $LINENO' ERR

# Check command success
if ! command -v git > /dev/null; then
    echo "Git is not installed"
    exit 1
fi

# Try-catch equivalent
{
    # Commands that might fail
    risky_command
} || {
    echo "Command failed, but continuing..."
}

# Check exit codes
cp file1.txt file2.txt
if [ $? -eq 0 ]; then
    echo "File copied successfully"
else
    echo "Failed to copy file"
    exit 1
fi
```

## Process Management

```bash
#!/bin/bash

# Run command in background
long_running_command &
bg_pid=$!

echo "Background process PID: $bg_pid"

# Check if process is running
if ps -p $bg_pid > /dev/null; then
    echo "Process is running"
fi

# Wait for background process
wait $bg_pid
echo "Background process completed"

# Kill process
# kill $bg_pid

# Get process information
ps aux | grep bash
pgrep -f "my_script.sh"

# Monitor system resources
echo "CPU usage:"
top -bn1 | grep "Cpu(s)"

echo "Memory usage:"
free -h

echo "Disk usage:"
df -h
```

## Monitoring and Automation

### System Monitoring Script
```bash
#!/bin/bash

# System monitoring script
LOG_FILE="/var/log/system_monitor.log"

log_message() {
    echo "$(date '+%Y-%m-%d %H:%M:%S') - $1" >> "$LOG_FILE"
}

# Check CPU usage
cpu_usage=$(top -bn1 | grep "Cpu(s)" | awk '{print $2}' | cut -d'%' -f1)
if (( $(echo "$cpu_usage > 80" | bc -l) )); then
    log_message "HIGH CPU USAGE: $cpu_usage%"
fi

# Check memory usage
mem_usage=$(free | grep Mem | awk '{printf "%.2f", $3/$2 * 100.0}')
if (( $(echo "$mem_usage > 90" | bc -l) )); then
    log_message "HIGH MEMORY USAGE: $mem_usage%"
fi

# Check disk usage
disk_usage=$(df / | tail -1 | awk '{print $5}' | cut -d'%' -f1)
if [ $disk_usage -gt 85 ]; then
    log_message "HIGH DISK USAGE: $disk_usage%"
fi

log_message "System check completed"
```

### Cron Jobs
```bash
# Cron job format: MM HH DOM MM DOW COMMAND
# Minute Hour DayOfMonth Month DayOfWeek Command

# Examples:
# Run every minute
* * * * * /path/to/script.sh

# Run daily at 2:30 AM
30 2 * * * /path/to/backup.sh

# Run every Monday at 9 AM
0 9 * * 1 /path/to/weekly_report.sh

# Run on the 1st of every month at midnight
0 0 1 * * /path/to/monthly_cleanup.sh

# Edit crontab
crontab -e

# List cron jobs
crontab -l

# Remove all cron jobs
crontab -r
```

## Remote Execution

### SSH Configuration
```bash
# Enable password authentication (if needed)
# Edit /etc/ssh/sshd_config
# Set: PasswordAuthentication yes
# Then restart SSH service
sudo systemctl restart ssh
```

### SSH Key-based Authentication
```bash
#!/bin/bash

# Generate SSH key pair
ssh-keygen -t rsa -b 4096 -C "your_email@example.com"

# Copy public key to remote server
ssh-copy-id user@remote_host

# SSH with specific key
ssh -i ~/.ssh/id_rsa user@remote_host

# SSH with custom port
ssh -p 2222 user@remote_host
```

### Remote Command Execution
```bash
#!/bin/bash

# Execute single command
ssh user@remote_host "ls -la"

# Execute multiple commands
ssh user@remote_host "
    cd /var/www
    ls -la
    df -h
"

# Run local script on remote machine
ssh user@remote_host 'bash -s' < local_script.sh

# Copy files to remote
scp file.txt user@remote_host:/path/to/destination/

# Copy files from remote
scp user@remote_host:/path/to/file.txt ./
```

### Multi-VM Management Script
```bash
#!/bin/bash

# List of VMs
VMS=("192.168.1.10" "192.168.1.11" "192.168.1.12")
USERNAME="admin"
SSH_KEY="~/.ssh/id_rsa"

# Install Git on multiple VMs
install_git_on_vms() {
    for vm in "${VMS[@]}"; do
        echo "Installing Git on $vm..."
        ssh -i $SSH_KEY $USERNAME@$vm "
            sudo apt update
            sudo apt install -y git
            git --version
        " || echo "Failed to install Git on $vm"
    done
}

# Deploy application to VMs
deploy_to_vms() {
    local repo_url=$1
    local deploy_path="/opt/myapp"
    
    for vm in "${VMS[@]}"; do
        echo "Deploying to $vm..."
        ssh -i $SSH_KEY $USERNAME@$vm "
            # Create deploy directory
            sudo mkdir -p $deploy_path
            sudo chown $USERNAME:$USERNAME $deploy_path
            
            # Clone or update repository
            if [ -d $deploy_path/.git ]; then
                cd $deploy_path
                git pull origin main
            else
                git clone $repo_url $deploy_path
            fi
            
            # Install dependencies and start service
            cd $deploy_path
            ./install.sh
            ./start.sh
        " || echo "Failed to deploy to $vm"
    done
}

# Usage
install_git_on_vms
deploy_to_vms "https://github.com/user/myapp.git"
```

### Code Deployment Script
```bash
#!/bin/bash

# Configuration
REPO_URL="https://github.com/user/myapp.git"
REMOTE_HOST="192.168.1.100"
REMOTE_USER="deploy"
DEPLOY_PATH="/var/www/myapp"
SERVICE_NAME="myapp"

# Colors for output
RED='\033[0;31m'
GREEN='\033[0;32m'
YELLOW='\033[1;33m'
NC='\033[0m' # No Color

log() {
    echo -e "${GREEN}[$(date '+%Y-%m-%d %H:%M:%S')]${NC} $1"
}

error() {
    echo -e "${RED}[ERROR]${NC} $1"
}

warn() {
    echo -e "${YELLOW}[WARNING]${NC} $1"
}

# Deploy function
deploy() {
    log "Starting deployment to $REMOTE_HOST..."
    
    # Create deployment script
    cat > /tmp/deploy.sh << 'EOF'
#!/bin/bash
set -e

DEPLOY_PATH=$1
SERVICE_NAME=$2
REPO_URL=$3

echo "Stopping service..."
sudo systemctl stop $SERVICE_NAME || true

echo "Backing up current version..."
if [ -d $DEPLOY_PATH ]; then
    sudo cp -r $DEPLOY_PATH ${DEPLOY_PATH}.backup.$(date +%Y%m%d_%H%M%S)
fi

echo "Updating code..."
if [ -d $DEPLOY_PATH/.git ]; then
    cd $DEPLOY_PATH
    sudo git pull origin main
else
    sudo rm -rf $DEPLOY_PATH
    sudo git clone $REPO_URL $DEPLOY_PATH
fi

cd $DEPLOY_PATH

echo "Installing dependencies..."
sudo ./install.sh

echo "Running tests..."
sudo ./test.sh

echo "Starting service..."
sudo systemctl start $SERVICE_NAME
sudo systemctl enable $SERVICE_NAME

echo "Deployment completed successfully!"
EOF

    # Copy and execute deployment script
    scp /tmp/deploy.sh $REMOTE_USER@$REMOTE_HOST:/tmp/
    ssh $REMOTE_USER@$REMOTE_HOST "bash /tmp/deploy.sh '$DEPLOY_PATH' '$SERVICE_NAME' '$REPO_URL'"
    
    # Cleanup
    rm /tmp/deploy.sh
    ssh $REMOTE_USER@$REMOTE_HOST "rm /tmp/deploy.sh"
    
    log "Deployment completed successfully!"
}

# Health check
health_check() {
    log "Performing health check..."
    
    ssh $REMOTE_USER@$REMOTE_HOST "
        if systemctl is-active --quiet $SERVICE_NAME; then
            echo 'Service is running'
            curl -f http://localhost:8080/health || exit 1
        else
            echo 'Service is not running'
            exit 1
        fi
    "
}

# Rollback function
rollback() {
    warn "Rolling back deployment..."
    
    ssh $REMOTE_USER@$REMOTE_HOST "
        BACKUP=\$(ls -1 ${DEPLOY_PATH}.backup.* | tail -n 1)
        if [ -n \"\$BACKUP\" ]; then
            sudo systemctl stop $SERVICE_NAME
            sudo rm -rf $DEPLOY_PATH
            sudo mv \$BACKUP $DEPLOY_PATH
            sudo systemctl start $SERVICE_NAME
            echo 'Rollback completed'
        else
            echo 'No backup found for rollback'
            exit 1
        fi
    "
}

# Main execution
case "$1" in
    deploy)
        deploy
        health_check || rollback
        ;;
    rollback)
        rollback
        ;;
    health)
        health_check
        ;;
    *)
        echo "Usage: $0 {deploy|rollback|health}"
        exit 1
        ;;
esac
```

## Best Practices

### Script Structure
```bash
#!/bin/bash

# Script: example.sh
# Description: Example bash script with best practices
# Author: Your Name
# Version: 1.0
# Date: $(date +%Y-%m-%d)

# Enable strict mode
set -euo pipefail

# Global variables
readonly SCRIPT_NAME=$(basename "$0")
readonly SCRIPT_DIR=$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)
readonly LOG_FILE="/var/log/${SCRIPT_NAME}.log"

# Configuration
CONFIG_FILE="${SCRIPT_DIR}/config.conf"
DEBUG=${DEBUG:-false}

# Load configuration if exists
if [[ -f "$CONFIG_FILE" ]]; then
    source "$CONFIG_FILE"
fi

# Logging function
log() {
    local level=$1
    shift
    echo "[$(date '+%Y-%m-%d %H:%M:%S')] [$level] $*" | tee -a "$LOG_FILE"
}

# Cleanup function
cleanup() {
    log "INFO" "Cleaning up..."
    # Add cleanup code here
    rm -f /tmp/$$.*
}

# Signal handlers
trap cleanup EXIT
trap 'log "ERROR" "Script interrupted"; exit 130' INT TERM

# Help function
usage() {
    cat << EOF
Usage: $SCRIPT_NAME [OPTIONS] ARGUMENTS

DESCRIPTION:
    Brief description of what the script does.

OPTIONS:
    -h, --help      Show this help message
    -v, --verbose   Enable verbose output
    -d, --debug     Enable debug mode

EXAMPLES:
    $SCRIPT_NAME --verbose file.txt
    $SCRIPT_NAME --debug --input data.csv

EOF
}

# Argument parsing
parse_arguments() {
    while [[ $# -gt 0 ]]; do
        case $1 in
            -h|--help)
                usage
                exit 0
                ;;
            -v|--verbose)
                VERBOSE=true
                shift
                ;;
            -d|--debug)
                DEBUG=true
                set -x
                shift
                ;;
            -*)
                log "ERROR" "Unknown option: $1"
                usage
                exit 1
                ;;
            *)
                POSITIONAL_ARGS+=("$1")
                shift
                ;;
        esac
    done
}

# Main function
main() {
    log "INFO" "Starting $SCRIPT_NAME"
    
    # Your main script logic here
    
    log "INFO" "Script completed successfully"
}

# Initialize
VERBOSE=${VERBOSE:-false}
POSITIONAL_ARGS=()

# Parse arguments and run main function
parse_arguments "$@"
main
```

### Security Best Practices
```bash
#!/bin/bash

# 1. Use quotes around variables
file_name="my file.txt"
rm "$file_name"  # Correct
# rm $file_name  # Wrong - will fail with spaces

# 2. Validate input
validate_input() {
    local input=$1
    if [[ ! $input =~ ^[a-zA-Z0-9_-]+$ ]]; then
        echo "Invalid input: only alphanumeric, underscore, and dash allowed"
        exit 1
    fi
}

# 3. Use absolute paths
readonly SECURE_DIR="/opt/secure"
readonly CONFIG_FILE="$SECURE_DIR/config.conf"

# 4. Set secure permissions
umask 077  # Files created with 600 permissions
mkdir -p "$SECURE_DIR"
chmod 700 "$SECURE_DIR"

# 5. Avoid eval and dangerous commands
# eval "$user_input"  # Never do this!

# 6. Use read-only variables for constants
readonly DATABASE_PASSWORD="secure_password"
readonly API_KEY="your_api_key"
```

## Common Use Cases

### System Backup Script
```bash
#!/bin/bash

# Backup script
BACKUP_SOURCE="/home/user"
BACKUP_DEST="/backup"
DATE=$(date +%Y%m%d_%H%M%S)
BACKUP_NAME="backup_$DATE.tar.gz"

# Create backup
tar -czf "$BACKUP_DEST/$BACKUP_NAME" "$BACKUP_SOURCE"

# Keep only last 7 backups
cd "$BACKUP_DEST"
ls -1t backup_*.tar.gz | tail -n +8 | xargs -r rm

echo "Backup completed: $BACKUP_NAME"
```

### Log Analysis Script
```bash
#!/bin/bash

# Analyze web server logs
LOG_FILE="/var/log/apache2/access.log"
REPORT_FILE="/tmp/log_report.txt"

{
    echo "=== Web Server Log Analysis ==="
    echo "Report generated: $(date)"
    echo
    
    echo "Top 10 IP addresses:"
    awk '{print $1}' "$LOG_FILE" | sort | uniq -c | sort -nr | head -10
    echo
    
    echo "Top 10 requested pages:"
    awk '{print $7}' "$LOG_FILE" | sort | uniq -c | sort -nr | head -10
    echo
    
    echo "HTTP status codes:"
    awk '{print $9}' "$LOG_FILE" | sort | uniq -c | sort -nr
    echo
    
    echo "Hourly request distribution:"
    awk '{print substr($4, 14, 2)}' "$LOG_FILE" | sort | uniq -c
    
} > "$REPORT_FILE"

echo "Report saved to: $REPORT_FILE"
```

### Database Backup and Restore
```bash
#!/bin/bash

# Database operations
DB_NAME="myapp"
DB_USER="admin"
DB_HOST="localhost"
BACKUP_DIR="/backups/mysql"

# Backup database
backup_database() {
    local backup_file="$BACKUP_DIR/${DB_NAME}_$(date +%Y%m%d_%H%M%S).sql"
    
    mysqldump -h "$DB_HOST" -u "$DB_USER" -p "$DB_NAME" > "$backup_file"
    
    if [ $? -eq 0 ]; then
        echo "Backup successful: $backup_file"
        gzip "$backup_file"
    else
        echo "Backup failed"
        exit 1
    fi
}

# Restore database
restore_database() {
    local backup_file=$1
    
    if [ ! -f "$backup_file" ]; then
        echo "Backup file not found: $backup_file"
        exit 1
    fi
    
    # Decompress if needed
    if [[ "$backup_file" == *.gz ]]; then
        gunzip -c "$backup_file" | mysql -h "$DB_HOST" -u "$DB_USER" -p "$DB_NAME"
    else
        mysql -h "$DB_HOST" -u "$DB_USER" -p "$DB_NAME" < "$backup_file"
    fi
    
    if [ $? -eq 0 ]; then
        echo "Restore successful"
    else
        echo "Restore failed"
        exit 1
    fi
}

# Usage
case "$1" in
    backup)
        backup_database
        ;;
    restore)
        restore_database "$2"
        ;;
    *)
        echo "Usage: $0 {backup|restore} [backup_file]"
        exit 1
        ;;
esac
```

### Service Management Script
```bash
#!/bin/bash

# Service management script
SERVICE_NAME="myapp"
PID_FILE="/var/run/$SERVICE_NAME.pid"
LOG_FILE="/var/log/$SERVICE_NAME.log"
APP_DIR="/opt/$SERVICE_NAME"
APP_COMMAND="java -jar $APP_DIR/app.jar"

start_service() {
    if [ -f "$PID_FILE" ] && kill -0 $(cat "$PID_FILE") 2>/dev/null; then
        echo "Service $SERVICE_NAME is already running"
        return 1
    fi
    
    echo "Starting $SERVICE_NAME..."
    cd "$APP_DIR"
    nohup $APP_COMMAND > "$LOG_FILE" 2>&1 &
    echo $! > "$PID_FILE"
    
    sleep 2
    if kill -0 $(cat "$PID_FILE") 2>/dev/null; then
        echo "Service $SERVICE_NAME started successfully"
    else
        echo "Failed to start service $SERVICE_NAME"
        rm -f "$PID_FILE"
        return 1
    fi
}

stop_service() {
    if [ ! -f "$PID_FILE" ]; then
        echo "Service $SERVICE_NAME is not running"
        return 1
    fi
    
    local pid=$(cat "$PID_FILE")
    echo "Stopping $SERVICE_NAME (PID: $pid)..."
    
    kill "$pid"
    
    # Wait for graceful shutdown
    local count=0
    while kill -0 "$pid" 2>/dev/null && [ $count -lt 10 ]; do
        sleep 1
        count=$((count + 1))
    done
    
    # Force kill if still running
    if kill -0 "$pid" 2>/dev/null; then
        echo "Force killing $SERVICE_NAME..."
        kill -9 "$pid"
    fi
    
    rm -f "$PID_FILE"
    echo "Service $SERVICE_NAME stopped"
}

service_status() {
    if [ -f "$PID_FILE" ] && kill -0 $(cat "$PID_FILE") 2>/dev/null; then
        echo "Service $SERVICE_NAME is running (PID: $(cat "$PID_FILE"))"
    else
        echo "Service $SERVICE_NAME is not running"
        return 1
    fi
}

restart_service() {
    stop_service
    sleep 2
    start_service
}

case "$1" in
    start)
        start_service
        ;;
    stop)
        stop_service
        ;;
    restart)
        restart_service
        ;;
    status)
        service_status
        ;;
    *)
        echo "Usage: $0 {start|stop|restart|status}"
        exit 1
        ;;
esac
```

### File Synchronization Script
```bash
#!/bin/bash

# File synchronization script
SOURCE_DIR="/local/data"
DEST_DIR="/backup/data"
REMOTE_HOST="backup.example.com"
REMOTE_USER="backupuser"
LOG_FILE="/var/log/sync.log"

# Local sync
sync_local() {
    echo "$(date): Starting local sync" >> "$LOG_FILE"
    
    rsync -av --delete --progress \
        --exclude '*.tmp' \
        --exclude '.cache/' \
        "$SOURCE_DIR/" "$DEST_DIR/"
    
    if [ $? -eq 0 ]; then
        echo "$(date): Local sync completed successfully" >> "$LOG_FILE"
    else
        echo "$(date): Local sync failed" >> "$LOG_FILE"
        exit 1
    fi
}

# Remote sync
sync_remote() {
    echo "$(date): Starting remote sync" >> "$LOG_FILE"
    
    rsync -av --delete --progress \
        -e "ssh -o StrictHostKeyChecking=no" \
        --exclude '*.tmp' \
        --exclude '.cache/' \
        "$SOURCE_DIR/" "$REMOTE_USER@$REMOTE_HOST:$DEST_DIR/"
    
    if [ $? -eq 0 ]; then
        echo "$(date): Remote sync completed successfully" >> "$LOG_FILE"
    else
        echo "$(date): Remote sync failed" >> "$LOG_FILE"
        exit 1
    fi
}

# Check connectivity
check_connectivity() {
    if ping -c 1 "$REMOTE_HOST" >/dev/null 2>&1; then
        return 0
    else
        echo "$(date): Cannot reach $REMOTE_HOST" >> "$LOG_FILE"
        return 1
    fi
}

# Main execution
case "$1" in
    local)
        sync_local
        ;;
    remote)
        if check_connectivity; then
            sync_remote
        fi
        ;;
    both)
        sync_local
        if check_connectivity; then
            sync_remote
        fi
        ;;
    *)
        echo "Usage: $0 {local|remote|both}"
        exit 1
        ;;
esac
```

### System Health Check Script
```bash
#!/bin/bash

# System health check script
ALERT_EMAIL="admin@example.com"
CPU_THRESHOLD=80
MEMORY_THRESHOLD=90
DISK_THRESHOLD=85
LOAD_THRESHOLD=5.0

# Health check functions
check_cpu() {
    local cpu_usage=$(top -bn1 | grep "Cpu(s)" | sed "s/.*, *\([0-9.]*\)%* id.*/\1/" | awk '{print 100 - $1}')
    echo "CPU Usage: ${cpu_usage}%"
    
    if (( $(echo "$cpu_usage > $CPU_THRESHOLD" | bc -l) )); then
        return 1
    fi
    return 0
}

check_memory() {
    local mem_usage=$(free | grep Mem | awk '{printf "%.1f", $3/$2 * 100.0}')
    echo "Memory Usage: ${mem_usage}%"
    
    if (( $(echo "$mem_usage > $MEMORY_THRESHOLD" | bc -l) )); then
        return 1
    fi
    return 0
}

check_disk() {
    local disk_usage=$(df / | tail -1 | awk '{print $5}' | sed 's/%//')
    echo "Disk Usage: ${disk_usage}%"
    
    if [ "$disk_usage" -gt "$DISK_THRESHOLD" ]; then
        return 1
    fi
    return 0
}

check_load() {
    local load_avg=$(uptime | awk '{print $(NF-2)}' | sed 's/,//')
    echo "Load Average (1min): $load_avg"
    
    if (( $(echo "$load_avg > $LOAD_THRESHOLD" | bc -l) )); then
        return 1
    fi
    return 0
}

check_services() {
    local services=("nginx" "mysql" "ssh")
    local failed_services=()
    
    for service in "${services[@]}"; do
        if ! systemctl is-active --quiet "$service"; then
            failed_services+=("$service")
        fi
    done
    
    if [ ${#failed_services[@]} -gt 0 ]; then
        echo "Failed services: ${failed_services[*]}"
        return 1
    else
        echo "All critical services are running"
        return 0
    fi
}

send_alert() {
    local message="$1"
    echo "$message" | mail -s "System Alert - $(hostname)" "$ALERT_EMAIL"
}

# Main health check
main() {
    echo "=== System Health Check - $(date) ==="
    
    local alerts=()
    
    if ! check_cpu; then
        alerts+=("High CPU usage detected")
    fi
    
    if ! check_memory; then
        alerts+=("High memory usage detected")
    fi
    
    if ! check_disk; then
        alerts+=("High disk usage detected")
    fi
    
    if ! check_load; then
        alerts+=("High system load detected")
    fi
    
    if ! check_services; then
        alerts+=("Critical services are down")
    fi
    
    # Send alerts if any issues found
    if [ ${#alerts[@]} -gt 0 ]; then
        local alert_message="System health check failed on $(hostname):
        
$(printf '%s\n' "${alerts[@]}")

System Details:
$(check_cpu)
$(check_memory)  
$(check_disk)
$(check_load)
$(check_services)"
        
        send_alert "$alert_message"
        echo "Alerts sent: ${#alerts[@]} issues found"
        return 1
    else
        echo "All systems normal"
        return 0
    fi
}

main
```

## Advanced Techniques

### Parallel Processing
```bash
#!/bin/bash

# Process files in parallel
process_file() {
    local file=$1
    echo "Processing $file..."
    # Simulate work
    sleep 2
    echo "Completed $file"
}

# Export function for parallel execution
export -f process_file

# Process files in parallel (max 4 jobs)
find /path/to/files -name "*.txt" | xargs -n 1 -P 4 -I {} bash -c 'process_file "$@"' _ {}

# Alternative using GNU parallel
# parallel -j 4 process_file ::: *.txt
```

### Configuration File Parsing
```bash
#!/bin/bash

# config.conf file format:
# DATABASE_HOST=localhost
# DATABASE_PORT=5432
# API_KEY=your_key_here

parse_config() {
    local config_file="$1"
    
    if [ ! -f "$config_file" ]; then
        echo "Config file not found: $config_file"
        exit 1
    fi
    
    # Parse configuration
    while IFS='=' read -r key value; do
        # Skip comments and empty lines
        [[ $key =~ ^[[:space:]]*# ]] && continue
        [[ -z $key ]] && continue
        
        # Remove leading/trailing whitespace
        key=$(echo "$key" | xargs)
        value=$(echo "$value" | xargs)
        
        # Export as environment variable
        export "$key"="$value"
        echo "Loaded: $key=$value"
    done < "$config_file"
}

# Usage
parse_config "config.conf"
echo "Database host: $DATABASE_HOST"
```

### JSON Processing
```bash
#!/bin/bash

# Process JSON using jq
API_RESPONSE='{"users":[{"id":1,"name":"John"},{"id":2,"name":"Jane"}],"total":2}'

# Extract values
total_users=$(echo "$API_RESPONSE" | jq -r '.total')
first_user_name=$(echo "$API_RESPONSE" | jq -r '.users[0].name')

echo "Total users: $total_users"
echo "First user: $first_user_name"

# Process array
echo "$API_RESPONSE" | jq -r '.users[] | "\(.id): \(.name)"'

# Read JSON from file
if [ -f "data.json" ]; then
    jq -r '.[] | select(.status == "active") | .name' data.json
fi
```

### Menu System
```bash
#!/bin/bash

# Interactive menu system
show_menu() {
    echo "================================="
    echo "       System Administration     "
    echo "================================="
    echo "1. Check System Status"
    echo "2. View Logs"
    echo "3. Restart Services"
    echo "4. Backup Database"
    echo "5. Exit"
    echo "================================="
}

check_system_status() {
    echo "Checking system status..."
    uptime
    free -h
    df -h
}

view_logs() {
    echo "Select log file:"
    echo "1. System Log"
    echo "2. Apache Log"
    echo "3. MySQL Log"
    
    read -p "Enter choice: " log_choice
    
    case $log_choice in
        1) tail -f /var/log/syslog ;;
        2) tail -f /var/log/apache2/error.log ;;
        3) tail -f /var/log/mysql/error.log ;;
        *) echo "Invalid choice" ;;
    esac
}

restart_services() {
    services=("nginx" "mysql" "redis")
    
    echo "Available services:"
    for i in "${!services[@]}"; do
        echo "$((i+1)). ${services[i]}"
    done
    
    read -p "Enter service number to restart: " service_num
    
    if [ "$service_num" -ge 1 ] && [ "$service_num" -le "${#services[@]}" ]; then
        service_name="${services[$((service_num-1))]}"
        sudo systemctl restart "$service_name"
        echo "$service_name restarted"
    else
        echo "Invalid choice"
    fi
}

# Main menu loop
while true; do
    show_menu
    read -p "Enter your choice [1-5]: " choice
    
    case $choice in
        1)
            check_system_status
            read -p "Press Enter to continue..."
            ;;
        2)
            view_logs
            ;;
        3)
            restart_services
            read -p "Press Enter to continue..."
            ;;
        4)
            echo "Starting database backup..."
            # Call backup function here
            read -p "Press Enter to continue..."
            ;;
        5)
            echo "Goodbye!"
            exit 0
            ;;
        *)
            echo "Invalid option. Please try again."
            read -p "Press Enter to continue..."
            ;;
    esac
done
```

## Debugging and Testing

### Debug Mode
```bash
#!/bin/bash

# Enable debug mode
DEBUG=${DEBUG:-false}

debug() {
    if [ "$DEBUG" = "true" ]; then
        echo "[DEBUG] $*" >&2
    fi
}

# Usage
debug "This is a debug message"

# Run with debug: DEBUG=true ./script.sh
```

### Testing Framework
```bash
#!/bin/bash

# Simple testing framework
TESTS_PASSED=0
TESTS_FAILED=0

assert_equals() {
    local expected="$1"
    local actual="$2"
    local message="$3"
    
    if [ "$expected" = "$actual" ]; then
        echo "✓ PASS: $message"
        TESTS_PASSED=$((TESTS_PASSED + 1))
    else
        echo "✗ FAIL: $message"
        echo "  Expected: '$expected'"
        echo "  Actual: '$actual'"
        TESTS_FAILED=$((TESTS_FAILED + 1))
    fi
}

# Test functions
test_string_operations() {
    local result=$(echo "hello world" | tr '[:lower:]' '[:upper:]')
    assert_equals "HELLO WORLD" "$result" "String uppercase conversion"
    
    local length=${#result}
    assert_equals "11" "$length" "String length calculation"
}

test_math_operations() {
    local sum=$((5 + 3))
    assert_equals "8" "$sum" "Addition operation"
    
    local product=$((4 * 7))
    assert_equals "28" "$product" "Multiplication operation"
}

# Run tests
echo "Running tests..."
test_string_operations
test_math_operations

# Results
echo
echo "Test Results:"
echo "Passed: $TESTS_PASSED"
echo "Failed: $TESTS_FAILED"

if [ $TESTS_FAILED -eq 0 ]; then
    echo "All tests passed!"
    exit 0
else
    echo "Some tests failed!"
    exit 1
fi
```

## Performance Optimization

### Efficient File Processing
```bash
#!/bin/bash

# Efficient way to process large files
process_large_file() {
    local file="$1"
    
    # Use while read for memory efficiency
    while IFS= read -r line; do
        # Process line
        echo "Processing: $line"
    done < "$file"
}

# Parallel processing for multiple files
process_files_parallel() {
    local max_jobs=4
    local job_count=0
    
    for file in *.txt; do
        {
            echo "Processing $file in background"
            process_large_file "$file"
        } &
        
        job_count=$((job_count + 1))
        
        # Limit concurrent jobs
        if [ $job_count -ge $max_jobs ]; then
            wait
            job_count=0
        fi
    done
    
    wait  # Wait for remaining jobs
}
```

## Conclusion

This comprehensive Bash scripting guide covers everything from basic syntax to advanced automation techniques. Bash scripts are powerful tools for system administration, deployment automation, monitoring, and general task automation.

### Key Takeaways:
- Always use proper error handling and validation
- Follow security best practices
- Use functions to organize code
- Document your scripts thoroughly
- Test scripts in safe environments first
- Use version control for script management

### Next Steps:
- Practice with real-world scenarios
- Learn about advanced tools like `awk`, `sed`, and `jq`
- Explore configuration management tools
- Study shell scripting best practices
- Contribute to open-source shell scripts

### Resources:
- [Bash Manual](https://www.gnu.org/software/bash/manual/)
- [ShellCheck](https://www.shellcheck.net/) - Shell script analysis tool
- [Bash Guide](https://mywiki.wooledge.org/BashGuide) - Advanced Bash scripting guide
- [Linux Command Line](https://linuxcommand.org/) - Command line tutorials

Remember: The best way to learn Bash scripting is through practice. Start with simple scripts and gradually build more complex automation tools as you gain experience.