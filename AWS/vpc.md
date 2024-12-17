vpc cmponents
traffic flow outside and inside
internet gateway, nat gateway ,route table,security group and nacl
## security group
used to add securty at ec2 label. by default aws all all the traffice of outboud and deny all inbound traffic.
## nacl(network access controll list)
used to add security at subnet label. it can add the same security to all the ec2 in that subnet.
these 2 are last label of security.
scp,boston host
# route 53
it provides dns as service.it is used for health check as well.
# application load balancer
it works for http and https or layer 7
#
each subnet has its data of which instance is asociated with which ip.
This is used to transfer traffice to that instance when request comes to subnet.

target group,security group,load balancer
what is vpc peering how a machine can communicate in same subnet/vpc or same subnet/vpc
nacl and subnet differnce between
# Internet gateway
It is used to connect vpc to internet or vice versa. It allow instances with public ip interact with Internet. It uses routing table for finding currct subnet.
# Nat gateway
It allow instancess in private subnet to access the Internet while preventing direct incomming connection from internet.It communicates with Internet gateway for internet communication.
# Routing Table: 
Directs the traffic to the correct subnet.

# Traffic Flow Through VPC Components
## Incoming Traffic (Example: Public Instance in Subnet)
1. Internet Gateway: Traffic enters the VPC through the IGW.
2. Routing Table: Directs the traffic to the correct subnet.
3. Network ACL: Filters traffic at the subnet level.
4. Security Group: Filters traffic at the instance level.
5. Instance: Receives the traffic if all rules permit it.
## Outgoing Traffic (Example: Private Instance Accessing Internet)
1. Instance: Traffic originates from the private instance.
2. Security Group: Outbound rules are checked.
3. Routing Table: Directs traffic to the NAT Gateway.
4. NAT Gateway: Translates private IP to public IP and forwards the traffic to the IGW.
5. Internet Gateway: Sends traffic to the destination on the internet.

# Summary of Responsibilities
1. Internet Gateway	Connects VPC to the internet; supports public IP access.
2. NAT Gateway	Provides internet access for private instances without allowing inbound internet traffic.
3. NACL	Stateless filtering of inbound/outbound traffic at the subnet level.
4. Routing Table	Determines the next hop for incoming and outgoing traffic based on destination IP.
5. Load Balancer	Distributes incoming traffic across multiple instances for scalability and availability.
6. Security Group	Stateful filtering of inbound/outbound traffic at the instance level.
   
Each component has a specific function in controlling and facilitating traffic, ensuring that only authorized data flows into or out of the VPC

# Summary Table of Traffic Flows

## Internet → Public Instance	
IGW → Routing Table → NACL → Security Group → Instance(	Direct access via public IP).
# Internet → Private Instance	
Bastion Host/VPN → NACL → Security Group → Instance	(No direct access; needs a jump server or private connection).
# Public Instance → Internet	
Security Group → Routing Table → IGW → Internet	(Direct internet access via IGW).
# Private Instance → Internet
Security Group → Routing Table → NAT Gateway → IGW → Internet	(NAT Gateway allows outbound internet access).
