In Ubuntu (and Linux in general), files are categorized by their type and function. Here are the main types of files:

## 1. Regular Files:

These are ordinary data files that contain information. They can be text, binary, or executable files.
Examples: .txt, .jpg, .py, .sh
## 2. Directory Files:

These are special files that store lists of other files and directories.
Directories are essentially folders that contain other files.
## 3. Symbolic Links:

These are files that point to another file or directory. They are like shortcuts in Windows.
Example: ln -s target symlink
## 4. Block Device Files:

These represent hardware devices that read or write data in blocks, such as hard drives.
Example: /dev/sda
## 5. Character Device Files:

These represent hardware devices that transmit data as characters (e.g., keyboards, serial ports).
Example: /dev/tty
## 6. Socket Files:

These are used for inter-process communication and networking.
Example: /var/run/docker.sock
FIFO (Named Pipes):

## 7. FIFO (First In, First Out) files allow for communication between processes, where data flows in a specific order.
Example: A pipe created using mkfifo.
## 8. Executable Files:

These are files that can be run as programs. They contain binary code or scripts that the system can execute.
Example: Bash scripts (.sh) or compiled binaries.
Each type has a specific purpose, and you can use commands like ls -l or file in the terminal to identify the type of a file.
## ln -s <orignalFilePath> <LinkFilePath> command is used to create soft link.




