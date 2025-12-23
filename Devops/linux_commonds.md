# 1. file
# 2. commands
# 3. software
# 4. servers



        open source software is a software with source code that anyone can inspect, modify and inhance.

        configuration file are stored in /etc

        server data is located in /var or /srv
        
        RHEL & Centos are RPM based OS & Ubuntu is Debian Based OS.
- Every thing is file in linux
```
With adduser command, the home folder for the user will be created as default.
With useradd command, there is no home folder for the user.
 ```
# Why linux as a server
- Opensource
- Community support
- Support wide veriety of hardware
- Customization
- Most server run on linux
- Automation
- Security
# Hardware->Kernel->shell->applications
# Directory system in linux

## 1. / (Root Directory)
The root of the entire file system. All other directories and files are nested under this directory. Only the root user has the ability to modify this directory.

## 2. /bin (Binaries)
Contains essential user binaries (executable programs) needed for system operation in both single-user and multi-user mode. Commands like ls, cp, mv, cat, etc., are stored here.
## 3. /boot
Stores bootloader files and the Linux kernel. This directory includes files necessary to boot the system, such as GRUB configuration files and the kernel itself (vmlinuz).
## 4. /dev (Devices)
Contains device files representing hardware components like hard drives, USB devices, and terminals. For example, /dev/sda might represent a hard disk.
## 5. /etc (Configuration Files)
Contains all the system-wide configuration files and shell scripts that startup services. This includes network settings, user account information, and application configurations (e.g., /etc/passwd for user accounts).
## 6. /home
This is where user home directories are located. Each user has a personal folder here (e.g., /home/username), where they can store personal files, settings, and data.
## 7. /lib (Libraries)
Contains shared libraries (similar to DLL files in Windows) required by system binaries and programs located in /bin and /sbin.
## 8. /media
This is where removable media such as USB drives, DVDs, and SD cards are automatically mounted when connected to the system.
## 9. /mnt (Mount)
A temporary mount point for manually mounting file systems, such as external hard drives or network shares. This is often used for temporary mounting during system administration.
## 10. /opt (Optional Software)
Stores optional software or third-party applications that aren’t part of the default Ubuntu installation. Commercial or proprietary software may be installed here.
## 11. /proc (Process Information)
A virtual file system that provides information about currently running processes and system resources. Files in this directory, like /proc/cpuinfo, provide dynamic information about the system’s hardware and running processes.
## 12. /root
The home directory of the root user (superuser). This is different from /home, which contains home directories for normal users. Only the root user has access to this directory.
## 13. /run
Contains run-time data such as information about the running system since the last boot. It holds data like process IDs and other system states.
## 14. /sbin (System Binaries)
Stores essential system administration binaries. These are commands used for system management and maintenance (e.g., ifconfig, reboot, shutdown). It is similar to /bin but contains commands primarily for the root user.
## 15. /srv (Service Data)
Holds data for services provided by the system, such as web servers (Apache) or FTP servers. For example, a web server might store website files in /srv/www.
## 16. /sys
Another virtual file system like /proc, but it provides access to kernel data structures. It is used to view and interact with the kernel's device tree.
## 17. /tmp (Temporary Files)
Stores temporary files created by applications and the system. Files here are typically deleted automatically after a certain period or upon system reboot.
## 18. /usr (User Programs)
Contains user binaries, documentation, libraries, and source code. Key subdirectories include:
/usr/bin: Non-essential user binaries.
/usr/sbin: Non-essential system binaries.
/usr/lib: Shared libraries for binaries in /usr/bin and /usr/sbin.
/usr/share: Architecture-independent data, like icons, documentation, and default configurations.
## 19. /var (Variable Data)
Contains files that are expected to grow in size over time, such as logs, caches, and mail spools. Important subdirectories include:
/var/log: System and application log files.
/var/tmp: Temporary files preserved between reboots.
/var/spool: Data waiting to be processed, like mail queues.

# vim Editor
There are three modes in vim
## Command mode 
when we entre in the file then it is in command mode. press esc keyword to go in command mode.
## Insert mode 
it comes when we press i key to enter something
## extended mode
go in command mode then perfprm some operation with : comminng in extended mode q/wq/q!
## : se nu
this command is used set line number in file.
## sift + g 
it is used go on the last line and gg command is used to go on first line
## n yy & p
n yy is used to copy n line and p is used to paste below.
## n dd & p
This command is used to cut n lines and p is used for paste below.

## /search keyword
this command is used to search in command mode

## :%s/search/replace/g
This command is used for replacing every occurance of search with replace. if we do not use g it will replace first occurance of in the line only.
# Commands 
##   sudo lsof -i :8443
        
This command will give which service is running on port 8443
##  whoami 
This command is used for current logged in user.
## cat /etc/os-release
This commond is used to see os related information.
## mkdir dir1 dir2
This command is used make directory dir1 and dir2
## touch devops{1..10}.txt
This will create 1 to 10 .txt file with name devops.

# File system
Everything in linux is file

## file /path/of/file
This command is used to check the type of file is.
## ls -l
This command is used to check the type of file

        - indicates a file
        d indicated directory
        l indicates link file
        c indicates character file
        b indicates block(storage/memory) file
        s is for socket file
        p is for pipe file
        ln -s <orignalFilePath> <LinkFilePath> command is used to create soft link.


