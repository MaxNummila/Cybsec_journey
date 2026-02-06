# Cybersecurity 101 path TryHackMe

This file covers my progress and what I have learned from the **cybersecurity 101** path, which I started on 10.7.2025.



## Path Overview
**Modules Completed:**
- Search Skills
- Active Directory Basics

**Skills Gained:**



## Key Concepts

### Search Skills
#### Search Engines
- Shodan, Censys, VirusTotal and HaveIBeenPWNd
#### Vulnerabilities and Exploits
- Common Vulnerabilities and Exposures (CVE)
- Exploit Databases
- Technical Documentation

### Active Directory
- Organizational Units (OU)
- Security Groups
#### Managing Users in AD
- Delegation, process of granting privileges to users
- RDP



## Own word notes
CMD Commands
ver – version of windows
systeminfo – displays system information
ping – check if one can reach a server
tracert – traces the route to a server
nslookup – looks up a server and returns its ip
netstat – shows connections and listening ports
ipconfig – shows information about internet settings
ipconfig /all – Shows all network information
dir – shows the child directiories
dir /a – shows hidden and system files
dir /s – displays files in the current directory and all subdirectories
tree – Shows the child directories in a tree
mkdir – creates a directory
type – dumps content of text file on the screen. 
copy dir x dir y – makes a copy of dir x called dir y
move – moves a directory
del / erase  - both used to delete files
* - used to refer to multiple files
tasklist – lists running processes
tasklist /FI “imagename eq sshd.exe” – will search for tasks related to sshd.exe. /FI is used to set the filter image name equals sshd.exe
taskkill /PID xxx – kills a task with the process ID of xxx
chkdsk – checks the file system and disk volumes for errors and bad sectors
driverquery – displays a list of installed device drivers
sfc /scannow – scans system files for corruption and repairs them if possible

PowerShell Commands
-	Get-command
o	List all available cmdlets, functions, aliases and scripts
-	Get-Command -CommandType “Function”
o	Lists only functions
-	Get-Help 
o	Provides detailed information about cmdlets like usage parameters and examples
-	dir / Get-ChildItem
-	cd / Set-Location 
o	Aliases to ease working between cmd and PS
-	Find-Module
o	To search for modules in online repositories which can be downloaded
-	Find-Module -Name “PowerShell*”
o	To search for a module with a similar name to powershell one adds the *
-	Install-Module 
o	Installs a certain module
-	New-Item
o	Create an item in PS, will need to specify path and type (-Path, -ItemType)
-	Remove-Item
o	Removes both directories and files
-	Copy-Item
o	Copies an item
-	Move-Item
o	Moves an item
-	Get-Content
o	Read and display contents of a file (Like cat on linux)
-	Piping  |
o	Same as Linux, it is used to allow the output of one command to be used as the input for another
-	Sort-Object
o	Sort objects by size
-	Where-Object
o	Used to filter for objects that only meet a desired criteria
-	-eq
o	Extension that means equal
-	-ne
o	Not equal
-	-gt
o	greater than
-	-ge
o	Greter than or equal to
-	-lt
o	Less than
-	-le
o	Less than or equal to
-	-like
o	Used to filter by a specified pattern such as “ship*”
-	Select-object
o	Used to select specific properties from objects or limit the number of objects returned
-	Select-String
o	Like grep, Searches for text patterns in files
-	Get-ComputerInfo
o	Retrieves comprehensive system information
-	Get-LocalUser
o	List all the local user accounts on the system
-	Get-NetIPConfiguration 
o	Provides detailed information about the network interfaces on the system
-	Get-NetIPAddress
o	Shows details for all the IP addresses configured on the system
-	Get-Process
o	Detailed view of all currently running processes
-	Get-Service
o	Retrieval of information about the status of services on the machine
-	Get-NetTCPConnection
o	Displays current TCP connections, with local and remote endpoints
-	Get-FileHash
o	Generates file hashes, which helps with verifying file integrity and potential tampering
-	Invoke-Command
o	Essential for executing commands on remote systems




Linux Commands
-	Pwd
o	Print working directory
-	Cd
o	Change directory
-	Ls
o	List contents of directory
-	Cat
o	Read and print content
-	Grep
o	Search for word pattern in file
-	Echo $SHELL
o	Displays the shell in use
-	Cat /etc/shells
o	Displays all installed shells
-	Zsh
o	Changes shell to zsh, same for all other shells
-	Chsh /usr/bin/zsh
o	Makes zsh the default shell
-	History
o	Shows all previous commands
-	Nano
o	Small editor
-	Echo
o	Prints to the console
-	Read
o	Takes a user input, used in scripting. Read name creates a variable name and fills it with user input
-	Chmod
o	Used to change permission of files
Scripting (Bash)
-	First create a file with the extension .sh (bash)
-	Nano first_script.sh
o	Creates a script
-	Every script should start from shebang
o	Shebang is a combination of characters, starting with #! Followed by the name of the interpreter to use.
-	In this case shebang would be: #!/bin/bash

