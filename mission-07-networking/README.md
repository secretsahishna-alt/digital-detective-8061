# Mission 7 — How Computers Communicate

## 1. Task / objective
Explain basic computer network types and concepts, observe network connectivity and DNS lookup tools, and describe the step-by-step process of opening a website.

## 2. Work completed
- **Task 7.1:** Completed the network concepts table explaining LAN, MAN, WAN, DNS, Router, Protocol, Packet switching, and Client-server with simple real-world examples.
- **Task 7.2:** Performed network connectivity verification (`ping`) and DNS domain resolution (`nslookup`) in Terminal, keeping local network identifiers privacy-safe.
- **Task 7.3:** Wrote a numbered 6-step explanation illustrating how client browsers, DNS servers, routers, protocols, and web servers interact when loading a web page.

## 3. Commands / tools used

- `ping -c 4 <domain>` 
- `nslookup <domain>` 

## 4. My Understanding
- Understood that computer networks scale from local areas (LAN) to city-wide areas (MAN) and global infrastructure (WAN).
- Learned that computers communicate using IP addresses rather than names, making the Domain Name System (DNS) a critical translation layer.
- Learned how routers use routing tables to direct packet-switched data across multiple networks to reach their destination.
- Understood how the client-server model functions with standard protocols like HTTP/HTTPS to request, process, and display web resources.

## 5. Difficulties faced
- Remembering to avoid exposing private network details such as home router gateway IPs or personal Wi-Fi network names in output files.

## 6. How I resolved them
- Sanitized all terminal outputs and replaced internal IP addresses and network identifiers with `[redacted]` placeholders.

## 7. Evidence / files
- `Task-7.1-Network-Concepts.md`
- `Task-7.2-Network-Observation.md`
- `Task-7.3-Website-Communication.md`
- `README.md`

## 8. Commit details
- **Commit message:** Explain networking concepts and website communication
- **Branch:** main
- **Repository:** digital-detective-8061
- **Status:** Ready to commit and push to GitHub.
