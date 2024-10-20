
| Feature                | API Gateway                         | Proxy                               | Reverse Proxy                     | Load Balancer                     |
|------------------------|-------------------------------------|-------------------------------------|-----------------------------------|-----------------------------------|
| **Primary Function**    | Manages API traffic, routing, security, etc. | Forwards requests on behalf of the client | Forwards requests to internal servers | Distributes traffic across multiple servers |
| **Client-Side View**    | Interacts with the gateway | Interacts with the proxy | Interacts with the proxy, unaware of internal servers | Unaware of load balancing mechanism |
| **Security**            | Handles authentication, rate limiting, etc. | Can anonymize client | Protects internal servers | Doesn't directly focus on security |
| **Traffic Distribution**| Manages request routing between services | No | Can distribute traffic among servers | Distributes traffic across servers |
| **Example**             | AWS API Gateway, Kong               | Corporate proxy server              | NGINX, HAProxy                    | AWS ELB, NGINX                    |


## All thses are servers
