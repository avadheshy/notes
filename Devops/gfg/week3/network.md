# Networking Concepts - Complete Guide

## Table of Contents
1. [How Systems Communicate](#how-systems-communicate)
2. [LAN/WAN](#lanwan)
3. [Network Devices: Switch, Router, IP](#network-devices)
4. [IP Address and Its Types](#ip-address-and-its-types)
5. [OSI Model](#osi-model)
6. [Subnetting](#subnetting)
7. [DNS Basics](#dns-basics)
8. [Switching + Routing](#switching--routing)

---

## How Systems Communicate

Systems communicate through a series of protocols and standards that enable data exchange. The communication process involves:

**Key Components:**
- **Sender**: The device initiating communication
- **Receiver**: The device receiving the communication
- **Medium**: Physical (cables, fiber) or wireless (Wi-Fi, radio waves)
- **Protocol**: Set of rules governing the communication (TCP/IP, HTTP, etc.)

**Communication Process:**
1. Data is broken into packets
2. Each packet is addressed with source and destination information
3. Packets travel through the network via various paths
4. Packets are reassembled at the destination
5. Acknowledgment is sent back to confirm receipt

---

## LAN/WAN

### Local Area Network (LAN)
A network that connects devices within a limited geographical area such as a home, office, or building.

**Characteristics:**
- Small geographic area (typically up to 1 km)
- High data transfer rates (100 Mbps to 10 Gbps)
- Low latency
- Privately owned and maintained
- Common technologies: Ethernet, Wi-Fi

**Examples:**
- Office network
- Home network
- School computer lab

### Wide Area Network (WAN)
A network that spans a large geographical area, often connecting multiple LANs.

**Characteristics:**
- Large geographic area (cities, countries, continents)
- Lower data transfer rates compared to LAN
- Higher latency
- Often uses public infrastructure
- Common technologies: MPLS, Frame Relay, Internet

**Examples:**
- The Internet (largest WAN)
- Corporate networks connecting multiple offices
- Banking networks

---

## Network Devices

### Switch
A Layer 2 (Data Link Layer) device that connects multiple devices within a LAN.

**Functions:**
- Forwards data based on MAC addresses
- Creates a collision domain for each port
- Maintains a MAC address table
- Enables full-duplex communication
- Operates within a single network

**Types:**
- Unmanaged switches (plug-and-play)
- Managed switches (configurable, VLANs, QoS)

### Router
A Layer 3 (Network Layer) device that connects different networks and routes packets between them.

**Functions:**
- Forwards data based on IP addresses
- Connects different networks (LAN to WAN)
- Makes routing decisions using routing tables
- Provides Network Address Translation (NAT)
- Implements security features (firewall, ACLs)

**Key Differences:**
| Feature | Switch | Router |
|---------|--------|--------|
| OSI Layer | Layer 2 | Layer 3 |
| Addressing | MAC Address | IP Address |
| Scope | Within LAN | Between Networks |
| Speed | Faster | Slower (more processing) |
| Broadcast Domain | Single | Multiple |

---

## IP Address and Its Types

### What is an IP Address?
An Internet Protocol (IP) address is a unique numerical identifier assigned to each device on a network, enabling communication and identification.

### IPv4 Address
- 32-bit address
- Format: Four octets separated by dots (e.g., 192.168.1.1)
- Range: 0.0.0.0 to 255.255.255.255
- Approximately 4.3 billion unique addresses

### IPv6 Address
- 128-bit address
- Format: Eight groups of hexadecimal numbers (e.g., 2001:0db8:85a3:0000:0000:8a2e:0370:7334)
- Approximately 340 undecillion unique addresses
- Created to address IPv4 exhaustion

### IP Address Classes (IPv4)

**Class A**
- Range: 1.0.0.0 to 126.0.0.0
- Default subnet mask: 255.0.0.0 (/8)
- Used for: Very large networks
- Networks: 126 | Hosts per network: 16,777,214

**Class B**
- Range: 128.0.0.0 to 191.255.0.0
- Default subnet mask: 255.255.0.0 (/16)
- Used for: Medium to large networks
- Networks: 16,384 | Hosts per network: 65,534

**Class C**
- Range: 192.0.0.0 to 223.255.255.0
- Default subnet mask: 255.255.255.0 (/24)
- Used for: Small networks
- Networks: 2,097,152 | Hosts per network: 254

**Class D**
- Range: 224.0.0.0 to 239.255.255.255
- Used for: Multicast groups

**Class E**
- Range: 240.0.0.0 to 255.255.255.255
- Reserved for: Experimental purposes

### Public vs Private IP Addresses

**Public IP:**
- Globally unique and routable on the Internet
- Assigned by ISPs
- Required for direct Internet communication

**Private IP (RFC 1918):**
- Used within private networks
- Not routable on the Internet
- Ranges:
  - 10.0.0.0 to 10.255.255.255 (Class A)
  - 172.16.0.0 to 172.31.255.255 (Class B)
  - 192.168.0.0 to 192.168.255.255 (Class C)

### Static vs Dynamic IP

**Static IP:**
- Manually assigned and doesn't change
- Used for servers, printers, network devices
- More expensive

**Dynamic IP:**
- Automatically assigned by DHCP
- Changes periodically
- Used for client devices
- More efficient use of IP addresses

---

## OSI Model

The Open Systems Interconnection (OSI) model is a conceptual framework that standardizes the functions of a communication system into seven abstraction layers.

### Layer 7: Application Layer
- **Function**: Provides network services directly to end-user applications
- **Protocols**: HTTP, HTTPS, FTP, SMTP, DNS, SNMP
- **Data Unit**: Data
- **Examples**: Web browsers, email clients

### Layer 6: Presentation Layer
- **Function**: Data translation, encryption, compression
- **Protocols**: SSL/TLS, JPEG, MPEG, ASCII
- **Data Unit**: Data
- **Examples**: Data encryption, format conversion

### Layer 5: Session Layer
- **Function**: Establishes, manages, and terminates connections
- **Protocols**: NetBIOS, RPC, PPTP
- **Data Unit**: Data
- **Examples**: Session authentication, reconnection

### Layer 4: Transport Layer
- **Function**: Reliable data transfer, flow control, error correction
- **Protocols**: TCP (connection-oriented), UDP (connectionless)
- **Data Unit**: Segment (TCP) / Datagram (UDP)
- **Key Features**: Port numbers, segmentation, acknowledgment

### Layer 3: Network Layer
- **Function**: Logical addressing, routing, path determination
- **Protocols**: IP, ICMP, IGMP, ARP
- **Data Unit**: Packet
- **Devices**: Router, Layer 3 Switch
- **Key Features**: IP addressing, routing tables

### Layer 2: Data Link Layer
- **Function**: Physical addressing, frame formation, error detection
- **Protocols**: Ethernet, PPP, HDLC, Frame Relay
- **Data Unit**: Frame
- **Devices**: Switch, Bridge, NIC
- **Key Features**: MAC addresses, collision detection

### Layer 1: Physical Layer
- **Function**: Physical transmission of raw bits
- **Standards**: Ethernet cables, fiber optics, Wi-Fi
- **Data Unit**: Bits
- **Devices**: Hub, Repeater, Cables, Connectors
- **Key Features**: Voltage levels, cable specs, physical topology

### Mnemonic to Remember OSI Layers
**Top to Bottom**: "All People Seem To Need Data Processing"
**Bottom to Top**: "Please Do Not Throw Sausage Pizza Away"

---

## Subnetting

Subnetting is the process of dividing a large network into smaller, manageable sub-networks (subnets).

### Why Subnet?
- Improves network performance and security
- Reduces network congestion
- Simplifies network management
- Efficient use of IP addresses

### Subnet Mask
A 32-bit number that divides an IP address into network and host portions.

**Common Subnet Masks:**
- 255.0.0.0 or /8 (Class A)
- 255.255.0.0 or /16 (Class B)
- 255.255.255.0 or /24 (Class C)
- 255.255.255.128 or /25
- 255.255.255.192 or /26

### CIDR Notation (Classless Inter-Domain Routing)
Represents IP addresses with a suffix indicating the number of network bits.

Example: 192.168.1.0/24
- /24 means the first 24 bits are the network portion
- Remaining 8 bits are for hosts
- Subnet mask: 255.255.255.0

### Subnetting Example

**Given**: 192.168.1.0/24
**Requirement**: Create 4 subnets

**Solution:**
- Original: /24 (256 addresses)
- Need 4 subnets: 2² = 4, so borrow 2 bits
- New subnet mask: /26 (255.255.255.192)
- Each subnet has 64 addresses (62 usable)

**Resulting Subnets:**
1. 192.168.1.0/26 (192.168.1.0 - 192.168.1.63)
2. 192.168.1.64/26 (192.168.1.64 - 192.168.1.127)
3. 192.168.1.128/26 (192.168.1.128 - 192.168.1.191)
4. 192.168.1.192/26 (192.168.1.192 - 192.168.1.255)

### Calculating Subnet Information

**Formula for number of subnets**: 2ⁿ (where n = borrowed bits)
**Formula for hosts per subnet**: 2ʰ - 2 (where h = host bits, -2 for network and broadcast)

**Quick Reference Table:**
| CIDR | Subnet Mask | Hosts per Subnet |
|------|-------------|------------------|
| /24 | 255.255.255.0 | 254 |
| /25 | 255.255.255.128 | 126 |
| /26 | 255.255.255.192 | 62 |
| /27 | 255.255.255.224 | 30 |
| /28 | 255.255.255.240 | 14 |
| /29 | 255.255.255.248 | 6 |
| /30 | 255.255.255.252 | 2 |

---

## DNS Basics

The Domain Name System (DNS) translates human-readable domain names into IP addresses.

### What is DNS?
DNS is often called the "phonebook of the Internet." It allows users to access websites using domain names (like google.com) instead of IP addresses (like 142.250.185.46).

### How DNS Works

**DNS Resolution Process:**
1. User enters URL in browser (e.g., www.example.com)
2. Browser checks local DNS cache
3. If not cached, query sent to DNS Resolver (usually ISP)
4. Resolver checks its cache
5. If not cached, Resolver queries Root DNS Server
6. Root server directs to TLD (Top-Level Domain) server (.com)
7. TLD server directs to Authoritative Name Server
8. Authoritative server returns IP address
9. Resolver caches the result and returns IP to browser
10. Browser connects to the IP address

### DNS Record Types

**A Record (Address Record)**
- Maps domain name to IPv4 address
- Example: example.com → 93.184.216.34

**AAAA Record**
- Maps domain name to IPv6 address
- Example: example.com → 2606:2800:220:1:248:1893:25c8:1946

**CNAME Record (Canonical Name)**
- Alias for another domain name
- Example: www.example.com → example.com

**MX Record (Mail Exchange)**
- Specifies mail servers for the domain
- Example: example.com → mail.example.com (priority: 10)

**NS Record (Name Server)**
- Specifies authoritative name servers
- Example: example.com → ns1.example.com

**PTR Record (Pointer)**
- Reverse DNS lookup (IP to domain)
- Used for verification and security

**TXT Record**
- Holds text information
- Used for SPF, DKIM, domain verification

### DNS Server Types

**Recursive Resolver**
- Receives queries from clients
- Performs the full DNS lookup process
- Examples: Google DNS (8.8.8.8), Cloudflare (1.1.1.1)

**Root Name Server**
- Top of DNS hierarchy
- 13 sets worldwide (a.root-servers.net to m.root-servers.net)

**TLD Name Server**
- Manages top-level domains (.com, .org, .net)

**Authoritative Name Server**
- Final authority for a specific domain
- Returns the actual IP address

### Common DNS Ports
- UDP/TCP Port 53 (standard DNS queries)
- TCP Port 853 (DNS over TLS)
- TCP/UDP Port 443 (DNS over HTTPS)

---

## Switching + Routing

### Switching

Switching operates at Layer 2 (Data Link Layer) and involves forwarding frames based on MAC addresses.

#### How Switching Works

**Learning Phase:**
1. Switch starts with an empty MAC address table
2. When a frame arrives, switch learns source MAC address and port
3. Builds MAC address table over time

**Forwarding Decision:**
1. Switch examines destination MAC address
2. Looks up MAC address in table
3. Forwards frame out the appropriate port
4. If MAC not in table, floods to all ports (except source)

#### Switching Methods

**Store-and-Forward**
- Receives entire frame before forwarding
- Performs error checking (CRC)
- Higher latency but more reliable

**Cut-Through**
- Forwards frame after reading destination MAC
- Lower latency
- No error checking

**Fragment-Free**
- Reads first 64 bytes before forwarding
- Checks for collision fragments
- Compromise between the above two

#### VLANs (Virtual LANs)
- Logically segments a network
- Devices in same VLAN can communicate even if on different switches
- Improves security and reduces broadcast domains
- Requires Layer 3 device for inter-VLAN routing

### Routing

Routing operates at Layer 3 (Network Layer) and involves forwarding packets based on IP addresses.

#### How Routing Works

**Routing Process:**
1. Router receives packet on an interface
2. Examines destination IP address
3. Consults routing table
4. Determines best path to destination
5. Forwards packet out appropriate interface
6. Decrements TTL (Time to Live)

#### Routing Table Components

**Routing Table Entry Contains:**
- Destination network
- Subnet mask
- Next hop (gateway) or exit interface
- Metric (cost)
- Routing protocol source

#### Types of Routing

**Static Routing**
- Manually configured by administrator
- Routes don't change unless manually updated
- Advantages: Secure, predictable, low overhead
- Disadvantages: Not scalable, no automatic failover
- Use case: Small networks, specific routes

**Dynamic Routing**
- Routes learned automatically through routing protocols
- Adapts to network changes
- Advantages: Scalable, automatic failover, less administration
- Disadvantages: Higher overhead, more complex
- Use case: Large networks, changing topologies

#### Routing Protocols

**Distance Vector Protocols**
- **RIP (Routing Information Protocol)**
  - Uses hop count as metric (max 15 hops)
  - Updates every 30 seconds
  - Simple but slow convergence

**Link-State Protocols**
- **OSPF (Open Shortest Path First)**
  - Uses cost as metric (based on bandwidth)
  - Fast convergence
  - Hierarchical design (areas)
  - Industry standard for enterprise networks

**Hybrid/Advanced Protocols**
- **EIGRP (Enhanced Interior Gateway Routing Protocol)**
  - Cisco proprietary (now open standard)
  - Uses bandwidth, delay, load, reliability
  - Fast convergence

**Path Vector Protocols**
- **BGP (Border Gateway Protocol)**
  - Used between autonomous systems (Internet backbone)
  - Path vector algorithm
  - Policy-based routing

#### Routing Metrics

**Common Metrics Used:**
- Hop count (number of routers)
- Bandwidth
- Delay
- Load
- Reliability
- Cost (calculated value)

#### Administrative Distance

Priority of routing information sources (lower is better):
- Connected: 0
- Static: 1
- EIGRP: 90
- OSPF: 110
- RIP: 120

### Switching vs Routing Summary

| Aspect | Switching | Routing |
|--------|-----------|---------|
| OSI Layer | Layer 2 | Layer 3 |
| Addressing | MAC Address | IP Address |
| Scope | Within a network | Between networks |
| Device | Switch | Router |
| Table | MAC Address Table | Routing Table |
| Speed | Faster (hardware-based) | Slower (software-based) |
| Decision | Based on MAC | Based on IP + metrics |
| Broadcast | Forwards broadcasts | Blocks broadcasts |

---

## Additional Resources

**Practice Tools:**
- Cisco Packet Tracer
- GNS3
- EVE-NG

**Useful Commands:**
- `ipconfig` / `ifconfig` - View IP configuration
- `ping` - Test connectivity
- `tracert` / `traceroute` - Trace route to destination
- `nslookup` / `dig` - DNS queries
- `arp -a` - View ARP cache
- `netstat` - Network statistics

**Further Reading:**
- TCP/IP Illustrated by W. Richard Stevens
- Computer Networking: A Top-Down Approach by Kurose and Ross
- Cisco CCNA Certification study materials