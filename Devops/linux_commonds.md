        open source software is a software with source code that anyone can insect, modify and inhance.

        configuration file are stored in /etc

        server data is located in /var or /srv
        
        RHEL & Centos are RPM based OS & Ubuntu is Debian Based OS.

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