# Computer Network Interview Questions & Answers

## 1. What is Computer Network? What are its advantages?

A Computer Network is a collection of interconnected computing devices that can communicate and share resources with each other. These devices include computers, servers, routers, switches, and other network equipment.

**Advantages of Computer Networks:**

- **Resource Sharing**: Share files, printers, internet connection, and applications
- **Communication**: Email, instant messaging, video conferencing
- **Cost Reduction**: Share expensive resources like printers and servers
- **Centralized Data Management**: Centralized backup and security
- **Scalability**: Easy to add new devices to the network
- **Remote Access**: Access resources from anywhere
- **Reliability**: Redundancy and fault tolerance
- **Performance**: Load distribution across multiple servers

## 2. Explain the OSI Model and its layers.

The OSI (Open Systems Interconnection) Model is a conceptual framework that standardizes network communication into seven layers.

**OSI Model Layers (Bottom to Top):**

### Layer 1 - Physical Layer
- **Function**: Transmits raw bits over physical medium
- **Components**: Cables, hubs, repeaters, network adapters
- **Examples**: Ethernet cables, fiber optic cables, wireless signals
- **Protocols**: RS-232, RJ-45

### Layer 2 - Data Link Layer
- **Function**: Error detection, correction, and frame synchronization
- **Components**: Switches, bridges, NICs
- **Addressing**: MAC addresses
- **Protocols**: Ethernet, PPP, Wi-Fi (802.11)

### Layer 3 - Network Layer
- **Function**: Routing and logical addressing
- **Components**: Routers, Layer 3 switches
- **Addressing**: IP addresses
- **Protocols**: IP, ICMP, ARP, OSPF, BGP

### Layer 4 - Transport Layer
- **Function**: End-to-end delivery and error recovery
- **Services**: Segmentation, flow control, error control
- **Protocols**: TCP, UDP
- **Addressing**: Port numbers

### Layer 5 - Session Layer
- **Function**: Establishes, manages, and terminates sessions
- **Services**: Session establishment, synchronization
- **Protocols**: NetBIOS, RPC, SQL sessions

### Layer 6 - Presentation Layer
- **Function**: Data formatting, encryption, compression
- **Services**: Data translation, encryption/decryption
- **Protocols**: SSL/TLS, JPEG, MPEG, ASCII

### Layer 7 - Application Layer
- **Function**: Network services to applications
- **Services**: File transfer, email, web browsing
- **Protocols**: HTTP, HTTPS, FTP, SMTP, DNS, DHCP

## 3. What is the difference between TCP and UDP?

| TCP (Transmission Control Protocol) | UDP (User Datagram Protocol) |
|-------------------------------------|------------------------------|
| Connection-oriented protocol | Connectionless protocol |
| Reliable data delivery | Unreliable data delivery |
| Guaranteed packet delivery | No guarantee of packet delivery |
| Maintains packet order | No guarantee of packet order |
| Flow control and congestion control | No flow control |
| Higher overhead | Lower overhead |
| Slower transmission | Faster transmission |
| Error detection and correction | Basic error detection only |
| Used for: HTTP, FTP, Email | Used for: DNS, DHCP, Video streaming |

**TCP Features:**
- Three-way handshake for connection establishment
- Sequence numbers for ordering
- Acknowledgments for reliability
- Window-based flow control

**UDP Features:**
- Simple header structure
- No connection establishment
- Best-effort delivery
- Suitable for real-time applications

## 4. Explain IP Addressing and different classes of IP addresses.

**IP Address** is a unique identifier assigned to each device on a network for communication purposes.

### IPv4 Address Structure
- 32-bit address (4 bytes)
- Written in dotted decimal notation (e.g., 192.168.1.1)
- Divided into network and host portions

### IP Address Classes

#### Class A
- **Range**: 1.0.0.0 to 126.255.255.255
- **Default Subnet Mask**: 255.0.0.0 (/8)
- **Network Bits**: 8, **Host Bits**: 24
- **Number of Networks**: 126
- **Hosts per Network**: 16,777,214
- **Usage**: Large organizations

#### Class B
- **Range**: 128.0.0.0 to 191.255.255.255
- **Default Subnet Mask**: 255.255.0.0 (/16)
- **Network Bits**: 16, **Host Bits**: 16
- **Number of Networks**: 16,384
- **Hosts per Network**: 65,534
- **Usage**: Medium-sized organizations

#### Class C
- **Range**: 192.0.0.0 to 223.255.255.255
- **Default Subnet Mask**: 255.255.255.0 (/24)
- **Network Bits**: 24, **Host Bits**: 8
- **Number of Networks**: 2,097,152
- **Hosts per Network**: 254
- **Usage**: Small organizations

#### Class D (Multicast)
- **Range**: 224.0.0.0 to 239.255.255.255
- **Usage**: Multicast groups

#### Class E (Reserved)
- **Range**: 240.0.0.0 to 255.255.255.255
- **Usage**: Experimental purposes

### Special IP Addresses
- **Loopback**: 127.0.0.1 (localhost)
- **Private Addresses**: 
  - 10.0.0.0/8
  - 172.16.0.0/12
  - 192.168.0.0/16
- **APIPA**: 169.254.0.0/16 (Automatic Private IP Addressing)

## 5. What is Subnetting? How does it work?

**Subnetting** is the process of dividing a large network into smaller, more manageable sub-networks (subnets).

