# network
communication between two or more network interfaces.
## components of computer network
1. two or more computer devices
2. cable as a link between computers
3. A network Interface card in each computer(NIC)
4. switches(used for conncting multiple network intrefaces NIC)
5. Routers (Used for connecting Networks)
6. Software called os
# OSI Model
7. Application Layer :Network process to application
6. Presentation  Layer :The functions of the presentation layer are translation, encryption/decryption, and compression.
5. Session Layer : Interhost communication .This is the layer responsible for opening and closing communication between the two devices. The time between when the communication is opened and closed is known as the session.
4. Transport layer :It is responsible for end to end delivery and reliablity of the data. (Gateway) Data will be in the from of segment.
3. Network layer : Here transmission of data from one node to other node happens. It works on IP address. Here data will be in the form of packets. (Router,Firewall and Layer3 switch)
3. Data Link Layer : Here data will be in the form of frame. Physical addressing happens here. (Bridg,layer2 switch)
1. Physical Layer : Here Date will be in form of bits (Hub)

In Tcp/Ip model Application, Presentation and session layer collectivelly called Application layer.(web server,mail server,browser)

# Type of network
## Lan local Network
## Man Network in city
# WAN network in country or glob

# Ip Adress
## Class A :10.0.0.0->10.255.255.255
## class B 172.16.0.0-> 172.31.255.255
## class c 192.168.0.0->192.168.255.255

# Protocals
## TCP 
It is a reliable protocals like http,https,ftp
## UDP 
It is unriable protocals like dns,arp rarp,dhcp, tftp
# Ports
        DNS-> 53
        HTTP-> 80
        HTTPS->443
        SMTP->25
        FTP->20/21
        SSH->22
# Commands for Network
## ifconfig
This command will show all the active network interfaces and their ip adress
## show ip addr
This command will show your own ip address
## ping ip
This command will show network connectivity with ip adress. If want to communticate with a machine using name instead of ip then add ip with a name in /etc/hosts file.
## netstat -antp
This command will show all the opend tcp ports.
## ss -tunlp
This will all the tcp and udp open port
## nmap localhost
This will show all the open port on the machine. This command can be used for other machine as well. This can be used for toubleshouting purpose for checking which post is open for communication.
## dig www.google.com
This is used for checking for dns resolution is working or not in your computer.
## route -n
This command used to check gateways.
## arp
THis command is used to data to kernel arp table.
## mtr www.google.com
This command is used for packet lost



