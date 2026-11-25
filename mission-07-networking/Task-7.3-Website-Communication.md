# Task 7.3 — What happens when you open a website?

A step-by-step breakdown (6 steps) of what happens behind the scenes from the moment you type a website URL to the moment the web page renders on your screen:

1. **User Request Initiated (Client Browser):**
   The user types a web address (e.g. `https://example.com`) into the browser's address bar and presses Enter. The browser acts as the **client**.

2. **DNS Resolution (Finding the IP Address):**
   The browser checks its local cache for the IP address. If not found, it queries a **DNS (Domain Name System)** server over the network. The DNS server acts like a phonebook and translates the human-readable domain name `example.com` into the numerical IP address `93.184.216.34`.

3. **Packet Transmission & Routing:**
   The client creates an HTTP/HTTPS connection request. The operating system breaks this request into small data packets and transmits them through the local Wi-Fi / **router**, which directs the packets across the Internet (WAN) using the TCP/IP **protocol** toward the destination IP address.

4. **Connection Establishment (Handshake):**
   The packets arrive at the destination **server** hosting the website. The client and server perform a secure handshake (TCP three-way handshake and TLS/SSL cryptographic negotiation) to establish a safe, encrypted communication channel.

5. **Server Processing & HTTP Response:**
   The **server** receives the client's HTTP request for the webpage, processes it, retrieves the necessary files (HTML, CSS, JavaScript, images), packages them into response data packets, and sends them back across the network to the client.

6. **Page Rendering (Client Display):**
   The client's browser reassembles the received packets, parses the HTML structure, applies CSS styling, executes JavaScript, and renders the fully visual web page on the screen for the user to interact with.