**Benefits of Subnetting:**
- Improved network performance
- Enhanced security
- Better network management
- Efficient IP address utilization
- Reduced broadcast traffic

### Subnetting Example

**Original Network**: 192.168.1.0/24 (256 addresses)

**Requirement**: Create 4 subnets

**Solution**:
- Borrow 2 bits from host portion (2² = 4 subnets)
- New subnet mask: /26 (255.255.255.192)
- Each subnet has 64 addresses (62 usable)

**Resulting Subnets**:
1. 192.168.1.0/26 (192.168.1.1 - 192.168.1.62)
2. 192.168.1.64/26 (192.168.1.65 - 192.168.1.126)
3. 192.168.1.128/26 (192.168.1.129 - 192.168.1.190)
4. 192.168.1.192/26 (192.168.1.193 - 192.168.1.254)

### VLSM (Variable Length Subnet Masking)
- Different subnets can have different subnet mask lengths
- More efficient IP address utilization
- Requires classless routing protocols

## 6. Explain DNS (Domain Name System) and how it works.

**DNS** is a hierarchical distributed naming system that translates human-readable domain names into IP addresses.

### DNS Hierarchy
```
Root (.)
    |
Top-Level Domains (.com, .org, .net, .edu)
    |
Second-Level Domains (google.com, facebook.com)
    |
Subdomains (www.google.com, mail.google.com)
```

### DNS Record Types
- **A Record**: Maps domain name to IPv4 address
- **AAAA Record**: Maps domain name to IPv6 address
- **CNAME**: Canonical name (alias) for another domain
- **MX Record**: Mail exchange server information
- **NS Record**: Name server information
- **PTR Record**: Reverse DNS lookup (IP to domain)
- **SOA Record**: Start of Authority information
- **TXT Record**: Text information