# filter and I/O Redirections

## grep -i string /file/path
This command is used to search string in the given file. Here -i is used for ignoring case sensitivity.
## grep -iR string * 
This command is used for searching string in all the file in the current directory. R is used for recursive.
## grep -iv search /file/path
this command is used to search except search keyword.
## less & more are reader command
## head -n /file/path
it is used for reading first n line of file
## tail -n /file/path
This is used for last n lines of the file
## tail -f /file/path 
This command is used to check live changes in the file.This command is used for trobleshooting purpose.

## ps aux | grep python | awk '{print $2}'
This command is used for listing all the running process and then take line which contains python as a keyword and then take 2nd attribute of each line.

## sed -i `s/search/replace/g` /file/path
This command is used for finding search and replacing this with replace
every occurance. if you are using i then it will find and replace otherwise it will find only.
## ls > /file/path
this command is used to write the output of the ls command in the file.
## ls >> /file/path
 This command is used for append the output of the cammnand in the file.
 ## df -h
 This command is used for showing harddisk partition utilization.
 ## df -h 1>> file.txt
 In this command 1 is used for for standard output and it is default. 2 is used for standard error. & is used for both standard output and error.
 ## ls | wc -l
 This command is used for count the number of files in current dirctory.

 ## Users and Groups
 There are three types of user in system
 1. Root user with user id 0 and group id 0 and home directory /root and shell is /bin/bash
 2. regular user with user and group id in range 1k-60k and home directory /home/user and shell /bin/bash
 3. Service user(ftp/ssh/apache) with user and group id in range 1-999 /var/ftp and shell /sbin/nologin
   
## id usename
this command will give user related info like user id group id and all those groups list which this user belongs.
## adduser username
this command is used for adding user
## groupadd groupname
This command is used for adding group
## addgroup -aG group user
This command is used to add user to group
## vim /etc/group
this command can used for adding user to a group using , seperated.
## passwd user
This command is used for setting password for user.This is used for changing or first time adding password. corrent logged in user can change password using passwd command as well.
## su - user
This command is used for swiching to user
## last 
This command is used for checking logs for last login user.
## who
This command is used for current login user.
## lsof -u user 
This command is used for cheking files open by user.
## userdel -r user
This command is used for deleting user and -r is used for deleting home directory files as well.
## groupdell group
This command is used for deleting group.
## Users password is stored(encrypted) in /etc/shadow file.


# File permissions
## ls -l
This command show list of file in a particular format. It start with 10 characters(first char indicates file type then next 3 user permission and next 3 group permission and last 3 for other permission). Each 3 character indicated read write and execute permissions.(r->read,w->writeand x->execute permission)

## chown -R User:group /file/dir
This command is used for changing the ower of a file or directory. use -R in case of directory only.
## chmod ugo+rwx
This command is used to add read write and execute permissions to user,group and others. you can use any combination of it. and - to remove permission from it.

## sudo 
### Only user in /etc/sudoers file or /etc/sudoers.d dir can use sudo -i command to switch to root user as mentioned below
### If user does not want to enter its password after running sudo command then add NOPASSWD option in user entry in sudoers as specific below username ALL=(ALL:ALL) NOPASSWD:ALL

### If normal user wants to run root commands and Admin cannot share root password as per compliance.
What should you do?
Ask admin to add your username in sudoers file.

# Packege management tools
## cat /etc/os-release
This commnand is used for checking your os type and its version.
## How to install single package in RedHat & Debian OS?
rpm -i packagename in RedHat .
dpkg -i packagename in Debian based Machine.
## Where are yum repos and apt repos files located?
/etc/yum.repose.d/ for yum
/etc/apt/sources.list and /etc/apt/cources.list.d for apt
## Before installing package in ubuntu with apt command, we should run apt update to refresh apt repository index.

# services
## systemctl start/stop/reload/status/is-active/is-enabled servicename
## systemctl enable servicename
This command is used to start service at boot time.

# process
## top 
This command is used for top processes
## ps aux
This command is used to show all the running process
## ps -ef
This will show parent process id
## ps aux | grep python | awk `{print $2}` | xargs kill -9
This command will kill all the python running processes.
## find difference betweeb arphon process and zombie process
A process is running even after its parent is terminated or completed without waiting for its child process to complete is called arphon process. A process is completed but still its entry is showing in process table is called zombie process.
## kill -9 PID 
command is to stop process forcefully and kill PID  is to stop process gracefully, child processes also will be stopped if parent process is stopped gracefully.

# Archive
## tar -czvf file.tar.gz /file/path
this command is used to convert tar file
## tar -xzvf /file/path
This command is used to archive tar file
## zip -r file.zip /file/path
make a zip file
## unzip file.zip
This unzip the file
# ubuntu cmds
## useradd user
This command creates user only
## adduser user
This command create user as well as home directory
## dpkg -l
It will show all the packages install 
## cat /etc/apt/sources.list
This will display packages repositiry information
## apt upgrade 
This command will upgrade all the packages
## apt remove package
This will remove package
## apt remove purge package
This will remove packe with data and configration

# provisioning
It means running script when vm comes up.






