#!/bin/bash
echo "Hey, what is your name?"
read name
echo "Fuck you, $name"
-	Then it needs to be saved but also made executable
-	chmod +x first_script.sh
-	To execute a script, write ./ and the name of the file. This is so that it searches for the file in the current directory
-	Example of a loop
#!/bin/bash
for i in {1..10}; 
do 
echo $i 
done
-	Example of conditional script
#!/bin/bash
echo "Please enter your name first:"
read name
if [ "$name" = "Stewart" ]; then
        echo "Welcome Stewart! Here is the secret: THM_Script"
else
        echo "Sorry! You are not authorized to access the secret."
Fi

The OSI model
7. Application – Providing services and interfaces to apps, HTTP, FTP, DNS, SMTP
6. Presentation – Data encoding, encryption, compression, Unicode, MIME, JPEG
5. Session – Establishing, maintaining and synchronizing sessions, NFS, RPC
4. Transport – End-to-end communication and data segmentation,  UDP, TCP
3. Network – Logical addressing and routing between networks, IP, ICMP, IPSec
2. Data link – Reliable data transfer between adjacent nodes, Ethernet (802.3), Wi-Fi (802.11)
1. Physical – Physical data transmission media, electrical, optical and wireless signals

TCP/IP Model
Application layer – OSI layers 5,6 and 7 in one
Transport layer – Layer 4
Internet layer – Layer 3
Link layer – Layer 2

IP and Subnets
IP is like a postage address
IPv4 is 32 bits and 4 octets
0 and 255 are reserved for the network and broadcast addresses
Subnet mask of 255.255.255.0 can be written as /24
Public and private IP addresses
Private IP is not to be reached from the outside world. For a private IP address to access the outside world it must go through a router that has a public IP address and that supports Network Address Translation (NAT).
IP address ranges are: 
10.0.0.0 – 10.255.255.255
172.16.0.0 – 172.31.255.255
192.168.0.0 – 192.168.255.255

Routing
Router is like a post office, where it sends your packet to the next one in order to get it closer to the destination. 
In technical terms, a router functions at layer 3 of OSI and inspects the IP address and forwards it to the best network (router) so that it gets closer to the destination.

UDP and TCP
-	User Datagram Protocol and Transmission Control Protocol are both transport protocols for allowing networked hosts to communicate with each other. 
UDP

-	UDP allows us to reach a specific process on the target host and works on layer 4. It is connectionless so it does not have a mechanism to guarantee that the packet has been delivered. 
-	An IP address identifies the host and a port determines the sending and receiving process. 
-	A port number ranges between 1 and 65535, port 0 is reserved.
TCP
-	Connection-oriented transport protocol.
-	Uses various mechanisms to ensure reliable data delivery
-	Layer 4, but needs an establishment of a connection before data is sent
-	Each data octet has a sequence number and the receiver has an acknowledgement number specifying the last received octet
-	Three-way handshake: SYN (Synchronise) ACK(Acknowledgement)
o	1. SYN Packet: Client initiates connection by sending a SYN packet that contains the clients randomly chosen initial sequence number
o	2. SYN-ACK Packet: The server responds with a SYN-ACK packet, which adds the initial sequence number randomly chosen by the server
o	3. ACK Packet: The client sends an ACK packet to acknowledge the reception of the SYN-ACK packet
Encapsulation
-	Process of every layer adding a header to the received unit of data and sending the encapsulated unit to the layer below.
-	Four steps:
Application data: User inputs the data they want to send to the app. The app formats the data and starts sending it according to the app protocol used, using the layer below it, the transport layer. 
Transport protocol segment or datagram: The transport layer (Such as TCP or UDP) adds the proper header information and creates the TCP segment (Or UDP datagram). This segment is sent to the layer below, the network layer.
Network packet: The network layer adds an IP header to the received TCP segment or UDP datagram. Then the IP packet is sent to the layer below, the data link layer.
Data link frame: The Ethernet or WiFi receives the IP packet and adds the proper header and trailer, creating a frame.