### DNS Resolution Process
1. **User enters URL** in browser
2. **Browser checks cache** for IP address
3. **Query local DNS resolver** (ISP's DNS server)
4. **Resolver queries root name server**
5. **Root server responds** with TLD server address
6. **Resolver queries TLD server**
7. **TLD server responds** with authoritative server address
8. **Resolver queries authoritative server**
9. **Authoritative server responds** with IP address
10. **IP address returned** to browser
11. **Browser connects** to web server

### DNS Caching
- Browsers cache DNS responses
- DNS resolvers cache responses
- TTL (Time To Live) determines cache duration
- Reduces DNS query load and improves performance

## 7. What is DHCP? How does it work?

**DHCP (Dynamic Host Configuration Protocol)** automatically assigns IP addresses and network configuration to devices on a network.

### DHCP Components
- **DHCP Server**: Assigns IP addresses and configuration
- **DHCP Client**: Requests IP address configuration
- **DHCP Relay Agent**: Forwards DHCP messages across subnets
- **DHCP Scope**: Range of IP addresses available for assignment

### DHCP Process (DORA)

#### 1. DISCOVER
- Client broadcasts DHCP Discover message
- Sent to 255.255.255.255 (broadcast)
- Source IP: 0.0.0.0

#### 2. OFFER
- DHCP server responds with DHCP Offer
- Contains available IP address and lease information
- Unicast or broadcast to client

#### 3. REQUEST
- Client broadcasts DHCP Request
- Accepts the offered IP address
- May receive multiple offers, accepts one

#### 4. ACKNOWLEDGE
- Server sends DHCP Acknowledgment
- Confirms IP address lease
- Includes lease duration and other parameters

### DHCP Configuration Parameters
- **IP Address**: Assigned to client
- **Subnet Mask**: Network portion identification
- **Default Gateway**: Router IP address
- **DNS Servers**: Domain name resolution
- **Lease Time**: Duration of IP address assignment
- **WINS Server**: NetBIOS name resolution

### DHCP Lease Renewal
- Client attempts renewal at 50% of lease time
- If no response, tries again at 87.5%
- If still no response, starts new DHCP process

## 8. Explain different types of Network Topologies.

Network topology refers to the physical or logical arrangement of network devices.

### Physical Topologies

#### Bus Topology
- **Structure**: All devices connected to a single cable (bus)
- **Advantages**: Simple, cost-effective, easy to implement
- **Disadvantages**: Single point of failure, performance degrades with more devices
- **Usage**: Early Ethernet networks

#### Star Topology
- **Structure**: All devices connected to central hub/switch
- **Advantages**: Easy to troubleshoot, failure of one device doesn't affect others
- **Disadvantages**: Central device failure affects entire network
- **Usage**: Modern Ethernet networks

#### Ring Topology
- **Structure**: Devices connected in circular fashion
- **Advantages**: Equal access to network, no collisions
- **Disadvantages**: Failure of one device affects entire network
- **Usage**: Token Ring networks, FDDI

#### Mesh Topology
- **Structure**: Every device connected to every other device
- **Full Mesh**: All devices interconnected
- **Partial Mesh**: Some devices have multiple connections
- **Advantages**: High redundancy, fault tolerance
- **Disadvantages**: Expensive, complex to manage
- **Usage**: Internet backbone, WANs

#### Tree Topology
- **Structure**: Hierarchical structure with root and branches
- **Advantages**: Scalable, supports prioritization
- **Disadvantages**: Root failure affects entire network
- **Usage**: Large networks, WAN connections

#### Hybrid Topology
- **Structure**: Combination of multiple topologies
- **Advantages**: Flexible, scalable
- **Disadvantages**: Complex design and management
- **Usage**: Large enterprise networks

## 9. What is Switching? Explain different types of switching.

**Switching** is the process of forwarding data packets between devices in a network.

### Types of Switching

#### Circuit Switching
- **Method**: Dedicated physical path established for entire communication
- **Characteristics**:
  - Connection-oriented
  - Fixed bandwidth allocation
  - No sharing of path during communication
- **Advantages**: Guaranteed bandwidth, predictable performance
- **Disadvantages**: Inefficient resource utilization
- **Example**: Traditional telephone networks

#### Packet Switching
- **Method**: Data divided into packets, each routed independently
- **Characteristics**:
  - Connectionless or connection-oriented
  - Dynamic route selection
  - Statistical multiplexing
- **Advantages**: Efficient resource utilization, fault tolerance
- **Disadvantages**: Variable delay, packet loss possible
- **Example**: Internet, IP networks

#### Message Switching
- **Method**: Entire message stored and forwarded by intermediate nodes
- **Characteristics**:
  - Store-and-forward mechanism
  - No direct connection between source and destination
- **Advantages**: Efficient for small messages
- **Disadvantages**: High delay for large messages
- **Example**: Email systems

### Layer 2 Switching (Ethernet Switching)
- **Function**: Forwards frames based on MAC addresses
- **Features**:
  - MAC address learning
  - Broadcast domain separation (VLANs)
  - Collision domain separation
  - Full-duplex communication

### Layer 3 Switching (IP Switching)
- **Function**: Routes packets based on IP addresses
- **Features**:
  - IP routing capability
  - VLAN routing
  - Access Control Lists (ACLs)
  - Quality of Service (QoS)

## 10. What is Routing? Explain static vs dynamic routing.

**Routing** is the process of selecting paths in a network to send data packets from source to destination.

### Static Routing
- **Definition**: Routes manually configured by network administrator
- **Characteristics**:
  - Fixed routing table entries
  - No automatic route updates
  - Administrative configuration required

**Advantages:**
- Simple configuration for small networks
- No routing protocol overhead
- Predictable routing behavior
- More secure (no routing advertisements)

**Disadvantages:**
- Manual configuration required
- No automatic failure recovery
- Not scalable for large networks
- Difficult to maintain

**Configuration Example:**
```
ip route 192.168.2.0 255.255.255.0 10.1.1.2
```

### Dynamic Routing
- **Definition**: Routes automatically learned and updated using routing protocols
- **Characteristics**:
  - Automatic route discovery
  - Automatic route updates
  - Adaptive to network changes

**Advantages:**
- Automatic route discovery
- Fault tolerance and recovery
- Scalable for large networks
- Reduced administrative overhead

**Disadvantages:**
- More complex configuration
- Routing protocol overhead
- Convergence time for route updates
- Potential security vulnerabilities

### Dynamic Routing Protocols

#### Distance Vector Protocols
- **Examples**: RIP, EIGRP
- **Characteristics**:
  - Share routing table with neighbors
  - Use hop count or composite metrics
  - Slower convergence
- **Algorithm**: Bellman-Ford algorithm

#### Link State Protocols
- **Examples**: OSPF, IS-IS
- **Characteristics**:
  - Share link state information
  - Build complete network topology
  - Faster convergence
- **Algorithm**: Dijkstra's shortest path algorithm

#### Path Vector Protocols
- **Examples**: BGP
- **Characteristics**:
  - Share path information
  - Policy-based routing
  - Used between autonomous systems

## 11. Explain HTTP vs HTTPS and how SSL/TLS works.

### HTTP (HyperText Transfer Protocol)
- **Port**: 80
- **Security**: No encryption (plain text)
- **Speed**: Faster (no encryption overhead)
- **Usage**: Non-sensitive data transfer

### HTTPS (HTTP Secure)
- **Port**: 443
- **Security**: Encrypted using SSL/TLS
- **Speed**: Slightly slower (encryption overhead)
- **Usage**: Sensitive data transfer (login, payment)

### SSL/TLS Working Process

#### 1. SSL/TLS Handshake
```
Client                          Server
  |                               |
  |------ Client Hello --------->|
  |                               |
  |<----- Server Hello -----------|
  |<----- Certificate -----------|
  |<----- Server Hello Done -----|
  |                               |
  |------ Client Key Exchange -->|
  |------ Change Cipher Spec --->|
  |------ Finished ------------->|
  |                               |
  |<----- Change Cipher Spec ----|
  |<----- Finished --------------|
  |                               |
  |<===== Encrypted Data ======>|
```

#### 2. Certificate Verification
- Client verifies server certificate
- Checks certificate authority (CA) signature
- Validates certificate expiration
- Confirms domain name match

#### 3. Key Exchange
- Client generates pre-master secret
- Encrypts with server's public key
- Server decrypts with private key
- Both derive session keys

#### 4. Secure Communication
- All data encrypted with session keys
- Symmetric encryption for performance
- Message authentication codes (MAC) for integrity

### SSL/TLS Security Features
- **Encryption**: Data confidentiality
- **Authentication**: Server identity verification
- **Integrity**: Data tampering detection
- **Non-repudiation**: Proof of data origin

## 12. What is NAT (Network Address Translation)? Types of NAT.

**NAT** translates private IP addresses to public IP addresses, allowing multiple devices to share a single public IP address.

### Why NAT is Used
- **IPv4 Address Conservation**: Reduces public IP address usage
- **Security**: Hides internal network structure
- **Cost Reduction**: Fewer public IP addresses needed
- **Network Management**: Simplifies internal addressing

### Types of NAT

#### Static NAT (One-to-One)
- **Mapping**: One private IP to one public IP
- **Characteristics**: Permanent mapping
- **Usage**: Servers that need consistent public IP
- **Example**: 192.168.1.10 ↔ 203.0.113.10

#### Dynamic NAT (Many-to-Many)
- **Mapping**: Multiple private IPs to pool of public IPs
- **Characteristics**: Temporary mapping from available pool
- **Usage**: General internet access
- **Limitation**: Number of public IPs limits concurrent connections

#### PAT (Port Address Translation) / NAT Overload
- **Mapping**: Multiple private IPs to single public IP using different ports
- **Characteristics**: Most common type of NAT
- **Usage**: Home and small office networks
- **Example**: 
  - 192.168.1.10:1024 → 203.0.113.1:2048
  - 192.168.1.11:1025 → 203.0.113.1:2049

### NAT Translation Table Example
| Inside Local | Inside Global | Outside Global | Outside Local |
|--------------|---------------|----------------|---------------|
| 192.168.1.10:1024 | 203.0.113.1:2048 | 8.8.8.8:53 | 8.8.8.8:53 |
| 192.168.1.11:1025 | 203.0.113.1:2049 | 74.125.224.72:80 | 74.125.224.72:80 |

### NAT Limitations
- **End-to-end connectivity issues**: Breaks some applications
- **Protocol complications**: FTP, SIP, P2P applications
- **Security concerns**: Port scanning, logging
- **IPv6 compatibility**: Not needed with IPv6

## 13. Explain VPN (Virtual Private Network) and its types.

**VPN** creates a secure, encrypted connection over a public network, allowing remote access to private networks.

### VPN Benefits
- **Security**: Encrypted data transmission
- **Privacy**: Anonymous internet browsing
- **Remote Access**: Access company resources from anywhere
- **Cost Effective**: Uses existing internet infrastructure
- **Geo-restriction Bypass**: Access region-locked content

### Types of VPN

#### Site-to-Site VPN
- **Purpose**: Connects entire networks
- **Usage**: Branch offices to headquarters
- **Implementation**: Router-to-router connection
- **Protocols**: IPSec, GRE

#### Remote Access VPN (Client-to-Site)
- **Purpose**: Individual users access corporate network
- **Usage**: Employees working from home
- **Implementation**: VPN client software
- **Protocols**: SSL/TLS, IPSec, PPTP, L2TP

#### Client-to-Client VPN (P2P)
- **Purpose**: Direct connection between two clients
- **Usage**: File sharing, gaming
- **Implementation**: Peer-to-peer software

### VPN Protocols

#### IPSec (Internet Protocol Security)
- **Layer**: Network layer (Layer 3)
- **Modes**: Transport mode, Tunnel mode
- **Security**: Strong encryption and authentication
- **Usage**: Site-to-site VPNs

#### SSL/TLS VPN
- **Layer**: Application layer (Layer 7)
- **Access**: Web browser based
- **Ease of Use**: No client software required
- **Usage**: Remote access VPNs

#### PPTP (Point-to-Point Tunneling Protocol)
- **Security**: Weak encryption (deprecated)
- **Speed**: Fast
- **Usage**: Legacy systems (not recommended)

#### L2TP/IPSec
- **Combination**: L2TP for tunneling + IPSec for security
- **Security**: Strong encryption
- **Usage**: Remote access VPNs

#### OpenVPN
- **Type**: Open-source SSL/TLS based
- **Security**: Strong encryption
- **Flexibility**: Highly configurable
- **Usage**: Various VPN implementations

### VPN Architecture Components
- **VPN Server**: Authenticates and manages connections
- **VPN Client**: Initiates connection to VPN server
- **Tunnel**: Encrypted pathway for data
- **Authentication Server**: Verifies user credentials
- **Encryption**: Protects data in transit

## 14. What is VLAN? How does VLAN work?

**VLAN (Virtual Local Area Network)** logically segments a physical network into multiple broadcast domains.

### VLAN Benefits
- **Network Segmentation**: Logical separation of devices
- **Security**: Isolate sensitive traffic
- **Performance**: Reduce broadcast traffic
- **Flexibility**: Easy device reassignment
- **Cost Effective**: No additional hardware required

### Types of VLANs

#### Port-based VLAN (Static)
- **Assignment**: Ports assigned to specific VLANs
- **Configuration**: Manual assignment
- **Characteristics**: Device location determines VLAN membership

#### MAC-based VLAN (Dynamic)
- **Assignment**: Based on device MAC address
- **Configuration**: MAC address database
- **Characteristics**: Device follows user regardless of location

#### Protocol-based VLAN
- **Assignment**: Based on network protocol
- **Examples**: IP traffic in one VLAN, IPX in another

### VLAN Implementation

#### VLAN Tagging (802.1Q)
- **Frame Format**: Additional 4-byte tag inserted
- **Tag Contents**: 
  - TPID (Tag Protocol Identifier): 0x8100
  - TCI (Tag Control Information): Priority + VLAN ID
- **VLAN ID Range**: 1-4094 (0 and 4095 reserved)

#### Trunk Ports
- **Purpose**: Carry traffic for multiple VLANs
- **Tagging**: All frames tagged except native VLAN
- **Usage**: Switch-to-switch connections

#### Access Ports
- **Purpose**: Connect end devices to single VLAN
- **Tagging**: Frames not tagged (untagged)
- **Usage**: Connect PCs, servers, printers

### VLAN Configuration Example
```
Switch(config)# vlan 10
Switch(config-vlan)# name Sales
Switch(config-vlan)# exit

Switch(config)# vlan 20
Switch(config-vlan)# name Engineering
Switch(config-vlan)# exit

Switch(config)# interface fa0/1
Switch(config-if)# switchport mode access
Switch(config-if)# switchport access vlan 10

Switch(config)# interface fa0/24
Switch(config-if)# switchport mode trunk
Switch(config-if)# switchport trunk allowed vlan 10,20
```

### Inter-VLAN Routing
- **Problem**: VLANs cannot communicate by default
- **Solutions**:
  - **Router on a Stick**: Single router interface with subinterfaces
  - **Layer 3 Switch**: Switch with routing capability
  - **Separate Router Interfaces**: One interface per VLAN

## 15. Explain different types of Network Attacks and Security measures.

### Common Network Attacks

#### Denial of Service (DoS) Attack
- **Purpose**: Make network resources unavailable
- **Methods**: 
  - Flooding with requests
  - Resource exhaustion
  - Protocol exploitation
- **Types**: SYN flood, UDP flood, ICMP flood
- **Mitigation**: Rate limiting, load balancing, firewalls

#### Distributed Denial of Service (DDoS) Attack
- **Purpose**: DoS attack from multiple sources
- **Methods**: Botnet coordination
- **Impact**: Difficult to block due to multiple sources
- **Mitigation**: DDoS protection services, traffic analysis

#### Man-in-the-Middle (MITM) Attack
- **Purpose**: Intercept communication between two parties
- **Methods**: 
  - ARP spoofing
  - DNS spoofing
  - SSL stripping
- **Mitigation**: Encryption, certificate validation, VPN

#### Packet Sniffing
- **Purpose**: Capture and analyze network traffic
- **Tools**: Wireshark, tcpdump
- **Risk**: Sensitive data exposure
- **Mitigation**: Encryption, switched networks, VLANs

#### SQL Injection
- **Purpose**: Execute malicious SQL commands
- **Method**: Inject SQL code through input fields
- **Impact**: Database compromise
- **Mitigation**: Input validation, parameterized queries

#### Cross-Site Scripting (XSS)
- **Purpose**: Execute malicious scripts in user's browser
- **Types**: Stored, reflected, DOM-based
- **Mitigation**: Input validation, output encoding

#### Phishing
- **Purpose**: Steal credentials through deception
- **Methods**: Fake websites, emails
- **Mitigation**: User education, email filtering

### Network Security Measures

#### Firewalls
- **Function**: Filter traffic based on rules
- **Types**: 
  - Packet filtering
  - Stateful inspection
  - Application layer
  - Next-generation firewalls (NGFW)

#### Intrusion Detection System (IDS)
- **Function**: Monitor and detect suspicious activities
- **Types**: 
  - Network-based IDS (NIDS)
  - Host-based IDS (HIDS)
- **Detection Methods**: Signature-based, anomaly-based

#### Intrusion Prevention System (IPS)
- **Function**: Detect and prevent malicious activities
- **Placement**: Inline with network traffic
- **Actions**: Block, alert, log suspicious traffic

#### Access Control Lists (ACLs)
- **Function**: Control traffic flow based on criteria
- **Types**: Standard, extended
- **Criteria**: Source/destination IP, ports, protocols

#### Virtual Private Networks (VPNs)
- **Function**: Secure remote access
- **Encryption**: IPSec, SSL/TLS
- **Authentication**: Username/password, certificates

#### Network Segmentation
- **Function**: Isolate network segments
- **Methods**: VLANs, subnets, firewalls
- **Benefits**: Contain breaches, improve performance

## 16. What is Quality of Service (QoS)? Why is it important?

**Quality of Service (QoS)** is a set of technologies that manage network traffic to ensure optimal performance for critical applications.

### QoS Parameters
- **Bandwidth**: Data transmission capacity
- **Delay (Latency)**: Time for packet to travel from source to destination
- **Jitter**: Variation in delay
- **Packet Loss**: Percentage of lost packets

### Applications Requiring QoS
- **Voice over IP (VoIP)**: Low latency, low jitter
- **Video Conferencing**: High bandwidth, low latency
- **Real-time Gaming**: Low latency, consistent performance
- **Streaming Media**: High bandwidth, controlled jitter
- **Critical Business Applications**: Guaranteed bandwidth

### QoS Mechanisms

#### Traffic Classification
- **Purpose**: Identify different types of traffic
- **Methods**: 
  - DSCP (Differentiated Services Code Point)
  - IP Precedence
  - Access Control Lists (ACLs)

#### Traffic Marking
- **Purpose**: Tag packets for QoS treatment
- **Locations**: Layer 2 (CoS), Layer 3 (DSCP, IP Precedence)

#### Traffic Shaping
- **Purpose**: Control traffic rate
- **Methods**: Token bucket, leaky bucket
- **Benefits**: Smooth traffic flow, prevent congestion

#### Traffic Policing
- **Purpose**: Enforce traffic rate limits
- **Actions**: Drop, mark down, forward
- **Difference from Shaping**: Immediate action vs buffering

#### Queuing
- **Purpose**: Manage packet transmission order
- **Algorithms**:
  - First In First Out (FIFO)
  - Priority Queuing (PQ)
  - Weighted Fair Queuing (WFQ)
  - Class-Based Weighted Fair Queuing (CBWFQ)

#### Congestion Avoidance
- **Purpose**: Prevent network congestion
- **Methods**: 
  - Random Early Detection (RED)
  - Weighted Random Early Detection (WRED)

### QoS Models

#### Best Effort
- **Characteristics**: No QoS guarantees
- **Usage**: Traditional internet traffic
- **Treatment**: All traffic treated equally

#### Integrated Services (IntServ)
- **Characteristics**: Per-flow QoS guarantees
- **Protocol**: RSVP (Resource Reservation Protocol)
- **Scalability**: Limited due to per-flow state

#### Differentiated Services (DiffServ)
- **Characteristics**: Class-based QoS
- **Scalability**: Highly scalable
- **Implementation**: DSCP marking, PHBs (Per-Hop Behaviors)

## 17. Explain Network Troubleshooting tools and techniques.

### Network Troubleshooting Methodology

#### 1. Problem Identification
- Define the problem clearly
- Gather information from users
- Determine scope of impact

#### 2. Information Gathering
- Network topology
- Recent changes
- Error messages
- Timeline of issues

#### 3. Hypothesis Development
- Possible causes
- Layer-by-layer analysis
- Most likely scenarios

#### 4. Testing and Implementation
- Test hypotheses systematically
- Implement solutions
- Monitor results

#### 5. Documentation
- Record problem and solution
- Update network documentation
- Share knowledge with team

### Network Troubleshooting Tools

#### Ping
- **Purpose**: Test connectivity and reachability
- **Protocol**: ICMP Echo Request/Reply
- **Information**: RTT, packet loss
- **Usage**: `ping 8.8.8.8`

#### Traceroute/Tracert
- **Purpose**: Trace packet path to destination
- **Method**: Incrementing TTL values
- **Information**: Hop-by-hop latency
- **Usage**: `traceroute google.com`

#### Nslookup/Dig
- **Purpose**: DNS troubleshooting
- **Functions**: DNS queries, reverse lookups
- **Information**: DNS records, server responses
- **Usage**: `nslookup google.com`

#### Netstat
- **Purpose**: Display network connections
- **Information**: 
  - Active connections
  - Listening ports
  - Routing table
  - Network statistics
- **Usage**: `netstat -an`

#### Wireshark
- **Purpose**: Network packet analysis
- **Capabilities**: 
  - Packet capture
  - Protocol analysis
  - Traffic statistics
  - Filter and search

#### ARP
- **Purpose**: Address Resolution Protocol management
- **Functions**: View/modify ARP table
- **Usage**: `arp -a`

#### Ipconfig/Ifconfig
- **Purpose**: Network interface configuration
- **Information**: IP address, subnet mask, gateway
- **Functions**: Release/renew DHCP lease
- **Usage**: `ipconfig /all`

### Layer-specific Troubleshooting

#### Physical Layer (Layer 1)
- Check cable connections
- Verify cable integrity
- Test network interfaces
- Check power and LED indicators

#### Data Link Layer (Layer 2)
- Verify MAC addresses
- Check switch port status
- Analyze VLAN configuration
- Check for duplex mismatches
- Monitor collision and error counters

#### Network Layer (Layer 3)
- Verify IP configuration
- Check routing tables
- Test gateway connectivity
- Analyze subnet masks
- Verify DHCP/static IP settings

#### Transport Layer (Layer 4)
- Check port accessibility
- Verify firewall rules
- Test specific services
- Monitor connection states
- Analyze TCP/UDP behavior

#### Application Layer (Layer 7)
- Test application-specific functions
- Check service availability
- Verify application configuration
- Monitor application logs
- Test user authentication

### Common Network Issues and Solutions

#### Connectivity Issues
- **Symptoms**: Cannot reach destination
- **Causes**: Physical problems, routing issues, firewall blocking
- **Troubleshooting**: Ping test, traceroute, check cables
- **Solutions**: Fix physical connections, update routing, configure firewall

#### Slow Network Performance
- **Symptoms**: High latency, low throughput
- **Causes**: Bandwidth saturation, congestion, hardware limitations
- **Troubleshooting**: Bandwidth monitoring, QoS analysis
- **Solutions**: Upgrade bandwidth, implement QoS, optimize traffic

#### DNS Resolution Problems
- **Symptoms**: Cannot resolve domain names
- **Causes**: DNS server issues, configuration errors
- **Troubleshooting**: nslookup, dig commands
- **Solutions**: Configure correct DNS servers, flush DNS cache

#### DHCP Issues
- **Symptoms**: Cannot obtain IP address
- **Causes**: DHCP server down, IP pool exhausted
- **Troubleshooting**: Check DHCP server, verify scope
- **Solutions**: Restart DHCP service, expand IP pool

## 18. What is IPv6? How is it different from IPv4?

**IPv6 (Internet Protocol version 6)** is the latest version of the Internet Protocol, designed to replace IPv4 and address its limitations.

### IPv4 vs IPv6 Comparison

| Feature | IPv4 | IPv6 |
|---------|------|------|
| Address Length | 32 bits | 128 bits |
| Address Space | ~4.3 billion addresses | ~3.4 × 10³⁸ addresses |
| Address Representation | Dotted decimal (192.168.1.1) | Hexadecimal with colons (2001:db8::1) |
| Header Size | 20-60 bytes (variable) | 40 bytes (fixed) |
| Fragmentation | Router and host | Host only |
| Checksum | Header checksum | No header checksum |
| Configuration | Manual or DHCP | Auto-configuration available |
| Security | Optional (IPSec) | Built-in (IPSec mandatory) |
| Quality of Service | Limited support | Better QoS support |

### IPv6 Address Structure

#### Address Format
- **Length**: 128 bits (16 bytes)
- **Notation**: 8 groups of 4 hexadecimal digits
- **Example**: 2001:0db8:85a3:0000:0000:8a2e:0370:7334

#### Address Compression
- **Leading Zero Suppression**: 2001:0db8 → 2001:db8
- **Zero Compression**: 2001:db8:0000:0000:8a2e → 2001:db8::8a2e
- **Rule**: Only one :: allowed per address

### IPv6 Address Types

#### Unicast Addresses
- **Global Unicast**: Globally routable addresses (2000::/3)
- **Link-Local**: Local network communication (fe80::/10)
- **Unique Local**: Private addresses (fc00::/7)
- **Loopback**: ::1 (equivalent to 127.0.0.1)

#### Multicast Addresses
- **Prefix**: ff00::/8
- **Purpose**: One-to-many communication
- **Examples**: 
  - ff02::1 (All nodes)
  - ff02::2 (All routers)

#### Anycast Addresses
- **Purpose**: One-to-nearest communication
- **Usage**: Load balancing, service discovery

### IPv6 Header Structure
```
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
|Version| Traffic Class |           Flow Label                  |
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
|         Payload Length        |  Next Header  |   Hop Limit   |
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
|                                                               |
+                                                               +
|                                                               |
+                        Source Address                         +
|                                                               |
+                                                               +
|                                                               |
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
|                                                               |
+                                                               +
|                                                               |
+                      Destination Address                      +
|                                                               |
+                                                               +
|                                                               |
+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
```

### IPv6 Benefits
- **Vast Address Space**: No address exhaustion
- **Improved Performance**: Simplified header processing
- **Enhanced Security**: IPSec built-in
- **Better Mobility**: Mobile IPv6 support
- **Quality of Service**: Flow labeling
- **Auto-configuration**: SLAAC (Stateless Address Auto-configuration)

### IPv4 to IPv6 Transition Mechanisms

#### Dual Stack
- **Method**: Run both IPv4 and IPv6 simultaneously
- **Advantages**: Gradual migration, full compatibility
- **Disadvantages**: Resource overhead

#### Tunneling
- **6to4**: IPv6 packets encapsulated in IPv4
- **Teredo**: IPv6 connectivity through NAT
- **ISATAP**: Intra-site automatic tunnel

#### Translation
- **NAT64**: Translate IPv6 to IPv4
- **DNS64**: DNS translation support
- **Usage**: IPv6-only networks accessing IPv4 services

## 19. What is Load Balancing? Explain different load balancing algorithms.

**Load Balancing** distributes incoming network traffic across multiple servers to ensure no single server becomes overwhelmed.

### Benefits of Load Balancing
- **High Availability**: Redundancy and fault tolerance
- **Scalability**: Handle increased traffic
- **Performance**: Faster response times
- **Reliability**: Automatic failover
- **Maintenance**: Zero-downtime updates

### Types of Load Balancers

#### Layer 4 Load Balancing (Transport Layer)
- **Based on**: IP address and port numbers
- **Protocols**: TCP, UDP
- **Advantages**: Fast, low overhead
- **Disadvantages**: Limited intelligence
- **Use Case**: Simple traffic distribution

#### Layer 7 Load Balancing (Application Layer)
- **Based on**: Application data (HTTP headers, URLs, cookies)
- **Protocols**: HTTP, HTTPS, FTP
- **Advantages**: Intelligent routing, content-based decisions
- **Disadvantages**: Higher overhead
- **Use Case**: Complex application routing

### Load Balancing Algorithms

#### Round Robin
- **Method**: Requests distributed sequentially to each server
- **Advantages**: Simple, equal distribution
- **Disadvantages**: Doesn't consider server capacity
- **Best For**: Servers with similar capacity

#### Weighted Round Robin
- **Method**: Servers assigned weights based on capacity
- **Distribution**: Higher weight = more requests
- **Advantages**: Considers server capacity
- **Example**: Server A (weight 3), Server B (weight 1)

#### Least Connections
- **Method**: Route to server with fewest active connections
- **Advantages**: Better for long-lived connections
- **Tracking**: Connection count per server
- **Best For**: Applications with varying request duration

#### Weighted Least Connections
- **Method**: Combines least connections with server weights
- **Formula**: Connections / Weight
- **Advantages**: Optimal for mixed server capacities

#### IP Hash
- **Method**: Hash client IP to determine server
- **Advantages**: Session persistence
- **Disadvantages**: Uneven distribution possible
- **Use Case**: Applications requiring sticky sessions

#### Least Response Time
- **Method**: Route to server with fastest response time
- **Measurement**: Health check response times
- **Advantages**: Performance-based routing
- **Disadvantages**: Requires continuous monitoring

#### Resource-Based
- **Method**: Route based on server resource utilization
- **Metrics**: CPU, memory, disk usage
- **Advantages**: Prevents server overload
- **Requirements**: Real-time monitoring

### Load Balancer Deployment

#### Hardware Load Balancers
- **Examples**: F5 BIG-IP, Citrix NetScaler
- **Advantages**: High performance, dedicated hardware
- **Disadvantages**: Expensive, vendor lock-in

#### Software Load Balancers
- **Examples**: HAProxy, NGINX, Apache HTTP Server
- **Advantages**: Cost-effective, flexible
- **Disadvantages**: Requires server resources

#### Cloud Load Balancers
- **Examples**: AWS ELB, Google Cloud Load Balancer, Azure Load Balancer
- **Advantages**: Managed service, auto-scaling
- **Features**: Global load balancing, SSL termination

### Health Check Mechanisms
- **TCP Health Checks**: Test port connectivity
- **HTTP Health Checks**: Test application response
- **Custom Health Checks**: Application-specific tests
- **Passive Health Checks**: Monitor actual traffic
- **Active Health Checks**: Periodic probes

### Session Persistence (Sticky Sessions)
- **Cookie-Based**: Use cookies to maintain session
- **IP-Based**: Route based on client IP
- **SSL Session ID**: Use SSL session identifier
- **Application-Controlled**: Application manages session routing

## 20. What is CDN (Content Delivery Network)? How does it work?

**CDN** is a geographically distributed network of servers that deliver web content to users based on their location.

### CDN Benefits
- **Reduced Latency**: Content served from nearest edge server
- **Improved Performance**: Faster page load times
- **Reduced Bandwidth**: Offload traffic from origin server
- **High Availability**: Redundancy and fault tolerance
- **DDoS Protection**: Absorb and mitigate attacks
- **Global Reach**: Serve users worldwide efficiently

### CDN Components

#### Edge Servers (Points of Presence - PoPs)
- **Location**: Distributed globally
- **Function**: Cache and serve content
- **Capacity**: High-bandwidth connections

#### Origin Server
- **Function**: Original source of content
- **Role**: Serves content not cached at edge
- **Backup**: Final fallback for requests

#### CDN Management System
- **Function**: Monitor and manage CDN
- **Features**: Analytics, configuration, purging

### How CDN Works

#### 1. Content Distribution
```
Origin Server → CDN Network → Edge Servers
```

#### 2. User Request Process
1. **User requests content** (e.g., image, video, webpage)
2. **DNS resolution** points to nearest CDN server
3. **Edge server checks** for cached content
4. **If cached**: Serve content directly
5. **If not cached**: 
   - Fetch from origin server
   - Cache content locally
   - Serve to user
6. **Subsequent requests** served from cache

#### 3. Cache Management
- **TTL (Time To Live)**: Cache expiration time
- **Cache Headers**: Control caching behavior
- **Purging**: Manual cache invalidation
- **Cache Hierarchy**: Multiple cache levels

### CDN Caching Strategies

#### Static Content Caching
- **Content Types**: Images, CSS, JavaScript, videos
- **Duration**: Long TTL (hours to days)
- **Benefits**: Significant performance improvement

#### Dynamic Content Caching
- **Content Types**: API responses, personalized content
- **Duration**: Short TTL (minutes to hours)
- **Techniques**: Edge Side Includes (ESI), dynamic caching

#### Smart Caching
- **Predictive Prefetching**: Cache likely-requested content
- **Adaptive TTL**: Adjust based on content popularity
- **Conditional Requests**: Use ETags and Last-Modified headers

### CDN Technologies

#### Anycast Routing
- **Method**: Same IP address announced from multiple locations
- **Benefit**: Automatic routing to nearest server
- **Use Case**: DNS and CDN services

#### Load Balancing
- **Geographic Load Balancing**: Route based on location
- **Performance-Based**: Route to fastest server
- **Health Monitoring**: Avoid failed servers

#### Content Optimization
- **Compression**: Gzip, Brotli compression
- **Minification**: Remove unnecessary code
- **Image Optimization**: Format conversion, compression
- **HTTP/2**: Multiplexing, server push

### CDN Providers

#### Major CDN Providers
- **Cloudflare**: Global network, security focus
- **Amazon CloudFront**: AWS integration
- **Akamai**: Enterprise solutions
- **Google Cloud CDN**: Google Cloud integration
- **Microsoft Azure CDN**: Azure integration

#### CDN Selection Criteria
- **Geographic Coverage**: PoP locations
- **Performance**: Speed and reliability
- **Features**: Security, analytics, optimization
- **Pricing**: Cost structure
- **Integration**: API and tooling

### CDN Security Features
- **DDoS Protection**: Absorb and filter attacks
- **Web Application Firewall (WAF)**: Filter malicious requests
- **SSL/TLS Termination**: Encrypt communications
- **Access Control**: Geographic and IP-based restrictions
- **Bot Management**: Detect and mitigate bots

This comprehensive guide covers the most important computer networking concepts commonly asked in technical interviews, providing detailed explanations and practical examples for each topic.