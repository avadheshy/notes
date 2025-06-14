# Forward Proxy vs Reverse Proxy

## What is a Forward Proxy?

A **forward proxy** (also known as a "proxy server") is a server that sits in front of one or more client computers and acts as an intermediary between the clients and the internet.

### How It Works:
- The client sends the request to the forward proxy.
- The proxy then sends the request to the internet on behalf of the client.
- The response from the internet is returned to the proxy, which forwards it to the client.

### Uses of Forward Proxy:
- **Client Anonymity**
- **Caching**
- **Traffic Control**
- **Logging**
- **Request/Response Transformation**
- **Encryption**

---

## What is a Reverse Proxy?

A **reverse proxy** is a server that sits in front of one or more web servers and acts as an intermediary between clients (from the internet) and the backend servers.

### How It Works:
- The client sends the request to the reverse proxy.
- The reverse proxy forwards the request to an appropriate backend server.
- The server processes the request and returns the response to the reverse proxy.
- The reverse proxy then sends the response back to the client.

### Uses of Reverse Proxy:
- **Server Anonymity**
- **Caching**
- **Load Balancing**
- **DDoS Protection**
- **Canary Experimentation**
- **URL/Content Rewriting**

---

## Difference Between Forward Proxy and Reverse Proxy

| Feature         | Forward Proxy                                     | Reverse Proxy                                                  |
|----------------|---------------------------------------------------|----------------------------------------------------------------|
| **Purpose**     | Provides anonymity and caching to clients         | Improves server performance, load balancing, and security      |
| **Location**    | Between the client and the internet               | Between the internet and server                                |
| **Visibility**  | The client is aware of the proxy                  | The server is not aware of the proxy                           |
| **Configuration**| The client must be configured to use the proxy   | The server must be configured to use the proxy                 |
| **Use Cases**   | Bypassing content filters, accessing restricted content | Load balancing, caching, SSL/TLS offloading, web application firewall |
| **Examples**    | Squid, Proxy, Tor                                 | Nginx, Apache, HAProxy                                         |

---