Example of a packet:

    On the TryHackMe search page, you enter your search query and hit enter.
    Your web browser, using HTTPS, prepares an HTTP request and pushes it to the layer below it, the transport layer.
    The TCP layer needs to establish a connection via a three-way handshake between your browser and the TryHackMe web server. After establishing the TCP connection, it can send the HTTP request containing the search query. Each TCP segment created is sent to the layer below it, the Internet layer.
    The IP layer adds the source IP address, i.e., your computer, and the destination IP address, i.e., the IP address of the TryHackMe web server. For this packet to reach the router, your laptop delivers it to the layer below it, the link layer.
    Depending on the protocol, The link layer adds the proper link layer header and trailer, and the packet is sent to the router.
    The router removes the link layer header and trailer, inspects the IP destination, among other fields, and routes the packet to the proper link. Each router repeats this process until it reaches the router of the target server.
Telnet
-	Teletype Network
-	Network protocol for remote terminal connection, which allows you to connect to and communicate with a remote system

Networking Essentials
-	When connecting to a network we need to configure atleast the IP address and subnet mask, router and DNS server.
-	Dynamic Host Configuration Protocol (DHCP) is a protocol at the application-level that relies on UDP
-	DHCP follows four steps: Discover, Offer, Request and acknowledge
1.	DHCP Discover: Client broadcasts a DHCPDISCOVER message, looking for the local DHCP if one exists
2.	DHCP Offer: The server responds with a DHCPOFFER message with an IP address available for the client to accept.
3.	DHCP Request: The client responds with a DHCPREQUEST message to indicate that it has accepted the IP
4.	DHCP Acknowledge: The server responds with a DHCPACK message to confirm that the IP address is now assigned to the client
ICMP
-	Internet Control Message Protocol is used for network diagnostics and error reporting
Commands:
-	Ping: Uses ICMP to test connectivity to a target system and measures the round-trip time (RTT)
-	Traceroute: Same as ping for linux and unix type systems
Routing
OSPF – Open shortest path first is a routing protocol that allows routers to share data about the network topology to calculate the most efficient route
EIGRP – Enhanced Interior Gateway Routing Protocol is a Cisco proprietary routing protocol
BGP – Border Gateway Protocol is the primary protocol used on the internet.
RIP – Routing Information Protocol is a simple protocol often used in small networks.

NAT
-	Network Access Translation
o	Idea is that one public IP address provides access to many private IP addresses
-	This means that it creates internal and external networks

Networking Core Protocols
DNS
-	Domain name system lets you remember names instead of IP addresses
-	Operates at the Application layer (layer 7)
-	Uses UDP port 53 as default and TCP port 53 as backup
o	A record is IPv4 addresses
o	AAAA record is IPv6
o	CNAME record is for mapping a domain name to another domain name
o	MX record is the mail exchange record that specifies the mail server responsible for handling emails for a domain
WHOIS
-	Records for the registrant of a domain name
-	Can be hidden from it
HTTP and HTTPS
-	Hypertext Transfer Protocol (Secure for HTTPS)
-	Commands and methods commonly used by web browsers:
o	GET
o	POST
o	PUT
o	DELETE
-	HTTP and HTTPS use TCP ports 80 and 443 respectively. Less commonly other ports like 8080 and 8443
FTP
-	File Transfer Protocol is designed to transfer files
-	Example commands:
o	USER
o	PASS
o	RETR
o	STOR
-	Default on port 21
SMTP
-	Simple Mail Transfer Protocol defines how a mail client talks with a mail server and how mail servers talk to one another
-	Commands:
o	HELO or EHLO
o	MAIL FROM
o	RCPT TO
o	DATA
o	.
POP3
-	Post Office Protocol Version 3 is designed to allow the client to communicate with a mail server and retrieve email messages
-	Commands:
o	USER <username>
o	PASS <password>
o	STAT
o	LIST
o	RETR <message_number>
o	DELE <message_number>
o	QUIT
-	Default on port 110
IMAP
-	Internet Message Access Protocol allows synchronization of messages instead of deleting a message after retrieving it. 
-	IMAP Commands:
o	LOGIN <username> <password>
o	SELECT <mailbox>
o	FETCH <mail_number> <data_item_name>
o	MOVE <sequence_set> <mailbox>
o	COPY <sequence_set> <data_item_name>
o	LOGOUT
-	Port 143 by default
 
TLS
-	Transport Layer Security is a cryptographic protocol operating at the transport layer
-	Allows for secure communication between a client and a server over an insecure network
-	The S in for example HTTPS stands for secure, because they use SSL/TLS (SSL is Secure Sockets Layer)
-	First step for TLS is that every server or client that needs to identify itself must get a signed TLS certificate.
-	Getting one costs an annual fee, but one can be gotten for free from lets encrypt

