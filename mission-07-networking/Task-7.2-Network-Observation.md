# Task 7.2 — Observe network information

## 1. Questions and Answers

### What does a connectivity test help you check?
A connectivity test helps you verify whether your computer has an active network connection and can successfully send data to and receive a response from a remote host. It also measureshow many milliseconds it takes for packets to travel back and forth and checks if any data packets were lost in transit.

---

### What information does a DNS lookup display?
A DNS lookup tool  displays the IP address (IPv4 and/or IPv6) assigned to a given domain name, along with the authoritative DNS server that answered the query.

---

### Describe the role of DNS when you enter a website name in a browser.
When you type a domain name  into your browser, the browser cannot directly find the server using letters. It immediately queries a DNS server to resolve that human-readable name into a numerical IP address .

---

## 2. Privacy-Safe Command Observations

### Connectivity Test (`ping`):
- **Command:** `ping -c 4 example.com

### DNS Lookup (`nslookup`):
- **Command:** `nslookup example.com`

#### observation >>
ping -c 4 example.com
PING example.com (104.20.23.154): 56 data bytes
64 bytes from 104.20.23.154: icmp_seq=0 ttl=58 time=5.970 ms
64 bytes from 104.20.23.154: icmp_seq=1 ttl=58 time=6.079 ms
64 bytes from 104.20.23.154: icmp_seq=2 ttl=58 time=5.706 ms
64 bytes from 104.20.23.154: icmp_seq=3 ttl=58 time=41.451 ms

--- example.com ping statistics ---
4 packets transmitted, 4 packets received, 0.0% packet loss
round-trip min/avg/max/stddev = 5.706/14.802/41.451/15.387 ms

nslookup example.com
Server:		[redacted DNS server]
Address:	[redacted]#53

Non-authoritative answer:
Name:	example.com
Address: 172.66.147.243
Name:	example.com
Address: 104.20.23.154