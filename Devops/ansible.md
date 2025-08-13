# Complete Ansible Learning Guide

## Table of Contents
1. [Introduction to Ansible](#introduction-to-ansible)
2. [Core Concepts](#core-concepts)
3. [Installation and Setup](#installation-and-setup)
4. [Inventory Management](#inventory-management)
5. [Modules](#modules)
6. [Playbooks](#playbooks)
7. [Variables and Facts](#variables-and-facts)
8. [Templates](#templates)
9. [Handlers](#handlers)
10. [Roles](#roles)
11. [Conditionals and Loops](#conditionals-and-loops)
12. [Vault (Encryption)](#vault-encryption)
13. [Best Practices](#best-practices)
14. [Advanced Topics](#advanced-topics)
15. [Troubleshooting](#troubleshooting)

---

## Introduction to Ansible

### What is Ansible?
Ansible is an open-source automation platform that simplifies complex tasks such as configuration management, application deployment, task automation, and orchestration. It uses human-readable YAML syntax and requires no agents on target systems.

### Key Features
- **Agentless**: No need to install software on managed nodes
- **Idempotent**: Same result every time you run it
- **Simple**: Uses YAML, which is easy to read and write
- **Powerful**: Can manage complex multi-tier applications
- **Flexible**: Works with existing tools and processes

### Architecture Overview
```
Control Node (Ansible Engine) → SSH → Managed Nodes
```

---

## Core Concepts

### 1. Control Node
The machine where Ansible is installed and from where automation is executed.

### 2. Managed Nodes
The target machines that Ansible manages (also called "hosts").

### 3. Inventory
A list of managed nodes organized in groups.

### 4. Modules
Units of code that Ansible executes on managed nodes.

### 5. Tasks
Individual actions performed by modules.

### 6. Playbooks
YAML files containing a series of tasks to be executed.

### 7. Plays
A set of tasks mapped to a group of hosts.

### 8. Roles
A way to organize playbooks and related files in a structured manner.

---

## Installation and Setup

### Prerequisites
- Python 2.7+ or Python 3.5+
- SSH access to managed nodes
- sudo privileges (if needed)

### Installation Methods

#### Via pip (Recommended)
```bash
pip install ansible
```

#### Via package manager (Ubuntu/Debian)
```bash
sudo apt update
sudo apt install ansible
```

#### Via package manager (CentOS/RHEL)
```bash
sudo yum install epel-release
sudo yum install ansible
```

### Verification
```bash
ansible --version
ansible localhost -m ping
```

---

## Inventory Management

### Static Inventory

#### INI Format
```ini
[webservers]
web1.example.com
web2.example.com
web3.example.com

[dbservers]
db1.example.com
db2.example.com

[production:children]
webservers
dbservers

[webservers:vars]
http_port=80
max_clients=200
```

#### YAML Format
```yaml
all:
  children:
    webservers:
      hosts:
        web1.example.com:
        web2.example.com:
        web3.example.com:
      vars:
        http_port: 80
        max_clients: 200
    dbservers:
      hosts:
        db1.example.com:
        db2.example.com:
    production:
      children:
        webservers:
        dbservers:
```

### Dynamic Inventory
Dynamic inventory scripts that pull inventory information from external sources like cloud providers, CMDB, or LDAP.

### Inventory Variables
- **Host variables**: Specific to individual hosts
- **Group variables**: Applied to all hosts in a group
- **Built-in variables**: Provided by Ansible (ansible_host, ansible_port, etc.)

---

## Modules

### What are Modules?
Modules are discrete units of code that can be used from the command line or in a playbook task.

### Common Module Categories

#### System Modules
- `user`: Manage user accounts
- `group`: Manage groups
- `service`: Manage services
- `systemd`: Manage systemd services
- `cron`: Manage cron jobs

#### File Modules
- `copy`: Copy files to remote locations
- `file`: Manage files and file properties
- `template`: Template a file out to a remote server
- `lineinfile`: Manage lines in text files
- `blockinfile`: Insert/update/remove blocks of lines

#### Package Modules
- `yum`: Manage packages with yum
- `apt`: Manage packages with apt
- `pip`: Manage Python packages
- `package`: Generic OS package manager

#### Cloud Modules
- `ec2`: Manage EC2 instances
- `s3`: Manage S3 buckets and objects
- `gcp_compute_instance`: Manage GCP instances

### Module Usage Examples

#### Command Line
```bash
ansible webservers -m ping
ansible webservers -m setup
ansible webservers -m yum -a "name=httpd state=present" --become
```

#### In Playbooks
```yaml
- name: Install Apache
  yum:
    name: httpd
    state: present

- name: Copy configuration file
  copy:
    src: /local/path/httpd.conf
    dest: /etc/httpd/conf/httpd.conf
    owner: root
    group: root
    mode: '0644'
```

---

## Playbooks

### Basic Structure
```yaml
---
- name: My First Playbook
  hosts: webservers
  become: yes
  vars:
    http_port: 80
  
  tasks:
    - name: Install Apache
      yum:
        name: httpd
        state: present
    
    - name: Start Apache service
      service:
        name: httpd
        state: started
        enabled: yes
```

### Playbook Components

#### Header
```yaml
---
- name: Descriptive name of the play
  hosts: target_hosts
  become: yes/no
  gather_facts: yes/no
  vars:
    variable_name: value
```

#### Tasks Section
```yaml
tasks:
  - name: Task description
    module_name:
      parameter1: value1
      parameter2: value2
    tags:
      - tag1
      - tag2
```

### Multiple Plays
```yaml
---
- name: Configure web servers
  hosts: webservers
  tasks:
    - name: Install Apache
      yum:
        name: httpd
        state: present

- name: Configure database servers
  hosts: dbservers
  tasks:
    - name: Install MySQL
      yum:
        name: mysql-server
        state: present
```

### Running Playbooks
```bash
ansible-playbook playbook.yml
ansible-playbook playbook.yml --limit webservers
ansible-playbook playbook.yml --tags "config"
ansible-playbook playbook.yml --skip-tags "packages"
ansible-playbook playbook.yml --check  # Dry run
```

---

## Variables and Facts

### Variable Types

#### Playbook Variables
```yaml
vars:
  http_port: 80
  server_name: web01
```

#### Inventory Variables
```ini
[webservers]
web1.example.com http_port=80 server_name=web01
web2.example.com http_port=8080 server_name=web02
```

#### Variable Files
```yaml
# vars/main.yml
http_port: 80
database_name: myapp_db
database_user: myapp_user
```

Include in playbook:
```yaml
vars_files:
  - vars/main.yml
```

#### Host and Group Variables
Directory structure:
```
inventory/
├── hosts
├── group_vars/
│   ├── all.yml
│   ├── webservers.yml
│   └── dbservers.yml
└── host_vars/
    ├── web1.example.com.yml
    └── db1.example.com.yml
```

### Variable Precedence (highest to lowest)
1. Extra vars (`-e` in command line)
2. Task vars (only for the specific task)
3. Block vars (only for the specific block)
4. Role and include vars
5. Play vars_files
6. Play vars_prompt
7. Play vars
8. Set_facts / registered vars
9. Host facts
10. Playbook host_vars
11. Playbook group_vars
12. Inventory host_vars
13. Inventory group_vars
14. Inventory vars
15. Role defaults

### Facts
Facts are system properties gathered by Ansible automatically.

#### Gathering Facts
```yaml
- name: Gather facts about remote hosts
  setup:

- name: Display OS family
  debug:
    msg: "OS family is {{ ansible_os_family }}"
```

#### Common Facts
- `ansible_hostname`: System hostname
- `ansible_fqdn`: Fully qualified domain name
- `ansible_os_family`: OS family (RedHat, Debian, etc.)
- `ansible_distribution`: Specific OS distribution
- `ansible_architecture`: System architecture
- `ansible_memtotal_mb`: Total memory in MB
- `ansible_processor_count`: Number of processors

#### Custom Facts
Create custom facts in `/etc/ansible/facts.d/`:
```bash
# /etc/ansible/facts.d/custom.fact
[database]
type=mysql
version=5.7
```

Access with: `{{ ansible_local.custom.database.type }}`

---

## Templates

### Jinja2 Templating
Ansible uses Jinja2 templating engine for dynamic content generation.

### Template Module
```yaml
- name: Generate configuration file
  template:
    src: httpd.conf.j2
    dest: /etc/httpd/conf/httpd.conf
    owner: root
    group: root
    mode: '0644'
  notify: restart apache
```

### Template Example (httpd.conf.j2)
```jinja2
# Apache Configuration File
# Generated by Ansible

ServerName {{ server_name }}
Listen {{ http_port }}

{% if ssl_enabled %}
Listen {{ https_port }} ssl
{% endif %}

# Virtual Hosts
{% for vhost in virtual_hosts %}
<VirtualHost *:{{ http_port }}>
    ServerName {{ vhost.name }}
    DocumentRoot {{ vhost.docroot }}
    
    {% if vhost.ssl is defined and vhost.ssl %}
    SSLEngine on
    SSLCertificateFile {{ vhost.ssl_cert }}
    SSLCertificateKeyFile {{ vhost.ssl_key }}
    {% endif %}
</VirtualHost>
{% endfor %}

# Include additional configuration
{% for config in additional_configs %}
Include {{ config }}
{% endfor %}
```

### Template Filters
```jinja2
{{ variable | default('default_value') }}
{{ list_variable | join(',') }}
{{ string_variable | upper }}
{{ number_variable | int }}
{{ path_variable | basename }}
{{ json_variable | to_nice_json }}
{{ yaml_variable | to_nice_yaml }}
```

### Conditional Statements
```jinja2
{% if condition %}
  # Content when condition is true
{% elif other_condition %}
  # Content when other_condition is true
{% else %}
  # Default content
{% endif %}
```

### Loops
```jinja2
{% for item in items %}
  # Content repeated for each item
  Item: {{ item }}
{% endfor %}
```

---

## Handlers

### What are Handlers?
Handlers are special tasks that run only when notified by other tasks. They're typically used for service restarts or reloads.

### Handler Definition
```yaml
handlers:
  - name: restart apache
    service:
      name: httpd
      state: restarted
  
  - name: reload nginx
    service:
      name: nginx
      state: reloaded
```

### Triggering Handlers
```yaml
tasks:
  - name: Copy Apache configuration
    copy:
      src: httpd.conf
      dest: /etc/httpd/conf/httpd.conf
    notify: restart apache
  
  - name: Install Apache module
    yum:
      name: mod_ssl
      state: present
    notify: restart apache
```

### Handler Execution
- Handlers run at the end of each play
- Handlers run only once, even if notified multiple times
- Handlers run in the order they're defined, not notified
- Use `meta: flush_handlers` to force immediate execution

### Advanced Handler Usage
```yaml
- name: Update configuration
  template:
    src: app.conf.j2
    dest: /etc/app/app.conf
  notify:
    - restart app
    - send notification

handlers:
  - name: restart app
    service:
      name: myapp
      state: restarted
  
  - name: send notification
    mail:
      to: admin@example.com
      subject: "App restarted on {{ inventory_hostname }}"
      body: "The application was restarted due to configuration changes."
```

---

## Roles

### What are Roles?
Roles are a way to organize playbooks and related files in a standardized structure, making them reusable and shareable.

### Role Directory Structure
```
roles/
└── webserver/
    ├── tasks/
    │   └── main.yml
    ├── handlers/
    │   └── main.yml
    ├── templates/
    │   └── httpd.conf.j2
    ├── files/
    │   └── index.html
    ├── vars/
    │   └── main.yml
    ├── defaults/
    │   └── main.yml
    ├── meta/
    │   └── main.yml
    └── README.md
```

### Role Components

#### tasks/main.yml
```yaml
---
- name: Install Apache
  yum:
    name: httpd
    state: present

- name: Copy configuration file
  template:
    src: httpd.conf.j2
    dest: /etc/httpd/conf/httpd.conf
  notify: restart apache

- name: Start Apache service
  service:
    name: httpd
    state: started
    enabled: yes
```

#### handlers/main.yml
```yaml
---
- name: restart apache
  service:
    name: httpd
    state: restarted
```

#### defaults/main.yml
```yaml
---
http_port: 80
server_name: "{{ ansible_fqdn }}"
document_root: "/var/www/html"
```

#### vars/main.yml
```yaml
---
apache_package: httpd
apache_service: httpd
config_file: /etc/httpd/conf/httpd.conf
```

#### meta/main.yml
```yaml
---
galaxy_info:
  author: Your Name
  description: Apache Web Server Role
  license: MIT
  min_ansible_version: 2.9
  platforms:
    - name: EL
      versions:
        - 7
        - 8
dependencies:
  - role: common
    vars:
      enable_firewall: true
```

### Using Roles in Playbooks
```yaml
---
- name: Configure web servers
  hosts: webservers
  roles:
    - common
    - webserver
    - { role: ssl, ssl_enabled: true }
```

### Role Tasks with Parameters
```yaml
- name: Configure web servers
  hosts: webservers
  tasks:
    - include_role:
        name: webserver
      vars:
        http_port: 8080
        server_name: custom.example.com
```

### Creating Roles with Ansible Galaxy
```bash
ansible-galaxy init webserver
ansible-galaxy install geerlingguy.apache
ansible-galaxy list
```

---

## Conditionals and Loops

### Conditionals

#### When Statement
```yaml
- name: Install Apache on RedHat family
  yum:
    name: httpd
    state: present
  when: ansible_os_family == "RedHat"

- name: Install Apache on Debian family
  apt:
    name: apache2
    state: present
  when: ansible_os_family == "Debian"
```

#### Complex Conditions
```yaml
- name: Restart service if config changed
  service:
    name: httpd
    state: restarted
  when:
    - config_updated is defined
    - config_updated.changed
    - not maintenance_mode
```

#### Boolean Conditions
```yaml
- name: Task runs when variable is true
  debug:
    msg: "Variable is true"
  when: my_boolean_var | bool

- name: Task runs when variable is false
  debug:
    msg: "Variable is false"
  when: not my_boolean_var | bool
```

### Loops

#### Simple Loop
```yaml
- name: Install packages
  yum:
    name: "{{ item }}"
    state: present
  loop:
    - httpd
    - php
    - mysql-server
```

#### Loop over Dictionaries
```yaml
- name: Create users
  user:
    name: "{{ item.name }}"
    group: "{{ item.group }}"
    shell: "{{ item.shell | default('/bin/bash') }}"
  loop:
    - { name: alice, group: users, shell: /bin/bash }
    - { name: bob, group: admin, shell: /bin/zsh }
    - { name: charlie, group: users }
```

#### Loop with Conditions
```yaml
- name: Install packages conditionally
  yum:
    name: "{{ item.name }}"
    state: present
  loop:
    - { name: httpd, required: true }
    - { name: mod_ssl, required: false }
    - { name: php, required: true }
  when: item.required
```

#### Nested Loops
```yaml
- name: Configure firewall rules
  firewalld:
    service: "{{ item.0 }}"
    source: "{{ item.1 }}"
    permanent: yes
    state: enabled
  loop: "{{ services | product(allowed_ips) | list }}"
  vars:
    services:
      - http
      - https
    allowed_ips:
      - 192.168.1.0/24
      - 10.0.0.0/8
```

#### Loop Controls
```yaml
- name: Process items with labels
  debug:
    msg: "Processing {{ item.name }}"
  loop:
    - { name: web1, ip: 192.168.1.10 }
    - { name: web2, ip: 192.168.1.11 }
  loop_control:
    label: "{{ item.name }}"
    pause: 2
```

### Register and Loop Results
```yaml
- name: Check service status
  command: systemctl is-active "{{ item }}"
  register: service_status
  loop:
    - httpd
    - mysql
    - sshd
  ignore_errors: yes

- name: Display results
  debug:
    msg: "{{ item.item }} is {{ item.stdout }}"
  loop: "{{ service_status.results }}"
```

---

## Vault (Encryption)

### What is Ansible Vault?
Ansible Vault is a feature that allows you to encrypt sensitive data such as passwords, keys, and other secrets.

### Creating Encrypted Files
```bash
ansible-vault create secrets.yml
ansible-vault create --vault-password-file=vault_pass.txt secrets.yml
```

### Editing Encrypted Files
```bash
ansible-vault edit secrets.yml
ansible-vault edit --vault-password-file=vault_pass.txt secrets.yml
```

### Encrypting Existing Files
```bash
ansible-vault encrypt existing_file.yml
ansible-vault encrypt --vault-password-file=vault_pass.txt existing_file.yml
```

### Decrypting Files
```bash
ansible-vault decrypt secrets.yml
ansible-vault view secrets.yml  # View without decrypting
```

### Changing Vault Password
```bash
ansible-vault rekey secrets.yml
```

### Using Encrypted Variables
```yaml
# secrets.yml (encrypted)
database_password: supersecretpassword
api_key: verysecretapikey
ssl_private_key: |
  -----BEGIN PRIVATE KEY-----
  ...
  -----END PRIVATE KEY-----
```

### In Playbooks
```yaml
---
- name: Deploy application
  hosts: webservers
  vars_files:
    - secrets.yml
  tasks:
    - name: Configure database connection
      template:
        src: database.conf.j2
        dest: /etc/app/database.conf
      vars:
        db_password: "{{ database_password }}"
```

### Running with Vault
```bash
ansible-playbook deploy.yml --ask-vault-pass
ansible-playbook deploy.yml --vault-password-file=vault_pass.txt
```

### Encrypting String Variables
```bash
ansible-vault encrypt_string 'secret_password' --name 'password'
```

Output:
```yaml
password: !vault |
          $ANSIBLE_VAULT;1.1;AES256
          66386439653838336464616231316663...
```

### Multiple Vault IDs
```bash
ansible-vault create --vault-id dev@prompt secrets_dev.yml
ansible-vault create --vault-id prod@prod_vault_pass.txt secrets_prod.yml
ansible-playbook deploy.yml --vault-id dev@prompt --vault-id prod@prod_vault_pass.txt
```

---

## Best Practices

### Playbook Organization
1. **Use meaningful names** for plays, tasks, and variables
2. **Group related tasks** into roles
3. **Keep playbooks simple** - use roles for complex logic
4. **Use version control** for all Ansible content

### Directory Structure
```
ansible-project/
├── ansible.cfg
├── inventories/
│   ├── development/
│   │   ├── hosts
│   │   ├── group_vars/
│   │   └── host_vars/
│   └── production/
│       ├── hosts
│       ├── group_vars/
│       └── host_vars/
├── playbooks/
│   ├── site.yml
│   ├── webservers.yml
│   └── dbservers.yml
├── roles/
│   ├── common/
│   ├── webserver/
│   └── database/
└── vars/
    ├── secrets.yml
    └── common.yml
```

### Security Best Practices
1. **Use Ansible Vault** for sensitive data
2. **Limit privilege escalation** - use `become` only when necessary
3. **Use specific modules** instead of shell/command when possible
4. **Validate inputs** and use proper error handling
5. **Keep secrets in separate files** from regular variables

### Performance Optimization
1. **Disable fact gathering** when not needed: `gather_facts: no`
2. **Use pipelining** in ansible.cfg: `pipelining = True`
3. **Increase parallelism**: `forks = 50`
4. **Use --limit** to target specific hosts
5. **Cache facts** when running multiple playbooks

### Error Handling
```yaml
- name: Task that might fail
  command: /path/to/command
  register: result
  ignore_errors: yes

- name: Handle failure
  debug:
    msg: "Command failed with: {{ result.stderr }}"
  when: result.failed

- name: Continue on failure
  block:
    - name: Risky task
      command: might_fail
  rescue:
    - name: Handle failure
      debug:
        msg: "Task failed, but continuing"
  always:
    - name: Always run
      debug:
        msg: "This always runs"
```

### Testing and Validation
```yaml
- name: Validate configuration
  uri:
    url: "http://{{ inventory_hostname }}/health"
    method: GET
    status_code: 200
  delegate_to: localhost

- name: Assert condition
  assert:
    that:
      - ansible_memtotal_mb >= 1024
    fail_msg: "Server needs at least 1GB RAM"
    success_msg: "Memory requirement satisfied"
```

---

## Advanced Topics

### Dynamic Includes
```yaml
- name: Include OS-specific variables
  include_vars: "{{ ansible_os_family }}.yml"

- name: Include OS-specific tasks
  include_tasks: "{{ ansible_os_family }}.yml"
```

### Delegation and Local Actions
```yaml
- name: Add host to load balancer
  uri:
    url: "http://loadbalancer/api/add"
    method: POST
    body_format: json
    body:
      host: "{{ inventory_hostname }}"
  delegate_to: localhost

- name: Run command on different host
  command: /usr/bin/some_command
  delegate_to: "{{ groups['monitoring'][0] }}"
```

### Custom Modules
```python
#!/usr/bin/python
# my_custom_module.py

from ansible.module_utils.basic import AnsibleModule

def main():
    module = AnsibleModule(
        argument_spec=dict(
            name=dict(required=True, type='str'),
            state=dict(default='present', choices=['present', 'absent'])
        )
    )
    
    name = module.params['name']
    state = module.params['state']
    
    # Module logic here
    
    module.exit_json(changed=True, msg=f"Successfully processed {name}")

if __name__ == '__main__':
    main()
```

### Callback Plugins
```python
# callback_plugins/my_callback.py
from ansible.plugins.callback import CallbackBase

class CallbackModule(CallbackBase):
    def v2_runner_on_ok(self, result):
        print(f"Task {result.task_name} succeeded on {result._host}")
```

### Strategy Plugins
```yaml
- name: Use free strategy
  hosts: webservers
  strategy: free
  tasks:
    - name: Task runs as soon as host is ready
      command: /usr/bin/long_running_command
```

### Lookups
```yaml
- name: Use file lookup
  debug:
    msg: "{{ lookup('file', '/etc/hostname') }}"

- name: Use environment variable
  debug:
    msg: "{{ lookup('env', 'HOME') }}"

- name: Use password lookup
  user:
    name: myuser
    password: "{{ lookup('password', '/tmp/password chars=ascii_letters,digits') | password_hash('sha512') }}"
```

---

## Troubleshooting

### Common Issues and Solutions

#### SSH Connection Problems
```bash
# Test SSH connection
ansible all -m ping -vvv

# Common fixes
ansible all -m ping --ask-pass
ansible all -m ping --ask-become-pass
ansible all -m ping -e "ansible_ssh_port=2222"
```

#### Debug Information
```yaml
- name: Display all variables
  debug:
    var: hostvars[inventory_hostname]

- name: Display specific variable
  debug:
    var: my_variable

- name: Conditional debug
  debug:
    msg: "Variable value is {{ my_var }}"
  when: debug_mode | default(false)
```

#### Verbose Output
```bash
ansible-playbook playbook.yml -v     # Verbose
ansible-playbook playbook.yml -vv    # More verbose
ansible-playbook playbook.yml -vvv   # Debug
ansible-playbook playbook.yml -vvvv  # Connection debug
```

#### Syntax Checking
```bash
ansible-playbook playbook.yml --syntax-check
ansible-playbook playbook.yml --check  # Dry run
ansible-playbook playbook.yml --diff   # Show differences
```

#### Step-by-Step Execution
```bash
ansible-playbook playbook.yml --step
ansible-playbook playbook.yml --start-at-task="Install packages"
```

### Log Analysis
```bash
# Enable logging in ansible.cfg
log_path = /var/log/ansible.log

# Analyze logs
tail -f /var/log/ansible.log
grep ERROR /var/log/ansible.log
```

### Performance Analysis
```yaml
- name: Time a task
  command: /usr/bin/long_command
  register: result
  
- name: Display execution time
  debug:
    msg: "Task took {{ result.delta }} to complete"
```

### Common Error Messages and Solutions

#### "Host key checking failed"
```bash
# In ansible.cfg
host_key_checking = False

# Or use environment variable
export ANSIBLE_HOST_KEY_CHECKING=False
```

#### "Permission denied"
```yaml
# Use become
- name: Task requiring privileges
  command: systemctl restart httpd
  become: yes
```

#### "Module not found"
```bash
# Check module path
ansible-config dump | grep DEFAULT_MODULE_PATH

# Install missing collections
ansible-galaxy collection install community.general
```

---

This comprehensive guide covers all the essential Ansible concepts you need to master automation. Start with the basics and gradually work your way through the advanced topics. Remember to practice with real examples and always test your playbooks in a safe environment before production use.